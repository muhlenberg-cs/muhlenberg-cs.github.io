---
title: Modes and stages
description: The four MuleCode modes, and the stages that unlock them during the semester.
---

MuleCode has four **modes**. Press <kbd>Tab</kbd> to switch between the ones you have. Your **stage** decides which modes those are, and it goes up as you show you understand what the agent did.

## Modes

| Mode | What it does |
|---|---|
| `sketch` | Reads code, asks clarifying questions and writes a plan to `plans/<name>.md`. It can't change anything else. When the plan is ready it asks whether to start building, and switches to your build mode if you say yes. |
| `pair` | Edits and creates files itself, but shows each diff and asks first (Allow once, Allow always, or Reject). At stage 0 it can't run shell commands and tells you the command to run instead. From stage 1 it asks before each one. It never pushes. |
| `build` | Edits without asking, and runs tests, lint and local git (status, diff, log, add, commit) on its own. Other commands ask first. It never pushes. |
| `solo` | Works on its own inside your repository. Pushing, creating or merging PRs and releasing are denied, and web access asks first. |

## Stages

| Stage | Modes you have | How you unlock it |
|---|---|---|
| 0 · Halter | sketch, pair (no shell) | Everyone starts here in week 1 |
| 1 · Lead rope | sketch, pair (shell asks first) | Iceberg Review #1, week 4 |
| 2 · Pack mule | + build | Your team's first spec and tests merged with CI green (week 7 check) |
| 3 · Open trail | + solo | Iceberg Review #2, weeks 12–13 |

You can edit and create files from week 1, in `pair`, approving each edit. Stages limit how much the agent does *without* you, not what you're allowed to build.

When you unlock a stage, the instructor gives you a block to paste into `~/.config/mulecode/opencode.json`. Then restart `mule`. Working above your stage is a process issue, not an integrity case, but your PR template and icebergs show which mode you used.

## Why stages?

An agent that edits and runs commands on its own is fast, and fast at being wrong. The stages make sure you can read and judge what it did before it does more without asking. That's also how professional teams adopt these tools.
