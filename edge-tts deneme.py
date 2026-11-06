import edge_tts
import _asyncio

async def merhaba():
    sesliMetin = edge_tts.Communicate(text="Merhaba YBS",voice="tr-TR-AhmetNeural")
    return sesliMetin

merhaba()