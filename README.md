# VoxPersona AI

VoxPersona AI is an AI-driven system that converts text into engaging advertisement-style videos using synthetic speech, a virtual character, and dynamic subtitles.  
The project is designed for AI demos, virtual presenters, and automated video content generation.

---

## ✨ Key Features

- Text-to-Speech voice narration
- Virtual character video presentation
- Automatic subtitle generation
- Vertical video format (1080x1920) for ads and social media
- Simple, modular Python codebase
- Fully offline and local execution

---

## 🧠 Tech Stack

- Python 3.9+
- MoviePy
- Pillow (PIL)
- NumPy
- SciPy
- Optional: Gradio (for UI extension)

---

## 📂 Project Structure

├── app.py
├── requirements.txt
├── tts/
│   ├── engine.py
│   └── voices.py
├── video/
│   └── make_video.py
├── assets/
│   ├── character.png      (optional)
│   └── bg_music.mp3       (optional)
├── output/
