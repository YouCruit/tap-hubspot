"""Tests standard tap features using the built-in SDK tests library."""

import os

from singer_sdk.testing import tap_sync_test

from tap_hubspot.tap import TapHubSpot

SAMPLE_CONFIG = {
    "hapikey": os.environ["TAP_HUBSPOT_HAPIKEY"],
    "start_from": "2022-04-13T07:41:30.007Z",
    "test": "yes",
    "no_search": True,
}


def test_sync():
    """Tests all streams"""
    (o, e) = tap_sync_test(TapHubSpot(config=SAMPLE_CONFIG))
    output = o.getvalue()
    # print(output)
    # Writes state messages
    assert '{"type": "STATE", "value": {"bookmarks":' in output
