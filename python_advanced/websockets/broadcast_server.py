#!/usr/bin/env python3
"""WebSocket broadcast server distributing messages to all clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message: str) -> None:
    """Send a prefixed message to all currently connected clients."""
    payload = f"B:{message}"
    for client in list(connected_clients):
        try:
            await client.send(payload)
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Register a client, broadcast its messages, and unregister on exit."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket broadcast server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
#!/usr/bin/env python3
"""WebSocket broadcast server distributing messages to all clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(message: str) -> None:
    """Send a prefixed message to all currently connected clients."""
    payload = f"B:{message}"
    for client in list(connected_clients):
        try:
            await client.send(payload)
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Register a client, broadcast its messages, and unregister on exit."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket broadcast server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
