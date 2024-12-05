from .sol import solve_part_a, solve_part_b


def test_solve_part_a():
    part_a_expected_output = 11
    assert solve_part_a("test_input.txt") == part_a_expected_output


def test_solve_part_b():
    part_b_expected_output = 31
    assert solve_part_b("test_input.txt") == part_b_expected_output
