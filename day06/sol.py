#!/usr/bin/env python3

from pathlib import Path
from pprint import pprint


def load_input(filename: str = "input.txt") -> list[list[str]]:
    """Load the input file and convert it to a grid represented as a list of lists.

    Parameters
    ----------
    filename : str, optional
        The name of the input file to read, by default 'test_input.txt'

    Returns
    -------
    list[list[str]]
        A grid represented as a list of lists of characters.

    """
    grid = []
    with Path(filename).open() as f:
        for line in f:
            line = line.rstrip("\n")
            grid.append(list(line))
    return grid


def find_start_location_and_direction(
    grid: list[list[str]],
) -> tuple[tuple[int, int], str]:
    """Find the location and direction of the start symbol in the grid.

    Parameters
    ----------
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    Returns
    -------
    tuple[tuple[int, int], str]
        A tuple containing the location as (i, j) and the direction as one of 'u', 'd',
        'l', 'r'.

    """
    direction_map = {"^": "u", "v": "d", "<": "l", ">": "r"}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in direction_map:
                return (i, j), direction_map[cell]
    raise ValueError("No direction symbol found in the grid")


def rotate_right(direction: str) -> str:
    """Rotate the direction 90 degrees to the right.

    Parameters
    ----------
    direction : str
        The current direction of the robot.

    Returns
    -------
    str
        The new direction of the robot.

    """
    return {"u": "r", "r": "d", "d": "l", "l": "u"}[direction]


def find_next_location(
    start_location: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    """Find the next location based on the current location and direction.

    Parameters
    ----------
    start_location : tuple[int, int]
        The current location as (i, j).
    direction : str
        The current direction.

    Returns
    -------
    tuple[int, int]
        The next location as (i, j).

    """
    i, j = start_location
    if direction == "u":
        return i - 1, j
    if direction == "d":
        return i + 1, j
    if direction == "l":
        return i, j - 1
    if direction == "r":
        return i, j + 1
    raise ValueError(f"Invalid direction: {direction}")


def is_in_grid(location: tuple[int, int], grid: list[list[str]]) -> bool:
    """Check if a location is within the grid.

    Parameters
    ----------
    location : tuple[int, int]
        The location to check as (i, j).
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    Returns
    -------
    bool
        True if the location is within the grid, False otherwise.

    """
    i, j = location
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


def is_obstacle(location: tuple[int, int], grid: list[list[str]]) -> bool:
    """Check if a location is an obstacle.

    Parameters
    ----------
    location : tuple[int, int]
        The location to check as (i, j).
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    Returns
    -------
    bool
        True if the location is an obstacle, False otherwise.

    """
    i, j = location
    return grid[i][j] == "#"


def mark_location_as_visited(location: tuple[int, int], grid: list[list[str]]) -> None:
    """Mark a location as visited.

    Parameters
    ----------
    location : tuple[int, int]
        The location to mark as (i, j).
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    """
    i, j = location
    grid[i][j] = "X"


def mark_location_as_obstacle(location: tuple[int, int], grid: list[list[str]]) -> None:
    """Mark a location as an obstacle.

    Parameters
    ----------
    location : tuple[int, int]
        The location to mark as (i, j).
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    """
    i, j = location
    grid[i][j] = "#"


def count_visited_locations(grid: list[list[str]]) -> int:
    """Count the number of visited locations in the grid.

    Parameters
    ----------
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    Returns
    -------
    int
        The number of visited locations.

    """
    return sum(row.count("X") for row in grid)


def traverse_grid_until_out(
    current_location: tuple[int, int],
    current_direction: str,
    grid: list[list[str]],
    return_grid: bool = False,
) -> None | list[list[str]]:
    """Traverse the grid until it moves out of the grid or encounters an obstacle.

    Parameters
    ----------
    current_location : tuple[int, int]
        The current location of the robot as (i, j).
    current_direction : str
        The current direction of the robot.
    grid : list[list[str]]
        The grid represented as a list of lists of characters.
    """
    while True:
        next_location, next_direction = take_one_step(
            current_location, current_direction, grid
        )
        if next_location is None:
            break
        current_location, current_direction = next_location, next_direction
        mark_location_as_visited(current_location, grid)

    if return_grid:
        return grid
    return None


def take_one_step(
    current_location: tuple[int, int],
    current_direction: str,
    grid: list[list[str]],
) -> tuple[tuple[int, int], str] | tuple[None, None]:
    """Take one step in the grid and return the new location and direction.

    Parameters
    ----------
    current_location : tuple[int, int]
        The current location as (i, j).
    current_direction : str
        The current direction.
    grid : list[list[str]]
        The grid represented as a list of lists of characters.

    Returns
    -------
    tuple[tuple[int, int], str] | tuple[None, None]
        A tuple containing the new location as (i, j) and the new direction or
        tuple[None, None] if the next step is out of the grid.

    """
    next_location = find_next_location(current_location, current_direction)
    next_direction = current_direction
    if not is_in_grid(next_location, grid):
        return (None, None)
    while is_obstacle(next_location, grid):
        next_direction = rotate_right(next_direction)
        next_location = find_next_location(current_location, next_direction)
    if not is_in_grid(next_location, grid):
        return (None, None)
    return next_location, next_direction


def solve_part_a(filename: str = "input.txt") -> int:
    """Solve part A of the puzzle.

    Parameters
    ----------
    filename : str, optional
        The name of the input file to read, by default 'input.txt'

    Returns
    -------
    int
        The number of intersections visited.

    """
    grid = load_input(filename)
    current_location, current_direction = find_start_location_and_direction(grid)
    mark_location_as_visited(current_location, grid)

    traverse_grid_until_out(current_location, current_direction, grid)

    return count_visited_locations(grid)


def solve_part_b(filename: str = "input.txt") -> int:
    """Solve part B of the puzzle.

    Parameters
    ----------
    filename : str, optional
        The name of the input file to read, by default 'input.txt'

    Returns
    -------
    int
        The number of intersections visited.

    """
    grid = load_input(filename)
    current_location, current_direction = find_start_location_and_direction(grid)
    mark_location_as_visited(current_location, grid)
    og_traversed_grid = traverse_grid_until_out(
        current_location,
        current_direction,
        [row.copy() for row in grid],
        return_grid=True,
    )

    counter = 0
    no_obstructions = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (  # There's no point in adding an obstacle in positions not visited
                og_traversed_grid[i][j] != "X"
            ):
                continue
            counter += 1
            if counter % 10 == 0:
                print(f"Counter: {counter}")

            new_grid = load_input(filename)
            current_location, current_direction = find_start_location_and_direction(
                new_grid,
            )
            visited_locations_and_directions = ((current_location, current_direction),)

            # Add an obstacle
            mark_location_as_obstacle((i, j), new_grid)

            while True:
                next_location, next_direction = take_one_step(
                    current_location,
                    current_direction,
                    new_grid,
                )
                if next_location is None:
                    break
                current_location, current_direction = next_location, next_direction
                if (
                    current_location,
                    current_direction,
                ) in visited_locations_and_directions:
                    no_obstructions += 1
                    break
                visited_locations_and_directions += (
                    (current_location, current_direction),
                )
    return no_obstructions


if __name__ == "__main__":
    result = solve_part_b(filename="input.txt")
    print(str(result))
