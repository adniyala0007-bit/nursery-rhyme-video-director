#!/usr/bin/env python3
"""Create a blank episode brief using only Python's standard library."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "episode.md"
EPISODES = ROOT / "episodes"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("Title must contain at least one letter or number.")
    return slug


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, help="Episode ID, for example ep-002")
    parser.add_argument("--title", required=True, help="Episode title")
    parser.add_argument("--runtime", default="2:00", help="Target runtime (default: 2:00)")
    parser.add_argument("--language", default="English", help="Episode language")
    args = parser.parse_args()

    episode_id = slugify(args.id)
    slug = slugify(args.title)
    folder = EPISODES / f"{episode_id}-{slug}"
    destination = folder / "episode.md"
    if destination.exists():
        parser.error(f"Episode already exists: {destination.relative_to(ROOT)}")

    template = TEMPLATE.read_text(encoding="utf-8")
    content = (
        template.replace("[Episode Title]", args.title)
        .replace("[ep-000]", episode_id)
        .replace("2:00", args.runtime)
        .replace("English (change if needed)", f"{args.language} (change if needed)")
    )
    folder.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
