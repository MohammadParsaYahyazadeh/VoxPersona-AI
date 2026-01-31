def emphasize(text):
    keywords = ["future", "new", "discover", "smart", "power"]
    for w in keywords:
        text = text.replace(w, f"... {w.upper()} ...")
    return text
