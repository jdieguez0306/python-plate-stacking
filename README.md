# Python Plate Stack Simulator

A command-line Python application that models a constrained stack of plates and demonstrates last-in, first-out (LIFO) behavior, input validation, and menu-driven program design.

## Features

- Add plates to the top of a stack
- Enforce a size-ordering rule so larger plates cannot be placed on smaller plates
- Remove one or more plates from the top of the stack
- Display the stack from top to bottom
- Validate menu choices and numeric input
- Handle empty-stack and invalid-removal cases

## Data Structure

The application uses a Python list as a stack:

```text
Top
 |
 v
[small plate]
[medium plate]
[large plate]
```

New plates are appended to the end of the list, and removals use `pop()`, demonstrating LIFO behavior.

## Example

```text
Main Menu
=========
0. Exit
1. Add a plate
2. Display plates
3. Remove plates
Select [0-3]: 1

Add a Plate
===========
Enter a plate size: 10
Success!
```

If a larger plate is placed on a smaller one:

```text
Cannot place a plate of size 12 on top of a plate of size 10.
```

## Concepts Demonstrated

- Python
- Stack data structures
- LIFO behavior
- Lists
- Functions
- Input validation
- Conditional logic
- Loops
- Command-line interfaces
- Error handling

## Project Structure

```text
python-plate-stack-simulator/
├── README.md
└── main.py
```

## Run

```bash
python main.py
```
