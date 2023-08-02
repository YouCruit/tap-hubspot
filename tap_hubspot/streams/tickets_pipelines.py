from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class TicketsPipelinesStream(HubSpotStream):
    """Tickets Pipelines"""

    name = "tickets_pipelines"
    path = "/crm/v3/pipelines/tickets/"
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
