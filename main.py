def recursive_sum(n: int) -> int:
    """
    Calculates the recursive sum of digits of an integer until a single digit is obtained.

    This function takes an integer, splits its digits, and recursively sums them up until a single digit remains.
    The process involves converting the integer to a string, splitting it into digits, converting back to integers,
    and performing the sum recursively.

    Parameters:
        n (int): The integer whose digits are to be summed recursively.

    Returns:
        int: The recursive sum of digits of the integer.
    """
    list_of_nums = [int(x) for x in str(n)]

    # base case
    if len(list_of_nums) == 1:
        return list_of_nums[0]

    # recursive case
    return list_of_nums.pop() + recursive_sum(int("".join([str(x) for x in list_of_nums])))


def main() -> None:
    """
    Main function to demonstrate the usage of recursive_sum function.
    """
    print(recursive_sum(1234))


if __name__ == "__main__":
    main()
