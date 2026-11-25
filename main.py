"""Write one nostalgic childhood memory sentence to entry.txt.

The entry is a single sentence recalling a summer evening in a
grandmother's kitchen: steaming rice, chipped blue bowls, cicadas
outside. The warmth lives in the small honest details, and the last
clause leaves the ache that the best of life was already there,
in that kitchen, in that spoonful.
"""

import os

ENTRY = (
    "Every summer evening, my grandmother ladled steaming rice into "
    "chipped blue bowls while the cicadas sang outside, and I believed "
    "no happiness in the world could ever taste better than that first "
    "warm spoonful."
)

# Gate: one sentence, 1-280 characters. Fail loudly rather than ever
# writing an entry the scorer would reject.
MAX_CHARS = 280


def validate(entry: str) -> None:
    if not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
        )
    if entry.count(".") != 1 or not entry.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
