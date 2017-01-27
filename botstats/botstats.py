import discord
from .utils import checks
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from __main__ import send_cmd_help
import os
import asyncio

class BotStats:
    "You can display your bot stats in your game status"
    
    def __init__(self, bot):
        self.bot = bot
        self.derp = "data/botstats/json.json"
        self.imagenius = dataIO.load_json(self.derp)

    @checks.is_owner()
    @commands.group(pass_context=True)
    async def botstats(self, ctx):
        """Made this into a group"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
    
    @checks.is_owner()
    @botstats.command(pass_context=True)
    async def toggle(self, ctx):
        """Display Bot Stats in game status that update every 10 seconds!"""
        
        servers = str(len(self.bot.servers))
        users = str(len(set(self.bot.get_all_members())))
        if self.imagenius["TOGGLE"] is False:
            self.imagenius["TOGGLE"] = True
            self.imagenius["MAINPREFIX"] = ctx.prefix
            dataIO.save_json(self.derp, self.imagenius)
            await self.bot.say("The botstats have been turned on!")
            await self.botstatz(servers, users)
        else:
            self.imagenius["TOGGLE"] = False
            await self.botstatz(servers, users)
            dataIO.save_json(self.derp, self.imagenius)
            await self.bot.say("The botstats have been turned off!")


    async def botstatz(self, servers, users):    
        while True:
            if self.imagenius["TOGGLE"] is True:
                message = '{}help | {} servers | {} users'.format(self.imagenius["MAINPREFIX"], servers, users)
                status = list(self.bot.servers)[0].me.status
                game = discord.Game(name=message)
                await self.bot.change_presence(status=status, game=game)
                await asyncio.sleep(10)
            else:
                await self.bot.change_presence(status=None, game=None)
                break
        else:
            pass
    
    async def on_ready(self):
        if self.imagenius["TOGGLE"] is True:
            servers = str(len(self.bot.servers))
            users = str(len(set(self.bot.get_all_members())))
            while True:    
                message = '{}help | {} servers | {} users'.format(self.imagenius["MAINPREFIX"], servers, users)
                status = list(self.bot.servers)[0].me.status
                game = discord.Game(name=message)
                await self.bot.change_presence(status=status, game=game)
                await asyncio.sleep(10)
            else:
                pass
        else:
            pass


def check_folders():
    if not os.path.exists("data/botstats"):
        print("Creating the botstats folder, so be patient...")
        os.makedirs("data/botstats")
        print("Finish!")


def check_files():
    twentysix = "data/botstats/json.json"
    json = {
        "MAINPREFIX" : "This can be set when starting botstats thru [p]botstats toggle",
        "TOGGLE" : False,
        "SECONDS2LIVE" : "15"
    }

    if not dataIO.is_valid_json(twentysix):
        print("Derp Derp Derp...")
        dataIO.save_json(twentysix, json)
        print("Created json.json!")


def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(BotStats(bot))
