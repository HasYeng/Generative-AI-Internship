import asyncio
import websockets
from datetime import datetime

clients = []


async def handle_client(websocket, path):
    """
    This function is responsible for managing individual client connections,
    including receiving messages from clients, broadcasting them to other clients,
    and managing join/leave notifications.
    """

    clients.append(websocket)
    nickname = await websocket.recv()
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{nickname} joined the chat at {t}!")
    await websocket.send(f"Hello, {nickname}! Joined at {t}.")

    for client in clients:
        if client != websocket:
            await client.send(f"{nickname} joined at {t}!")

    try:
        async for message in websocket:
            t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Received message from {nickname} at {t}: {message}")
            for client in clients:
                if client != websocket:
                    await client.send(f"{nickname} at {t}: {message}")

    except:
        pass

    finally:
        t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{nickname} left the chat at {t}.")
        clients.remove(websocket)
        for client in clients:
            await client.send(f"{nickname} left the chat at {t}!")


start_s = websockets.serve(handle_client, "localhost", 12345)

print(f"Chat server started on localhost:12345")
asyncio.get_event_loop().run_until_complete(start_s)
asyncio.get_event_loop().run_forever()
