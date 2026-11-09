#!/usr/bin/env python3
"""Copy published course PDFs from the local Google Drive folder into the site.

    python3 scripts/sync-from-drive.py           # show what would be copied
    python3 scripts/sync-from-drive.py --copy    # copy it

Drive stays the source of truth. This copies only:
  Schedule/W<NN> .../W<NN>-T *.pdf and W<NN>-R *.pdf  ->  public/decks/W<NN>-T.pdf, W<NN>-R.pdf
  Syllabus/370.syllabus.s27.pdf                       ->  public/syllabus.pdf
Older-format files (e.g. "W02 Clustering.pdf") are skipped.

The site is public. Before pushing, open each new PDF and check it has no student names,
grades or instructor-only notes. A deck that has them stays in Drive.
Override the Drive folder with CUE_DRIVE=/path/to/CUE.
"""
import os
import re
import shutil
import sys
from pathlib import Path

DRIVE = Path(
    os.environ.get(
        "CUE_DRIVE",
        "~/Library/CloudStorage/GoogleDrive-hamedyaghoobian@muhlenberg.edu/My Drive/Courses/27 Spring/CUE",
    )
).expanduser()
SITE = Path(__file__).resolve().parent.parent
DECK = re.compile(r"^(W\d\d-[TR]) .+\.pdf$")
# Anything that looks private never gets copied, whatever folder it's in.
PRIVATE = re.compile(r"roster|grade|student|feedback|private|answer", re.IGNORECASE)


def main(copy: bool):
    if not DRIVE.is_dir():
        sys.exit(f"No Drive folder at {DRIVE} (set CUE_DRIVE)")
    pairs = [
        (pdf, SITE / "public/decks" / f"{match.group(1)}.pdf")
        for pdf in sorted((DRIVE / "Schedule").glob("W*/*.pdf"))
        if (match := DECK.match(pdf.name))
    ]
    syllabus = DRIVE / "Syllabus/370.syllabus.s27.pdf"
    if syllabus.exists():
        pairs.append((syllabus, SITE / "public/syllabus.pdf"))
    for source, dest in pairs:
        if PRIVATE.search(source.name):
            print(f"skip (looks private): {source.relative_to(DRIVE)}")
            continue
        same = dest.exists() and dest.read_bytes() == source.read_bytes()
        print(f"{'same' if same else 'copy'}: {source.relative_to(DRIVE)} -> {dest.relative_to(SITE)}")
        if copy and not same:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, dest)
    if not copy:
        print("\nDry run. Re-run with --copy, then open each new PDF before pushing.")


if __name__ == "__main__":
    main("--copy" in sys.argv)
