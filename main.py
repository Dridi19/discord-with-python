import discord 
from discord.ext import commands
from random import randint
import youtube_dl
import os
from neuralintents import GenericAssistant
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 10
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def print_first(self):
        spaces = ' ' * self.get_level() * 10
        print(self.data)
        choice = int(input())
        if choice >= len(self.children):
            if self.parent:
                self.parent.print_first()
            else:
                return
        if self.children[choice].children:
            self.children[choice].print_first()   

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def getresponse(self):
        return self.data
    def getchildnumber(self):
        if self.children:
            return len(self.children)
        else:
            return 0

# tictac



def build_product_tree():
    root = TreeNode("Bonjour, quelle aide voulez-vous ? Pour Python taper 0, Pour javascript 1, Pour html et css 2, Pour PHP 3")
    python = TreeNode("Vous avez choisi Python: taper 0 pour les cours, taper 1 pour les documentation, taper 2 pour revenir en arrière, taper admin pour appeler un admin ou exit pour sortir")
    javascript = TreeNode("Vous avez choisi javascript : taper 0 pour les cours, taper 1 pour les documentation, taper 2 pour revenir en arrière, taper admin pour appeler un admin ou exit pour sortir")
    html_et_css = TreeNode("Vous avez choisi html et css: taper 0 pour les cours, taper 1 pour les documentation, taper 2 pour revenir en arrière, taper admin pour appeler un admin ou exit pour sortir")
    PHP = TreeNode("Vous avez choisi PHP: taper 0 pour les cours, taper 1 pour les documentation, taper 2 pour revenir en arrière,taper admin pour appeler un admin ou exit pour sortir")
#python
    python_option1 = TreeNode("Vous avez choisi cours Python: https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/, taper 0 pour revenir en arrière")
    python_option2 = TreeNode("Vous avez choisi documentation Python: docs.python.org/3/, taper 0 pour un approfondissement, taper 1 pour revenir en arrière")

    python_approfondissement = TreeNode("Vous avez choisi approfondissement Python: taper 0 pour classe, taper 1 pour variables, taper 2 pour Data Strucures, taper 3 pour revenir aux choix Python")
    python_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement classe Python:https://courspython.com/classes-et-objets.html/, tapez 0 pour revenir en arrière"))
    python_approfondissement.add_child(TreeNode("Vous avez choisi appronfondissemnt variable Python:https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/Variables, tapez 0 pour revenir en arrière "))
    python_approfondissement.add_child(TreeNode("vous avez choisi appronfidessement Data structures Python://https://docs.python.org/3/tutorial/datastructures.html, tapez 0 pour revenir en arriére "))
    python_option2.add_child((python_approfondissement))
    python.add_child((python_option2))
    python.add_child((python_option1))


####javascript 
    javascript_option1 = TreeNode("Vous avez choisi cours javascript: https://www.freecodecamp.org/news/search?query=cours%20javascript, taper 0 pour revenir en arrière")
    javascript_option2 = TreeNode("Vous avez choisi documentation javascript: https://librecours.net/module/js/js19?V=print, taper 0 pour un approfondissement, taper 1 pour revenit en arrière")
    javascript_approfondissement = TreeNode("Vous avez choisi approfondissement javascript: taper 0 pour les nombres, taper 1 pour les objets, taper 2 pour les fonctions, taper 3 pour les tableaux, taper 4 pour revenir aux choix javascript")
    javascript_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement les nombres javascript:https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Numbers_and_dates, taper 0 pour revenir en arriére "))
    javascript_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement les objets javascript:https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Working_with_Objects, taper 0 pour revenir en arriére"))
    javascript_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement des fonctions Javascript:https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Functions, tapez 0 pour revenir en arriere"))
    javascript_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement les tableaux javascript:https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Array, tapez 0 pour revenir en arriere"))
    javascript_option2.add_child((javascript_approfondissement))
    javascript.add_child((javascript_option2))
    javascript.add_child((javascript_option1))




    
    
