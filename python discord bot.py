import json
import discord
from discord import *
from discord_components import DiscordComponents
import discord.ext.commands as commands
import asyncio
import os
from mcstatus import MinecraftServer
from mcipc.query import Client

punkte_file = 
playtime_file = "
plugin_path = 
test = 12345678  # discord channel id

thumbnail = ""

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


client = commands.Bot(command_prefix="/", help_command=None)
DiscordComponents(client)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command nicht vorhanden!")

@client.event
async def on_member_join(member):
    guild = client.get_guild()
    role = discord.utils.get(guild.roles, name="Verifiziert")
    await client.add_roles(member, role)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")
    
    with open(PFAD "r") as f:
        await asyncio.sleep(1)
        data = json.load(f)
        channel = client.get_channel(938885783811674213)   # discord channel id
        y = data
        
        y = str(y).replace("[", "")
        y = str(y).replace("'", "")
        y = str(y).replace("{", "")
        y = str(y).replace("}", "")
            
            
        message = await channel.send(y)
        await asyncio.sleep(1)
    
    while True:
        server = MinecraftServer.lookup("hoshire.de")
        status = server.status()
        await client.change_presence(activity=discord.Game(name=f"auf dem Server | {(status.players.online)} Spieler online. | Ping: {(status.latency)} |"))
        
        with open("C:/Users/eks20/Music/Python/discord bot/Punkte/Punkte.json", "r") as f:
            await asyncio.sleep(1)
            data = json.load(f)

        y = data
                
        y = str(y).replace("[", "")
        y = str(y).replace("'", "")
        y = str(y).replace("{", "")
        y = str(y).replace("}", "")
            
        await message.edit(content=y)


@client.command()
async def help(ctx):
                
    embed = discord.Embed(
        title  = "Hilfe",
        color = 0xA9D6EB
        )
    embed.add_field(name="Server Ip:",value="/ip",inline=False)
    embed.add_field(name="Player Online:",value="/state",inline=False)
    embed.add_field(name="Player list:",value="/list",inline=False)
    embed.add_field(name="Server Email:",value="/email",inline=False)
    embed.add_field(name="Support Email:",value="/support",inline=False)
    embed.add_field(name="Server Plugins:",value="/plugin",inline=False)
    embed.add_field(name="Music:",value="/play (youtube link), /stop, /pause, /resume, /leave",inline=False)
    embed.add_field(name="GuessGame:",value="/guessgame /choose (Zahl)",inline=False)
    embed.add_field(name="Punkte:",value="/punkte (Discord Name)",inline=False)
    

    embed.set_thumbnail(url=thumbnail)

    await ctx.channel.send(embed=embed)


@client.command()
async def ip(ctx):
    embed4 = discord.Embed(
            title  = "Netzwerk Information",
            color = 0xA9D6EB
            )
    embed4.set_thumbnail(url=thumbnail)

    embed4.add_field(name="Server Adresse",value="________",inline=False)

    await ctx.channel.send(embed=embed4)
                

@client.command()
async def state(ctx):
    try:
        with Client(("hoshire.de"), int("25565"), timeout=1.5) as client:
            basic_stats = client.stats()
            embed3 = discord.Embed(title  = "Status", color = 0xA9D6EB)
                            
            embed3.set_thumbnail(url=thumbnail)

            embed3.add_field(name="Spieler online",value=str(basic_stats.num_players),inline=False)
            embed3.add_field(name="Max. Spieler",value=str(basic_stats.max_players),inline=False)
            await ctx.channel.send(embed=embed3)

    except:
        await ctx.channel.send('Server ist offline oder keine Spieler sind online!')


@client.command()
async def list(ctx):
    try:
        with Client(("hoshire.de"), int("25565"), timeout=1.5) as client:
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


@client.command()
async def plugin(ctx):
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

    await ctx.channel.send(embed=embed1) 
  

client.run(YOUR TOKEN)
