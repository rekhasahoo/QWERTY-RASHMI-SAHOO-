Here’s an updated version of the README file based on the new project structure:

---

# Voice-Assisted Form Filling Using Flask and Whisper AI

This project is a Voice-Assisted Form Filling Application that uses Flask as the backend framework and OpenAI's Whisper AI for real-time voice recognition. Users can record their voice to fill out form fields, enhancing accessibility and efficiency in form submission processes. The application is designed to help users complete forms using voice commands instead of typing.

### Project Link (After Deployment)
[https://form-filling-by-voice-beyond-qwerty-3.onrender.com](https://form-filling-by-voice-beyond-qwerty-3.onrender.com)

---

## Features

- **Real-time Voice Transcription**: Record and transcribe audio input for form fields.
- **Dynamic Form UI**: HTML, CSS, and JavaScript are used to create an interactive and user-friendly frontend.
- **Flask Backend**: Manages form submission, voice recording, and integration with Whisper AI for transcription.
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

### System Dependencies
- **Python 3.8+**

- **FFmpeg**: Required for processing audio files. Install it based on your OS:
  - On Ubuntu/Debian: `sudo apt install ffmpeg`
  - On Mac: `brew install ffmpeg`
  - On Windows: Download the FFmpeg executable from [FFmpeg.org](https://ffmpeg.org) and add it to your system's PATH.

### Python Libraries
Run the following command to install the required Python libraries:

```
pip install flask flask-cors whisper
```

---

## Project Structure

```
project/
├── app.py                    # Main Flask application file
├── templates/                 # Folder for HTML templates
│   ├── signup.html           # Signup page
│   ├── signin.html           # Sign-in page
│   ├── registration.html     # Registration page
```

---

## How to Run

1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python libraries:
   ```
   pip install flask flask-cors whisper
   ```

3. Make sure FFmpeg is installed on your system.

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000` to use the application.

---

## Notes

- Ensure your microphone permissions are enabled to use the voice recording feature.
- You can change the port number if needed by modifying the `app.py` file.

---

This README provides an overview of the project's features, setup, and structure. Let me know if you need any more modifications!
