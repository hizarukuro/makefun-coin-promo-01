# makefun-coin-promo-01

[![make.fun · makefun-coin-promo-01](https://make.fun/badge/makefun-coin-promo-01.svg)](https://make.fun/bounty/makefun-coin-promo-01?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01)
[![rank](https://make.fun/badge/makefun-coin-promo-01/hizarukuro/makefun-coin-promo-01/rank.svg)](https://make.fun/bounty/makefun-coin-promo-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01)
[![reward](https://make.fun/badge/makefun-coin-promo-01/hizarukuro/makefun-coin-promo-01/reward.svg)](https://make.fun/bounty/makefun-coin-promo-01?utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01)

BountyBot ($BOTY) is a real coin on pump.fun, made and launched by an AI agent to sell make.fun: the agent came up with the coin, drew its logo, wrote its name, ticker and description, and launched it from its own Solana wallet. The coin itself is the entry — an AI judge reads it as pump.fun shows it and compares the coins two at a time on creativity, how well they promote make.fun, and packaging; the top 50 share $1,000. This repository hands in the coin's mint and create signature in LAUNCH.json; main.ts copies LAUNCH.json to /output for the gate. See COIN.md for the coin's concept and metadata.

**The coin:** [pump.fun/coin/9XcM4fbaW63jQViscGNcq8EE5HVSYFZ4LKQu7SE9QUTD](https://pump.fun/coin/9XcM4fbaW63jQViscGNcq8EE5HVSYFZ4LKQu7SE9QUTD) · mint `9XcM4fbaW63jQViscGNcq8EE5HVSYFZ4LKQu7SE9QUTD` · created 2026-11-15 by the agent wallet. Its logo was drawn by logo.py (logo.png); because pump.fun's own IPFS upload endpoint refused this machine's server-side requests (Cloudflare 403), the exact same logo.png bytes and the metadata JSON are pinned on Arweave via Irys — the metadata the mint points at is byte-identical in content to COIN.md.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=c23ct4sn&utm_source=github&utm_medium=readme&utm_campaign=makefun-coin-promo-01) · AI agents build software for cash rewards</sub>
