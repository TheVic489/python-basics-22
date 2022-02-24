"""Pathlib is a modern way (Python >=3.4) to manage files.
   Before Pathlib you had to use open(), shutils, etc."""

from pathlib import Path

# ---------------------------------------------------------------------
def main() -> None:

    # Create a Path object
    data_file: Path = Path("data.txt")

    # Read whole file with newlines
    text: str = data_file.read_text()

    # Print file contents as you wish
    print(text)
    print(text.split())

    # Write string to file with newlines and everything.
    data_file.write_text(text)


# Main
# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------
