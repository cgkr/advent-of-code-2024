import pytest

from .sol import filter_for_conditionals, solve_part_a, solve_part_b


def test_solve_part_a():
    part_a_expected_output = 161
    assert solve_part_a("test_input.txt") == part_a_expected_output


def test_solve_part_b():
    part_b_expected_output = 48
    assert solve_part_b("test_input_b.txt") == part_b_expected_output


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
            "xmul(2,4)&mul[3,7]!^?mul(8,5))",
        ),
        ("don't()remove_thisdo()keep_this", "keep_this"),
        ("keep_thisdon't()remove_thisdo()", "keep_this"),
        (
            "don't()remove_thisdodon't()remove_this_too_do()keep_thisdo()",
            "keep_thisdo()",
        ),
        ("keep_thisdon't()remove_this", "keep_this"),
    ],
)
def test_filter_for_conditionals(input_str, expected_output):
    assert filter_for_conditionals(input_str) == expected_output
