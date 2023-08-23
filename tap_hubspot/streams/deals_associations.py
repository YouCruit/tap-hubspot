from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class DealsAssociationsStream(HubSpotStream):
    """Deal's associations"""

    def get_properties(self):
        return []

    name = "deals_associations"
    path = "/crm/v4/objects/deal/?associations=companies,contacts&propertiesWithHistory=hubspot_owner_id"
    properties_object_type = "deals"
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
