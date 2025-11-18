"""Day 9 example: iterate through paginated API responses."""

from __future__ import annotations

import itertools
from typing import Iterable, Iterator


def paginate(sequence: Iterable[int], page_size: int = 3) -> Iterator[list[int]]:
    iterator = iter(sequence)
    while chunk := list(itertools.islice(iterator, page_size)):
        yield chunk


def main() -> None:
    fake_api_results = list(range(1, 11))
    for page_number, page in enumerate(paginate(fake_api_results), start=1):
        print(f"Page {page_number}: {page}")


if __name__ == "__main__":
    main()
