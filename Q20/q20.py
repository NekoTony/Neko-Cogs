#WORK IN PRGRESS

import discord
from discord.ext import commands
import time

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
        
        time = time.time() + 60*5 
        userz = []
        await self.bot.say("Want to join? Well say `join` to particapet`")
        while True:
            picked = 10
            answer = await self.bot.wait_for_message(channel=channel)
            
            if answer.content == "join":
                #add user to list aka apend
                userz.append(answer.author.id)
                picked = picked - 1
            
            if picked >= 0 or time =< 0:
                break
            
            time = time - 1
            
        totalusers = len(userz)
        
        if totalusers > 1:
            await self.bot.say("Sorry but you need atleast 1 person to play")
            return

def setup(bot):
    bot.add_cog(Q20(bot))
