
# Wordsmith

> A smart, customizable CLI tool for generating targeted password wordlists.

Wordsmith is a Python-based, modular wordlist generator designed for security researchers and ethical hackers. It takes a handful of base words (like names, dates, or pet names) and automatically generates hundreds of smart permutations using case transformations, leet speak, and combinatorics.

## Features

- Smart Transformations: Automatically generates uppercase, lowercase, and capitalized versions of base words.
- Leet Speak Engine: Swaps common letters for numbers/symbols (e.g., password -> p4$$w0rd).
- Combinatorics (WIP): Intelligently combines words and numbers using common separators (-, _, .).
- Granular Filtering: Specify minimum and maximum lengths to keep your wordlists focused and efficient.
- Modular Architecture: Built with a clean, extensible backend design.

## Installation

Clone the repository and run it directly using Python 3:

```bash
git clone [https://github.com/keroxlabs/wordsmith.git](https://github.com/keroxlabs/wordsmith.git)
cd wordsmith

```

Note: Wordsmith uses only Python standard libraries, so there are no requirements.txt to install.

## Usage

Wordsmith operates entirely from the command line.

Basic Usage:
Provide a comma-separated list of target words:

```bash
python wordsmith.py -w yuvraj,biswal,2005

```

Advanced Usage (with flags):
Enable Leet Speak (-l) and set a strict password length constraint (min 8, max 16):

```bash
python wordsmith.py -w yuvraj,biswal,2005 -l -m 8 -M 16

```

### Options

| Flag | Long Flag | Description | Default |
| --- | --- | --- | --- |
| -w | --words | Comma-separated base words | Required |
| -m | --min | Minimum password length | 4 |
| -M | --max | Maximum password length | 12 |
| -l | --leet | Enable leet speak transformations | False |
| -h | --help | Show the help message and exit | - |

## Architecture

Wordsmith is built with a modular data pipeline, inspired by professional offensive security tools:

1. Transformers: Mutates single strings (Case switching, Leet Speak).
2. Combinators: Mixes different base words and separators together.
3. Filters: Removes duplicates and enforces min/max length constraints.
4. I/O Engine: Efficiently writes the final output to disk.
