import cv2
from deepface import DeepFace
import sounddevice as sd
import soundfile as sf
import librosa
import numpy as np

def detect_face_emotion():
    cap = cv2.VideoCapture(0)
    print("🎥 Webcam started (press 'q' to stop)")
    dominant_emotion = "neutral"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']
            cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        except:
            pass

        cv2.imshow("Detecting...", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return dominant_emotion

def record_audio(duration=5, filename='audio.wav'):
    samplerate = 44100
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, audio, samplerate)

def extract_voice_features(filename='audio.wav'):
    audio, sr = librosa.load(filename)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)
