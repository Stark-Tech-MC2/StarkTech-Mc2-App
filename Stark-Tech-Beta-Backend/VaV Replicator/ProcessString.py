def process_string(text):
    """
    Processes a string by adding leading zeros for single digits, removing spaces,
    replacing periods with hyphens, and keeping consecutive digits unchanged.

    Args:
        text: The input string to be processed.

    Returns:
        The processed string.
    """
    result = ""
    prev_char = ""  # Track the previous character

    for char in text:
        if char.isdigit():
            # Add leading zero only if single digit and not preceded by another digit or hyphen
            if len(result) > 0 and not prev_char.isdigit() and prev_char != "-":
                result += "0"
            result += char
        elif char == " ":
            result += "-"
        elif char == ".":
            if prev_char.isdigit():
                # Replace period with hyphen only if preceded by a digit
                result += "-"
            else:
                # Treat period as part of consecutive digits
                result += char
        else:
            result += char

        prev_char = char  # Update previous character for all characters

    # Remove any trailing hyphens
    result = result.rstrip("-")

    # Add leading zero to the last part if it's a single digit
    parts = result.split("-")
    last_part = parts[-1]
    if len(last_part) == 1 and last_part.isdigit():
        parts[-1] = "0" + last_part

    result = "-".join(parts)

    return result