#!/usr/bin/env python3
import asyncio

import websockets


async def handler(websocket, path):
    print("[ws_server] New WS connection")
    try:
        async for msg in websocket:
            print("[ws_server] Received:", msg)
            await websocket.send("echo: " + msg)
    except websockets.exceptions.ConnectionClosed:
        print("[ws_server] Connection closed")


async def main():
    host = "127.0.0.1"
    port = 9002
    async with websockets.serve(handler, host, port):
        print(f"[ws_server] Listening on :{port}")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
