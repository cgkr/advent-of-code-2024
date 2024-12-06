#!/usr/bin/env python3


def load_data(filename: str) -> list:
    """Load data from a file.

    Parameters
    ----------
    filename : str
        The name of the file to load data from.

    Returns
    -------
    list
        A list of lists, where each inner list represents a row of integers from the
        file.

    """
    with open(filename, "r") as file:
        return [list(map(int, line.split())) for line in file]


def is_monotonic(row: list) -> bool:
    """Check if each row in the array is either all increasing or all decreasing.

    Parameters
    ----------
    row : list
        The input row.

    Returns
    -------
    bool
        A boolean indicating if the row is monotonic.

    """
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)
    return increasing or decreasing


def is_acceptable_diff(row: list) -> bool:
    """Check if any two adjacent levels differ by at least one and at most three.

    Parameters
    ----------
    row : list
        The input row.

    Returns
    -------
    bool
        A boolean indicating if the row satisfies the condition.

    """
    diffs = [abs(row[i + 1] - row[i]) for i in range(len(row) - 1)]
    return all(1 <= d <= 3 for d in diffs)


def is_safe(row: list, allow_dampened: bool = False) -> bool:
    """Check if each row in the array is safe based on monotonicity and acceptable
    differences.

    Parameters
    ----------
    row : list
        The input row.
    allow_dampened : bool, optional
        Whether to allow removing one element to make the row safe (default is False).

    Returns
    -------
    bool
        A boolean indicating if the row is safe.

    """
    if is_monotonic(row) and is_acceptable_diff(row):
        return True

    if allow_dampened:
        for i in range(len(row)):
            sub_row = row[:i] + row[i + 1 :]
            if is_monotonic(sub_row) and is_acceptable_diff(sub_row):
                return True

    return False


def solve_part_a(filename: str = "input.txt") -> int:
    """Solve part A of the problem.

    Parameters
    ----------
    filename : str, optional
        The name of the file to load data from (default is "input.txt").

    Returns
    -------
    int
        The number of safe rows in the data.

    """
    data = load_data(filename)
    return sum(is_safe(row) for row in data)


def solve_part_b(filename: str = "input.txt") -> int:
    """Solve part B of the problem.

    Parameters
    ----------
    filename : str, optional
        The name of the file to load data from (default is "input.txt").

    Returns
    -------
    int
        The number of safe rows in the data, allowing one element to be removed to make
        the row safe.

    """
    data = load_data(filename)
    return sum(is_safe(row, allow_dampened=True) for row in data)


if __name__ == "__main__":
    result = solve_part_b(filename="input.txt")
    print(str(result))
