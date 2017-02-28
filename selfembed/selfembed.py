import discord
from .utils import checks
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from __main__ import send_cmd_help
import os
import asyncio

class SelfEmbed:
    """SELF BOT ONLY - Change messages to embedz"""
    
    def __init__(self, bot):
        self.bot = bot
        self.cakeme = "data/selfembed/wow.json"
        self.eee = dataIO.load_json(self.cakeme)
    
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def embedtoggle(self, ctx):
        """Allows you to turn on SelfEmbed on and off for realz"""
        
        if self.eee["toggle"] is False:
            self.eee["toggle"] = True
            dataIO.save_json(self.cakeme, self.eee)
            await self.bot.say("All messages will be embed now!")
        else:
            self.eee["toggle"] = False
            dataIO.save_json(self.cakeme, self.eee)
            await self.bot.say("All messages will not be embed now!")

    async def on_message(self, message):
        author = message.author
        if self.eee["toggle"] and author.id == self.bot.owner.user.id:
            embed=discord.Embed(description=message.content, color=author.color)
            await bot.edit_message(message, new_content=" ", embed=embed)


def check_folders():
    if not os.path.exists("data/selfembed"):
        print("Creating the selfembed folder, so be patient...")
        os.makedirs("data/selfembed")
        print("Finish!")

def check_files():
    twentysix = "data/selfembed/derp.json"
    json = {
        "toggle" : False
    }

    if not dataIO.is_valid_json(twentysix):
        print("Derp Derp Derp...")
        dataIO.save_json(twentysix, json)
        print("Created derp.json!")

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(SelfEmbed(bot))
