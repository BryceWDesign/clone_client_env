import asyncio
from typing import Iterable
from multiprocessing.connection import Connection
import multiprocessing as mp

from clone_client.client import Client
from clone_client.error_frames import RpcTimeoutError

from clone_client_env.utils import client_connection
from clone_client_env.worker import Worker


class CtrlWorker(Worker):
    """Worker that sends muscle actions to the server."""

    def __init__(
        self,
        hostname: str,
        queue: mp.Queue,
        conn: Connection,
        timeout: float,
    ):
        self._hostname = hostname
        self._timeout = timeout
        self._queue = queue
        target = self._start_ctrl

        super().__init__(target=target)
        self._conn = conn

    async def _set_muscles(
        self, client: Client, current_actions: Iterable[float]
    ) -> None:
        try:
            await asyncio.wait_for(
                client.controller_tunnel.set_muscles(current_actions),
                timeout=self._timeout,
            )
        except (asyncio.TimeoutError, RpcTimeoutError):
            pass

    def _start_ctrl(self) -> None:
        with client_connection(self._hostname) as (loop, client):
            while True:
                actions = self._queue.get()
                loop.run_until_complete(self._set_muscles(client, actions))
