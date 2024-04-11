from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class CallAssociationsStream(HubSpotStream):
    """Contact's associations."""

    def get_properties(self):
        return []

    request_limit = 50

    name = "call_associations"
    path = (
        "/crm/v4/objects/call/?associations=companies,contacts"
    )
    properties_object_type = "call"
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
        )
    ).to_dict()
