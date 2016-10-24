import discord
from random import choice as randchoice
from discord.ext import commands

class Fuck:
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot
        self.fuck = ["Fuck you, {}. ~{}"]

    @commands.command()
    async def fuck(self, name):
        """Get fuck statements"""

        user = ctx.message.user.name
        fuck = "+ randchoice(self.fuck) +".format(name, user)
        await self.bot.say(fuck)

def setup(bot):
    bot.add_cog(Fuck(bot))
