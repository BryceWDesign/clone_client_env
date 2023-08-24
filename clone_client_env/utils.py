import asyncio
from os import environ
from contextlib import contextmanager
from typing import Iterator

from clone_client.client import Client


RPC_CLIENT_CONTINUOUS_TIMEOUT = str(0.005)  # 5ms
RPC_CLIENT_CRITICAL_TIMEOUT = str(0.0035)  # 3.5ms


async def connect_client(hostname) -> Client:
    environ["CONTROL_CLIENT_CRITICAL_RPC_TIMEOUT"] = RPC_CLIENT_CRITICAL_TIMEOUT
    environ["CONTROL_CLIENT_CONTINUOUS_RPC_TIMEOUT"] = RPC_CLIENT_CONTINUOUS_TIMEOUT
    environ["STATE_CLIENT_CRITICAL_RPC_TIMEOUT"] = RPC_CLIENT_CRITICAL_TIMEOUT
    environ["STATE_CLIENT_CONTINUOUS_RPC_TIMEOUT"] = RPC_CLIENT_CONTINUOUS_TIMEOUT

    client = Client(server=hostname)
    await client.__aenter__()  # pylint: disable=unnecessary-dunder-call
    return client


@contextmanager
def client_connection(hostname) -> Iterator[tuple[asyncio.AbstractEventLoop, Client]]:
    loop = asyncio.new_event_loop()
    client = loop.run_until_complete(connect_client(hostname))
    yield (loop, client)

    loop.run_until_complete(
        client.__aexit__(None, None, None)
    )  # pylint: disable=unnecessary-dunder-call
