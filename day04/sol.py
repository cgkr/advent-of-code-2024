#!/usr/bin/env python3

from pathlib import Path


def count_horizontal(grid: list[list[str]], word: str) -> int:
    """Count occurrences of a word horizontally in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    word_len = len(word)
    for row in grid:
        row_str = "".join(row)
        # Forward and backward
        for dir_word in [word, word[::-1]]:
            for i in range(len(row_str) - word_len + 1):
                if row_str[i : i + word_len] == dir_word:
                    count += 1
    return count


def count_vertical(grid: list[list[str]], word: str) -> int:
    """Count occurrences of a word vertically in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    word_len = len(word)
    cols = len(grid[0])
    rows = len(grid)
    for col in range(cols):
        col_str = "".join([grid[row][col] for row in range(rows)])
        # Forward and backward
        for dir_word in [word, word[::-1]]:
            for i in range(len(col_str) - word_len + 1):
                if col_str[i : i + word_len] == dir_word:
                    count += 1
    return count


def count_diagonal_down_right(grid: list[list[str]], word: str) -> int:
    """Count occurrences of a word diagonally down and right in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows - word_len + 1):
        for col in range(cols - word_len + 1):
            for dir_word in [word, word[::-1]]:
                match = True
                for k in range(word_len):
                    if grid[row + k][col + k] != dir_word[k]:
                        match = False
                        break
                if match:
                    count += 1
    return count


def count_diagonal_down_left(grid: list[list[str]], word: str) -> int:
    """Count occurrences of a word diagonally down and left in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows - word_len + 1):
        for col in range(word_len - 1, cols):
            for dir_word in [word, word[::-1]]:
                match = True
                for k in range(word_len):
                    if grid[row + k][col - k] != dir_word[k]:
                        match = False
                        break
                if match:
                    count += 1
    return count


def count_diagonal_up_right(grid: list[list[str]], word: str) -> int:
    """Count occurrences of a word diagonally up and right in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    for row in range(word_len - 1, rows):
        for col in range(cols - word_len + 1):
            for dir_word in [word, word[::-1]]:
                match = True
                for k in range(word_len):
                    if grid[row - k][col + k] != dir_word[k]:
                        match = False
                        break
                if match:
                    count += 1
    return count


def count_diagonal_up_left(grid: list[list[str]], word: str) -> int:
    """Count occurrences of a word diagonally up and left in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    word_len = len(word)
    rows = len(grid)
    cols = len(grid[0])
    for row in range(word_len - 1, rows):
        for col in range(word_len - 1, cols):
            for dir_word in [word, word[::-1]]:
                match = True
                for k in range(word_len):
                    if grid[row - k][col - k] != dir_word[k]:
                        match = False
                        break
                if match:
                    count += 1
    return count


def count_word_occurrences(grid: list[list[str]], word: str) -> int:
    """Count total occurrences of a word in all directions in the grid.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.

    Returns
    -------
    int
        The total number of occurrences found.

    """
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:
                for dx, dy in directions:
                    if check_word(grid, word, x, y, dx, dy):
                        total += 1
    return int(total)


def check_word(
    grid: list[list[str]], word: str, x: int, y: int, dx: int, dy: int
) -> bool:
    """Check if a word exists starting from a position in a given direction.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.
    word : str
        The word to search for.
    x : int
        Starting row index.
    y : int
        Starting column index.
    dx : int
        Row direction delta (-1, 0, 1).
    dy : int
        Column direction delta (-1, 0, 1).

    Returns
    -------
    bool
        True if the word is found, False otherwise.

    """
    for k in range(len(word)):
        nx = x + dx * k
        ny = y + dy * k
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != word[k]:
                return False
        else:
            return False
    return True


def count_mas(grid: list[list[str]]) -> int:
    """Count occurrences where both diagonals centered around 'A' form 'MAS' or 'SAM'.

    Parameters
    ----------
    grid : list of list of str
        The grid to search within.

    Returns
    -------
    int
        The number of occurrences found.

    """
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    patterns = ["MAS", "SAM"]

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if grid[row][col] == "A":  # Check if 'A' is in the center
                if (
                    any(
                        grid[row - 1][col - 1] == pattern[0]
                        and grid[row + 1][col + 1] == pattern[2]
                        for pattern in patterns
                    )
                    and any(
                        grid[row - 1][col + 1] == pattern[0]
                        and grid[row + 1][col - 1] == pattern[2]
                        for pattern in patterns
                    )
                ) or (
                    any(
                        grid[row + 1][col + 1] == pattern[0]
                        and grid[row - 1][col - 1] == pattern[2]
                        for pattern in patterns
                    )
                    and any(
                        grid[row + 1][col - 1] == pattern[0]
                        and grid[row - 1][col + 1] == pattern[2]
                        for pattern in patterns
                    )
                ):
                    count += 1
    return count


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
    with Path(filename).open() as f:
        grid = [list(line.strip()) for line in f]

    return count_word_occurrences(grid, "XMAS")


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
    with Path(filename).open() as f:
        grid = [list(line.strip()) for line in f]

    return count_mas(grid)


if __name__ == "__main__":
    result = solve_part_b(filename="input.txt")
    print(str(result))
