import discord
from mcstatus import MinecraftServer
from mcipc.query import Client

serverip = "Your ip"
serverport = "Your Port"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        while True:
            server = MinecraftServer.lookup(serverip)
            status = server.status()
            await client.change_presence(activity=discord.Game(name=f"on server are | {(status.players.online)} player online"))
                   
    async def on_message(self, message):
        if message.content.startswith('!ip'):
            await message.channel.send("The ip is Your Ip")

        if message.content.startswith('!state'):
            try:
                with Client((serverip), int(serverport), timeout=1.5) as client:
                    basic_stats = client.stats()
                    await message.channel.send(basic_stats.motd + ' is online! With ' + str(basic_stats.num_players) + ' out of ' + str(basic_stats.max_players) + ' players.')

            except:
                await message.channel.send('Server is offline or no player are online!')

        if message.content.startswith('!list'):
            try:
                with Client(serverip, int(serverport), timeout=1.5) as client:
                    full_stats = client.stats(full=True)
                    player_list_message = "Player Liste: \n"
                    for player_name in full_stats.players:
                        player_list_message = player_list_message + "- " + player_name + "\n"

                    await message.channel.send(player_list_message)

            except:
                await message.channel.send('Server is offline or no player are online!')
                
        if message.content.startswith('!help'):
            await message.channel.send("ip:                                        !ip")
            await message.channel.send("amount of player:          !state")
            await message.channel.send("list of player:  !list")
            
client = MyClient()
client.run("Your Token")