####html & css
    html_et_css_option1 = TreeNode("Vous avez choisi cours html et css: https://www.freecodecamp.org/news/search?query=html%20cours, taper 0 pour revenir en arrière")
    html_et_css_option2 = TreeNode("Vous avez choisi documentation html et css: https://devdocs.io/html/, taper 0 pour revenir en arrière, taper 1 pour un approfondisssement")
    html_et_css_approfondissement = TreeNode("Vous avez choisi approfondissement html et css: taper 0 pour html en jQuery, taper 1 pour programation AJAX, taper 2 pour revenir aux choix html et css")
    html_et_css_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement pour html en jQuery:https://api.jquery.com/html/, taper 0 pour revenir "))
    html_et_css_approfondissement.add_child(TreeNode("Vous avez choisi l'approfondissement pour programation AJAX:https://developer.mozilla.org/fr/docs/Web/Guide/AJAX, taper 0 pour revenir"))
    html_et_css_option2.add_child((html_et_css_approfondissement))
    html_et_css.add_child((html_et_css_option2))
    html_et_css.add_child((html_et_css_option1))
#####php
    PHP_option1 = TreeNode("Vous avez choisi cours PHP: https://www.freecodecamp.org/news/search?query=cours%20PHP, taper 0 pour revenir en arrière")
    PHP_option2 = TreeNode("vous avez choisi documentation PHP: https://www.php.net/manual/fr/index.php, taper 0 pour revenir en arrière, taper 1 pour un approfondisssement")
    PHP_approfondissement = TreeNode("Vous avez choisi approfondissement PHP:  taper 0 pour MySQL, taper 1 pour variable prédefinis, taper 2 pour les objets, taper 3 pour revenir aux choix PHP")
    PHP_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement my sql php:https://www.php.net/manual/fr/book.mysql.php, taper 0 pour revenir"))
    PHP_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement variable predefini php:https://www.php.net/manual/fr/language.variables.predefined.php, taper 0 pour revenir"))
    PHP_approfondissement.add_child(TreeNode("Vous avez choisi approfondissement objet php:https://www.php.net/manual/fr/language.types.object.php, taper 0 pour revenir"))
    PHP_option2.add_child((PHP_approfondissement))
    PHP.add_child((PHP_option2))
    PHP.add_child((PHP_option1))



    root.add_child((python))
    root.add_child((javascript))
    root.add_child((html_et_css))
    root.add_child((PHP))

    return root

# bot
if __name__ == '__main__':
    aibot = GenericAssistant("intents.json")
    aibot.train_model()
    aibot.save_model()
    root = build_product_tree()
    client = commands.Bot(command_prefix="!",intents = discord.Intents.all())
    @client.command()
    async def aide(ctx):
        data = root.getresponse()
        await ctx.send("{}".format(data))

        def check(msg):
            if msg.content.isdigit():
                return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            
        msg = await client.wait_for("message", check=check)
        firtlevel= root.children[int(msg.content)]
        response = firtlevel.getresponse()
        childlevel = firtlevel.getchildnumber()
        await ctx.send(response)
        while response and msg.content != "exit":
            def check(msg):
                if msg.content == "admin":
                    return msg.author == ctx.author and msg.channel == ctx.channel and True
                if msg.content == "exit":
                    return msg.author == ctx.author and msg.channel == ctx.channel and True
                if msg.content.isdigit():
                    return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


            msg = await client.wait_for("message", check=check)
            
            if msg.content == "admin":
                user = await client.fetch_user(254227799429218306)
                await user.send("{} need help".format(msg.author))
                await ctx.send("message envoyé à l'admin")
            elif msg.content == "exit":
                await ctx.send("exit")

            elif int(msg.content)< childlevel:
                firtlevel= firtlevel.children[int(msg.content)]
                response = firtlevel.getresponse()
                childlevel = firtlevel.getchildnumber()
                await ctx.send(response)
                
            elif int(msg.content)== childlevel:
                firtlevel = firtlevel.parent
                response = firtlevel.getresponse()
                childlevel = firtlevel.getchildnumber()
                await ctx.send(response)
    @client.event
    async def on_message(message):
        if message.author ==client.user:
            return

        if message.content.startswith("bot"):
            response = aibot.request(message.content[3:])
            await message.channel.send(response)
        await client.process_commands(message)













    # music
    @client.command()
    async def play(ctx, url : str):
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music to end or use the 'stop' command")
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Général')
        await voiceChannel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))


    @client.command()
    async def leave(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")


    @client.command()
    async def pause(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Currently no audio is playing.")


    @client.command()
    async def resume(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")


    @client.command()
    async def stop(ctx):
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
#####
            
    

    client.run("OTc4MjI5MzcxNTY1MzkxOTAy.GrKLsp.DHZAD3rzaOrmh5xXFYfNWVf2dUcBG5M1gcspgA")




