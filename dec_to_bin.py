def recursive_dec_to_bin_converter(dec_num: int) -> int:
    """
        Recursively converts a decimal number to its binary representation.

        Parameters:
        dec_num (int): The decimal number to be converted.

        Returns:
        int: The binary representation of the decimal number.
    """

    if dec_num == 0:
        return 0
    elif dec_num // 2 == 0:
        return 1

    m = dec_num // 2

    return recursive_dec_to_bin_converter(m) * 10 + (dec_num % 2)


def main() -> None:
    """
    Main function to demonstrate the usage of recursive_dec_to_bin_converter function.
    """
    print(recursive_dec_to_bin_converter(12))


if __name__ == "__main__":
    main()
