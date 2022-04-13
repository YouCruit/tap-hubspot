"""HubSpot tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_hubspot.streams import (
    CompaniesStream,
)
STREAM_TYPES = [
    CompaniesStream,
]


class TapHubSpot(Tap):
    """HubSpot tap class."""
    name = "tap-hubspot"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="HubSpot API key"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
