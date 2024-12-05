#!/usr/bin/env python3
import numpy as np


def load_and_split_data(filename: str):
    data = np.loadtxt(filename)
    left_column = np.sort(data[:, 0])
    right_column = np.sort(data[:, 1])
    return left_column, right_column


def solve_part_a(filename: str = "input.txt") -> int:
    left_column, right_column = load_and_split_data(filename)
    diff_column = np.abs(right_column - left_column)
    return int(np.sum(diff_column))


if __name__ == "__main__":
    result = solve_part_a()
    print(str(result))
