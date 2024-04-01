import time


def recursive_count_down(n: int) -> int:
    """
        Performs a countdown from a given number to 1, pausing for one second between each step.

        This function demonstrates a simple use of recursion combined with time delay to create a countdown effect.
        It prints each number of the countdown to the console, pausing for one second before proceeding to the next
        number, until it reaches 1.

        Parameters:
            n (int): The starting number of the countdown.

        Returns:
            int: The final number of the countdown, which is always 1.
        """
    if n == 1:
        return 1

    print(n)
    time.sleep(1)

    return recursive_count_down(n - 1)

def main() -> None:
    """
    Main function to demonstrate the usage of recursive_count_down function.
    """
    print(recursive_count_down(10))


if __name__ == "__main__":
    main()
