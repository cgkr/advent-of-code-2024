#!/usr/bin/env python3
from pathlib import Path

import numpy as np


def parse_file(filename: str) -> list[tuple[int, tuple[int, ...]]]:
    """Parse the specified file and return a list of tuples.

    Parameters
    ----------
    filename : str
        The path to the file to parse.

    Returns
    -------
    list_of_tuples : list[tuple[int, tuple[int, ...]]]
        A list of tuples where each tuple represents an (x, (y1, y2, ...)) pair from
        the file.

    """
    list_of_tuples = []
    with Path(filename).open() as file:
        for line in file:
            key, values = line.split(":")
            values_tuple = tuple(map(int, values.split()))
            list_of_tuples.append((int(key), values_tuple))
    return list_of_tuples


def can_form_target(
    nums: list[int],
    target: int,
    index: int = 0,
    current_value: int | None = None,
) -> bool:
    """Determine if the target value can be formed using addition or multiplication of
    the numbers in the list.

    Parameters
    ----------
    nums : list[int]
        The list of numbers to use.
    target : int
        The target value to form.
    index : int, optional
        The current index in the list, by default 0.
    current_value : int, optional
        The current value formed, by default None.

    Returns
    -------
    bool
        True if the target value can be formed, False otherwise.

    """
    if current_value is None:
        current_value = nums[0]  # Start with the first number

    # Base case: If we've used all numbers in the list
    if index == len(nums) - 1:
        return current_value == target

    # Recursive case: Try both addition and multiplication
    next_num = nums[index + 1]
    return can_form_target(
        nums,
        target,
        index + 1,
        current_value + next_num,
    ) or can_form_target(nums, target, index + 1, current_value * next_num)


def can_form_target_with_concat(
    nums: list[int],
    target: int,
    index: int = 0,
    current_value: int | None = None,
) -> bool:
    """Determine if the target value can be formed using addition, multiplication or
    concatenation of the numbers in the list.

    Parameters
    ----------
    nums : list[int]
        The list of numbers to use.
    target : int
        The target value to form.
    index : int, optional
        The current index in the list, by default 0.
    current_value : int, optional
        The current value formed, by default None.

    Returns
    -------
    bool
        True if the target value can be formed, False otherwise.

    """
    if current_value is None:
        current_value = nums[0]  # Start with the first number

    # Base case: If we've used all numbers in the list
    if index == len(nums) - 1:
        return current_value == target

    # Recursive case: Try addition, multiplication, and concatenation
    next_num = nums[index + 1]

    # Addition
    if can_form_target_with_concat(nums, target, index + 1, current_value + next_num):
        return True

    # Multiplication
    if can_form_target_with_concat(nums, target, index + 1, current_value * next_num):
        return True

    # Concatenation (convert to string, concatenate, then back to integer)
    concatenated_value = int(str(current_value) + str(next_num))
    if can_form_target_with_concat(nums, target, index + 1, concatenated_value):
        return True

    return False


def solve_part_a(filename: str) -> int:
    """Solve part A of the day.

    Parameters
    ----------
    filename : str
        The path to the file to parse.

    Returns
    -------
    int
        The solution to part A.

    """
    input_list = parse_file(filename)
    total_calibration_result = 0

    for test_value, remaining_numbers in input_list:
        if can_form_target(list(remaining_numbers), test_value):
            total_calibration_result += test_value

    return total_calibration_result


def solve_part_b(filename: str) -> int:
    """Solve part A of the day.

    Parameters
    ----------
    filename : str
        The path to the file to parse.

    Returns
    -------
    int
        The solution to part A.

    """
    input_list = parse_file(filename)
    total_calibration_result = 0

    for test_value, remaining_numbers in input_list:
        # Attempt to first form the target without using concat as it's a lot faster.
        if can_form_target(
            list(remaining_numbers),
            test_value,
        ) or can_form_target_with_concat(list(remaining_numbers), test_value):
            total_calibration_result += test_value

    return total_calibration_result


if __name__ == "__main__":
    result = solve_part_b(filename="input.txt")
    print(str(result))
