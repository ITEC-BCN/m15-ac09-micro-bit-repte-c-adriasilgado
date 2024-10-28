let numeroRandomReceptor = 0
let numeroRandomEmisor = 0
// Hola
radio.onReceivedNumber(function (receivedNumber) {
    numeroRandomReceptor = receivedNumber
    if (numeroRandomEmisor > numeroRandomReceptor) {
        basic.showIcon(IconNames.Happy)
    } else if (numeroRandomEmisor < numeroRandomReceptor) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendString("Si lees esto me debes un beso, si sigues leyendo, dos.")
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    numeroRandomEmisor = randint(1, 6)
    radio.sendNumber(numeroRandomEmisor)
    if (numeroRandomEmisor > numeroRandomReceptor) {
        basic.showIcon(IconNames.Happy)
    } else if (numeroRandomEmisor < numeroRandomReceptor) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
