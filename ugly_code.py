"""
Ta normalnie docstring jest dodawany
"""
import numpy as np
import cv2


def insanely_long_function(
    who_the_f_needs_so_long_argument_name,
    and_another_one,
    next_one_and_still_going,
    whatadafak,
    pls_stop_im_done,
):
    """Ta normalnie docstring funkcji"""
    what_are_we_even_doing = (
        who_the_f_needs_so_long_argument_name
        + and_another_one**2
        + next_one_and_still_going
        + whatadafak
        + pls_stop_im_done
    )
    return what_are_we_even_doing


if __name__ == "__main__":
    print(cv2.__version__, np.__version__)
    test_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(insanely_long_function(123, 456, 789, test_array, 101112))
