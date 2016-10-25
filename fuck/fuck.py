import discord
from discord.ext import commands
from random import choice as randchoice

class Fuck:
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot
        self.fuck = ["Fuck you, {}. ~{}", "Fucking fuck off, {}. ~{}"]

    @commands.command(pass_context=True)
    async def fuk(self, ctx, name):
        """Get fuck you statements"""
        user = ctx.message.author
        await self.bot.say("**" + randchoice(self.fuck).format(name, user) + "**")

def setup(bot):
    bot.add_cog(Fuck(bot))
