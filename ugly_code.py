from dataclasses import dataclass

import cv2
import numpy as np


@dataclass
class InsanelyLongFunctionInput:
    introduction: str
    number_to_be_squared: int
    text_to_be_shouted: str
    expansion: str
    conlusion: str


def insanely_long_function(text_input: InsanelyLongFunctionInput):
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
        insanely_long_function(InsanelyLongFunctionInput("hehe", 123132, "siuuuu", np.array2string(test_array), "wow!"))
    )
