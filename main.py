from thread import FFMpegThreads


if __name__ == "__main__":
    max_workers = int(input())
    with FFMpegThreads(max_workers=max_workers) as thread:
        for i in range(max_workers):
            thread.add_message(i)

        thread.wait_for_complete()
