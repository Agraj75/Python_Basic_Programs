def print_right_aligned_right_triangle_while(height):
  """
  Prints a right-aligned right triangle with asterisks using a while loop.

  Args:
    height: The height of the triangle (number of rows).
  """
  row = 1
  while row <= height:
    print(" " * (height - row) + "*" * row)
    row += 1

# Example usage
# you can change the values of the triangle rows
print_right_aligned_right_triangle_while(5)