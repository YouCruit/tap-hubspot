"""HubSpot tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_hubspot.streams import (
    CompaniesStream,
    ContactsStream,
    CallsStream,
    DealsStream,
    DealsPipelinesStream,
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
            "hapikey",
            th.StringType,
            required=True,
            description="HubSpot API key"
        ),
        th.Property(
            "start_from",
            th.DateTimeType,
            required=False,
            description="Starts incremental stream from this updated timestamp"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
