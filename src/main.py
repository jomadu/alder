#!/usr/bin/env python3
"""
Alder

A work simulation utility.
"""

__author__ = "Max Dunn"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse


def main(args):
    """ Main entry point of the app """
    print("hello world")
    print(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-wf", "--workers-file", action="store", dest="workers_file", required=True)
    parser.add_argument("-wif", "--work-items-file", action="store", dest="work_items_file", required=True)
    parser.add_argument("-wwcf", "--weighted-work-categories-file", action="store", dest="weighted_work_categories_file", required=True)
    parser.add_argument("-s", "--start-date", action="store", dest="weighted_work_categories_file", required=True)
    parser.add_argument("-p", "--cycle-period", action="store", dest="weighted_work_categories_file", required=True)
    parser.add_argument("-o", "--output-file", action="store", dest="weighted_work_categories_file", required=True)

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)
