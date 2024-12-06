from .sol import solve_part_a


def test_solve_part_a():
    part_a_expected_output = 2
    assert solve_part_a("test_input.txt") == part_a_expected_output
