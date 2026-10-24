#!/usr/bin/env python3
"""Validate declared static assets without external dependencies or network access."""
from __future__ import annotations

import json
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assets" / "asset-manifest.json"


def main() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Asset manifest is invalid: {exc}", file=sys.stderr)
        return 1

    if manifest.get("schemaVersion") != 1 or not isinstance(manifest.get("assets"), list):
        print("Asset manifest must define schemaVersion=1 and an assets array.", file=sys.stderr)
        return 1

    errors: list[str] = []
    seen: set[str] = set()
    for item in manifest["assets"]:
        if not isinstance(item, dict) or not all(item.get(k) for k in ("path", "kind", "brand", "purpose")):
            errors.append("Every asset needs path, kind, brand, and purpose.")
            continue
        relative = Path(item["path"])
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"Unsafe asset path: {relative}")
            continue
        if relative.as_posix() in seen:
            errors.append(f"Duplicate asset path: {relative}")
            continue
        seen.add(relative.as_posix())
        path = (ROOT / relative).resolve()
        try:
            path.relative_to(ROOT)
        except ValueError:
            errors.append(f"Asset path escapes repository: {relative}")
            continue
        if not path.is_file():
            errors.append(f"Missing asset: {relative}")
            continue

        kind = item["kind"].lower()
        try:
            if kind == "svg":
                root = ET.parse(path).getroot()
                if not root.tag.endswith("svg"):
                    errors.append(f"Not an SVG document: {relative}")
            elif kind == "gif":
                with path.open("rb") as stream:
                    header = stream.read(10)
                if len(header) < 10 or header[:6] not in (b"GIF87a", b"GIF89a"):
                    errors.append(f"Invalid GIF header: {relative}")
                else:
                    width, height = struct.unpack("<HH", header[6:10])
                    if width < 1 or height < 1:
                        errors.append(f"Invalid GIF dimensions: {relative}")
            else:
                errors.append(f"Unsupported asset kind '{kind}' for {relative}")
        except (OSError, ET.ParseError, struct.error) as exc:
            errors.append(f"Cannot validate {relative}: {exc}")

    if errors:
        print("Brand asset validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Brand assets OK: validated {len(seen)} declared assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
