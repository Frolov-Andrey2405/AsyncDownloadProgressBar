import asyncio
import httpx
import tqdm


# Function to download files asynchronously
async def download_files(url: str, filename: str):
    """
    Downloads a file from the given URL and saves it with the specified filename.

    :param url: The URL of the file to download.
    :param filename: The name of the file to save.
    """
    with open(filename, 'wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url) as r:
                r.raise_for_status()
                total = int(r.headers.get('content-length', 0))

                # Initialize a progress bar using tqdm
                prog_bar = tqdm.tqdm(
                    total=total, unit='MB',
                    unit_scale=True, desc=url)
                async for chunk in r.aiter_bytes():
                    f.write(chunk)
                    # Update the progress bar
                    prog_bar.update(len(chunk) // (1 << 20))


# Main function to initiate downloads
async def main():
    """
    Downloads multiple files concurrently using asyncio.
    """
    loop = asyncio.get_running_loop()

    urls = [
        ('http://ipv4.download.thinkbroadband.com/50MB.zip', '50MB.zip'),
        ('http://ipv4.download.thinkbroadband.com/200MB.zip', '200MB.zip'),
        ('http://ipv4.download.thinkbroadband.com/20MB.zip', '20MB.zip'),
    ]

    # Create tasks for each download and gather them using asyncio.gather
    tasks = [
        loop.create_task(download_files(url, filename))
        for url, filename in urls]
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    # Run the main function using asyncio.run()
    asyncio.run(main())
