print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP14, board.GP15)
keyboard.row_pins = (board.GP16, board.GP17)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


// 2*2マトリクスのうち、2行めは1キーだけ使用する例
coord_mapping = []
coord_mapping.extend(ic(0, x) for x in range(2))
coord_mapping.append(ic(1, 1))

keyboard.keymap = [
    [KC.A,  KC.B],
    [       KC.C]
]

if __name__ == '__main__':
    keyboard.go()