#!/usr/bin/env python3
"""ASGI application serving static web client files and a WebSocket."""

from pathlib import Path
from starlette.applications import Starlette
from starlette.routing import Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocketDisconnect

BASE_DIR = Path(__file__).resolve().parent


async def websocket_endpoint(websocket):
    """Accept a WebSocket connection on /ws and echo text messages."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        WebSocketRoute("/ws", websocket_endpoint),
        Mount(
            "/",
            app=StaticFiles(directory=str(BASE_DIR), html=True),
            name="static",
        ),
    ]
)
