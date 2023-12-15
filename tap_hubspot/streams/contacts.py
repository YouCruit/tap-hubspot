from typing import Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class ContactsStream(HubSpotStream):
    """Contacts."""

    name = "contacts"
    search_path = "/crm/v3/objects/contacts/search"
    full_path = "/crm/v3/objects/contacts"
    properties_object_type = "contacts"
    primary_keys = ["id"]

    @property
    def schema(self):
        props = th.PropertiesList(
            th.Property(
                "id",
                th.StringType,
            ),
            th.Property(
                "properties",
                th.StringType,
            ),
            th.Property(
                "createdAt",
                th.DateTimeType,
            ),
            th.Property(
                "updatedAt",
                th.DateTimeType,
            ),
            th.Property(
                "archived",
                th.BooleanType,
            ),
            th.Property(
                "archivedAt",
                th.DateTimeType,
            ),
            th.Property(
                "associations",
                th.StringType,
            ),
        )

        # Needs to be defined manually since 2023-07-12 when
        # the list of properties in hubspot became to long for a request.
        # Error: 414 Client Error: URI Too Long for path
        self.extra_properties = [
            "email",
            "firstname",
            "lastname",
            "jobtitle",
            "call_center_candidate_id",
            "candidate_id",
            "interested_in_lanefinder_driver_force",
            "hs_last_sales_activity_timestamp",
            "hs_lead_status",
            "hs_searchable_calculated_international_mobile_number",
            "hubspot_owner_id",
            "hs_calculated_phone_number",
            "hs_timezone",
        ]

        if self.replication_key:
            props.append(
                th.Property(
                    self.replication_key,
                    th.DateTimeType,
                )
            )

        return props.to_dict()

    @property
    def replication_key(self) -> Optional[str]:
        return None if self.config.get("no_search", False) else "hs_lastmodifieddate"

    @replication_key.setter
    def replication_key(self, _):
        "Just to shut Lint up"
        pass

    @property
    def path(self) -> str:
        return (
            self.full_path if self.config.get("no_search", False) else self.search_path
        )

    @path.setter
    def path(self, _):
        "Just to shut Lint up"
        pass
