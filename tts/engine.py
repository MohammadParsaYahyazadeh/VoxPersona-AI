import edge_tts
import asyncio
import threading

def _run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro)
    loop.close()

async def _speak(text, voice, out):
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="+5%",
        pitch="+0Hz"
    )
    await communicate.save(out)

def text_to_speech(text, voice, out):
    t = threading.Thread(
        target=_run_async,
        args=(_speak(text, voice, out),)
    )
    t.start()
    t.join()
