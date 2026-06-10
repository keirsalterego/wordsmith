import argparse


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

    parse.add_argument(
        "-m",
        "--min",
        type=int,
        default=4,
        help="Minimum password length"
    )

    parse.add_argument(
        "-M",
        "--max",
        type=int,
        default=12,
        help="Maximum password length"
    )

    parse.add_argument(
        "-l",
        "--leet",
        action="store_true",
        help="Enable leet speak transformation"
    )

    # parse the arguments that the user typed in the terminal
    args = parser.parse_args()

    if args.words:
        # if the user passed a single string like "Yuvraj,biswal" we gonna neeed to split it by the comma to turn it into a python list
        base_wordlist = args.words.split(",")
        print(f"[*] base words loaded: {base_wordlist}")
    else:
        print("[!] No words provided. use -w to provide base words.")


if __name__ == "__main__":
    main()
