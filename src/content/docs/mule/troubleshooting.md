---
title: Troubleshooting
description: Fixes for the problems students hit most often with MuleCode, Ollama and GitHub.
---

## "Ollama isn't answering" or connection refused on localhost:11434

Ollama isn't running. Open the Ollama app (look for its icon in the menu bar or system tray), then try again.

## `mule models local` doesn't list `local/coder`

The course config isn't in `~/.config/mulecode`. Redo step 3 of [Install mule](/start/install-mule/).

## "model not found" or "mule-coder" errors

The course model wasn't created. Redo step 3 of [Ollama and the model](/start/ollama/), then check with `ollama list`.

## The first answer takes a minute

That's normal: Ollama is loading the model into memory. Later answers are faster. If every answer is slow, close other heavy apps. The model needs several GB of free RAM.

## `operation not permitted` on a Mac

The sandbox blocked a write outside your project. See [When mule says no](/mule/sandbox/).

## The sprint sidebar is empty

Sign in to `gh` (step 5), and make sure you're inside your team's repository. If the board is missing, run `gh auth refresh -s project`.

## mule crashed

The crash screen offers to copy a report. Paste it in a message to the instructor, along with what you were doing.

## Still stuck?

Bring the exact error, and what you ran before it, to class.
