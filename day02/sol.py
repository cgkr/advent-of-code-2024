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


def is_monotonic(row: list, allow_dampened: bool = False) -> bool:
    """Check if each row in the array is either all increasing or all decreasing,
    or if removing any one element would make it so if allow_dampened is True.

    Parameters
    ----------
    row : list
        The input row.
    allow_dampened : bool, optional
        Whether to allow removing one element to make the row monotonic (default is
        False).

    Returns
    -------
    bool
        A boolean indicating if the row is monotonic or can be made monotonic by
        removing one element.
    """

    def check_monotonic(sub_row):
        diffs = [sub_row[i + 1] - sub_row[i] for i in range(len(sub_row) - 1)]
        increasing = all(d > 0 for d in diffs)
        decreasing = all(d < 0 for d in diffs)
        return increasing or decreasing

    if check_monotonic(row):
        return True

    if allow_dampened:
        for i in range(len(row)):
            if check_monotonic(row[:i] + row[i + 1 :]):
                return True

    return False


def is_acceptable_diff(row: list, allow_dampened: bool = False) -> bool:
    """Check if any two adjacent levels differ by at least one and at most three,
    or if removing any one element would make it so if allow_dampened is True.

    Parameters
    ----------
    row : list
        The input row.
    allow_dampened : bool, optional
        Whether to allow removing one element to make the row satisfy the condition
        (default is False).

    Returns
    -------
    bool
        A boolean indicating if the row satisfies the condition or can be made to
        satisfy by removing one element.
    """

    def check_diff(sub_row):
        diffs = [abs(sub_row[i + 1] - sub_row[i]) for i in range(len(sub_row) - 1)]
        return all(1 <= d <= 3 for d in diffs)

    if check_diff(row):
        return True

    if allow_dampened:
        for i in range(len(row)):
            if check_diff(row[:i] + row[i + 1 :]):
                return True

    return False


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
    return is_monotonic(row, allow_dampened=allow_dampened) and is_acceptable_diff(
        row, allow_dampened=allow_dampened
    )


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
    result = solve_part_a(filename="input.txt")
    print(str(result))
