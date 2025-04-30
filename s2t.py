import argparse
import os
from transcribers.deepgram_backend import transcribe_deepgram
from transcribers.faster_whisper_backend import transcribe_whisper

def main():
    parser = argparse.ArgumentParser(description="Transcribe audio using Whisper or Deepgram.")
    parser.add_argument("audio_path", help="Path to the audio file (WAV/MP3)")
    parser.add_argument("-l", "--language", help="The language of the audio.", default="en")
    parser.add_argument("--offline", action="store_true", help="Use Whisper locally instead of Deepgram API")

    args = parser.parse_args()

    if args.offline:
        print("[+] Running in offline mode (Faster Whisper)...")
        text = transcribe_whisper(args.audio_path, language=args.language)
    else:
        print("[+] Running in online mode (Deepgram)...")
        text = transcribe_deepgram(args.audio_path, language=args.language)

    print("\n📝 Transcription:\n")
    print(text)

if __name__ == "__main__":
    main()
