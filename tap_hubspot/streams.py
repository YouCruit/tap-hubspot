"""Stream type classes for tap-hubspot."""

from typing import Optional

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_hubspot.client import HubSpotStream


class CompaniesStream(HubSpotStream):
    """Companies."""

    name = "companies"
    search_path = "/crm/v3/objects/companies/search"
    full_path = "/crm/v3/objects/companies"
    properties_object_type = "companies"
    primary_keys = ["id"]

    @property
    def schema(self):
        props = th.PropertiesList(
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
        )

        if self.replication_key:
            props.append(self.replication_key)

        return props.to_dict()

    @property
    def replication_key(self) -> Optional[str]:
        return "hs_lastmodifieddate" if self.is_sorted else None

    @replication_key.setter
    def replication_key(self, _):
        "Just to shut Lint up"
        pass

    @property
    def path(self) -> str:
        return self.search_path if self.is_sorted else self.full_path

    @path.setter
    def path(self, _):
        "Just to shut Lint up"
        pass


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


# Associations streams
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


class ContactAssociationsStream(HubSpotStream):
    """Contact's associations."""

    name = "contact_associations"
    path = "/crm/v4/objects/contact/?associations=companies,deals"
    properties_object_type = "contacts"
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
