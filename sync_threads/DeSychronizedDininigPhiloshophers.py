from threading import Lock, Thread
import logging


class DeSynchronizedDiningPhilosophers:

    def __init__(self):
        # Set the number of forks.
        self.N_FORKS = 5
        # Initialize the fork-related locks.
        self.forks = [Lock() for n in range(self.N_FORKS)]
        # Initialize philosophers' names.
        self.philosopherNames = ['Aristotle','Kant','Buddha','Marx', 'Russel']
        # Initialize philosopher threads.
        self.philosophers = []
        # Set the logging format.
        log_format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

    def philosopher(self, name, left, right):
        while True:
            with left:
                with right:
                    logging.info('Philosopher {:s} is eating'.format(name))

    def create_philosophers(self):
        for n in range(self.N_FORKS):
            thread = Thread(target=self.philosopher,args=(self.philosopherNames[n],
                                                          self.forks[n], self.forks[(n+1) % self.N_FORKS]))
            self.philosophers.append(thread)

    def run_philosophers(self):
        for p in self.philosophers:
            p.start()


def main():
    de_sync_philosophers = DeSynchronizedDiningPhilosophers()
    de_sync_philosophers.create_philosophers()
    de_sync_philosophers.run_philosophers()


if __name__ == '__main__':
    main()