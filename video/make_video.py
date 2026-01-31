from moviepy.editor import *
import os

AUDIO = "output/voice.wav"
IMAGE = "assets/character.png"  # optional
MUSIC = "assets/bg_music.mp3"   # optional
OUT = "output/ad.mp4"

def make_ad():
    audio = AudioFileClip(AUDIO)

    if os.path.exists(IMAGE):
        clip = ImageClip(IMAGE).set_duration(audio.duration)
    else:
        clip = ColorClip((1080,1920), color=(10,10,10)).set_duration(audio.duration)

    clip = clip.set_audio(audio)

    if os.path.exists(MUSIC):
        bg = AudioFileClip(MUSIC).volumex(0.2)
        final_audio = CompositeAudioClip([bg, audio])
        clip = clip.set_audio(final_audio)

    clip.write_videofile(OUT, fps=24)

make_ad()
