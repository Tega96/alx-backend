#!/usr/bin/env/ python3
""" Helper function index_range that takes two int args."""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end indices for pagination.

    Given a page number and the size of the page (number of items per page),
    this function retruns a typle containing the start index and the end
    index for that page.

    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and the end index.
    """

    # Calculate the start index for the given page
    start_index = (page - 1) * page_size

    # Calculate the start index for the given page
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page from the dataset.

        Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        List[List]: The list of rows for the requested page.
        """
        assert isinstance(
                page, int) and page > 0, "page must be an int, > 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
