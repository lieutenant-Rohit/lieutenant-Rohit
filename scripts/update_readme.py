#!/usr/bin/env python3
"""
Fetches live LeetCode stats for a given username and rewrites the block
between <!--LEETCODE:START--> and <!--LEETCODE:END--> markers in README.md.

Run manually:
    python scripts/update_readme.py rohit316

Runs automatically via .github/workflows/update-readme.yml on a daily
schedule and on manual dispatch.
"""

import re
import sys
from datetime import datetime, timezone

import requests

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

QUERY = """
query userProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
    }
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""


def fetch_stats(username: str) -> dict:
    resp = requests.post(
        LEETCODE_GRAPHQL_URL,
        json={"query": QUERY, "variables": {"username": username}},
        headers={"Content-Type": "application/json", "Referer": "https://leetcode.com"},
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()["data"]["matchedUser"]
    if data is None:
        raise RuntimeError(f"LeetCode user '{username}' not found")

    counts = {c["difficulty"]: c["count"] for c in data["submitStatsGlobal"]["acSubmissionNum"]}
    return {
        "total": counts.get("All", 0),
        "easy": counts.get("Easy", 0),
        "medium": counts.get("Medium", 0),
        "hard": counts.get("Hard", 0),
        "ranking": data["profile"]["ranking"],
    }


def render_block(stats: dict, username: str) -> str:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return (
        "<!--LEETCODE:START-->\n"
        "```text\n"
        f"$ leetcode --profile {username}\n"
        f"Solved     : {stats['total']} problems\n"
        f"  Easy     : {stats['easy']}\n"
        f"  Medium   : {stats['medium']}\n"
        f"  Hard     : {stats['hard']}\n"
        f"Global rank: {stats['ranking']:,}\n"
        f"Updated    : {updated}\n"
        "```\n"
        "<!--LEETCODE:END-->"
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: update_readme.py <leetcode-username>", file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1]
    stats = fetch_stats(username)
    new_block = render_block(stats, username)

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r"<!--LEETCODE:START-->.*?<!--LEETCODE:END-->", re.DOTALL)
    if not pattern.search(content):
        print("No <!--LEETCODE:START--> ... <!--LEETCODE:END--> markers found in README.md", file=sys.stderr)
        sys.exit(1)

    content = pattern.sub(new_block, content)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md updated with latest LeetCode stats.")


if __name__ == "__main__":
    main()