def recursive_reverse(string: str) -> str:

    """
    Recursively reverses the given string.

    Parameters:
    string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    result = [x for x in string]

    if len(string) == 1:
        return string[0]

    return result.pop() + recursive_reverse("".join([x for x in result]))


def main() -> None:
    """
    Main function to demonstrate the usage of recursive_reverse function.
    """
    print(recursive_reverse("hello"))


if __name__ == "__main__":
    main()
