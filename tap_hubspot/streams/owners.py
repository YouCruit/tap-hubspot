from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class OwnersStream(HubSpotStream):
    """Owners."""

    name = "owners"
    path = "/crm/v3/owners/"
    properties_object_type = None
    primary_keys = ["id"]
    # Owners is so small, there is no reason to deal with its specialness
    # to force incremental sync on it
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
        ),
        th.Property(
            "email",
            th.StringType,
        ),
        th.Property(
            "firstName",
            th.StringType,
        ),
        th.Property(
            "lastName",
            th.StringType,
        ),
        th.Property(
            "userId",
            th.IntegerType,
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
            "teams",
            th.ArrayType(
                th.PropertiesList(
                    th.Property(
                        "id",
                        th.StringType,
                    ),
                    th.Property(
                        "name",
                        th.StringType,
                    ),
                ),
            ),
        ),
    ).to_dict()
