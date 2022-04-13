"""REST client handling, including HubSpotStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
import json

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import APIKeyAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class HubSpotStream(RESTStream):
    """HubSpot stream class."""

    url_base = "https://api.hubapi.com"

    records_jsonpath = "$.results[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.paging.next.after"  # Or override `get_next_page_token`.

    # Override in subclass to fetch additional properties
    properties_object_type = None
    # Used to cache extra properties fetched
    extra_properties = None

    @property
    def authenticator(self) -> APIKeyAuthenticator:
        """Return a new authenticator object."""
        return APIKeyAuthenticator.create_for_stream(
            self,
            key="hapikey",
            value=self.config.get("api_key"),
            location="params"
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if self.config.get("test", False):
            # Return a single page in unit tests
            return None
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            next_page_token = response.headers.get("X-Next-Page", None)

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {
            # Hubspot sets a limit of most 100 per request. Default is 10
            "limit": self.config.get("limit", 100)
        }
        props_to_get = self.get_properties()
        if props_to_get:
            params["properties"] = props_to_get
        if next_page_token:
            params["after"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def get_properties(self) -> Iterable[str]:
        """Override to return a list of properties to fetch for objects"""
        if self.extra_properties is not None:
           return self.extra_properties

        if not self.properties_object_type:
           self.extra_properties = []
           return self.extra_properties

        r = requests.get(
            "".join([self.url_base, f"/crm/v3/properties/{self.properties_object_type}"]),
            headers=self.http_headers,
            params={"hapikey": self.config.get("api_key")},
        )

        if r.status_code != 200:
            raise RuntimeError(f"Could not fetch properties: {r.status_code}, {r.text}")

        self.extra_properties = []
        j = r.json()
        for p in extract_jsonpath("$.results[*]", input=r.json()):
            print(p)
            self.extra_properties.append(p["name"])
        return self.extra_properties

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # Convert properties and associations back into JSON
        if 'properties' in row:
            jsonprops = json.dumps(row.get('properties'))
            row['properties'] = jsonprops
        if 'associations' in row:
            jsonassoc = json.dumps(row.get('associations'))
            row['associations'] = jsonassoc
        return row
