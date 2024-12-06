#!/usr/bin/env python3


def load_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [list(map(int, line.split())) for line in file]


def is_monotonic(row: list) -> bool:
    """Check if each row in the array is either all increasing or all decreasing.

    Parameters
    ----------
    row (list): The input row.

    Returns
    -------
    bool: A boolean indicating if the row is monotonic.

    """
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)
    return increasing or decreasing


def is_acceptable_diff(row: list) -> bool:
    """Check if any two adjacent levels differ by at least one and at most three.

    Parameters
    ----------
    row (list): The input row.

    Returns
    -------
    bool: A boolean indicating if the row satisfies the condition.

    """
    diffs = [abs(row[i + 1] - row[i]) for i in range(len(row) - 1)]
    return all(1 <= d <= 3 for d in diffs)


def is_safe(row: list) -> bool:
    """Check if each row in the array is safe based on monotonicity and acceptable
    differences.

    Parameters
    ----------
    row (list): The input row.

    Returns
    -------
    bool: A boolean indicating if the row is safe.

    """
    return is_monotonic(row) and is_acceptable_diff(row)


def solve_part_a(filename: str = "input.txt") -> int:
    data = load_data(filename)
    return sum(is_safe(row) for row in data)


if __name__ == "__main__":
    result = solve_part_a(filename="input.txt")
    print(str(result))
