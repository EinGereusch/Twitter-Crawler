import asyncio
import os
from typing import List
import aiohttp
import youtube_dl

event_loop = asyncio.get_event_loop()


async def download_photos(urls: List[str], destination_dir: str):
    async with aiohttp.ClientSession() as session:
        for image in urls:
            response = await session.get(image, allow_redirects=True)
            open(f"{destination_dir}{os.sep}{image.split('/')[-1]}", 'wb').write(await response.read())


async def download_video(url: str, destination_dir: str):
    opts = {
        "outtmpl": f"{destination_dir}{os.sep}%(id)s.%(ext)s"
    }
    with youtube_dl.YoutubeDL(opts) as ydl:
        try:
            await event_loop.run_in_executor(None, lambda: ydl.download([url]))
        except:
            pass
