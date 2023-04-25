from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class CompanyAssociationsStream(HubSpotStream):
    """Company's associations."""

    name = "company_associations"
    path = "/crm/v4/objects/company/?associations=contacts,deals"
    properties_object_type = "companies"
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
