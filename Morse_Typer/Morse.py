import numpy
import pyaudio

#The entire ContinuousWaves class was written by AI. I am not proud of myself.

class ContinuousWaves:

    def __init__(self):
        self.frequency = 815
        self.samplerate = 44100
        self.volume = 0.8

    def generate_tone(self, duration_ms):
        num_samples = int(self.samplerate * duration_ms / 1000) #From ms to Samples   cus that's how u do it

        t = numpy.arange(num_samples) / self.samplerate
        return self.volume * numpy.sin(2 * numpy.pi * self.frequency * t)

    def generate_silence(self, duration_ms):
        num_samples = int(self.samplerate * duration_ms / 1000)
        return numpy.zeros(num_samples)

    def play(self, signal):
        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.samplerate,
                        output=True)

        stream.write(signal.astype(numpy.float32).tobytes())
        stream.stop_stream()
        stream.close()
        p.terminate()

def morse_to_letters():
    alphabet = {
        #-----------PUNCTUATION
        "|": "\n",
        #-----------ALPHABET
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        #-----------NUMBERS
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
    }
    cw = ContinuousWaves()

    transmitting = True
    while transmitting:
        translated_phrase = []

        User_Input = input("Type 'list' fo a list of symbols and abbreviations\n>>  ")
        if User_Input == "list":
            print('R = Roger, Yes\nN = No, Negative\nDE = This is from [Code Name]\nEC = End of Transmission\nQRZ = "Who is calling me?"')
            continue



        signal = []
        Dot_Time = 100

        """
        User_Input = "-.. .  .-.. --- -..."
        
        User_Input.split(" ") will give ['-..', '.', '', '.-..', '---', '-...']
        The "" isn't recognized in alphabet[letter] and that causes [Unknown Value]
        
        by adding the if letter == "" this problem is resolved
        """

        for letter in User_Input.split(" "):
            if letter == "":
                translated_phrase.append(" ")
                continue
            try:
                translated_phrase.append(alphabet[letter])
            except KeyError:
                translated_phrase.append("[Unknown Value]")


        for symbol in User_Input:

            if symbol == ".":
                signal.append(cw.generate_tone(Dot_Time))
            elif symbol == "-":
                signal.append(cw.generate_tone(Dot_Time * 3))
            elif symbol == " ":
                signal.append(cw.generate_silence(Dot_Time * 3))
            elif symbol == "|":
                signal.append(cw.generate_silence(Dot_Time * 2))
            signal.append(cw.generate_silence(Dot_Time))

        print("".join(translated_phrase))


        if ". -.-." in User_Input: # if EC is in the user's text...
            print("-_-_-Transmission ended-_-_-")
            transmitting = False

        final_signal = numpy.concatenate(signal)
        cw.play(final_signal) #MUST be at the end or else it'll be annoying.

if __name__ == "__main__":
    morse_to_letters()