import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr


class VoiceAssistant:
    def __init__(self, wake_word: str | None = None):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.wake_word = wake_word.lower() if wake_word else None

    def speak(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, phrase_time_limit: int = 5) -> str | None:
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source, phrase_time_limit=phrase_time_limit)
        try:
            text = self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
        return text.lower()

    def wait_for_wake_word(self) -> str | None:
        if not self.wake_word:
            return self.listen()
        while True:
            heard = self.listen()
            if heard is None:
                continue
            if self.wake_word in heard:
                self.speak("Yes")
                break
        return self.listen()

    def tell_time(self) -> str:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {now}"

    def open_app(self, command: str) -> str:
        if "chrome" in command:
            os.system("open -a 'Google Chrome'")
            return "Opening Google Chrome"
        if "notes" in command:
            os.system("open -a 'Notes'")
            return "Opening Notes"
        if "spotify" in command:
            os.system("open -a 'Spotify'")
            return "Opening Spotify"
        return "I do not know that application"

    def search_web(self, command: str) -> str:
        trigger_words = ["search", "google", "look up"]
        query = command
        for word in trigger_words:
            query = query.replace(word, "")
        query = query.strip()
        if not query:
            return "What should I search for"
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Searching the web for {query}"

    def handle_command(self, command: str | None) -> str:
        if command is None:
            return "I did not catch that"
        if "time" in command:
            return self.tell_time()
        if "open" in command:
            return self.open_app(command)
        if "search" in command or "google" in command or "look up" in command:
            return self.search_web(command)
        if "help" in command:
            return (
                "You can say, what time is it, open Chrome, "
                "open Notes, search cute cat videos, or say stop to quit"
            )
        if "stop" in command or "exit" in command or "quit" in command:
            return "exit"
        return "I do not recognize that command"

    def run(self) -> None:
        self.speak("Hello, I am your personal voice assistant")
        while True:
            if self.wake_word:
                command = self.wait_for_wake_word()
            else:
                command = self.listen()
            response = self.handle_command(command)
            if response == "exit":
                self.speak("Goodbye")
                break
            self.speak(response)


def main() -> None:
    assistant = VoiceAssistant(wake_word=None)
    assistant.run()


if __name__ == "__main__":
    main()
