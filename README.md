# Wordsmith: a password generator that doesn't use `random`

A CLI password and wordlist generator for security research and ethical hacking.

**Dual-mode:** generate cryptographically-random passwords or build targeted wordlists from base words with case variants and leet speak transformations.

## Installation

```bash
git clone https://github.com/keirsalterego/wordsmith.git
cd wordsmith
```

No dependencies — uses only Python standard library.

## Usage

### Password mode

Generate a random password with `secrets`:

```bash
python wordsmith.py --mode password --length 20 --charset all
```

Charset options: `all`, `lower`, `upper`, `digits`, `symbols`.

### Wordlist mode

Build a wordlist from base words:

```bash
python wordsmith.py -w keir,2024 -l -m 4 -M 16 -o wordlist.txt
```

### Options

| Flag | Long Flag   | Description                                                 | Default    |
| ---- | ----------- | ----------------------------------------------------------- | ---------- |
| `-w` | `--words`   | Comma-separated base words                                  | Required\* |
| `-l` | `--leet`    | Enable leet speak (a→4, e→3, i→1, o→0, s→5)                 | False      |
| `-m` | `--min`     | Minimum candidate length                                    | 4          |
| `-M` | `--max`     | Maximum candidate length                                    | 12         |
| `-o` | `--output`  | Write wordlist to file instead of stdout                    | —          |
| `-L` | `--length`  | Password length (password mode only)                        | 16         |
|      | `--mode`    | `password` or `wordlist`                                    | wordlist   |
|      | `--charset` | Character set: `all`, `lower`, `upper`, `digits`, `symbols` | all        |
| `-h` | `--help`    | Show help                                                   | —          |

\* Required in wordlist mode only.

## Edge cases handled

- `--length 0` or negative → clean usage error, not a traceback
- Empty charset → `ValueError` with a clear message
- Missing `--words` in wordlist mode → `parser.error`

## Why `secrets` over `random`

Python's `random` module is deterministic — anyone who learns the seed can reproduce every "random" value. `secrets` uses OS-provided cryptographic randomness. Never use `random` for passwords. This distinction is a real infosec interview question.

## Writeup

### Wordsmith: a password generator that doesn't use `random`

A year into building security tools I noticed most wordlist generators dump every permutation of every word from SecLists or ship a dependency tree the size of a browser. I wanted something I could audit in one sitting. So I wrote wordsmith.

**Password mode** uses Python's `secrets` module to generate random passwords. Pick length and charset (lower, upper, digits, symbols, or all). No `random`, no seed to crack.

```bash
python wordsmith.py --mode password --length 20 --charset all
# F7{53=J'~$c<Y%bz
```

**Wordlist mode** takes base words (names, dates, keywords) and builds permutations: case variants, leet substitutions, length filtering. Output to stdout or a file.

```bash
python wordsmith.py -w keir,2024 -l -m 4 -M 16 -o wordlist.txt
```

The `secrets` vs `random` thing matters. `random` is deterministic: know the seed, know every password. `secrets` pulls from the OS entropy pool. One line change, huge difference.

**Defensive take:** length beats complexity. `secrets` with 20 chars from `ascii_letters + digits + punctuation` is about 130 bits of entropy.
