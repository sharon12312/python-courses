#!/usr/bin/env python3

"""Retrieve the print words from a URL.

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.

    :param
        url: The URL of a UTF-8 text document.

    :return:
        A list of strings containing the word from
        the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items one per line

    :param
        An iterable series of printable items.

    :return:
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from at a URL.

    :param
        url: The URL of a UTF-8 text document.

    :return:
    """
    words = fetch_words(url)
    print_items(words)


# help our module run as a script when we call 'python3 words.py'
if __name__ == '__main__':
    # writing this url in the command line when calling this script:
    # 'http://sixty-north.com/c/t.txt'
    main(sys.argv[1])
