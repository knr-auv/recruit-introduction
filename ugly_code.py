"""docstring"""
import cv2
import numpy as np


def insanely_long_function(
    who_the_f_needs_so_long_argument_name, and_another_one, next_one_and_still_going, whatadafak, pls_stop_im_done
):
    """docstring"""
    what_are_we_even_doing = (
        who_the_f_needs_so_long_argument_name
        + "\n"
        + and_another_one * 2
        + "\n"
        + str(next_one_and_still_going).upper()
        + "\n"
        + whatadafak
        + "\n"
        + pls_stop_im_done
    )
    return what_are_we_even_doing


if __name__ == "__main__":
    print(cv2.__version__, np.__version__)
    test_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(insanely_long_function("hehe", "siuuuu", 123132, str(test_array), "wow!"))
