# Nonogram Solver

A Python implementation of a nonogram puzzle solver using constraint propagation and recursive backtracking.

## Overview

Nonograms are logic puzzles in which cells in a grid must be filled according to numerical clues describing consecutive blocks of filled cells in each row and column.

The solver determines cell values by combining logical deduction with search. It reads a puzzle from an input file and writes the resulting grid to an output file.

## Algorithm

The solver combines two techniques:

### 1. Constraint Propagation

- Checks whether a row or column is compatible with its numerical clues and currently assigned cells.
- Tests whether each unknown cell can be filled or left empty while preserving feasibility.
- Assigns a cell when only one of the two possibilities remains valid.
- Uses a queue to revisit affected rows and columns after new deductions.
- Detects contradictions when a row or column has no valid configuration.

### 2. Recursive Backtracking

When constraint propagation cannot determine all cells, the solver selects an unresolved cell and explores both possible assignments.

After each assignment, constraint propagation is performed again. If a contradiction is detected, the solver backtracks and explores the alternative assignment.

This approach combines logical deductions with systematic search to solve puzzles that cannot be completed by deduction alone.

## Input and Output

The program reads the puzzle from `zad_input.txt`.

The first line contains the grid dimensions:

```text
<number_of_rows> <number_of_columns>
```

The following lines contain the clues for each row, followed by the clues for each column.

The solution is written to `zad_output.txt`, using `#` for filled cells and `.` for empty cells.

## Technologies

- Python
- Constraint propagation
- Recursive backtracking
- Queue-based processing
- Grid and state representation

## Running the Solver

Run the program with Python:

```bash
python solver.py
```

Make sure `zad_input.txt` is present in the working directory before running the program.

The solution will be written to `zad_output.txt`.
