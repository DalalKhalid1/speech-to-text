import speech_recognition as sr
import pyttsx3
import cohere

# Cohere API
COHERE_API_KEY = "YOUR_COHERE_API_KEY"
co = cohere.Client(COHERE_API_KEY)

# تحويل النص إلى صوت
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# تحويل الصوت إلى نص
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio, language="en")
        print(" You said:", text)
        return text
    except sr.UnknownValueError:
        print(" Could not understand audio.")
        return ""
    except sr.RequestError:
        print(" Service unavailable.")
        return ""

# توليد رد من LLM
def generate_response(prompt):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=100
    )
    reply = response.generations[0].text.strip()
    print("🤖 Bot:", reply)
    return reply

# تشغيل البوت
while True:
    command = listen()
    if command:
        reply = generate_response(command)
        speak(reply)