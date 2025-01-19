input.onButtonPressed(Button.A, function () {
    duty = Math.min(duty + 1, 5)
    pins.analogWritePin(AnalogPin.P1, duty * 200)
    basic.showNumber(duty)
})
input.onButtonPressed(Button.AB, function () {
    music.play(music.stringPlayable("- - B - B - B - ", 300), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C5 C5 B A - G - G ", 300), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("E - G D D D - - ", 300), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    duty = Math.max(duty - 1, 0)
    pins.analogWritePin(AnalogPin.P1, duty * 200)
    basic.showNumber(duty)
})
let duty = 0
duty = 0
basic.showNumber(duty)
