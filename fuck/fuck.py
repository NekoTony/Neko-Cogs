import discord
from discord.ext import commands

class Fuck:
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fuck(self, name):
        """Get fuck statements"""

        await self.bot.say("Coming Soon")

def setup(bot):
    bot.add_cog(Fuck(bot))
