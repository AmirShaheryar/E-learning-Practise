from faster_whisper import WhisperModel
import os

print("Loading local Whisper model...")
model = WhisperModel("base", device="cpu", compute_type="int8")

video_file = os.path.join("data", "raw_media", "lecture.mp4")

print(f"Transcribing {video_file}...")
segments, info = model.transcribe(video_file)

print(f"\nLanguage Detected: {info.language} (Confidence: {info.language_probability:.2f})\n")

print("--- TIMESTAMPED TRANSCRIPT ---")
for segment in segments:

    start_min = int(segment.start // 60)
    start_sec = int(segment.start % 60)
    
    end_min = int(segment.end // 60)
    end_sec = int(segment.end % 60)
    
    time_tag = f"[{start_min:02d}:{start_sec:02d} -> {end_min:02d}:{end_sec:02d}]"
    
    print(f"{time_tag} {segment.text}")