import cv2
import numpy as np

import utils


def insanely_long_function(
    who_the_f_needs_so_long_argument_name, and_another_one, next_one_and_still_going, whatadafak, pls_stop_im_done
):
    what_are_we_even_doing = (
        who_the_f_needs_so_long_argument_name
        + str(and_another_one**2)
        + next_one_and_still_going.upper()
        + whatadafak
        + pls_stop_im_done
    )
    return what_are_we_even_doing


if __name__ == "__main__":
    print(f"OpenCV version: {cv2.__version__}", f"NumPy version: {np.__version__}", sep='\n')
    test_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(insanely_long_function("hehe", "siuuuu", 123132, test_array, "wow!"))
