---
title: Git in one page
description: The handful of git commands you need for this course, and what each one is for.
---

Git keeps the history of your project. GitHub is where your team shares it.

| You want to | Run |
|---|---|
| Get your team's repo onto your laptop | `git clone <url>` |
| See what changed | `git status` and `git diff` |
| Get your teammates' latest work | `git switch main` then `git pull` |
| Start work on issue 12 | `git switch -c 12-add-login` (or `/next` in mule) |
| Save a step | `git add <files>` then `git commit -m "Add login form"` |
| Share your branch | `git push -u origin 12-add-login` |
| Open a pull request | `gh pr create` |

Commit small and often, with a message that says what changed. You never push to `main` directly: every change reaches `main` through a pull request. See [the team flow](/github/team-flow/).
