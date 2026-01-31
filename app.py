import gradio as gr
from tts.engine import text_to_speech
from tts.voices import VOICES
import os

def generate(text, character):
    os.makedirs("output", exist_ok=True)
    out = "output/voice.wav"
    text_to_speech(text, VOICES[character], out)
    return out

ui = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(lines=4, label="Ad Script"),
        gr.Dropdown(list(VOICES.keys()), label="Voice")
    ],
    outputs=gr.Audio(type="filepath"),
    title="AI Ad Voice Generator"
)

ui.launch()
