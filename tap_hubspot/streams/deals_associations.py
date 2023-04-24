from typing import Optional
from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_hubspot.client import HubSpotStream
class DealsAssociationsStream(HubSpotStream):
    """Deal's associations"""

    name = "deals_associations"
    path = "/crm/v4/objects/deal/?associations=companies,contacts"
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
    ).to_dict()