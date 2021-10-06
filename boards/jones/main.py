print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GP15,
    board.GP14,
    board.GP13,
    board.GP12,
    board.GP11
    ,
    board.GP10,
    board.GP9,
    board.GP8,
    board.GP7,
    board.GP6
)
keyboard.row_pins = (
    board.GP15,
    board.GP14,
    board.GP13,
    board.GP12,
    board.GP11,
    board.GP10,
    board.GP9,
    board.GP8,
    board.GP7,
    board.GP6
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    keyboard.go()