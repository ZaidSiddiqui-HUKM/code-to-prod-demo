"""
The 'Deploy' stage builds this page from the application itself.

It imports app.main and reads the SAME greeting() and version() the tests
just checked. So the page you see in the browser is genuinely produced by
the code that travelled through the pipeline - not a static file someone
edited by hand. Change version(), push, and this page changes.
"""

import os

from app.main import greeting, version

sha = os.environ.get("GITHUB_SHA", "local")[:7]
built = os.environ.get("BUILT_AT", "just now")
run = os.environ.get("GITHUB_RUN_NUMBER", "-")

print(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Code to Production - live</title>
<style>
  :root {{ color-scheme: dark; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; min-height: 100vh; display: grid; place-items: center;
    background: #0d1117; color: #e6edf3;
    font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
    padding: 6vh 4vw; text-align: center;
  }}
  .live {{
    display: inline-flex; align-items: center; gap: .6rem;
    font-size: clamp(.8rem, 1.6vw, 1rem); letter-spacing: .18em;
    text-transform: uppercase; color: #3fb950; font-weight: 600;
  }}
  .dot {{
    width: .7em; height: .7em; border-radius: 50%; background: #3fb950;
    box-shadow: 0 0 0 0 rgba(63,185,80,.7); animation: pulse 2s infinite;
  }}
  @keyframes pulse {{
    70% {{ box-shadow: 0 0 0 .9em rgba(63,185,80,0); }}
    100% {{ box-shadow: 0 0 0 0 rgba(63,185,80,0); }}
  }}
  h1 {{
    font-size: clamp(2rem, 6vw, 4.5rem); margin: .5em 0 .2em;
    font-weight: 700; line-height: 1.1;
  }}
  .version {{
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: clamp(3.5rem, 15vw, 11rem); font-weight: 700;
    color: #58a6ff; line-height: 1; margin: .1em 0;
    text-shadow: 0 0 60px rgba(88,166,255,.35);
  }}
  .label {{
    font-size: clamp(.8rem, 1.8vw, 1.05rem); letter-spacing: .2em;
    text-transform: uppercase; color: #8b949e;
  }}
  .meta {{
    margin-top: 3rem; font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: clamp(.75rem, 1.5vw, .95rem); color: #8b949e; line-height: 2;
  }}
  .meta b {{ color: #e6edf3; font-weight: 600; }}
  .journey {{
    margin-top: 2.5rem; font-size: clamp(.7rem, 1.5vw, .95rem);
    color: #6e7681; letter-spacing: .05em;
  }}
  .journey b {{ color: #3fb950; }}
</style>
</head>
<body>
<main>
  <div class="live"><span class="dot"></span> Live in Test</div>
  <h1>{greeting()}</h1>
  <div class="label">Deployed version</div>
  <div class="version">{version()}</div>
  <div class="journey">
    commit &rarr; push &rarr; build &rarr; test &rarr; package &rarr; <b>deployed</b>
  </div>
  <div class="meta">
    commit <b>{sha}</b> &nbsp;&middot;&nbsp; pipeline run <b>#{run}</b><br>
    deployed automatically at <b>{built}</b><br>
    nobody touched a server
  </div>
</main>
</body>
</html>""")
