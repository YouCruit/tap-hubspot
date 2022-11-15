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

from tap_hubspot.streams import (
    CallsStream,
    CompaniesStream,
    ContactsStream,
    DealsPipelinesStream,
    DealsStream,
    EmailsStream,
    MeetingsStream,
    NotesStream,
    OwnersStream,
    TasksStream,
    TicketsStream,
)

STREAM_TYPES = [
    CompaniesStream,
    ContactsStream,
    DealsStream,
    DealsPipelinesStream,
    OwnersStream,
    TicketsStream,
    # Doing engagements last since
    # they are most likely to run into limits
    CallsStream,
    EmailsStream,
    MeetingsStream,
    TasksStream,
    NotesStream,
]


class TapHubSpot(Tap):
    """HubSpot tap class."""

    name = "tap-hubspot"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "hapikey", th.StringType, required=True, description="HubSpot API key"
        ),
        th.Property(
            "start_from",
            th.DateTimeType,
            required=False,
            description="Starts incremental stream from this updated timestamp",
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
