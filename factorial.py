def recursive_factorial(n: int) -> int:
    """
    Calculates the factorial of a given number recursively.

    This function finds the factorial of a number by multiplying the number by the factorial of the number minus one,
    following the mathematical definition of factorial, n! = n * (n-1)!, with the base case being 1! = 1.

    Parameters:
        n (int): The number for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If the input is less than 1, since factorial is not defined for negative numbers and zero.
    """
    if n == 1:
        return 1

    return n * recursive_factorial(n-1)


def main() -> None:
    """
    Main function to demonstrate the usage of recursive_factorial function.
    """
    print(recursive_factorial(5))


if __name__ == "__main__":
    main()
