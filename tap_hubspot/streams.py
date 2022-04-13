"""Stream type classes for tap-hubspot."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
import requests

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class CompaniesStream(HubSpotStream):
    """Companies."""
    name = "companies"
    path = "/crm/v3/objects/companies"
    properties_object_type = "companies"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
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
            th.StringType,
        ),
        th.Property(
            "updatedAt",
            th.StringType,
        ),
        th.Property(
            "archived",
            th.BooleanType,
        ),
        th.Property(
            "archivedAt",
            th.StringType,
        ),
        th.Property(
            "associations",
            th.StringType,
        ),
    ).to_dict()
