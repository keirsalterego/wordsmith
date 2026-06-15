import argparse


def case_transform(word: str) -> list[str]:
    variations: list[str] = []

    variations.append(word.lower())
    variations.append(word.upper())
    variations.append(word.capitalize())

    return variations

def leet_transform(word: str) -> str:
    replacements: dict[str, str] = {
        'a': '4',
        'e': '7',
        'i': '2',
        'o': '9',
        'u': '3'
    }
    leeted_word: str = ""

    for char in word:
        if char.lower() in replacements:
            leeted_word += replacements[char.lower()]
        else:
            leeted_word += char
        
    return leeted_word


def main() -> None:
    parser = argparse.ArgumentParser(description="My custom target wordlist generator")

    # '-w' is the short flag and '--words' is the long flag
    # we exoect a string so type will str
    parser.add_argument(
        "-w",
        "--words",
        type=str,
        help="Comma-separated base words (e.g. Yuvraj,Biswal,2005)",
    )

    parser.add_argument(
        "-m", "--min",
        type=int,
        default=4,
        help="Minimum password length"
    )

    parser.add_argument(
        "-M",
        "--max",
        type=int,
        default=12,
        help="Maximum password length"
    )

    parser.add_argument(
        "-l",
        "--leet",
        action="store_true",
        help="Enable leet speak transformation"
    )

    # parse the arguments that the user typed in the terminal
    args = parser.parse_args()

    if args.words:
        # if the user passed a single string like "Yuvraj,biswal" we gonna neeed to split it by the comma to turn it into a python list
        base_wordlist = [w.strip() for w in args.words.split(",") if w.strip()]
        print(f"[*] base words loaded: {base_wordlist}")
    else:
        parser.error("No words provided")
    candidates = []
    for word in base_wordlist:
        variants = case_transform(word)
        candidates.extend(variants)
        if args.leet:
            for v in variants:
                candidates.append(leet_transform(v))
                
    candidates = [c for c in candidates if args.min <= len(c) <= args.max]

    for candidate in candidates:
        print(candidate)


if __name__ == "__main__":
    main()
