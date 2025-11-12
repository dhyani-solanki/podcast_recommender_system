# 🎧 Emotion-Based Spotify Podcast Recommender  

## 💡 Project Overview  

This project is an **AI-powered Flask web application** that detects a user’s **emotion** using **facial expressions** and **voice tone**, and then recommends matching **Spotify podcasts** based on the detected mood.  

It combines **computer vision**, **audio processing**, and **Spotify’s Web API** to create a personalized and emotionally intelligent listening experience.  

---

## 🚀 Key Features  

- 😄 **Facial Emotion Detection** — Uses camera input to detect emotions like *happy, sad, angry, surprised, neutral*, etc.  
- 🎤 **Voice Emotion Analysis** — Records your voice and extracts acoustic features for emotion recognition.  
- 🎧 **Spotify Podcast Recommendation** — Fetches mood-appropriate podcasts using the Spotify API.  
- 🧠 **Smart Emotion Fusion** — Combines both face and voice cues for more accurate emotion prediction.  
- 🌐 **Interactive Flask Web Interface** — Simple and intuitive UI built with HTML templates.  

---

## 🧠 Tech Stack  

| Component | Technology |
|------------|-------------|
| **Backend** | Python (Flask) |
| **Frontend** | HTML, CSS |
| **Face Emotion Detection** | OpenCV, DeepFace) |
| **Voice Analysis** | PyAudio, NumPy |
| **Spotify API** | Spotify Web API via `requests` or `spotipy` |
| **Machine Learning** | Pre-trained emotion recognition models |

---

## ⚙️ How It Works  

1. **User visits the web app** (home page).  
2. The system:  
   - Captures a photo using the webcam.  
   - Records a short voice sample.  
3. Extracts features from both sources and predicts emotion (e.g., *happy*, *sad*, *angry*).  
4. Uses **Spotify API** to fetch **podcasts that match the emotion**.  
5. Displays the detected emotion and recommended podcasts on the web page.  

---

## 🧩 Folder Structure  
<img width="547" height="245" alt="image" src="https://github.com/user-attachments/assets/5b35fd55-4626-479f-a7a2-03cda4c70ae1" />


---

## 🔑 Environment Variables  

You’ll need to provide your **Spotify API credentials**:  

```python
CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"


