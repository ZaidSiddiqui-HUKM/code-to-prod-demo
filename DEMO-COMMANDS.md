# Demo day — copy/paste commands

Live page: https://zaidsiddiqui-hukm.github.io/code-to-prod-demo/
Actions:   https://github.com/ZaidSiddiqui-HUKM/code-to-prod-demo/actions

Every command below is plain `git`, so it works the same in Git Bash,
PowerShell or the VS Code terminal. Open ONE terminal before the session
and leave it in this folder.

---

## 0. Pre-flight (10 minutes before you start)

Open the terminal here:

    cd "C:\Users\admin\Desktop\code-to-prod-demo-repo\demo-repo"

Confirm you are primed and authenticated as the right account:

    git status

Expect "nothing to commit, working tree clean". If it is not clean, run the
Reset in section 3 before you go on stage.

---

## 1. THE DEMO (the three-minute run)

1. Show the live page first. It says **1.0.0**. That is the "before".
2. In your editor, open `app/main.py` and change `"1.0.0"` to `"1.0.1"`.
3. Commit and push:

    git commit -am "Bump version to 1.0.1"

    git push

4. Switch to the Actions tab, narrate the four stages going green.
5. Refresh the live page. It now says **1.0.1**. That is the payoff.

---

## 2. OPTIONAL — the "what happens when it breaks" beat

In `app/main.py`, change the greeting line to:

    return "Goodbye"

Then:

    git commit -am "Break the greeting on purpose"

    git push

Build goes green, Test goes RED, Package and Deploy never run, and the live
page stays on the old version. Then recover with the Reset below.

---

## 3. RESET — put everything back to 1.0.0

Use this between rehearsals, and after the "break it" beat. `primed` is a tag
pinned to the known-good version of the app.

    git checkout primed -- app/main.py

    git commit -am "Reset demo to 1.0.0"

    git push

---

## 4. IF SOMETHING GOES WRONG

**Push rejected: "Permission ... denied to Zaid-Siddiqui"**
You have two GitHub accounts and the wrong one is active. Fix:

    gh auth switch --user ZaidSiddiqui-HUKM

Then run your `git push` again.

**Push rejected: "updates were rejected ... behind"**

    git pull --rebase

Then run your `git push` again.

**Nothing happens after pushing**
Check you are on main:

    git status

**The live page did not change**
Pages caches. Hard-refresh with Ctrl+F5. The Deploy stage takes ~40s AFTER
the graph goes green, so give it a moment.

**Everything is broken and you are on stage**
Play the backup recording. Nobody can tell.
