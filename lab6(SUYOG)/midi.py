# Ensure you install the required libraries first
# pip install pydub pygame

import os
from pydub import AudioSegment
from pydub.playback import play
import pygame

def play_wav(file_path):
    # Load the WAV file
    audio = AudioSegment.from_wav(file_path)
    # Play the WAV file
    play(audio)

def play_midi(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the MIDI file
    pygame.mixer.music.load(file_path)
    # Play the MIDI file
    pygame.mixer.music.play()
    # Wait until the music finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    # Example file paths
    wav_file = ""
    midi_file = "example.mid"

    if os.path.exists(wav_file):
        print(f"Playing WAV file: {wav_file}")
        play_wav(wav_file)
    else:
        print(f"WAV file not found: {wav_file}")

    if os.path.exists(midi_file):
        print(f"Playing MIDI file: {midi_file}")
        play_midi(midi_file)
    else:
        print(f"MIDI file not found: {midi_file}")

if __name__ == "__main__":
    main()
