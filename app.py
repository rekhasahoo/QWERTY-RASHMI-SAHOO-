from flask import Flask, request, jsonify, send_from_directory,render_template, redirect, url_for  # type: ignore
import os
import whisper  # type: ignore

app = Flask(__name__)

# Load the Whisper model
'''model = whisper.load_model("base")'''
model = whisper.load_model("tiny")


'''@app.route('/')
def home():
    """Redirects to the signup page."""
    return redirect(url_for('serve_signup'))

@app.route('/signup')
def serve_signup():
    """Serves the signup page."""
    return send_from_directory('.', 'signup.html')

@app.route('/signin')
def serve_signin():
    """Serves the signin page."""
    return send_from_directory('.', 'signin.html')

@app.route('/registration')
def serve_registration():
    """Serves the registration page."""
    return send_from_directory('.', 'registration.html')
'''    
@app.route('/')
def home():
    """Redirects to the signup page."""
    return redirect(url_for('serve_signup'))

@app.route('/signup')
def serve_signup():
    """Serves the signup page."""
    return render_template('signup.html') # type: ignore

@app.route('/signin')
def serve_signin():
    """Serves the signin page."""
    return render_template('signin.html') # type: ignore

@app.route('/registration')
def serve_registration():
    """Serves the registration page."""
    return render_template('registration.html') # type: ignore


@app.route('/upload', methods=['POST'])
def upload_audio():
    """Handles audio file uploads, processes transcription, and returns the result."""
    if 'audio_file' not in request.files:
        return jsonify({"message": "No audio file provided"}), 400

    audio_file = request.files['audio_file']
    context = request.form.get("context", "").lower()  # Optional context (e.g., "email")
    filename = audio_file.filename

    # Save the audio file to the 'uploads' directory
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", filename)
    audio_file.save(file_path)

    try:
        # Transcribe the audio using Whisper
        result = model.transcribe(file_path)
        transcribed_text = result.get("text", "")

        # Preprocess transcription if the context indicates email
        if context == "email":
            transcribed_text = preprocess_email_transcription(transcribed_text)

        # Delete the uploaded file to save space
        os.remove(file_path)

        return jsonify({"message": "Audio file processed successfully.", "text": transcribed_text})
    except Exception as e:
        return jsonify({"message": f"Failed to process audio: {str(e)}"}), 500

def preprocess_email_transcription(transcription):
    """
    Preprocess transcription text to format it as an email address.

    Replaces common verbal patterns like "at the rate" and "dot" with "@" and ".".
    """
    transcription = transcription.lower()
    transcription = transcription.replace("at the rate", "@")
    transcription = transcription.replace("dot", ".")
    transcription = transcription.replace(" ", "")  # Remove spaces for email formatting
    return transcription

'''if __name__ == '__main__':
    app.run(debug=True)'''
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
