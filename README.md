# Speech-to-Text Voice Assistant

This project is a simple Python-based voice assistant that:

- Converts audio input to text
- Generates responses using OpenAI's API
- Converts responses back to audio

## 1. Features
- Speech recognition → SpeechRecognition  
- Text-to-speech → pyttsx3  
- AI-powered responses → OpenAI API  

## 2. Files Structure
- `main.py` → main script of the voice assistant

## Screenshots
![App Screenshot](voice-assistant/Screenshot_1.png.png)

## 3. Installation
- Create and activate a conda environment:
```bash
conda create -n voicebot python=3.10
conda activate voicebot
 ```
```bash
- Install dependencies:

conda install -c conda-forge pyaudio
pip install SpeechRecognition pyttsx3 openai
 ```
 
## 4. Usage

1.Add your OpenAI API Key inside main.py.
2.Run the program:
python main.py

Speak into your microphone and the assistant will reply with voice output.

## 5. Example

-Input: "Hello"
-Output: "Hi! How can I help you today?"

