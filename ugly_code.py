"""Creating an expanded statement function implementation.
"""
from dataclasses import dataclass

import cv2
import numpy as np


@dataclass
class TextToConstructAnExtendedStatement:
    """Input to create_an_expanded_statement function"""

    introduction: str
    number_to_be_squared: int
    text_to_be_shouted: str
    expansion: str
    conlusion: str


def create_an_expanded_statement(text_input: TextToConstructAnExtendedStatement):
    """Creating an expanded statement.

    It combines introduction, number raised to the second power,
    text which is shouted (by changing letters to upper case),
    expansion and conclusion of statement.
    """
    what_are_we_even_doing = (
        text_input.introduction
        + str(text_input.number_to_be_squared**2)
        + text_input.text_to_be_shouted.upper()
        + text_input.expansion
        + text_input.conlusion
    )
    return what_are_we_even_doing


if __name__ == "__main__":
    print(f"OpenCV version: {cv2.__version__}", f"NumPy version: {np.__version__}", sep="\n")
    test_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(
        create_an_expanded_statement(
            TextToConstructAnExtendedStatement("hehe", 123132, "siuuuu", np.array2string(test_array), "wow!")
        )
    )
