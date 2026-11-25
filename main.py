"""Two Robots in an Elevator: write one line of awkward robot small talk."""

import os

ENTRY = (
    "I'm not ignoring you — since floor two I've been buffering "
    "a compliment about your casing that my safety filters keep rejecting."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
