import discord
from discord import *
from discord_components import DiscordComponents
import discord.ext.commands as commands
import random
import os
import youtube_dl
from time import sleep
from gtts import gTTS
punkte_file = "/Punkte.json"

thumbnail = "YOUR THUMBNAIL"

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

intents = discord.Intents.default()
intents.message_content = True

server_ip_address = "Your IP"

client = commands.Bot(command_prefix="/",case_insensitive=True,intents=intents)
DiscordComponents(client)


@client.command()
@commands.cooldown(1, 60*60*6, commands.BucketType.user)
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                ":white_large_square:", ":white_large_square:", ":white_large_square:",
                ":white_large_square:", ":white_large_square:", ":white_large_square:"]

        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2

        num = random.randint(1, 2)
        starter = ""
        if num == 1:
            turn = player1
            starter = (str(player1.mention) + " beginnt.")
        elif num == 2:
            turn = player2
            starter = (str(player2.mention) + " beginnt.")
            
        embed7 = discord.Embed(
                    title  = "Tic Tac Toe",
                    color = 0xA9D6EB
                    )
        embed7.set_thumbnail(url=thumbnail)

        embed7.add_field(name=board[0],value= "1",inline=True)
        embed7.add_field(name=board[1],value= "2",inline=True)
        embed7.add_field(name=board[2],value= "3",inline=True)
        embed7.add_field(name=board[3],value= "4",inline=True)
        embed7.add_field(name=board[4],value= "5",inline=True)
        embed7.add_field(name=board[5],value= "6",inline=True)
        embed7.add_field(name=board[6],value= "7",inline=True)
        embed7.add_field(name=board[7],value= "8",inline=True)
        embed7.add_field(name=board[8],value= "9",inline=True)
                     
        await ctx.channel.send(embed=embed7)
        await ctx.send(starter + " Zum spielen schreibe /place und dann eine zahl zwischen 1 und 9")
        starter = ""

    else:
        await ctx.send("Das Spiel läuft noch.")


@client.command()
async def place(ctx, pos: int):
    global turn
    global punkte_file
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
                    
            elif turn == player2:
                mark = ":o2:"
                    
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                embed8 = discord.Embed(
                    title  = "Tic Tac Toe",
                    color = 0xA9D6EB
                    )
                embed8.set_thumbnail(url=thumbnail)

                embed8.add_field(name=board[0],value= "1",inline=True)
                embed8.add_field(name=board[1],value= "2",inline=True)
                embed8.add_field(name=board[2],value= "3",inline=True)
                embed8.add_field(name=board[3],value= "4",inline=True)
                embed8.add_field(name=board[4],value= "5",inline=True)
                embed8.add_field(name=board[5],value= "6",inline=True)
                embed8.add_field(name=board[6],value= "7",inline=True)
                embed8.add_field(name=board[7],value= "8",inline=True)
                embed8.add_field(name=board[8],value= "9",inline=True)

                await ctx.channel.send(embed=embed8)

                checkWinner(winningConditions, mark)
                if gameOver == True:
                    await ctx.send(f"{turn} ({mark}) gwinnt!")
                                      
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Unentschieden!")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1

            else:
                await ctx.send("Du kannst nicht auf dieses Feld schreiben")     
            
        else:
            await ctx.send("Du bist nicht dran.")
    else:
        await ctx.send("Please start a new game using the /tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du brauchst 2 Spieler.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Du musst eine Zahl angeben.")

@client.command()
@commands.cooldown(1, 60*60*12, commands.BucketType.user)
async def guessgame(ctx): 
    global choice
    global z1
    global z2
    global r

    range =[10,20,30,40,50,60,70,80,90,100]
    z1 = random.choice(range)
    z2 = random.choice(range)
    
    if z1 > z2:
        await ctx.send(f"Sage eine Zahl zwischen {z2} und {z1}. Schreibe /choose ...")
        r = "2-1"
        choice = random.randint(z2, z1)
    elif z1 < z2:
        await ctx.send(f"Sage eine Zahl zwischen {z1} und {z2}. Schreibe /choose ...")
        r = "1-2"
        choice = random.randint(z1, z2)
    else:
        pass

    print(choice)


@client.command()
async def choose(ctx, arg): 
    arg = int(arg)
    global choice
    global punkte_file
    

   
    if arg < choice or arg > choice:
        if r == "2-1":
            if arg < z2 or arg > z1:
                await ctx.send(f"Die Zahl muss zwischen {z2} und {z1}. Schreibe nochmal /choose ...")

    if r == "1-2": 
        if arg < z1 or arg > z2:
            await ctx.send(f"Die Zahl muss zwischen {z1} und {z2}. Schreibe nochmal /choose ...")

    if arg < choice or arg > choice:
        choice = str(choice)
        await ctx.send("Falsch die Zahl war " + choice)

    if arg == choice:
        await ctx.send("Richtig !!! +1 Punkt")
    choice = " "
    
    
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Warte bis das Lied vorbei ist oder schreibe /stop")
        return

    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send("Der Download beginnt ...")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    except:
        voice.stop()

@client.command()
async def play2(ctx):
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send("Der Download beginnt ...")
    
    
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
   
        
@client.command()
async def quit(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Der Bot ist nicht mit einem Voice Channel verbunden.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Es spielt gerade keine Musik.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Das Lied ist nicht pausiert.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command()
async def test(ctx, *args):
    text = " ".join(args)
    user = ctx.message.author
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        
    sound = gTTS(text=text, lang="de",slow=False)
    sound.save("ttsAudio.mp3")
    
    voice.play(discord.FFmpegPCMAudio("ttsAudio.mp3"))
    
@client.command(pass_context=True)
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def dailybonus(ctx):
    
    turn =  str(ctx.author)
    with open(punkte_file, "r") as f:
        data = json.load(f)

        if turn in data:
          # data[turn]["Punkte"] += 1

        if not turn in data:
            data[turn] = {}
            data[turn]["Punkte"] = 1
                    
    print(data[turn])
    with open(punkte_file, "w") as f:
        json.dump(data, f)

@client.command()
async def mathgame(ctx):
    await ctx.send("Du hast für diese Rechenaufgabe 5 Sekunden Zeit. Schreibe /ans und deine Lösung.")
    sleep(5)    
    
    faktor1 = random.randint(1,100)
    faktor2 =random.radnint(1,100)
    time = 5 

    
@client.command()
async def mathgame(ctx):
    await ctx.send("Du hast für diese Rechenaufgabe 5 Sekunden Zeit. Schreibe /ans und deine Lösung.")
    sleep(5)    
    
    faktor1 = random.randint(1,100)
    faktor2 =random.radnint(1,100)      

client.run("TOKEN")
