"""Interactive stack simulator demonstrating LIFO behavior and input validation."""

plates = []


def read_positive_integer(prompt):
    """Return a positive integer entered by the user, or None for invalid input."""
    value = input(prompt).strip()

    if not value.isdigit():
        print("Error: value must be a positive integer.")
        return None

    value = int(value)

    if value <= 0:
        print("Error: value must be greater than 0.")
        return None

    return value


def add_plate():
    """Add a plate while preserving the size-ordering constraint."""
    print("\nAdd a Plate")
    print("===========")

    plate_size = read_positive_integer("Enter a plate size: ")

    if plate_size is None:
        return

    if plates and plate_size > plates[-1]:
        print(
            f"Cannot place a plate of size {plate_size} "
            f"on top of a plate of size {plates[-1]}."
        )
        return

    plates.append(plate_size)
    print("Success!")


def display_plates():
    """Display the current stack from top to bottom."""
    print("\nPlate Stack")
    print("===========")

    if not plates:
        print("There are no stacked plates.")
        return

    for plate in reversed(plates):
        print(plate)


def remove_plates():
    """Remove a user-selected number of plates from the top of the stack."""
    print("\nRemove Plates")
    print("=============")

    if not plates:
        print("There are no plates to remove.")
        return

    remove_count = read_positive_integer("How many plates should be removed? ")

    if remove_count is None:
        return

    if remove_count > len(plates):
        print(
            f"Error: cannot remove {remove_count} plates; "
            f"only {len(plates)} are currently stacked."
        )
        return

    for _ in range(remove_count):
        plates.pop()

    print("Success!")


def run():
    """Run the interactive command-line interface."""
    while True:
        print("\nMain Menu")
        print("=========")
        print("0. Exit")
        print("1. Add a plate")
        print("2. Display plates")
        print("3. Remove plates")

        option = input("Select [0-3]: ").strip()

        if option == "0":
            print("Goodbye!")
            break
        elif option == "1":
            add_plate()
        elif option == "2":
            display_plates()
        elif option == "3":
            remove_plates()
        else:
            print("Error: select a valid option from 0 to 3.")


if __name__ == "__main__":
    run()
