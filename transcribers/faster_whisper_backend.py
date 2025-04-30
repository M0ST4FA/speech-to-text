from faster_whisper import WhisperModel
import os

def transcribe_whisper(audio_path: str, language: str = "en") -> str:
        """
        Transcribe an audio file using faster-whisper.
        """
        model = WhisperModel(
            "base",
            device="cuda",
            compute_type="float16"
        )
        segments, info = model.transcribe(audio_path, language=language)

        transcript = []
        for segment in segments:
            transcript.append(segment.text.strip())

        return "\n".join(transcript)