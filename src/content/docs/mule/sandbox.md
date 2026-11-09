---
title: When mule says no
description: Why MuleCode sometimes refuses or blocks something, and what to do about it.
---

There are two kinds of "no": a **permission**, decided by your stage and mode, and the **sandbox**, a wall around the commands the agent runs.

## Permissions

Each mode allows, asks about or denies each kind of action. In `pair` at stage 0, shell commands are denied, so the agent tells you the command to run yourself. A denial isn't an error. It means *you* are in the loop for that step. If you think a rule is wrong for your team, raise it in class rather than working around it.

`--yolo`, `--auto` and `--dangerously-skip-permissions` are turned off in MuleCode.

## The sandbox (macOS)

On a Mac, every shell command the agent runs can only **write** inside your project, temp folders and package-manager caches. Reading files and using the network still work, so `git fetch`, `npm install` and `pip install` in a virtual environment are fine.

When the sandbox blocks a command you'll see `operation not permitted`, the agent is told the sandbox probably blocked it, and `/iceberg` marks the call. Don't ask the agent to retry the same write. Either do the work inside the project, or do the outside step yourself after reading what it does.

The sandbox doesn't protect the files *inside* your project. Commit often, and push to GitHub: that's your backup.

On Windows there's no sandbox, only permissions. Read each command before you approve it.
