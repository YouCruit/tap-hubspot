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
        return None if self.config.get("no_search", False) else "lastmodifieddate"

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
