import sys

from lib.kafka import write
from lib.settings import read_settings

def main():
    settings = read_settings()

    write(
        settings['kafka']['servers'],
        settings['kafka']['topic'],
        sys.stdin
    )

if __name__ == "__main__":
    main()
