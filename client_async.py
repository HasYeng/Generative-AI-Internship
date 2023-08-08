import asyncio
import websockets
import concurrent.futures


async def receive_messages(websocket):
    """
    Coroutine to continuously receive messages from the server.
    """
    try:
        while True:
            message = await websocket.recv()
            print(message)
    except websockets.exceptions.ConnectionClosedOK:
        print("You have disconnected from the server.")


def input_message():
    """Function to get input message from the user."""
    return input()


async def chat_client():
    """
    This function handles connecting to the server, sending messages,
    and receiving messages using websockets.
    """
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        nickname = input("Enter your nickname: ")
        await websocket.send(nickname)
        asyncio.get_event_loop().create_task(receive_messages(websocket))

        while True:
            message = await asyncio.get_event_loop().run_in_executor(
                concurrent.futures.ThreadPoolExecutor(), input_message
            )
            if message.lower() == "quit":
                break
            await websocket.send(message)


asyncio.get_event_loop().run_until_complete(chat_client())