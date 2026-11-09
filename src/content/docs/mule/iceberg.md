---
title: Icebergs
description: What an iceberg records, how to read one, and what to check before you commit it.
---

The chat is the tip. An **iceberg** is everything underneath: what the model was told, what it did, and what it was allowed to do. You link one from every pull request that merges agent work, and two graded reviews ask you to explain one.

## What it records

- Your request, the agent's text, each tool call with its input and output, edit diffs, the files changed, and tokens at each step.
- The system prompt the model was given, including your AGENTS.md exactly as it saw it, and the list of tools it could use.
- Every permission decision at the tool call it belongs to: what a rule allowed or denied without asking you, what the agent asked, and what you answered.
- Whether the macOS sandbox was on, and which commands it probably blocked.

It records what happened, not *why* the model chose it. The model's reasons are only as visible as its own text.

## Saving and reading one

- In `mule`, run `/iceberg` to see the current session. Press `s` for the full system prompt and `e` to save it to `icebergs/`.
- For a saved file, `python3 scripts/iceberg_print.py icebergs/<file>.json` prints it step by step. Add `--full` for everything.
- Name files `<YYYY-MM-DD>-<topic>.json` and link them from the PR.

## Things worth noticing

- **A claim with no tool call under it.** A model can say "I ran the tests" without running anything. The iceberg shows whether a tool call actually happened.
- **The context bar.** When the context fills up, the model starts forgetting the start of the conversation.
- **Silent decisions.** A rule allowed or denied a call without asking you. Was that what you expected?

## Before you commit one

Read it first. It holds every file the agent read and every command's output, so don't commit one that contains a password, API key or token.
