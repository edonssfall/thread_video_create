import concurrent.futures
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
app_path = os.environ['APP_PATH']


class FFMpegThreads:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self.futures = []

    def run_command(self, command):
        subprocess.run(['python3', app_path])

    def add_message(self, message):
        future = self.executor.submit(self.run_command, message)
        self.futures.append(future)

    def wait_for_complete(self):
        for future in concurrent.futures.as_completed(self.futures):
            print(f'Future {future} finished.')
        print('All commands finished.')
