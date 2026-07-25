# TournamentStats Trivia Bot

A small example of building on the [TournamentStats API](https://tournamentstats.co.uk) — generates real multiple-choice football trivia questions from World Cup and Euros top-scorer data.

```
Q1.
Who scored more goals: Pelé (Brazil) or Miroslav Klose (Germany)?
  A. Miroslav Klose
  B. Pelé
Answer: Miroslav Klose (16 goals)
```

This is meant as a starting point, not a finished app. Fork it, swap in a different endpoint (player careers, match results, awards, head-to-head records), or wire the output into a Discord bot, a quiz app, a newsletter — whatever you're building.

## Quick start

```bash
git clone https://github.com/delboy1966/tournamentstats-trivia-bot
cd tournamentstats-trivia-bot
pip install -r requirements.txt

export RAPIDAPI_KEY=your-key-here   # free tier, no card required
python trivia_bot.py
```

Get a free API key at [rapidapi.com/tspencer1966-mZ9H3geS_7j/api/tournamentstats-api](https://rapidapi.com/tspencer1966-mZ9H3geS_7j/api/tournamentstats-api).

## Options

```bash
python trivia_bot.py --competition euro --count 5
```

`--competition` is `world-cup` (default) or `euro`. `--count` sets how many questions to generate.

## About the API

TournamentStats covers every FIFA World Cup since 1930 and every UEFA European Championship since 1960 — matches, squads, players, stats, awards, and officials, all under one consistent schema. Full docs: [tournamentstats.co.uk](https://tournamentstats.co.uk).

TournamentStats is an independent project and is not affiliated with, endorsed by, or sponsored by FIFA, UEFA, or any national football association.

## License

MIT — see [LICENSE](LICENSE).
