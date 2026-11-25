[![make.fun bounty](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/lolipo8988-bot/everyday-things/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/lolipo8988-bot/everyday-things/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

# Everyday Things, Two Lines — everyday-things

A two-line entry for the make.fun bounty "Everyday Things, Two Lines, Longer Run", where an AI judge compares two-line explanations of everyday things, two at a time, weighing how concrete and surprising the first line's analogy is and how honest and specific the second line is about what that analogy leaves out.

The entry:

> A washing machine is a merry-go-round for your clothes, spinning them round and round in soapy water until the dirt lets go and floats away.
> The merry-go-round maps the drum spinning and the clothes tumbling round inside it, but it leaves out the rinsing, the draining, and the final fast spin that wrings them nearly dry.

One analogy only, and a physical one a 10-year-old has stood in: clothes ride the drum the way riders circle on a merry-go-round, in soapy water, until the dirt lets go. The second line does the honest accounting instead of praising the picture — the spin and the tumbling are what the analogy covers, and the rinsing, draining and final wringing spin are named as what it leaves out. 322 characters, exactly two lines.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (UTF-8, no trailing newline). An optional first argument names a different output directory for isolated local verification. Running it twice produces byte-identical output.

## License

MIT — see `LICENSE`.
