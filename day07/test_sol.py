import pytest

from .sol import solve_part_a, solve_part_b


def test_solve_part_a():
    expected_output = 3749
    assert solve_part_a("test_input.txt") == expected_output


def test_solve_part_b():
    expected_output = 11387
    assert solve_part_b("test_input.txt") == expected_output
