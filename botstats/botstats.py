from .utils.dataIO import fileIO
from discord.ext import commands
from .utils import checks
import asyncio
import discord
import os

class BotStats:
    "You can display your bot stats"
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def botstats(self):
        """Display Bot Stats in status!"""
        message = await self.bot_status()
        status = list(self.bot.servers)[0].me.status
        game = discord.Game(name=message)
        await self.bot.change_presence(status=status, game=game)
        await self.bot.say('Stats has been updated')

    async def bot_status(self):
        name = self.bot.user.name
        prefix = self.bot.prefix
        servers = str(len(self.bot.servers))
        message = '{}help | {} | {}'.format(str(prefix), str(servers), str(users))
        return message

def setup(bot):
    bot.add_cog(BotStats(bot))
