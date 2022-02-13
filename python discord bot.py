import asyncio
from discord.ext import commands
import random
import os
import discord
from mcstatus import MinecraftServer
from mcipc.query import Client

PlayerListPath = ""
plugin_path = ""
thumbnail = ""
IP = "DEINE IP"
PORT = "DEIN PORT"


client = discord.Client()


@client.event
async def on_ready():
        
        print('Bot logged on!')
            
        while True:
            server = MinecraftServer.lookup(IP)
            status = server.status()
            await client.change_presence(activity=discord.Game(name=f"{(status.players.online)} Spieler online. | Ping: {(status.latency)} |"))
            await asyncio.sleep(1)

@client.event
async def on_message(message):
    
    if str(message.channel) == "commands":  # bot commands will only get recognized when you write sth in a channel called commands

        if message.content.startswith("/help"):
            
            embed = discord.Embed(
                title  = "Hilfe",
                color = 0xA9D6EB

            )
            embed.add_field(name="Server Ip:",value="/ip",inline=False)
            embed.add_field(name="Player Online:",value="/state",inline=False)
            embed.add_field(name="Player list:",value="/list",inline=False)
            embed.add_field(name="Server Plugins:",value="/plugin",inline=False)
            embed.add_field(name="Playtime:",value="/playtime (Player Name)",inline=False)


            embed.set_thumbnail(url=thumbnail)

            await message.channel.send(embed=embed)
            await asyncio.sleep(1)


        if message.content.startswith('/ip'):
            embed4 = discord.Embed(
                    title  = "Netzwerk Information",
                    color = 0xA9D6EB
                    )
            embed4.set_thumbnail(url=thumbnail)

           

            embed4.add_field(name="Vereinfachte Domain",value=IP ,inline=False)


                
            await message.channel.send(embed=embed4)
            

        if message.content.startswith('/state'):
            try:
                with Client((IP), int(PORT), timeout=1.5) as client:
                    basic_stats = client.stats()
                    embed3 = discord.Embed(title  = "Status", color = 0xA9D6EB)
                        
                    embed3.set_thumbnail(url=thumbnail)

                    embed3.add_field(name="Player online",value=str(basic_stats.num_players),inline=False)
                    embed3.add_field(name="Max. PLayer",value=str(basic_stats.max_players),inline=False)
                    await message.channel.send(embed=embed3)

            except:
                await message.channel.send('Server is offline!')
                    
        if message.content.startswith('/list'):
            try:
                with Client((IP), int(PORT), timeout=1.5) as client:
                    full_stats = client.stats(full=True)
                    basic_stats = client.stats
                    player_list_message = " "
                    for player_name in full_stats.players:
                        player_list_message = player_list_message + "- " + player_name + " "
                        

                    embed2 = discord.Embed(
                    title  = "Liste",
                    color = 0xA9D6EB
                    )
                    embed2.set_thumbnail(url=thumbnail)            

                    embed2.add_field(name="Spieler online",value=player_list_message,inline=False)
                    await message.channel.send(embed=embed2)

            except:
                await message.channel.send('Server is offline !')


            
        if message.content.startswith('/plugin'):                               #list the plugins of the plugin path
            included_extensions = ['jar']
            file_names = [fn for fn in os.listdir(plugin_path)
                        if any(fn.endswith(ext) for ext in included_extensions)]
                
            embed1 = discord.Embed(
            title  = "Plugins",
            color = 0xA9D6EB
            )
                
            embed1.set_thumbnail(url=thumbnail)            
            count = 0 
            for i in file_names:
                total = (file_names[count])
                count += 1
                embed1.add_field(name=count,value=total,inline=False)
            await message.channel.send(embed=embed1)



        if message.content.startswith("/playerstats"):                          #gives you the playtime of player on your server.
            Spieler = message.content.replace("/playerstats ", "")              #only works when you have a minecraft server plugin for it
            f = open(PlayerListPath)
            if Spieler in (f.read()):
                with open(PlayerListPath) as f:
                    for num, line in enumerate(f, 0):
                        if Spieler in line:
                            line = num + 1 
                            Playtime = f.readlines(line)
                            line2 = num + 2
                            Playtime2 = f.readlines(line2)
                            
                        
                    Playtime = str(Playtime).replace("[", "")
                    Playtime = str(Playtime).replace("]", "")
                    Playtime = str(Playtime).replace("'", "")

                    Playtime2 = str(Playtime2).replace("[", "")
                    Playtime2 = str(Playtime2).replace("]", "")
                    Playtime2 = str(Playtime2).replace("'", "")

                    if "-" in Playtime2:
                        await message.channel.send(Playtime) 
                    
                    else:
                        await message.channel.send(Playtime)      
                        await message.channel.send(Playtime2)


            else:
                await message.channel.send(f"{Spieler} wasn't online yet!" )      
    

                    



client.run("YOUR TOKEN", bot = True)
