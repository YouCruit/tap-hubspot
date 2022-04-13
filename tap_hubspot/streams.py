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


class ContactsStream(HubSpotStream):
    """Contacts."""
    name = "contacts"
    path = "/crm/v3/objects/contacts"
    properties_object_type = "contacts"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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

class DealsStream(HubSpotStream):
    """Deals."""
    name = "deals"
    path = "/crm/v3/objects/deals"
    properties_object_type = "deals"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class TicketsStream(HubSpotStream):
    """Tickets."""
    name = "deals"
    path = "/crm/v3/objects/tickets"
    properties_object_type = "tickets"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class CallsStream(HubSpotStream):
    """Calls."""
    name = "calls"
    path = "/crm/v3/objects/calls"
    properties_object_type = "calls"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class EmailsStream(HubSpotStream):
    """Emails."""
    name = "emails"
    path = "/crm/v3/objects/emails"
    properties_object_type = "emails"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class MeetingsStream(HubSpotStream):
    """Meetings."""
    name = "meetings"
    path = "/crm/v3/objects/meetings"
    properties_object_type = "meetings"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class NotesStream(HubSpotStream):
    """Notes."""
    name = "notes"
    path = "/crm/v3/objects/notes"
    properties_object_type = "notes"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class TasksStream(HubSpotStream):
    """Tasks."""
    name = "tasks"
    path = "/crm/v3/objects/tasks"
    properties_object_type = "tasks"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
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


class OwnersStream(HubSpotStream):
    """Owners."""
    name = "owners"
    path = "/crm/v3/owners/"
    properties_object_type = None
    primary_keys = ["id"]
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
