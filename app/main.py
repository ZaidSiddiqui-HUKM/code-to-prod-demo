"""
Code to Production - demo app.

A deliberately tiny web app. Its only job is to give the training session
something real to build, test, package and deploy on screen.

The interesting part isn't this file - it's the journey this code takes
once you push it. Watch the Actions tab.
"""

def greeting(name: str = "world") -> str:
    """Return a greeting. This is the 'feature' we ship in the demo."""
    return f"Hello, {name}! This code travelled from a PC to a container."


def version() -> str:
    # Change this string live during the session, commit, and watch the
    # whole pipeline run. This is your "tiny safe change".
    return "1.0.0"


# Minimal WSGI app so there's something a container can actually run.
def app(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [greeting().encode("utf-8")]


if __name__ == "__main__":
    # Lets you run it locally: python app/main.py
    from wsgiref.simple_server import make_server
    print(greeting())
    print(f"version {version()}")
    srv = make_server("0.0.0.0", 8000, app)
    print("Serving on http://localhost:8000 (Ctrl+C to stop)")
    srv.serve_forever()
