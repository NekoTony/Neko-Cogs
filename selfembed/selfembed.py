import discord
from .utils import checks
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from __main__ import send_cmd_help
import os
import asyncio

class SelfEmbed:
    """Change messages to an embed for selfbots..."""
    
    def __init__(self, bot):
        self.bot = bot
        self.embed = "data/selfembed/toggle.json"
        self.toggle = dataIO.load_json(self.embed)
    
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def embedtoggle(self, ctx):
        """Allows you to turn on SelfEmbed on and off for realz"""
        
        if self.toggle["toggle"] is False:
            self.toggle["toggle"] = True
            dataIO.save_json(self.embed, self.toggle)
            await self.bot.say("All messages will be embed now!")
        else:
            self.toggle["toggle"] = False
            dataIO.save_json(self.embed, self.toggle)
            await self.bot.say("All messages will not be embed now!")

    async def on_message(self, message):
        author = message.author
        try:
            color = author.color
        except:
            color = 0x585858
        if self.toggle["toggle"] and author.id == self.bot.user.id:
            embed=discord.Embed(description=message.content, color=color)
            await self.bot.edit_message(message, new_content=" ", embed=embed)


def check_folders():
    if not os.path.exists("data/selfembed"):
        print("Creating the selfembed folder, so be patient...")
        os.makedirs("data/selfembed")
        print("Finish!")

def check_files():
    directory = "data/selfembed/toggle.json"
    json = {
        "toggle" : False
    }

    if not dataIO.is_valid_json(directory):
        dataIO.save_json(directory, json)
        print("Created toggle.json!")

def setup(bot):
    if bot.settings.self_bot:
        check_folders()
        check_files()
        bot.add_cog(SelfEmbed(bot))
    else:
        print("Sorry, but this cog is for selfbots only..")
