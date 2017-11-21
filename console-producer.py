#!/usr/bin/env python
# pylint: disable=invalid-name

import sys

from src.kafka import write
from src.settings import read_settings

def main():
    settings = read_settings()

    write(
        settings['kafka']['servers'],
        settings['kafka']['topic'],
        (line.rstrip() for line in sys.stdin)
    )

if __name__ == "__main__":
    main()
