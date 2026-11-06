"""EPUB Meta Edit — Read and set title and author on an EPUB file."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='epub_meta_edit',
        description='Read and set title and author on an EPUB file.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('EPUB Meta Edit')
    print('Fix EPUB metadata without a Calibre stack.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# revisit later (2026-11-03)
# minor adjust (2026-11-03)
# small fix (2026-11-03)
# tweak (2026-11-04)
# tune (2026-11-05)
# refactor bit (2026-11-05)
# refactor bit (2026-11-05)
# tweak (2026-11-05)
# refactor bit (2026-11-06)
