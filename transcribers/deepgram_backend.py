import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load from .env if available

API_KEY = os.getenv("DEEPGRAM_API_KEY")

def transcribe_deepgram(audio_path: str, language: str = "en") -> str:
    if not API_KEY:
        raise RuntimeError("DEEPGRAM_API_KEY not found in environment.")

    with open(audio_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    response = requests.post(
        "https://api.deepgram.com/v1/listen",
        headers={
            "Authorization": f"Token {API_KEY}",
            "Content-Type": "audio/wav",  # Adjust if using MP3, etc.
        },
        data=audio_data,
        params={
            "language": language,
        }
    )

    if response.status_code != 200:
        raise RuntimeError(f"Deepgram failed: {response.status_code} - {response.text}")

    return response.json()['results']['channels'][0]['alternatives'][0]['transcript']
