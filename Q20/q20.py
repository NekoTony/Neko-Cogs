import discord
from discord.ext import commands
import time

#Cog is a work in progress
class Q20:
    """Play 20 Questions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def play20Q(self, ctx, questions=None):
        """Play 20 questions!"""

        author = ctx.message.author
        channel = ctx.message.channel
        

        if questions is None:
            q = 20

        try:
            int(q)
        except:
            await self.bot.say("Sorry, but the number you provided must be a number.")
            return
        
        userz = []
        await self.bot.say("Want to join? Well say `join` to participate`")
        timez = time.time() + 300
        while True:
            picked = 10
            answer = await self.bot.wait_for_message(channel=channel)
            
            user = answer.author
            if answer.content == "join" and user.id != author.id:
                userz.append(user.id)
                picked = picked - 1
                await self.bot.say("{} has joined the game".format(answer.author))
            
            if  time.time() > timez:
                await self.bot.say("Times up!")
                break
            
            timez = timez - 1
            
        totalusers = len(userz)
        
        if totalusers < 1:
            await self.bot.say("Sorry but you need atleast 1 person to play")
            return
        else:
            await self.bot.say(str(userz))

def setup(bot):
    bot.add_cog(Q20(bot))
