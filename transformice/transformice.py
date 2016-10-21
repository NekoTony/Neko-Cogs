from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from __main__ import settings as bot_settings
import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import os

class Transformice:
    """Get user/tribe info from Transformice.com"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(name="tfm", pass_context=True, invoke_without_command=True)
    async def tfm(self, ctx):
        """Get Transformice Stats"""
        await send_cmd_help(ctx)
            
    @tfm.command(pass_context=True)
    async def mouse(self, ctx, *, user):
        """Get Transformice mouse info"""
        
        try:
            self.bot.send_typing(ctx.message.channel)
            link = "http://api.micetigri.fr/json/player/{}".format(user)
            async with aiohttp.get(link) as m:
            	   result = await m.json()
            	   name = result['name']
            	   mouseid = result['id']
            	   tribe = result['tribe']
            	   title = result['title']
            	   date = result['registration']
            	   exp = result ['experience']
            	   msg = "Transformice Username Info:\n"
            	   msg += "**Mouse:** {}\n".format(name)
            	   msg += "**Id:** {}\n".format(mouseid)
            	   msg += "**Tribe:** {}\n".format(tribe)
            	   msg += "**Title:** {}\n".format(title)
            	   msg += "**Join Date:** {}\n".format(date)
            	   msg += "**Experience:** {}\n".format(exp)
            	   await self.bot.say(msg)
        except ValueError:
                await self.bot.say("Please provide a valid transformice username! Try registering at transformice.com")
    
    @tfm.command(pass_context=True)
    async def tribe(self, ctx, *, tribe):
        """Get Transformice tribe info."""
        
        try:
            self.bot.send_typing(ctx.message.channel)
            link = "http://api.micetigri.fr/json/tribe/{}".format(tribe)
            async with aiohttp.get(link) as t:
            	   result = await t.json()
            	   tribe = result['name']
            	   tribeid = result['id']
            	   members = result['members']
            	   join = result['forum_recruitment']
            	   msg2 = "Transformice Tribe Info:\n"
            	   msg2 += "**Tribe:** {}\n".format(tribe)
            	   msg2 += "**Id:** {}\n".format(tribeid)
            	   msg2 += "**Members:** {}\n".format(members)
            	   msg2 += "**Openings:** {}\n".format(join)
            	   await self.bot.say(msg2)
        except ValueError:
        	await self.bot.say("The tribe doesn't exist")

def setup(bot):    
    n = Transformice(bot)
    bot.add_cog(n)