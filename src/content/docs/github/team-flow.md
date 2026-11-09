---
title: The team flow
description: From issue to merged pull request, the path every change takes in your team repo.
---

Every change takes the same path:

1. **Issue.** The work is a story, task or bug on your board, with an owner.
2. **Branch.** It's named `<issue number>-<short-name>`, e.g. `12-add-login`. In `mule`, `/next` does this for you.
3. **Commits.** Small, often, with clear messages.
4. **Pull request.** Open it early with `gh pr create`. Fill in the template: what and why, `Closes #12`, how you checked it, and how you used an agent (stage, iceberg link, what it got wrong).
5. **Review.** A teammate who didn't write it reads it, comments and approves.
6. **Merge.** Once CI is green and there's an approval, merge it. The issue closes itself.

## The rules on `main`

Every course repository protects `main`:

- changes reach it only through a pull request;
- a pull request needs one approval from someone other than its author;
- the `check` CI job has to pass;
- no force-pushes.

If GitHub won't let you merge, one of these isn't met yet. See [Reading CI](/github/ci/).
