from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.keymap = [
    [
        KC.ESC,     KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.EQL,   KC.PSLS,  KC.PAST,  KC.PMNS,  KC.PPLS,
            KC.TAB,     KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,       KC.BSPC,      KC.P7,    KC.P8,    KC.P9,
            KC.LCTL,    KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.MINS,    KC.ENT,       KC.P4,    KC.P5,    KC.P6,
        KC.LSFT,    KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.NO,    KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.UP,    KC.P1,    KC.P2,    KC.P3,
        KC.NO,      KC.NO,    KC.LALT,     KC.LGUI,      KC.SPC,             KC.SPC,         KC.RGUI,    KC.RALT,     KC.LEFT,    KC.DOWN,  KC.RGHT,  KC.P0,    KC.PDOT
    ]
]

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
