#!/usr/bin/env python3

from pathlib import Path


def parse_file(filename: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    """Parse the specified file and return two lists.

    Parameters
    ----------
    filename : str
        The path to the file to parse.

    Returns
    -------
    list_of_tuples : list[tuple[int, int]]
        A list of tuples where each tuple represents an (x, y) pair from the first part
        of the file.
    list_of_lists : list[list[int]]
        A list of lists where each inner list contains integers from the second part of
        the file.

    """

    with Path(filename).open() as file:
        content = file.read()
    first_part, second_part = content.strip().split("\n\n")
    list_of_tuples = []
    for line in first_part.strip().split("\n"):
        x, y = line.strip().split("|")
        list_of_tuples.append((int(x), int(y)))
    list_of_lists = []
    for line in second_part.strip().split("\n"):
        nums = [int(num) for num in line.strip().split(",")]
        list_of_lists.append(nums)
    return list_of_tuples, list_of_lists


def update_is_valid(
    update: list[int], list_of_constraints: list[tuple[int, int]]
) -> bool:
    """Check if the update is valid.

    Parameters
    ----------
    update : list[int]
        The update to check.
    list_of_constraints : list[tuple[int, int]]
        A list of constraints.

    Returns
    -------
    bool
        True if the update is valid, False otherwise.

    """
    for c1, c2 in list_of_constraints:
        if c1 in update and c2 in update:

            # find the positions of c1 and c2 in update
            c1_i, c2_i = update.index(c1), update.index(c2)

            # if c1 is not to the left of c2, then the update is invalid
            if c1_i >= c2_i:
                return False

    return True


def solve_part_a(filename: str = "input.txt") -> int:
    """Solve part A of the problem.

    Parameters
    ----------
    filename : str, optional
        The name of the input file (default is "input.txt").

    Returns
    -------
    int
        The result for part A.

    """
    list_of_constraints, list_of_updates = parse_file(filename)

    middle_page_sum = 0

    for update in list_of_updates:
        if update_is_valid(update, list_of_constraints):
            # find the middle element of update and add it to middle_page_sum
            middle_page_sum += update[len(update) // 2]

    return middle_page_sum


def solve_part_b(filename: str = "input.txt") -> int:
    """Solve part B of the problem.

    Parameters
    ----------
    filename : str, optional
        The name of the input file (default is "input.txt").

    Returns
    -------
    int
        The result for part B.

    """
    list_of_constraints, list_of_updates = parse_file(filename)

    middle_page_sum = 0

    for update in list_of_updates:
        if not update_is_valid(update, list_of_constraints):
            has_been_updated = True
            while has_been_updated:
                has_been_updated = False
                for c1, c2 in list_of_constraints:
                    if c1 in update and c2 in update:

                        # find the positions of c1 and c2 in update
                        c1_i, c2_i = update.index(c1), update.index(c2)

                        # if c1 is not to the left of c2, then the update is invalid
                        if c1_i >= c2_i:
                            # swap c1 and c2
                            update[c1_i], update[c2_i] = update[c2_i], update[c1_i]
                            has_been_updated = True

            # find the middle element of update and add it to middle_page_sum
            middle_page_sum += update[len(update) // 2]

    return middle_page_sum


if __name__ == "__main__":
    result = solve_part_b(filename="input.txt")
    print(str(result))
