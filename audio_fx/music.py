import librosa

def mix_music(voice, music_path, sr=24000):
    music, _ = librosa.load(music_path, sr=sr)
    music = music[:len(voice)]
    return voice + 0.15 * music
