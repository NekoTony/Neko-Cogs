import discord
from discord.ext import commands
from .utils.dataIO import dataIO
import asyncio

messagem = {}
messager = {}
class PressF:
    """You can now pay repect to a person"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def pressf(self, ctx, user : discord.User=None):
        """Pay Respects by pressing f"""

        author = ctx.message.author
        channel = ctx.message.channel
        global messager
        global messagem
        if channel.id in messager or channel.id in messagem:
            return await self.bot.send_message(channel, "Opps, can only pay respects if i'm not already paying respects in a channel. Wait till i'm done.")
        
        if user is None:
            await self.bot.send_message(channel, "What do you want to pay respects to?")
            message = await self.bot.wait_for_message(author=author, timeout=120, channel=channel)

            if message is None:
                return await self.bot.say("You took too long to reply.")
        
            answer = message.content
            msg = "Everyone, let's pay respects to **{}**! Press f reaction on the this message to pay respects.".format(answer)
        
        else:
            msg = "Everyone, let's pay respects to **{}**! Press f reaction on the this message to pay respects.".format(user.mention)

        message = await self.bot.send_message(channel, msg)

        try:
            await self.bot.add_reaction(message, "\U0001f1eb")
            messager[channel.id] = [author.id]
            react = True
        except:
            msg = "Everyone, let's pay respects to **{}**! Type `f` to pay respects.".format(answer)
            await self.bot.edit_message(message, msg)
            messagem[channel.id] = [author.id]
            react = False

        await asyncio.sleep(120)
        await self.bot.delete_message(message)
        if react:
            amount = len(messager[channel.id]) - 1
        else:
            amount = len(messagem[channel.id]) - 1
        
        await self.bot.send_message(channel, "**{}** ppl has payed respects to **{}**".format(amount, answer))
        if react:
            del messager[channel.id]
        else:
            del messagem[channel.id]
    
    async def on_reaction_add(self, reaction, user):
        message = reaction.message
        channel = message.channel
        global messager
        if user.id == self.bot.user.id:
            return
        if channel.id not in messager:
            return    
        if user.id not in messager[channel.id]:
            if str(reaction.emoji) == "\U0001f1eb": 
                await self.bot.send_message(channel, "**{}** has payed respects.".format(user.display_name))
                messager[channel.id].append(user.id)

    async def on_message(self, message):
        channel = message.channel
        user = message.author
        global messagem
        if channel.id not in messagem:
            return    
        if user.id not in messagem[channel.id]:
            if message.content.lower() == "f":
                await self.bot.send_message(channel, "**{}** has payed respects.".format(user.display_name))
                messagem[channel.id].append(user.id)

def setup(bot):
    bot.add_cog(PressF(bot))
