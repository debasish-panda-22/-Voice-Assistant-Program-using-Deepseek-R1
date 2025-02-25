import speech_recognition as sr
import webbrowser
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import whisper
import numpy as np
import wave
import os
import ffmpeg
import torch
import ollama
import re





# Initialization of models
recognizer = sr.Recognizer()
engine = pyttsx3.init()

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("base", device=device)
desiredModel="deepseek-r1:1.5b"


def speak(result):
    engine.say(result)
    engine.runAndWait()




# transcribe recorded audio to text using openA Whisper
def transcribe(temp_audio_file):
    result = model.transcribe(temp_audio_file, language="en")  # Force English
    text = result["text"].strip().lower()

    # Ignore hallucinations (very long/repetitive text)
    if len(text) > 50 or text.count("a little bit") > 3:
        print("⚠️ Ignoring hallucinated text:", text)
        return ""

    return text


def processCommand(c):
    print(f"Processing command: {c}")  # Debugging output
    c = c.lower().strip()

    if "open" in c:
        c=c.split()           # split sentence into words and put it in the list
        speak(f"Opening{c[1]}")
        webbrowser.open_new(f"https://www.{c[1]}.com")
    else:
        speak("Initializing Deepseek")
        questionToAsk=c
        response= ollama.chat(model=desiredModel, messages=[                 # using ollama and deepseek r1 1.5b model to answer question  
        
            {
                "role":"system",
                "content":questionToAsk
            }

        ])
        pattern = r'<think>.*?</think>'          

        OllamaResponse=response["message"]["content"]      
        output_text = re.sub(pattern, '', OllamaResponse, flags=re.DOTALL)      #removing <think> <think> using regular expression

        speak(output_text.strip())



if __name__ == "__main__":
    speak("Initializing")
    while True:
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1.2)  # Adjust to background noise
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)

            # Save AudioData to a temporary WAV file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
                temp_wav.write(audio.get_wav_data())
                temp_wav_path = temp_wav.name

            word = model.transcribe(temp_wav_path, language="en")  # Force English
            os.remove(temp_wav_path)  # Clean up temp file

            spoken_text = word["text"].strip().lower()

            # Ignore if Whisper generates hallucinated text
            if len(spoken_text) > 50 or spoken_text.count("a little bit") > 3:
                print("⚠️ Ignoring hallucinated text:", spoken_text)
                continue

            print(f"Recognized speech: {spoken_text}")

            if spoken_text == "computer":  # Use a better wake word than "hello"
                speak("Yes? Listening for command.")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Listening to command...")
                    try:
                        audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)
                    except sr.WaitTimeoutError:
                        print("⚠️ No command detected, retrying...")
                        continue

                # Save command audio to a file for transcription
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_cmd_wav:
                    temp_cmd_wav.write(audio.get_wav_data())
                    temp_cmd_wav_path = temp_cmd_wav.name

                command_text = transcribe(temp_cmd_wav_path)
                os.remove(temp_cmd_wav_path)  # Clean up

                if command_text:
                    processCommand(command_text)
        
        except sr.WaitTimeoutError:
            print("⚠️ No speech detected, retrying...")
            continue  # Keep the loop running

        except Exception as e:
            print(f"❌ Error: {e}")
