from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class TaskAssociationsStream(HubSpotStream):
    """Task's associations."""

    def get_properties(self):
        return []

    request_limit = 50

    name = "task_associations"
    path = """/crm/v4/objects/task/?associations=contacts
    &propertiesWithHistory=hubspot_owner_id"""
    properties_object_type = "task"
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
