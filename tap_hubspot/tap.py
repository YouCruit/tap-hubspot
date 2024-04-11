"""HubSpot tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th  # JSON schema typing helpers
from singer_sdk.helpers._classproperty import classproperty
from singer_sdk.helpers.capabilities import (
    CapabilitiesEnum,
    PluginCapabilities,
    TapCapabilities,
)

from tap_hubspot.streams.calls import CallsStream
from tap_hubspot.streams.companies import CompaniesStream
from tap_hubspot.streams.company_associations import CompanyAssociationsStream
from tap_hubspot.streams.contact_associations import ContactAssociationsStream
from tap_hubspot.streams.contacts import ContactsStream
from tap_hubspot.streams.deals import DealsStream
from tap_hubspot.streams.deals_associations import DealsAssociationsStream
from tap_hubspot.streams.deals_pipelines import DealsPipelinesStream
from tap_hubspot.streams.emails import EmailsStream
from tap_hubspot.streams.meetings import MeetingsStream
from tap_hubspot.streams.notes import NotesStream
from tap_hubspot.streams.owners import OwnersStream
from tap_hubspot.streams.task_associations import TaskAssociationsStream
from tap_hubspot.streams.tasks import TasksStream
from tap_hubspot.streams.tickets import TicketsStream
from tap_hubspot.streams.tickets_associations import TicketsAssociationsStream
from tap_hubspot.streams.tickets_pipelines import TicketsPipelinesStream
from tap_hubspot.streams.calls_associations import CallAssociationsStream

STREAM_TYPES = [
    CompaniesStream,
    ContactsStream,
    DealsStream,
    DealsPipelinesStream,
    OwnersStream,
    TicketsStream,
    TicketsPipelinesStream,
    # Doing engagements last since
    # they are most likely to run into limits
    CallsStream,
    EmailsStream,
    MeetingsStream,
    TasksStream,
    NotesStream,
    # Associations
    DealsAssociationsStream,
    CompanyAssociationsStream,
    ContactAssociationsStream,
    TaskAssociationsStream,
    TicketsAssociationsStream,
    CallAssociationsStream
]


class TapHubSpot(Tap):
    """HubSpot tap class."""

    name = "tap-hubspot"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "hapikey",
            th.StringType,
            required=True,
            description="HubSpot private app token",
        ),
        th.Property(
            "start_from",
            th.DateTimeType,
            required=False,
            description="Starts incremental stream from this updated timestamp",
        ),
        th.Property(
            "no_search",
            th.BooleanType,
            required=False,
            default=False,
            description=(
                "Set to True to avoid using the search API"
                " - implies full table replication"
            ),
        ),
        th.Property(
            "batch_size",
            th.IntegerType,
            required=False,
            default=1_000_000,
            description="Size of batch files",
        ),
        th.Property(
            "batch_config",
            th.ObjectType(
                th.Property(
                    "encoding",
                    th.ObjectType(
                        th.Property("format", th.StringType, required=True),
                        th.Property("compression", th.StringType, required=True),
                    ),
                    required=True,
                ),
                th.Property(
                    "storage",
                    th.ObjectType(
                        th.Property("root", th.StringType, required=True),
                        th.Property(
                            "prefix", th.StringType, required=False, default=""
                        ),
                    ),
                    required=True,
                ),
            ),
            required=False,
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

    @classproperty
    def capabilities(self) -> List[CapabilitiesEnum]:
        """Get tap capabilities.

        Returns:
            A list of capabilities supported by this tap.
        """
        return [
            TapCapabilities.CATALOG,
            TapCapabilities.STATE,
            TapCapabilities.DISCOVER,
            PluginCapabilities.ABOUT,
            PluginCapabilities.STREAM_MAPS,
            PluginCapabilities.FLATTENING,
            PluginCapabilities.BATCH,
        ]
