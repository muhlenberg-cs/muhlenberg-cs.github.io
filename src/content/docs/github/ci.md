---
title: Reading CI
description: What the green check and red cross on a pull request mean, and how to find out why it failed.
---

CI (continuous integration) runs your project's checks on every pull request. In course repos, that's the `check` job, which runs `scripts/lint.sh` and `scripts/test.sh`.

- **Green check:** lint and tests passed. You can merge once someone approves.
- **Red cross:** something failed. Click **Details** next to `check`, open the failing step, and read the last lines of the log. That's where the actual error is.

Then reproduce it on your laptop with `bash scripts/test.sh` (or `lint.sh`), fix it, commit and push. CI runs again on its own.

Until your team fills them in during Sprint 0, both scripts only print a warning and pass.

Don't "fix" CI by deleting or weakening a test, and don't let an agent do it either. An iceberg makes that easy to spot.
