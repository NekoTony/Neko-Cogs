import discord
from discord.ext import commands
from .utils.dataIO import dataIO
import asyncio

class PressF:
    """You can now pay repect to a person"""

    def __init__(self, bot):
        self.bot = bot
        self.messager = {}
        self.messagem = {}

    @commands.command(pass_context=True, no_pm=True)
    async def pressf(self, ctx, user : discord.User=None):
        """Pay Respects by pressing f"""

        author = ctx.message.author
        channel = ctx.message.channel
        if channel.id in self.messager or channel.id in self.messagem:
            return await self.bot.send_message(channel, "Opps, can only pay respects if i'm not already paying respects in a channel. Wait till i'm done.")
        
        if user is None:
            await self.bot.send_message(channel, "What do you want to pay respects to?")
            message = await self.bot.wait_for_message(author=author, timeout=120, channel=channel)

            if message is None:
                return await self.bot.say("You took too long to reply.")
        
            answer = message.content
            msg = "Everyone, let's pay respects to **{}**! Press f reaction on the this message to pay respects.".format(answer)
        
        else:
            msg = "Everyone, let's pay respects to **{}**! Press f reaction on the this message to pay respects.".format(user.display_name)

        message = await self.bot.send_message(channel, msg)

        try:
            await self.bot.add_reaction(message, "\U0001f1eb")
            self.messager[channel.id] = []
            react = True
        except:
            self.messagem[channel.id] = []
            react = False

        await asyncio.sleep(120)
        await self.bot.delete_message(message)
        if react:
            amount = len(self.messager[channel.id]) - 1
        else:
            amount = len(self.messagem[channel.id]) - 1
        
        if user is None:
            await self.bot.send_message(channel, "**{}** {} payed respects to **{}**.".format(amount, "person has" if amount == "1" else "people have", answer))
        else:
            await self.bot.send_message(channel, "**{}** {} payed respects to **{}**.".format(amount, "person has" if amount == "1" else "people have", user.display_name))
        
        if react:
            del self.messager[channel.id]
        else:
            del self.messagem[channel.id]
    
    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        channel = message.channel
        if user.id == self.bot.user.id:
            return
        if channel.id not in self.messager:
            return    
        if user.id not in self.messager[channel.id]:
            if str(reaction.emoji) == "\U0001f1eb": 
                await self.bot.send_message(channel, "**{}** has paid respects.".format(user.display_name))
                self.messager[channel.id].append(user.id)

    async def on_message(self, message):
        channel = message.channel
        user = message.author
        if channel.id not in self.messagem:
            return    
        if user.id not in self.messagem[channel.id]:
            if message.content.lower() == "f":
                await self.bot.send_message(channel, "**{}** has paid respects.".format(user.display_name))
                self.messagem[channel.id].append(user.id)

def setup(bot):
    bot.add_cog(PressF(bot))
