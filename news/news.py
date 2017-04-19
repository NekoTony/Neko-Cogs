import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils import checks
from __main__ import send_cmd_help
import os
import asyncio

class Newsletter:
    """Allow users to sign up for a newsletter from the owner"""

    def __init__(self, bot):
        self.bot = bot
        self.new = "data/news/registered.json"
        self.news = dataIO.load_json(self.new)
        

    @commands.group(pass_context=True, invoke_without_command=True)
    async def newsletter(self, ctx):
        """Newsletter Commands"""
        
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
    

    @newsletter.command(pass_context=True)
    async def signup(self, ctx):
        """Signup for our Newsletter"""
        
        weeb = ctx.message.author
        if weeb.id not in self.news:
            await self.bot.say("Ok, let me set up your acconut for our newsletter!!")
            self.news[weeb.id] = {'send' : True}
            dataIO.save_json(self.new, self.news)
            await self.bot.say("Congrats, you will now recieve our newsletter! You can turn it off by saying `{}newsletter toggle`".format(ctx.prefix))
        else:
            await self.bot.say("Sorry, you already have registered for a newsletter acconut?")
 
    @newsletter.command(pass_context=True)
    async def toggle(self, ctx):
        """Allows you to turn on and off the Newsletter whenever you feel like it!"""
        
        weeb = ctx.message.author
        if weeb.id in self.news:
            news = self.news[weeb.id]['send']
            if news is False:
                self.news[weeb.id]['send'] = True 
                dataIO.save_json(self.new, self.news)
                await self.bot.say("Congrats, you will now start recieving newsletter thru pm!")
            else:
                self.news[weeb.id]['send'] = False 
                dataIO.save_json(self.new, self.news)
                await self.bot.say("Congrats, you will now stop recieving newsletter thru pm!")
        else:
            await self.bot.say("{}, uou need a newsletter acconut to start receiving the latest info. Say `{}newsletter signup` now!".format(weeb.mention, ctx.prefix))

    @checks.is_owner()
    @newsletter.command(pass_context=True)
    async def send(self, ctx, *, msg):
        """Owner only, sends announcement for people who !!!!"""

        if len(self.news) <= 0:
            await self.bot.say("You can't send a newsletter if no one is registered.")
            return
        
        for id in self.news:
            if self.news[id]['send']: 
                user = self.bot.get_user_info(id)
                message = "**{} Newsletter!\n\n**".format(self.bot.user.name)
                message += msg
                message += "\n\n*You can always disable newsletter by saying `{}newsletter toggle!`*".format(ctx.prefix)
                users = discord.utils.get(self.bot.get_all_members(),
                                  id=id)
                try:
                    await self.bot.send_message(users, message)
                    
                except:
                    await self.bot.say("The message didn't go thru you `Fox News has edited this word out due to censorship, we apologize` owner! :angry:")
                
                asyncio.sleep(1)
            else:
                pass
        else:
            await self.bot.say("Newsletter has all been sent out to everyone who wanted it!")

def check_folders():
    if not os.path.exists("data/news"):
        print("Creating the news folder, so be patient...")
        os.makedirs("data/news")
        print("Finish!")

def check_files():
    twentysix = "data/news/registered.json"
    json = {}
    if not dataIO.is_valid_json(twentysix):
        print("Derp Derp Derp...")
        dataIO.save_json(twentysix, json)

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Newsletter(bot))
