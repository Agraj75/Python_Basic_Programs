def print_left_aligned_right_triangle_while(height):
  """
  Prints a left-aligned right triangle with asterisks using a while loop.

  Args:
    height: The height of the triangle (number of rows).
  """
  row = 1
  while row <= height:
    print("*" * row)
    row += 1

# Example usage
# you can change the values of the triangle rows
print_left_aligned_right_triangle_while(5)