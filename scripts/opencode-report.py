#!/usr/bin/env python3
"""Print a privacy-preserving report from OpenCode's local SQLite database."""

import argparse
import json
import os
import sqlite3
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--db",
        default=os.path.expanduser("~/.local/share/opencode/opencode.db"),
        help="OpenCode SQLite database path",
    )
    parser.add_argument("--directory", help="Only include sessions in this directory")
    parser.add_argument(
        "--since",
        type=date.fromisoformat,
        help="Only include sessions created on or after YYYY-MM-DD",
    )
    return parser.parse_args()


def model_parts(raw_model):
    try:
        model = json.loads(raw_model or "{}")
    except json.JSONDecodeError:
        model = {}
    provider = model.get("providerID", "unknown")
    model_id = model.get("id", "unknown")
    return provider, model_id


def fmt_tokens(value):
    return f"{value:,}"


def main():
    args = parse_args()
    if not os.path.isfile(args.db):
        raise SystemExit(f"Database not found: {args.db}")

    query = """
        SELECT agent, model, cost, tokens_input, tokens_output,
               tokens_reasoning, tokens_cache_read, tokens_cache_write,
               time_created, time_updated, directory
        FROM session
        WHERE time_created IS NOT NULL
    """
    params = []
    if args.directory:
        query += " AND directory = ?"
        params.append(args.directory)
    if args.since:
        query += " AND time_created >= ?"
        params.append(int(datetime.combine(args.since, datetime.min.time(), timezone.utc).timestamp() * 1000))
    query += " ORDER BY time_created"

    try:
        connection = sqlite3.connect(f"file:{os.path.abspath(args.db)}?mode=ro", uri=True)
        connection.row_factory = sqlite3.Row
        rows = connection.execute(query, params).fetchall()
    except sqlite3.Error as error:
        raise SystemExit(f"Could not read database in read-only mode: {error}") from error
    finally:
        if "connection" in locals():
            connection.close()

    period = args.since.isoformat() if args.since else "all available sessions"
    print("# OpenCode usage report")
    print(f"\nPeriod: **{period}**")
    if args.directory:
        print(f"Directory: `{args.directory}`")
    print("\n> Privacy: this report reads the local database in read-only mode and never prints prompts, titles, or session contents.")

    if not rows:
        print("\nNo matching sessions.")
        return

    total_cost = sum(row["cost"] or 0 for row in rows)
    total_tokens = sum(
        (row["tokens_input"] or 0)
        + (row["tokens_output"] or 0)
        + (row["tokens_reasoning"] or 0)
        + (row["tokens_cache_read"] or 0)
        + (row["tokens_cache_write"] or 0)
        for row in rows
    )
    durations = [
        max(0, (row["time_updated"] - row["time_created"]) / 60000)
        for row in rows
        if row["time_updated"] and row["time_created"]
    ]
    print("\n## Summary")
    print(f"- Sessions: **{len(rows)}**")
    print(f"- Projects/directories: **{len({row['directory'] for row in rows})}**")
    print(f"- Recorded cost: **{total_cost:.4f}**")
    print(f"- Total tokens (including cache): **{fmt_tokens(total_tokens)}**")
    if durations:
        print(f"- Average session elapsed lifetime: **{sum(durations) / len(durations):.1f} minutes**")

    by_agent = defaultdict(lambda: {"sessions": 0, "cost": 0.0, "tokens": 0})
    by_model = defaultdict(lambda: {"sessions": 0, "cost": 0.0, "tokens": 0})
    for row in rows:
        tokens = sum((row[key] or 0) for key in (
            "tokens_input", "tokens_output", "tokens_reasoning",
            "tokens_cache_read", "tokens_cache_write"))
        agent = row["agent"] or "unknown"
        provider, model_id = model_parts(row["model"])
        model = f"{provider}/{model_id}"
        for bucket, key in ((by_agent, agent), (by_model, model)):
            bucket[key]["sessions"] += 1
            bucket[key]["cost"] += row["cost"] or 0
            bucket[key]["tokens"] += tokens

    print("\n## By agent")
    print("\n| Agent | Sessions | Recorded cost | Tokens |\n|---|---:|---:|---:|")
    for key, value in sorted(by_agent.items()):
        print(f"| `{key}` | {value['sessions']} | {value['cost']:.4f} | {fmt_tokens(value['tokens'])} |")

    print("\n## By model")
    print("\n| Model | Sessions | Recorded cost | Tokens |\n|---|---:|---:|---:|")
    for key, value in sorted(by_model.items()):
        print(f"| `{key}` | {value['sessions']} | {value['cost']:.4f} | {fmt_tokens(value['tokens'])} |")


if __name__ == "__main__":
    main()
