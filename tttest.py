
import discord
import eel
eel.init('web')

x = 'ODE1MjI5NTUxNTMzNDkwMjI2.YDpXrw.rZt_YXNtGI9nQzlMCvyAWQRbr7w'
y = int(815233775683502134)
channelID = y

try:
    eel.start('index.html',size = (325,160))
    client = discord.Client()
    client.run(x)
except:

    print("Wololo!")