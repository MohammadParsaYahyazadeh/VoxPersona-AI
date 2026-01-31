def emotion_settings(emotion):
    presets = {
        "neutral": {"speed": 1.0},
        "energetic": {"speed": 1.15},
        "dramatic": {"speed": 0.9},
        "happy": {"speed": 1.1},
        "calm": {"speed": 0.95}
    }
    return presets.get(emotion, presets["neutral"])
