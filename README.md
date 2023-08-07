# AsyncDownloadProgressBar

## Description

AsyncDownloadProgressBar is a Python script that allows you to download multiple files asynchronously using the asyncio framework. It provides a progress bar using the `tqdm` library to visually track the download progress. This script is designed to efficiently download large files concurrently.

## Technology Used and Library Installation

To use the AsyncDownloadProgressBar script, you need to have Python installed on your system. The script uses the `httpx` library for making asynchronous HTTP requests and the `tqdm` library for displaying progress bars. You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

Make sure you have `pip` installed and properly configured.

## How to Use Using venv

1. Clone or download the repository to your local machine.

2. Navigate to the project directory using your terminal.

3. Create a virtual environment (venv) to isolate the project dependencies:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required libraries from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the `main.py` script to start downloading the files asynchronously:

   ```bash
   python main.py
   ```

The script will initiate the asynchronous download of the specified files from the provided URLs. The progress bars will indicate the download progress for each file. Here is an example of how the download progress might look in the console:

```
http://ipv4.download.thinkbroadband.com/200MB.zip:  0%|■■■■■■■        | 0.00/210M [00:00<?, ?MB/s]
http://ipv4.download.thinkbroadband.com/50MB.zip:   0%|■■■■■          | 0.00/52.4M [00:00<?, ?MB/s]
http://ipv4.download.thinkbroadband.com/50MB.zip:   0%|■■■            | 0.00/52.4M [00:00<?, ?MB/s]
```

Once the downloads are complete, the script will exit.

Remember to deactivate the virtual environment after you are done using the script:

```bash
deactivate
```

Enjoy efficient and concurrent file downloads with the AsyncDownloadProgressBar script!

**Note:** The provided URLs in the `main.py` script are for demonstration purposes. You can modify the `urls` list in the script to specify your own URLs and filenames for downloading.
