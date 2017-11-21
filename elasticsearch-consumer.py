#!/usr/bin/env python
# pylint: disable=invalid-name

from src.es import write
from src.kafka import read
from src.settings import read_settings

def main():
    settings = read_settings()
    reader = read(
        settings['kafka']['servers'],
        settings['kafka']['topic']
    )
    write(
        settings['elasticsearch']['servers'],
        settings['elasticsearch']['index'],
        settings['elasticsearch']['type'],
        reader
    )

if __name__ == "__main__":
    main()
