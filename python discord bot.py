import discord
from discord import *
from discord_components import DiscordComponents
import discord.ext.commands as commands
import asyncio
from time import sleep
from mcstatus import MinecraftServer
from mcipc.query import Client


thumbnail = "Your Thumbnail"

intents = discord.Intents.default()
intents.message_content = True
server_ip_address = "Your Ip"

client = commands.Bot(command_prefix="/",case_insensitive=True,intents=intents, help_command=None)
DiscordComponents(client)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")
    while True:
        server = MinecraftServer.lookup("server_ip_address")
        status = server.status()
        await client.change_presence(activity=discord.Game(name=f"auf {(server_ip_address)} sind {(status.players.online)} Spieler online. | Ping: {(status.latency)}|"))
        await asyncio.sleep(1)
       
    


               
@client.command()
async def state(ctx):
    
    server = MinecraftServer.lookup("server_ip_address")
    status = server.status()
    
    embed3 = discord.Embed(title  = "Status", color = 0xA9D6EB)
                            
    embed3.set_thumbnail(url=thumbnail)
    
    embed3.add_field(name="Spieler online",value=str(status.players.online),inline=False)
    embed3.add_field(name="Max. Spieler",value="128 Spieler",inline=False)
    embed3.add_field(name="Ping",value=str(status.latency),inline=False)
    await ctx.channel.send(embed=embed3)
    


@client.command()
async def list(ctx):
    try:
        with Client((server_ip_address), int("25565"), timeout=1.5) as client:
            full_stats = client.stats(full=True)
            player_list_message = " "
            for player_name in full_stats.players:
                player_list_message = player_list_message + "- " + player_name + " "
                            
                embed2 = discord.Embed(title  = "Liste", color = 0xA9D6EB)
                embed2.set_thumbnail(url=thumbnail)            

                embed2.add_field(name="Spieler online",value=player_list_message,inline=False)
                await ctx.channel.send(embed=embed2)

    except:
        await ctx.channel.send('Server ist offline oder keine Spieler sind online!')


client.run("TOKEN")
