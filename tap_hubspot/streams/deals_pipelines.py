from typing import Optional
from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_hubspot.client import HubSpotStream
class DealsPipelinesStream(HubSpotStream):
    """Deals Pipelines"""

    name = "deals_pipelines"
    path = "/crm/v3/pipelines/deals/"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
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
            "label",
            th.StringType,
        ),
        th.Property(
            "displayOrder",
            th.IntegerType,
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
            "stages",
            th.ArrayType(
                th.PropertiesList(
                    th.Property(
                        "id",
                        th.StringType,
                    ),
                    th.Property(
                        "label",
                        th.StringType,
                    ),
                    th.Property(
                        "displayOrder",
                        th.IntegerType,
                    ),
                ),
            ),
        ),
    ).to_dict()