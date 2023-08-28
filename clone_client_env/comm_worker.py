import asyncio
from multiprocessing.connection import Connection
import multiprocessing as mp
from typing import Iterable, Optional

from clone_client.client import Client
from clone_client.error_frames import RpcTimeoutError

from clone_client_env.utils import client_connection
from clone_client_env.worker import Worker


class CommWorker(Worker):
    """Worker that sreads telemetry data from the server."""

    def __init__(
        self,
        hostname: str,
        observations: Iterable[float],
        lock: mp.Lock,
        conn: Connection,
        timeout: float,
    ):
        self._hostname = hostname
        self._timeout = timeout
        self._lock = lock
        target = self._start_comm
        args = (observations,)

        super().__init__(target=target, args=args)
        self._conn = conn

    async def _get_pressures(self, client: Client) -> Optional[Iterable[float]]:
        try:
            return await asyncio.wait_for(client.get_pressures(), timeout=self._timeout)
        except (asyncio.TimeoutError, RpcTimeoutError):
            return None

    def _start_comm(self, current_obs) -> None:
        with client_connection(self._hostname) as (loop, client):
            while True:
                pressures = loop.run_until_complete(self._get_pressures(client))
                if pressures is not None:
                    with self._lock:
                        current_obs[:] = pressures
