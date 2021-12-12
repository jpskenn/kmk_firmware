import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP15
    )
    row_pins = (
        board.GP6,
        board.GP27,
        board.GP22,
        board.GP19,
        board.GP17,
        board.GP7,
        board.GP26,
        board.GP21,
        board.GP18,
        board.GP16
    )
    diode_orientation = DiodeOrientation.COLUMNS
    rollover_cols_every_rows = 5

