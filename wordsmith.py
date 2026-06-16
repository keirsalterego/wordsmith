import secrets
import string
import argparse


def case_transform(word: str) -> list[str]:
    variations: list[str] = []

    variations.append(word.lower())
    variations.append(word.upper())
    variations.append(word.capitalize())

    return variations


# leet_transform is deterministic
def leet_transform(word: str) -> str:
    replacements: dict[str, str] = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
    leeted_word: str = ""

    for char in word:
        if char.lower() in replacements:
            leeted_word += replacements[char.lower()]
        else:
            leeted_word += char

    return leeted_word


def generate_password(length: int, charset: str) -> str:
    pool = ""
    if charset == "all":
        pool = string.ascii_letters + string.digits + string.punctuation
    elif charset == "lower":
        pool = string.ascii_lowercase
    elif charset == "upper":
        pool = string.ascii_uppercase
    elif charset == "digits":
        pool = string.digits
    elif charset == "symbols":
        pool = string.punctuation
    else:
        raise ValueError(f"Unknown charset: {charset}")
    if not pool:
        raise ValueError("Empty charset - no characters to choose from")
    return "".join(secrets.choice(pool) for _ in range(length))


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
        "-m", "--min", type=int, default=4, help="Minimum password length"
    )

    parser.add_argument(
        "-M", "--max", type=int, default=12, help="Maximum password length"
    )

    parser.add_argument(
        "-l", "--leet", action="store_true", help="Enable leet speak transformation"
    )

    parser.add_argument(
        "--mode",
        type=str,
        default="wordlist",
        choices=["password", "wordlist"],
        help="Generation mode: password or wordlist",
    )

    parser.add_argument(
        "--length",
        "-L",
        type=int,
        default=16,
        help="password length (used in password mode)",
    )

    parser.add_argument(
        "--charset",
        type=str,
        default="all",
        choices=["all", "lower", "upper", "digits", "symbols"],
        help="character set for password generation",
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Write the wordlist to file instead of stdout"
    )

    # parse the arguments that the user typed in the terminal
    args = parser.parse_args()

    if args.length < 1:
        parser.error("Length must be atleast 1")
    if args.mode == "password":
        password = generate_password(args.length, args.charset)
        print(password)
        return

    if not args.words:
        parser.error("No words provided")
    base_wordlist = [w.strip() for w in args.words.split(",") if w.strip()]
    candidates = []
    for word in base_wordlist:
        variants = case_transform(word)
        candidates.extend(variants)
        if args.leet:
            for v in variants:
                candidates.append(leet_transform(v))

    candidates = [c for c in candidates if args.min <= len(c) <= args.max]

    if args.output:
        with open(args.output, "w") as f:
            for candidate in candidates:
                f.write(candidate + "\n")
        print(f"Wrote {len(candidates)} candidates to {args.output}")
    else:
        for candidate in candidates:
            print(candidate)


if __name__ == "__main__":
    main()
