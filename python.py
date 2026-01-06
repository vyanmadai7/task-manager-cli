import pyttsx3  # Import text to speech library

engine = pyttsx3.init()  # Initialize the TTS engine

# Set voice properties
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 1)  # Volume level

# Function to make the AI speak
def speak(text):
    engine.say(text)        # Text to speak
    engine.runAndWait()     # Play the speech

# Main program
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            speak("Goodbye")
            break
        speak(user_input)   # Repeats what you write
