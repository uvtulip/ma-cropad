import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler


keyboard = KMKKeyboard()


#Direct pins
keyboard.col_pins = (
    board.GP26, #SW1
    board.GP27, #SW2
    board.G28,  #SW3
    board.G29,  #SW4
    board.GP6,  #SW5
    board.GP4,  #EC11_S1
)


keyboard.row_pins = (board.GP0,)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW


#Coordinate Mapping
keyboard.coord_mapping = [
    0, 1, 2, 3, 4, 5
]


#Keymap
keyboard.keymap = [[
    KC.COPY,  #SW1
    KC.PASTE, #SW2
    KC.CUT,   #SW3
    KC.UNDO,  #SW4
    KC.DELETE,#SW5
    KC.MUTE,  #EC11_S1
]]


encoder = EncoderHandler()
keyboard.modules.append(encoder)


encoder.pins = (
    (board.GP2, board.GP3, None),
)


encoder.map = [
    ((KC.VOLD, KC.VOLU),),
]


if __name__=='__main__':
    keyboard.go()

    