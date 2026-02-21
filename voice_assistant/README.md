# Syntecxhub_Personal_voice_Assistant

This is a simple personal voice assistant written in Python. It:

- Listens to your voice through the microphone
- Uses online speech-to-text to understand commands
- Maps commands to actions (tell time, open apps, search the web)
- Speaks responses back using text-to-speech

## Requirements

- Python 3.10+
- macOS (the `open` commands are written for macOS apps)
- Microphone with permission granted to your terminal app

## Installation

Create and activate a virtual environment (recommended), then install dependencies:

```bash
cd /Users/macbook/Documents/trae_projects/voice_assistant
pip install pyttsx3 SpeechRecognition pyaudio
```

If `pyaudio` fails to install on macOS, install PortAudio first:

```bash
brew install portaudio
pip install pyaudio
```

## Running the assistant

From the project folder:

```bash
python assistant.py
```

You should hear a greeting such as:

> Hello, I am your personal voice assistant

Then you can speak commands like:

- "What time is it"
- "Open Chrome"
- "Open Notes"
- "Open Spotify"
- "Search cute cat videos"
- "Google Python tutorial"
- "Look up weather today"
- "Help"
- "Stop" / "Exit" / "Quit"

The assistant will perform the action and speak a response. Saying "stop", "exit", or "quit" will end the program.

## Changing behavior

To use a wake word (for example, "assistant"), open `assistant.py` and change:

```python
assistant = VoiceAssistant(wake_word=None)
```

to:

```python
assistant = VoiceAssistant(wake_word="assistant")
```

You can add more applications to open by editing the `open_app` function in `assistant.py` and adding more `if` checks with the appropriate `open -a 'App Name'` commands.
