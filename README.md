# Signal Stickers Maker API  

This is an API made by Python ( Flask ) , the goal of this API is to made Stickers in Signal Messenger App .

## Installation
First add project in your local computer or server .

- Cd the the project dir

- Install Virtual env for flask 
```bash
$ virtualenv flask
```
- Then 
```bash
$ cd flask 
```
- Now let's activate the virtualenv
```bash
$ source bin/activate 
```
Now you should see (flask) on the left of the command line.



- Install all the requirements 

```bash
$ pip install -r requirements.txt
```

## Usage

```python
    # Instanciate the client with your Signal crendentials
    async with StickersClient('YOUR_SIGNAL_USERID', 'YOUR_SIGNAL_PASSWORD') as client:
        # Upload the pack
        pack_id, pack_key = await client.upload_pack(pack)

# How to obtain your Signal credentials? In Signal Desktop, open the Developer Tools, and type
# window.reduxStore.getState().items.uuid_id to get your USER
# and  window.reduxStore.getState().items.password to get your PASSWORD.
```
- Now Let's set the flask app 
```bash
# Linux 
$ export FLASK_APP=signalStickersAPI.py
$ export FLASK_ENV=development
# Windows
> set FLASK_APP=signalStickersAPI.py
> set FLASK_ENV=development
```
- Let's Run the API

```bash
$ flask run
```
* Now send a Post Request to [localhost:port/makeSticks]()

```bash
# Post Request Body Example :  
{
    "authorName":"Fayz Sabir",
    "packName":"Fayz Pack",
    "listOfSticks":["img1.webp","img2.webp","img3.webp"], # or png with limte size of 500*500
    "cover":"img.webp" # or png with limte size of 500*500
}
# PS : the files should be in local storage 
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/FayzSa/SignalStickersMakerAPI/blob/main/LICENSE)
