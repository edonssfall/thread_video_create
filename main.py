from thread import FFMpegThreads


if __name__ == "__main__":
    max_workers = 4
    with FFMpegThreads(max_workers=max_workers) as thread:
        thread.add_message(0)
        thread.add_message(1)
        thread.add_message(2)
        thread.add_message(3)

        thread.wait_for_complete()
