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

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def botstats(self, ctx):
        """Display Bot Stats in status!"""
        
        await asyncio.sleep(120)
        name = self.bot.user.name
        prefix = ctx.prefix
        servers = str(len(self.bot.servers))
        users = str(len(set(self.bot.get_all_members())))
        message = '{}help | {} servers| {} users'.format(prefix, servers, users)
        status = list(self.bot.servers)[0].me.status
        game = discord.Game(name=message)
        await self.bot.change_presence(status=status, game=game)
        await self.bot.say('Bot stats is now displaying in status!!')

def setup(bot):
    bot.add_cog(BotStats(bot))
