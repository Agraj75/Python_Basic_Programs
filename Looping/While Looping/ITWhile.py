def print_isosceles_triangle_while(height):
  """
  Prints an isosceles triangle with asterisks using a while loop.

  Args:
    height: The height of the triangle (number of rows).
  """
  row = 1
  while row <= height:
    print(" " * (height - row) + "*" * (2 * row - 1))
    row += 1

# Example usage
# you can change the values of the triangle rows
print_isosceles_triangle_while(5)