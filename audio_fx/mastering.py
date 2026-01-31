import pyloudnorm as pyln

def normalize_loudness(audio, sr=24000):
    meter = pyln.Meter(sr)
    loudness = meter.integrated_loudness(audio)
    return pyln.normalize.loudness(audio, loudness, -16.0)
