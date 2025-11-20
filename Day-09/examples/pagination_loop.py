"""Day 9 example: iterate through paginated API responses."""

from __future__ import annotations

import itertools
from typing import Iterable, Iterator


def paginate(sequence: Iterable[int], page_size: int = 3) -> Iterator[list[int]]:
    """
    Breaks a long list into smaller chunks (pages).
    This is useful when an API returns thousands of results and you want to process them 100 at a time.
    """
    iterator = iter(sequence)
    # This loop keeps going as long as we can grab another 'chunk' of data
    while chunk := list(itertools.islice(iterator, page_size)):
        yield chunk  # 'yield' gives us one chunk at a time, then pauses the function


def main() -> None:
    # Create a fake list of numbers from 1 to 10
    fake_api_results = list(range(1, 11))
    
    # Loop through the pages
    # enumerate() gives us a counter (page_number) along with the data (page)
    for page_number, page in enumerate(paginate(fake_api_results), start=1):
        print(f"Page {page_number}: {page}")


if __name__ == "__main__":
    main()
