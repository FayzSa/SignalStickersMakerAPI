import asyncio
import os
import anyio
from signalstickers_client import StickersClient
from signalstickers_client.models import LocalStickerPack, Sticker
from flask import Flask, jsonify
import requests
import json
import time
from flask import request

app = Flask(__name__)


async def main(packTitle, packAuthor, listofStick, coverStick):
    def add_sticker(path, emoji):

        stick = Sticker()
        stick.id = pack.nb_stickers
        stick.emoji = emoji

        with open(path, "rb") as f_in:
            stick.image_data = f_in.read()

        pack._addsticker(stick)

    pack = LocalStickerPack()

    # Set here the pack title and author
    pack.title = packTitle
    pack.author = packAuthor

    # Add the stickers here, with their emoji
    # Accepted format:
    # - Non-animated webp
    # - PNG
    # - GIF <100kb for animated stickers
    for i in listofStick:
        add_sticker(i, "🤪")

    # Specifying a cover is optionnal
    # By default, the first sticker is the cover
    cover = Sticker()
    cover.id = pack.nb_stickers
    # Set the cover file here
    with open(coverStick, "rb") as f_in:
        cover.image_data = f_in.read()
    pack.cover = cover

    # Instanciate the client with your Signal crendentials
    async with StickersClient('165f3c42-886c-4017-a620-f3199c049d49.2', 'T7dYGpKVqVCc90DP5cMeyg') as client:
        # Upload the pack
        pack_id, pack_key = await client.upload_pack(pack)

# How to obtain your Signal credentials? In Signal Desktop, open the Developer Tools, and type
# window.reduxStore.getState().items.uuid_id to get your USER
# and  window.reduxStore.getState().items.password to get your PASSWORD.

    print("Pack uploaded!\n\nhttps://signal.art/addstickers/#pack_id={}&pack_key={}".format(pack_id, pack_key))
    link = {
        "link": "https://signal.art/addstickers/#pack_id={}&pack_key={}".format(pack_id, pack_key)
    }

    response = app.response_class(
        response=json.dumps(link),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/makeSticks/', methods=['POST'])
def create_Stickers():
    D = asyncio.run(main(request.json['packName'], request.json['authorName'],
                         request.json['listOfSticks'], request.json['cover']))

    # D = asyncio.run(main(request.json['packName'],  request.json['authorName'],
    #      request.json['listofStick'], request.json['cover']))
    return D, 201


if __name__ == "__main__":
    app.run(debug=False, use_reloader=True)
