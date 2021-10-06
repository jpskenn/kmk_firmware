import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.GP15,
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11
        # ,
        # board.GP10,
        # board.GP9,
        # board.GP8,
        # board.GP7,
        # board.GP6
    )
    col_pins = (
        # board.GP15,
        # board.GP14,
        # board.GP13,
        # board.GP12,
        # board.GP11,
        board.GP10,
        board.GP9,
        board.GP8,
        board.GP7,
        board.GP6
    )
    diode_orientation = DiodeOrientation.COL2ROW
    # i2c = board.I2C
    powersave_pin = board.GP23
