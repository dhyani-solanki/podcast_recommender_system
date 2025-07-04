from flask import Flask, render_template, request
from spotify import get_spotify_podcasts
from emotion import detect_face_emotion, record_audio, extract_voice_features

app = Flask(__name__)

CLIENT_ID = "c8b7e54cca1548be8971646d6e983746"
CLIENT_SECRET = "71427c9e1c1e43edad7a63f510a218a7"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    face_emotion = detect_face_emotion()
    record_audio()
    voice_features = extract_voice_features()

    podcasts = get_spotify_podcasts(face_emotion, CLIENT_ID, CLIENT_SECRET)

    return render_template('index.html',
                           emotion=face_emotion,
                           podcasts=podcasts)

if __name__ == '__main__':
    app.run(debug=True)
