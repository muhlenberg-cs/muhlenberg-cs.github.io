---
title: Commands
description: The slash commands MuleCode adds for the course, and when to use each.
---

Type these at the `mule` prompt. They work in every mode. The ones that change files still follow your mode's permissions.

| Command | What it does | First used |
|---|---|---|
| `/spec` | Drafts a spec (PRD) from a user story into `specs/` | Week 3 |
| `/plan` | Research, propose, plan: writes a plan for a change into `plans/` | Week 6 |
| `/test-first` | Writes failing tests for a behaviour before anyone implements it | Week 5 |
| `/review` | Reviews your current diff with a read-only reviewer agent | Week 8 |
| `/secure` | A security pass over the repo or your diff: secrets, injection, dependencies | Week 10 |
| `/standup` | Drafts today's standup from git history and the sprint board | Sprint 1 |
| `/retro` | Drafts the sprint report and retrospective from git and the board | Sprint 1 |
| `/next` | Lists your assigned issues, switches to the issue's branch and puts the issue in the prompt | Sprint 1 |
| `/iceberg` | Shows everything below the chat for this session. `e` saves it to `icebergs/` | Week 1 |
| `/theme` | Picks one of seven color themes | Any time |

Drafts are drafts. `/standup`, `/retro` and `/review` only read your repo and GitHub, and they're wrong whenever the board is wrong. Fix them before you use them.
