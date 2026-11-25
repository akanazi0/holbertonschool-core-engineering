#!/usr/bin/env python3
"""Minimal WebSocket echo server."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Receive messages from a client and echo them back unchanged."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
