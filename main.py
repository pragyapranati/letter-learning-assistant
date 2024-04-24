import os
import speech_recognition as sr
from gtts import gTTS
import pygame

# Function to recognize speech using PocketSphinx
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_sphinx(audio)
        print("Letter which you have spoken : "+text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Could not request results from PocketSphinx service.")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()  # Stop playback before removing the file
    pygame.quit()  # Clean up Pygame resources
    # Add a delay to ensure the file is fully released
    pygame.time.wait(100)
    os.remove("output.mp3")

# Main function
def main():
    letters = ['a','b','c','apple','bullet','car']  # List of letters to teach
    for letter in letters:
        # Teach the letter
        speak(f"Let's learn the letter {letter}.")
        speak(f"This is the letter {letter}. Can you say '{letter}'?")
        
        # Listen for the child's response
        response = recognize_speech()
        
        # Provide feedback
        if response == letter:
            speak("Great job! You said the letter correctly.")
        else:
            speak(f"Oops! That doesn't sound like the letter {letter}. Try again!")

if __name__ == "__main__":
    main()
