import pygame
import os

# Initialize pygame mixer once
pygame.mixer.init()

def play_audio(file_path):
    """Play an audio file (WAV or MIDI) using pygame."""
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")

        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except pygame.error as e:
        print(f"Error playing {file_path}: {e}")

def main():
    # Example file paths
    wav_file = "wave.wav"
    midi_file = "lonely.mid"

    for file in [wav_file, midi_file]:
        if os.path.exists(file):
            play_audio(file)
        else:
            print(f"File not found: {file}")

if __name__ == "__main__":
    main()
