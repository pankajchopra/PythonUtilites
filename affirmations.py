# import speech
import time

import pyttsx3

def text_to_speech(text, rate=200, pause_duration=0.5):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set speech rate (speed)
    engine.setProperty('rate', rate)

    # Convert the text to speech
    engine.say(text)

    # Set pause duration between sentences
    engine.setProperty('pause', pause_duration)

    # Wait for the speech to finish
    engine.runAndWait()

# if __name__ == "__main__":
#     input_text = input("Enter the text you want to convert to speech: ")
#     input_rate = int(input("Enter the speech rate speed (default is 200): "))
#     input_pause = float(input("Enter the pause duration between sentences in seconds (default is 0.5): "))
#     text_to_speech(input_text, rate=input_rate, pause_duration=input_pause)

def count_words(sentence):
    # Split the sentence into words 
    words = sentence.split()  # Count the number of words 
    num_words = len(words)
    return num_words


def speak_affirmations(_affirmations, _repeat):
    index = 1
    for _ in range(_repeat):
        for affirmation in _affirmations:
            text_to_speech(affirmation, rate=100)
            text_to_speech(affirmation, rate=100)
            # time.sleep(count_words(affirmation)/2)
            text_to_speech("again, speak after me..")
            text_to_speech(affirmation, rate=100)
            # time.sleep(count_words(affirmation)/2)
            index = index + 1
        text_to_speech("Don't forget you are the best.", rate=100)


if __name__ == "__main__":
    affirmations = ["This is a temporary phase, and I trust in my ability to create a brighter future.",
                    "My worth is not defined by my job, and I possess valuable skills and strengths.",
                    "I deserve success and abundance, and I will persevere with confidence.",
                    "Every challenge is an opportunity for growth, and I will emerge stronger from this experience.",
                    "I am surrounded by love and support.",
                    "I am capable of overcoming any challenge that comes my way.",
                    "I am worthy of a life filled with joy, peace, and vitality.",
                    "God is with me always me every moment."]
    repeat = 1  # Number of times to repeat each affirmation
    speak_affirmations(affirmations, repeat)
