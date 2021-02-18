from threading import Lock, Thread
import logging
import time


class SynchronizedThreads:

    def __init__(self):
        # Initialize a list for threads.
        self.threads = []
        # Initialize lock objects.
        self.lock_a = Lock()
        self.lock_b = Lock()
        # Set the logging format.
        log_format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

    def thread_a(self):
        logging.info('Thread A is starting ...')
        logging.info('Thread A is waiting to acquire lock A.')
        self.lock_a.acquire()
        logging.info('Thread A has acquired lock A, performing some calculation...')
        time.sleep(2)
        logging.info('Thread A is waiting to acquire lock B.')
        self.lock_b.acquire()
        logging.info('Thread A has acquired lock B, performing some calculation...')
        time.sleep(2)
        logging.info('Thread A is releasing both locks.')
        self.lock_a.release()
        self.lock_b.release()

    def thread_b(self):
        logging.info('Thread B is starting...')
        logging.info('Thread B is waiting to acquire lock B.')
        self.lock_a.acquire()
        logging.info('Thread B has acquired lock B, performing some calculation...')
        time.sleep(5)
        logging.info('Thread B is waiting to acquire lock A.')
        self.lock_b.acquire()
        logging.info('Thread B has acquired lock A, performing some calculation...')
        time.sleep(5)
        logging.info('Thread B is releasing both locks.')
        self.lock_b.release()
        self.lock_a.release()

    def start_threads(self):
        for thread_func in [self.thread_a, self.thread_b]:
            self.threads.append(Thread(target=thread_func))
            self.threads[-1].start()

    def join_threads(self):
        for thread in self.threads:
            thread.join()


def main():
    sync_threads = SynchronizedThreads()
    sync_threads.start_threads()
    sync_threads.join_threads()
    logging.info('Finished')


if __name__ == '__main__':
    main()