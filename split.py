import os
import sys
import pysrt
from pydub import AudioSegment

def split_audio(srt_path, audio_path):
    # Load SRT and audio files
    subs = pysrt.open(srt_path, encoding="utf-8")
    if not os.path.exists(srt_path):
        print(f"SRT file not found: {srt_path}")
        sys.exit(1)
    if len(subs) == 0:
        print("No subtitles found")
        sys.exit(1)

    audio = AudioSegment.from_mp3(audio_path)

    # Create output directory if it doesn't exist
    if not os.path.exists("fracs"):
        os.mkdir("fracs")

    # Split audio based on SRT timestamps
    for index, sub in enumerate(subs):
        print(f"Processing {index + 1}/{len(subs)}")
        start_time = sub.start.to_time().strftime("%H:%M:%S.%f")
        end_time = sub.end.to_time().strftime("%H:%M:%S.%f")
        content = sub.text.replace("\n", " ").replace(" ", "_")

        start_time_ms = sub.start.ordinal
        end_time_ms = sub.end.ordinal

        # Extract and export the audio segment
        audio_segment = audio[start_time_ms:end_time_ms]
        audio_segment.export(f"fracs/{content}.ogg", format="ogg")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <srt_file_path> <audio_file_path>")
        sys.exit(1)

    srt_path = sys.argv[1]
    audio_path = sys.argv[2]

    split_audio(srt_path, audio_path)

if __name__ == "__main__":
    main()
