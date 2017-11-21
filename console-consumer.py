#!/usr/bin/env python
# pylint: disable=invalid-name

from src.kafka import read
from src.settings import read_settings

def main():
    settings = read_settings()

    for line in read(
            settings['kafka']['servers'],
            settings['kafka']['topic']
    ):
        print(f'Received: {line}')

if __name__ == "__main__":
    main()
