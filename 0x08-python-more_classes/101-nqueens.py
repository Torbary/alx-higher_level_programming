#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

# Import the sys module
from sys import argv

if __name__ == "__main__":
    """Initialize an empty list to store the solution"""
    a = []

    if len(argv) != 2:
        """checks is the number of arguments is correct"""
        print("Usage: nqueens N")
        exit(1)

    if argv[1].isdigit() is False:
        """Check if the argument is a number"""
        print("N must be a number")
        exit(1)

    # Convert the argument to an integer and store it in the variable n
    n = int(argv[1])

    # Check if the value of n is at least 4
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the answer list
    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """Funcition to checks if the queen already exist in the
            same row( y value)
        """
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """Function that reject a solution if its not valid"""
        if (already_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """Function to clear the solution from a point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """Recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):  # Accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # Continue with the next x value

    # Start the backtracking process at x = 0
    nqueens(0)
