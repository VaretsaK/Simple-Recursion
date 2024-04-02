def recursive_fibonacci(n: int) -> int:
    """
        Recursively computes the nth Fibonacci number.

        Parameters:
        n (int): The index of the Fibonacci number to be computed. Must be a positive integer.

        Returns:
        int: The nth Fibonacci number.

        Raises:
        ValueError: If the input is not a positive integer.
    """
    if n < 1:
        raise ValueError("Only positive numbers!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def main() -> None:
    """
    Main function to demonstrate the usage of recursive_fibonacci function.
    """
    print(recursive_fibonacci(10))


if __name__ == "__main__":
    main()
