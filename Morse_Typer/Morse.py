
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

    transmitting = True
    while transmitting:
        translated_phrase = []

        User_Input = input("Type 'list' fo a list of symbols and abbreviations\n>>  ")

        if User_Input == "list":
            print('R = Roger, Yes\nN = No, Negative\nDE = This is from [Code Name]\nEC = End of Transmission\nQRZ = "Who is calling me?"')
            continue

        words = User_Input.split("  ")

        for word in words:
            for letter in word.split(" "):
                try:
                    translated_phrase.append(alphabet[letter])
                except KeyError:
                    translated_phrase.append("[Unknown Value]")
            translated_phrase.append(" ")

        print("".join(translated_phrase))

        if ". -.-." in User_Input: # if EC is in the user's text...
            print("-_-_-Transmission ended-_-_-")
            transmitting = False


if __name__ == "__main__":
    morse_to_letters()