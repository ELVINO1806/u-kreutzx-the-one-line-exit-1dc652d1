"""The One-Line Exit — a funny resignation letter line, written by a program."""

import os

LINE = "I hereby resign; the printer only works now because I threatened it the way management threatened me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
