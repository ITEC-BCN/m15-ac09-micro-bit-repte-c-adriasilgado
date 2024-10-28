numeroRandomReceptor = 0
numeroRandomEmisor = 0
#Hola

def on_received_number(receivedNumber):
    global numeroRandomReceptor
    numeroRandomReceptor = receivedNumber
    if numeroRandomEmisor > numeroRandomReceptor:
        basic.show_icon(IconNames.HAPPY)
    elif numeroRandomEmisor < numeroRandomReceptor:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.ASLEEP)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("Si lees esto me debes un beso, si sigues leyendo, dos.")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global numeroRandomEmisor
    numeroRandomEmisor = randint(1, 6)
    radio.send_number(numeroRandomEmisor)
    if numeroRandomEmisor > numeroRandomReceptor:
        basic.show_icon(IconNames.HAPPY)
    elif numeroRandomEmisor < numeroRandomReceptor:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)
