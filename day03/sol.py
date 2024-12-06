#!/usr/bin/env python3

import re


def load_data(filename: str) -> str:
    """Load a file into a single string, replacing new lines with a new line symbol.

    Parameters
    ----------
    filename : str
        The name of the file to load data from.

    Returns
    -------
    str
        A single string representing the contents of the file.
    """
    with open(filename, "r") as file:
        return file.read().replace("\n", "\\n")


def find_valid_mult_instances(s: str) -> list:
    """Find all instances of `mul(x,y)` in a string where x and y are 1-3 digit numbers.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    list
        A list of strings, each representing an instance of `mul(x,y)`.
    """
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, s)


def filter_for_conditionals(s: str) -> str:
    """Remove the substring contained between the most recent `don't()` and the nearest `do()`.
    If there's a `don't()` without a matched `do()`, remove the bit between the `don't()` and the end of the line.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        The filtered string with the substring between the most recent `don't()` and `do()` removed.
    """
    while "don't()" in s:
        start = s.find("don't()")
        end = s.find("do()", start)
        if end != -1:
            end += len("do()")
            s = s[:start] + s[end:]
        else:
            s = s[:start]
            break
    return s


def calculate_mult_instances(mult_list: list) -> list:
    """Multiply every set of x and y in a list of `mult(x,y)` strings.

    Parameters
    ----------
    mult_list : list
        A list of strings, each representing an instance of `mult(x,y)`.

    Returns
    -------
    list
        A list of integers, each representing the product of x and y.
    """
    results = []
    for mult_str in mult_list:
        x, y = map(int, re.findall(r"\d{1,3}", mult_str))
        results.append(x * y)
    return results


def solve_part_a(filename: str = "input.txt") -> int:
    """Solve part A of the problem.

    Parameters
    ----------
    filename : str, optional
        The name of the file to load data from (default is "input.txt").

    Returns
    -------
    int
        The total sum of all multiplications of `mul(x,y)` instances in the file.
    """
    data = load_data(filename)
    mult_instances = find_valid_mult_instances(data)
    mult_results = calculate_mult_instances(mult_instances)
    return sum(mult_results)


def solve_part_b(filename: str = "input.txt") -> int:
    """Solve part B of the problem.

    Parameters
    ----------
    filename : str, optional
        The name of the file to load data from (default is "input.txt").

    Returns
    -------
    int
        The total sum of all multiplications of `mul(x,y)` instances in the file after filtering.
    """
    data = load_data(filename)
    filtered_data = filter_for_conditionals(data)
    mult_instances = find_valid_mult_instances(filtered_data)
    mult_results = calculate_mult_instances(mult_instances)
    return sum(mult_results)


if __name__ == "__main__":
    result = solve_part_b(filename="input.txt")
    print(str(result))
