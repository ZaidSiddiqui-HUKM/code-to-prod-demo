# Code to Production — live demo repo

A tiny, self-contained project whose only purpose is to show a CI/CD pipeline
running live during **Session 1: Code to Production**. Push a change, and the
GitHub Actions graph draws the exact journey from the slides:

```
Build → Test → Package → Deploy
```

Nothing here touches any real production system. It runs entirely on GitHub's free
runners, so it's safe to run live and safe to run a hundred times.

---

## One-time setup (do this before the session)

1. Create a new **empty** repo — either in your organisation or your
   personal account. Call it something like `code-to-prod-demo`.
2. Push these files to it:
   ```bash
   git init
   git add .
   git commit -m "Initial demo pipeline"
   git branch -M main
   git remote add origin <your-new-repo-url>
   git push -u origin main
   ```
3. Open the **Actions** tab. The pipeline runs automatically on that first push.
   Wait for all four stages to go green. That confirms it works on your account.

That's it. You now have a working pipeline you fully control.

---

## Running it live during the session (your 3-minute demo)

**The live page:** https://zaidsiddiqui-hukm.github.io/code-to-prod-demo/
This is the real, public result of the pipeline. It is rebuilt from `app/main.py`
on every push, so the version on screen changes when you change the code.

**Before you start:** open three tabs — the **Actions** tab, the **live page**
above, and `app/main.py` in an editor. Show the live page first, on `1.0.0`,
so the audience sees the "before".

1. Say: *"I'm going to make a tiny change and we'll watch the journey we just
   drew — live."*
2. In `app/main.py`, change the version string in `version()` from `"1.0.0"`
   to `"1.0.1"`. (Any trivial change works — this one is safe and visible.)
3. Commit and push:
   ```bash
   git commit -am "Bump version to 1.0.1"
   git push
   ```
4. Switch to the **Actions** tab and click into the running workflow. Narrate
   each stage as it goes green:
   - *"There's the trigger — my push started it."*
   - *"Now it's building — turning our code into something runnable."*
   - *"Now tests are running… green. If they'd failed, it would stop right here."*
   - *"Now it's packaging into a container."*
   - *"Now deploying to Test."*
5. **The payoff.** Switch to the live page tab and refresh it. The version has
   changed to `1.0.1`. *"That page is built from the code I just edited. I never
   touched a server — the pipeline did all of it."*
6. Land it: *"That's the whole journey — automatic, in under a minute.
   Nobody touched a server. Nobody copied a file at 2am."*

---

## Optional: the "what happens when it breaks" moment (powerful, 1 min)

If you want to *show* the safety gate rather than just describe it:

1. In `app/main.py`, break the greeting on purpose — change
   `return f"Hello, {name}! ..."` to `return "Goodbye"`.
2. Commit and push. Watch **Test** go red and **Package** / **Deploy** never run.
3. Say: *"The bad code physically cannot reach deploy. The pipeline stopped it."*
4. Revert the change, push again, watch it go green.

Do this **only** if your live run is going smoothly and you have time — it's a
great beat but it adds risk. Rehearse it first.

---

## Backup plan

**Record the successful run beforehand** (screen-record the Actions graph going
green). If the live network dies or a runner is slow on the day, play the
recording and narrate over it — the audience can't tell the difference.

---

## What each file is (in case anyone asks)

| File | Which stage of the journey it is |
|---|---|
| `app/main.py` | The application — the code that makes the journey |
| `tests/test_main.py` | The **Test** stage — automated checks that stop bad code |
| `Dockerfile` | The **Package** stage — the recipe for the sealed container |
| `.github/workflows/pipeline.yml` | The pipeline itself — Build → Test → Package → Deploy |
| `conftest.py` | Lets the tests import the app. Without it the Test stage cannot even start |
| `scripts/render.py` | The **Deploy** stage — builds the live page from the app itself |
| `DEMO-COMMANDS.md` | Your copy/paste commands for demo day |

---

## Run it on your own laptop (optional, to rehearse)

```bash
python app/main.py          # runs the app on http://localhost:8000
pip install pytest && pytest -v   # runs the tests
```
