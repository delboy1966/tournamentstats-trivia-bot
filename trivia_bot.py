#!/usr/bin/env python3
"""
tournamentstats-trivia-bot
---------------------------
A minimal example of building on the TournamentStats API: generates
real multiple-choice trivia questions from World Cup / Euros top-scorer
data. Meant as a starting point, not a finished app - fork it, swap in
different endpoints (player careers, match results, awards), or wire
the output into a Discord bot, a quiz app, whatever.

Usage:
    pip install -r requirements.txt
    export RAPIDAPI_KEY=your-key-here      # free tier at rapidapi.com
    python trivia_bot.py
    python trivia_bot.py --competition euro --count 5
"""

import argparse
import os
import random
import sys

import requests

API_HOST = "tournamentstats-api.p.rapidapi.com"
BASE_URL = f"https://{API_HOST}/v1"


def fetch_top_scorers(competition: str, limit: int, api_key: str) -> list[dict]:
    """Pull the all-time top-scorers leaderboard for a competition."""
    response = requests.get(
        f"{BASE_URL}/{competition}/leaderboards/top-scorers",
        params={"limit": limit},
        headers={
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": API_HOST,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()["data"]

def make_question(scorers: list[dict]) -> str:
    """Turn two random leaderboard entries into a multiple-choice question."""
    a, b = random.sample(scorers, 2)
    correct = a if a["goals"] >= b["goals"] else b
    options = [a["common_name"], b["common_name"]]
    random.shuffle(options)

    lines = [
        f"Who scored more goals: {a['common_name']} ({a['team_name']}) or {b['common_name']} ({b['team_name']})?",
        *(f"  {chr(65 + i)}. {name}" for i, name in enumerate(options)),
        f"Answer: {correct['common_name']} ({correct['goals']} goals)",
    ]
    return "\n".join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate football trivia from the TournamentStats API")
    parser.add_argument("--competition", choices=["world-cup", "euro"], default="world-cup")
    parser.add_argument("--count", type=int, default=3, help="number of questions to generate")
    args = parser.parse_args()

    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        print("Set RAPIDAPI_KEY first - get a free key at https://rapidapi.com/tspencer1966-mZ9H3geS_7j/api/tournamentstats-api", file=sys.stderr)
        return 1

    scorers = fetch_top_scorers(args.competition, limit=20, api_key=api_key)
    if len(scorers) < 2:
        print("Not enough data returned to build a question.", file=sys.stderr)
        return 1

    for i in range(args.count):
        print(f"\nQ{i + 1}.")
        print(make_question(scorers))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
