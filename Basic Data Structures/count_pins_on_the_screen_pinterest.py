def get_max_pins(pins, screen_len):
    """
    O(nlogn) sort
    O(n) for storing columns
    Split the pins into two lists: one for the left column (L) and one for the right column (R).
    Sort pins in each column by their bottom index.
    greedy approach to select the maximum number of non-overlapping pins that fit within the screen length.
    res is the max num of non-overlapping pins within the screen size
    """
    # Separate pins by columns
    left_pins = [(top, bottom) for top, bottom, column in pins if column == "L"]
    right_pins = [(top, bottom) for top, bottom, column in pins if column == "R"]

    def max_pins_in_column(pins, screen_len):
        # Sort pins by bottom index
        pins.sort(key=lambda x: x[1])
        count = 0
        current_bottom = 0

        for top, bottom in pins:
            if top >= current_bottom and bottom - top <= screen_len:
                count += 1
                current_bottom = bottom

        return count

    # Calculate maximum pins visible for each column
    max_left = max_pins_in_column(left_pins, screen_len)
    max_right = max_pins_in_column(right_pins, screen_len)

    # Return the total maximum pins visible
    return max_left + max_right

# Example Input
pins = [(1, 4, "L"), (2, 3, "R"), (4, 8, "R"), (6, 9, "L")]
screen_len = 5
print(get_max_pins(pins, screen_len))  # Output: 2
