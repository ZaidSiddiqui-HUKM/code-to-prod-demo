"""
Automated tests - the 'Test' stage of the pipeline.

If any of these fail, the pipeline STOPS and nothing gets deployed.
That's the whole point: bad code can't move forward on its own.

Live-demo tip: to show a red pipeline, temporarily break greeting()
in app/main.py (e.g. return "Goodbye") and push. Watch this test fail
and the deploy stage never run. Then fix it and push again - green.
"""

from app.main import greeting, version


def test_greeting_default():
    assert greeting() == "Hello, world! This code travelled from a laptop to a container."


def test_greeting_named():
    assert greeting("Alex").startswith("Hello, Alex!")


def test_version_is_set():
    # A trivial test so there's always something green to point at.
    assert version() != ""
