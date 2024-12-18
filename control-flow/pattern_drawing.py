# pattern_drawing.py

def draw_pattern():
    # Prompt User for Pattern Size
    size = int(input("Enter the size of the pattern: "))

    # Ensure the size is positive
    if size <= 0:
        print("Please enter a positive integer.")
        return

    # Draw the Pattern
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after completing a row
        row += 1

if __name__ == "__main__":
    draw_pattern()