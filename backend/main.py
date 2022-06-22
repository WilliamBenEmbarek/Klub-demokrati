from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import os
import eyed3
import random

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # Modify below function to vote
    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    # Modify below function to broadcast winning track (to show information on user devices)
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()
admins = []
players = []
songs = []

directory = "../assets"

class Song:
    def __init__(self, id, song_name, artist_name, votes):
        self.id = id
        self.song_name = song_name
        self.artist_name = artist_name
        self.votes = votes  

def load_songs(songs):
    i = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f.endswith(".mp3"):
            audio = eyed3.load(f)
            song_name = audio.tag.title
            song_artist = audio.tag.artist
            song_image = audio.tag.images[0]
            image_descriptor = open(os.path.join(directory,filename+".jpg"), "wb")
            image_descriptor.write(song_image.image_data)
            image_descriptor.close()        
            songs.append(Song(i, song_name, song_artist, 0))
            i = i + 1

load_songs(songs)

def vote(id):
    #TODO
    print(f"voted for song {id}")

def choose_new_songs(songs):
    songs_in_round = random.sample(songs, k)
    print(f"Chose songs {*songs_in_round.title,}")
    songs = [song for song in songs if song not in songs_in_round]
    return songs_in_round


@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Game Logic Time!
            message_handler(data)
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

@app.websocket("/ws/admin/{client_id}")
def message_handler(data):
    game_data = data.split(":")
    match game_data[0]:
        case "adminJoin":
            print(f"an admin joined the game with id {game_data[1]}")
            admins.append(game_data[1])
        case "playerJoin":
            print(f"A player with id {game_data[1]} joined the game")
            players.append(game_data[1])
        case "playerVote":
            print(f"player with id {game_data[1]} voted for song {game_data[2]}")

