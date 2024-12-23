# Voice-Assisted Form Filling Using Flask and Whisper AI  

This project is a **Voice-Assisted Form Filling Application** that uses **Flask** as the backend framework and **OpenAI's Whisper AI** for real-time voice recognition. Users can record their voice to fill out form fields, enhancing accessibility and efficiency in form submission processes.  
Thelink afterdeployment of the project: https://form-filling-by-voice-beyond-qwerty-3.onrender.com

---

## Features  

- **Real-time Voice Transcription**: Record and transcribe audio input for form fields.  
- **Dynamic Form UI**: HTML, CSS, and JavaScript are used to create an interactive and user-friendly frontend.  
- **Flask Backend**: Handles form submission, voice recording, and integration with Whisper AI for transcription.  
- **Whisper AI Integration**: Uses Whisper for highly accurate transcription of user voice input.  

---

## Technologies Used  

### Frontend  
- **HTML**: Structure of the web interface.  
- **CSS**: Styling for an aesthetically pleasing design.  
- **JavaScript**: Adds interactivity, such as recording buttons and dynamic field updates.  

### Backend  
- **Python**: Programming language for the backend logic.  
- **Flask**: Framework for managing API endpoints and server operations.  
- **Whisper AI**: OpenAI's state-of-the-art model for speech-to-text processing.  

---

## Prerequisites  

Before running the project, ensure you have the following installed:  

- **Python 3.8+**  
- **FFmpeg**: Required for processing audio files. Install it based on your OS:  
  - On Ubuntu/Debian: `sudo apt install ffmpeg`  
  - On Mac: `brew install ffmpeg`  
  - On Windows: Download the FFmpeg executable from [FFmpeg.org](https://ffmpeg.org/) and add it to your system's PATH.  

- **Python Libraries**:  
  ```bash
  pip install flask flask-cors whisper
