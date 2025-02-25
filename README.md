# Voice Assistant Program using Deepseek-R1

## Overview
This is a **Python-based Voice Assistant** that listens for a wake word ("computer"), recognizes voice commands, and performs various tasks such as opening websites and answering questions using AI. It utilizes **OpenAI Whisper** for speech recognition, **Deepseek-R1 (via Ollama)** for answering questions, and **pyttsx3** for text-to-speech output.

## Features
### 🎤 Voice Command Processing
- Listens for the wake word **"computer"** to start processing commands.
- Uses **Whisper AI** for accurate speech-to-text transcription.
- Ignores hallucinated or irrelevant text to improve accuracy.

### 🌐 Web Browsing
- Opens websites based on voice commands.  
  Example:  
  - **User:** "Open YouTube"  
  - **Assistant:** *"Opening YouTube"* (Launches `https://www.youtube.com` in the browser)

### 🤖 AI-Powered Responses
- Uses **Deepseek-R1 (via Ollama)** to generate intelligent answers for general queries.
- Filters unnecessary text (such as `<think>` tags) to improve response quality.

### 🗣️ Speech Output
- Converts responses into natural-sounding speech using **pyttsx3**.
- Speaks back AI-generated answers or confirms actions like opening websites.

### 🔥 GPU Support
- Detects if a **CUDA-compatible GPU** is available for faster **Whisper AI** transcription.

## Technologies Used
| Technology         | Purpose |
|--------------------|---------|
| `SpeechRecognition` | Captures and converts speech to text |
| `Webbrowser`       | Opens websites based on commands |
| `Pyttsx3`          | Converts text to speech |
| `Whisper (OpenAI)` | High-accuracy speech-to-text transcription |
| `Ollama` + `Deepseek-R1` | AI model for answering questions |
| `Torch (CUDA)`     | Uses GPU for performance optimization |

## How It Works
1. The assistant listens continuously for the wake word **"computer"**.
2. Once activated, it records and transcribes the user's voice command.
3. If the command includes **"open [website]"**, it opens the corresponding website.
4. Otherwise, it sends the command to **Deepseek-R1** via Ollama for an AI-generated response.
5. The response is cleaned, processed, and converted into speech output.

## Installation
### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install speechrecognition pyttsx3 sounddevice scipy whisper torch ollama
```

### 2️⃣ Run the Program
```bash
python voice_assistant.py
```

### 3️⃣ Usage Instructions
- **Say "computer"** to activate the assistant.
- **Give a command**, such as:
  - `"Open Google"` (Opens `https://www.google.com`)
  - `"What is the capital of Japan?"` (AI responds: `"The capital of Japan is Tokyo."`)
  - `"Who is Elon Musk?"` (AI provides details about Elon Musk)

## File Structure
```
/voice_assistant
│── voice_assistant.py   # Main program file
│── requirements.txt     # Dependencies list
│── README.txt           # Documentation
```

## Notes
- Requires a **working microphone** for voice input.
- The assistant only processes **English commands**.
- GPU acceleration is **optional** but recommended for better performance.

## Future Improvements
✅ Improve wake word detection with **hotword libraries** like **Porcupine**  
✅ Add **multi-language support** using Whisper’s multilingual models  
✅ Implement a **GUI interface** for easier interaction  

## License
This project is for **educational purposes only**. Not affiliated with OpenAI or Hulu.

## Author
Created by **Debasish Panda**
