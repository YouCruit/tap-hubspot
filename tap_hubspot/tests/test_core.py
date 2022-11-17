"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests, tap_sync_test

from tap_hubspot.tap import TapHubSpot

SAMPLE_CONFIG = {
    "hapikey": "test",
    "start_from": "2022-04-13T07:41:30.007Z",
    "test": "yes",
    #  "limit": 1,
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapHubSpot, config=SAMPLE_CONFIG)
    for test in tests:
        test()


def test_sync():
    """Tests companies stream"""
    (o, e) = tap_sync_test(TapHubSpot(config=SAMPLE_CONFIG))
    output = o.getvalue()
    print(output)
