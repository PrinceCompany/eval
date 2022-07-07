from pyrogram import Client

a = 1086018
b = '3c2f1a043c1a22d5b0af74b8268993d5'
c = '5053843367:AAHR2tDQr4sygSqbSl5v_ihB6Hat_Pl2OTQ'

app = Client(name="my_account",api_id=a,api_hash=b,bot_token=c,plugins=dict(root="plugins"))

app.run()
