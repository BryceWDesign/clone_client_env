import multiprocessing as mp
import traceback


class Worker(mp.Process):
    """A worker process that can return exceptions from the worker process"""

    def __init__(self, *args, **kwargs):
        mp.Process.__init__(self, *args, **kwargs)
        self._conn, _ = mp.Pipe(duplex=True)
        self._exception = None

    def run(self):
        """Runs the worker process and sends any exceptions to the parent process"""
        try:
            mp.Process.run(self)
            self._conn.send(None)
        except Exception as err:  # pylint: disable=broad-except
            trace = traceback.format_exc()
            self._conn.send((err, trace))

    @property
    def exception(self):
        """Returns the exception thrown by the worker process, if any"""
        if self._conn.poll(0.0001):
            self._exception = self._conn.recv()

        return self._exception
