result = ""


def recursive_reverse(string: str) -> str:

    """
    Recursively reverses the given string.

    Parameters:
    string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    global result
    if len(string) == 1:
        result += string
        return result
    result += string[-1]
    return recursive_reverse(string[:-1])


def main() -> None:
    """
    Main function to demonstrate the usage of recursive_reverse function.
    """
    print(recursive_reverse("hello"))


if __name__ == "__main__":
    main()
