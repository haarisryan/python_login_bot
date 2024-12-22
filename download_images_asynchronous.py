import asyncio
import aiohttp
async def download_image(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(filename, 'wb') as f:
                f.write(await response.read())
            print(f"Downloaded {filename}")

async def function1():
    url="https://wallpapercave.com/wp/wp2113016.jpg"
    await download_image(url,"wwe1.jpg")
    print("func1")
async def function2():
    url="https://wallpapercave.com/wp/wp2113016.jpg"
    await download_image(url,"wwe2.jpg")
    print("func2")
async def function3():
    url="https://wallpapercave.com/wp/wp2113016.jpg"
    await download_image(url,"wwe3.jpg")
    print("func3")


async def main():
    await asyncio.gather(function1(),function2(),function3())
    
asyncio.run(main())    
