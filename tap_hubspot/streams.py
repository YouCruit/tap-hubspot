"""Stream type classes for tap-hubspot."""

import requests
from typing import Any, Optional
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class CompaniesStream(HubSpotStream):
    """Companies."""
    name = "companies"
    path = "/crm/v3/objects/companies/search"
    properties_object_type = "companies"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


class ContactsStream(HubSpotStream):
    """Contacts."""
    name = "contacts"
    path = "/crm/v3/objects/contacts/search"
    properties_object_type = "contacts"
    primary_keys = ["id"]
    replication_key = "lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()

    def get_url(self, context: Optional[dict]) -> str:
        """Get stream entity URL.

        Because contacts is buggy by returning unsorted data,
        can't use the search api when fetching the initial data because
        its limit of 10k items.
        """
        if self.forced_get:
            # Contacts is not sorted. So use other endpoint
            path = "/".join(self.path.split("/")[:-1])
        else:
            path = self.path

        return "".join([self.url_base, path])

    def prepare_request(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> requests.PreparedRequest:
        # This method is called for of all
        if not self.get_starting_replication_key_value(context):
            # Contacts is not sorted. So use other endpoint
            self.forced_get = True
        return super().prepare_request(context, next_page_token)


class DealsStream(HubSpotStream):
    """Deals."""
    name = "deals"
    path = "/crm/v3/objects/deals/search"
    properties_object_type = "deals"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()

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


class TicketsStream(HubSpotStream):
    """Tickets."""
    name = "tickets"
    path = "/crm/v3/objects/tickets/search"
    properties_object_type = "tickets"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


class CallsStream(HubSpotStream):
    """Calls."""
    name = "calls"
    path = "/crm/v3/objects/calls/search"
    properties_object_type = "calls"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


class EmailsStream(HubSpotStream):
    """Emails."""
    name = "emails"
    path = "/crm/v3/objects/emails/search"
    properties_object_type = "emails"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


class MeetingsStream(HubSpotStream):
    """Meetings."""
    name = "meetings"
    path = "/crm/v3/objects/meetings/search"
    properties_object_type = "meetings"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


class NotesStream(HubSpotStream):
    """Notes."""
    name = "notes"
    path = "/crm/v3/objects/notes/search"
    properties_object_type = "notes"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


class TasksStream(HubSpotStream):
    """Tasks."""
    name = "tasks"
    path = "/crm/v3/objects/tasks/search"
    properties_object_type = "tasks"
    primary_keys = ["id"]
    replication_key = "hs_lastmodifieddate"
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
            "associations",
            th.StringType,
        ),
        th.Property(
            replication_key,
            th.DateTimeType,
        ),
    ).to_dict()


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
