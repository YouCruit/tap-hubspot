from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class ContactAssociationsStream(HubSpotStream):
    """Contact's associations."""

    def get_properties(self):
        return []

    request_limit = 50

    name = "contact_associations"
    path = "/crm/v4/objects/contact/?associations=companies,deals" \
           "&propertiesWithHistory=hubspot_owner_id"
    properties_object_type = "contacts"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
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
            "associations",
            th.StringType,
        ),
        th.Property(
            "propertiesWithHistory",
            th.StringType,
        ),
    ).to_dict()
