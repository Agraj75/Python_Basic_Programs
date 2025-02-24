def print_left_aligned_right_triangle(height):
  """
  Prints a left-aligned right triangle with asterisks.

  Args:
    height: The height of the triangle (number of rows).
  """
  for i in range(1, height + 1):
    print("*" * i)

# Example usage 
# you can change the values of the triangle rows
print_left_aligned_right_triangle(5)