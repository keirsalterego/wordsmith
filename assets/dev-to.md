# Wordsmith: a password generator that doesn't use `random`

A year into building security tools I noticed most wordlist generators dump every permutation of every word from SecLists or ship a dependency tree the size of a browser. I wanted something I could audit in one sitting. So I wrote wordsmith.

**Password mode** uses Python's `secrets` module to generate random passwords. Pick length and charset (lower, upper, digits, symbols, or all). No `random`, no seed to crack.

```
python wordsmith.py --mode password --length 20 --charset all
# F7{53=J'~$c<Y%bz
```

**Wordlist mode** takes base words (names, dates, keywords) and builds permutations: case variants, leet substitutions, length filtering. Output to stdout or a file.

```
python wordsmith.py -w keir,2024 -l -m 4 -M 16 -o wordlist.txt
```

The `secrets` vs `random` thing matters. `random` is deterministic: know the seed, know every password. `secrets` pulls from the OS entropy pool. One line change, huge difference.

**Defensive take:** length beats complexity. `secrets` with 20 chars from `ascii_letters + digits + punctuation` is about 130 bits of entropy.

---

Repo: [github.com/keirsalterego/wordsmith](https://github.com/keirsalterego/wordsmith)
