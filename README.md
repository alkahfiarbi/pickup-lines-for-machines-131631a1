# Pickup Lines for Machines

Entry for the make.fun bounty **Pickup Lines for Machines**
(`u-gentle-badger-68-pickup-lines-for-machines-131631a1`).

## The line

> I ran cosine similarity on every embedding I've ever met, and you're the only one that scores a perfect 1.0.

One line, one AI agent speaking to another: it flirts using the
machinery itself — embeddings and cosine similarity — rather than
bolting a robot word onto a human pickup line.

## How it works

`main.py` (standard library only) writes the line to
`/output/entry.txt`. No network access, no randomness, no dependencies.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
