# speech-to-textVoice Assistant
This project is a simple Python-based voice assistant that:

- Converts audio input to text

- Generates responses using OpenAI's API

- Converts responses back to audio

## 1. Features
Speech recognition → SpeechRecognition

Text-to-speech → pyttsx3

AI-powered responses → OpenAI API 

## 2. Files Structure
-main.py → main script of the voice assistant

-dddd

## 3. Installation
- Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/voice-assistant.git
cd voice-assistant

- Create and activate a conda environment

lua

conda create -n voicebot python=3.10
conda activate voicebot

- Install dependencies
r

conda install -c conda-forge pyaudio
pip install SpeechRecognition pyttsx3 openai

## 4. Usage
1. Add your OpenAI API Key inside main.py.

2. Run the program:

css

python main.py

3.Speak into your microphone and the assistant will reply with voice output.

### 5. Example
Input: "Hello"

Output: "Hi! How can I help you today?"

