"""Getting some practice with dictionary functions!"""

__author__: str = "730580318"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if value in inverted_dict:
            raise KeyError("Duplicate values found in input dictionary!")
        inverted_dict[value] = key
    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(color_dict: dict[str, str]) -> str:
    color_counts: dict[str, int] = {}
    for person in color_dict:
        color = color_dict[person]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    most_common_color = ""
    highest_count = 0

    for color in color_counts:
        if color_counts[color] > highest_count:
            most_common_color = color
            highest_count = color_counts[color]

    return most_common_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    output_dict = {}
    for word in words:
        length = len(word)
        if length not in output_dict:
            output_dict[length] = set()
        output_dict[length].add(word)
    return output_dict
