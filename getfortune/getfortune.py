import discord
from discord.ext import commands
import aiohttp
import json
import random
from random import randint
from random import choice


class YourFortune:
    """It's time to get your fortune!!!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def getfortune(self, ctx):
        """What is your fortune? Well then, lets find out..."""
        
        user = ctx.message.author
        page = randint(1,6)
        link = "http://fortunecookieapi.herokuapp.com/v1/fortunes?limit=&skip=&page={}".format(page)
        async with aiohttp.get(link) as m:
            result = await m.json()
            message = choice(result)
            fortune = discord.Embed(colour=user.colour)
            fortune.add_field(name="{}'s Fortune!".format(user.display_name),value="{}".format(message["message"]))
            await self.bot.say(embed=fortune)

def setup(bot):
    bot.add_cog(YourFortune(bot))
