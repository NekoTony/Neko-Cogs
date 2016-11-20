import discord
from discord.ext import commands
from cogs.utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
from .utils.chat_formatting import *

class Account:
    """The About Me Cog"""

    def __init__(self, bot):
        self.bot = bot
        self.profile = 'data/account/accounts.json'
    
    @commands.command(name="signup", pass_context=True, invoke_without_command=True, no_pm=True)
    async def _reg(self, ctx):
        """Sign up to get your own account today!"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        
        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            connect[server.id][user.id] = {}
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:", value="You have officaly created your acconut for **{}**, {}.".format(server, user.mention))
            await self.bot.say(embed=data)
        else: 
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Opps, it seems like you already have an account, {}.".format(user.mention))
            await self.bot.say(embed=data)
        
    
    @commands.command(name="account", pass_context=True, invoke_without_command=True, no_pm=True)
    async def _acc(self, ctx, user : discord.Member=None):
        """Your/Others Account"""
                    
        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        
        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if not user:
            user = ctx.message.author
            if user.id in connect[server.id]:
                data = discord.Embed(description="{}".format(server), colour=user.colour)
                if "Age" in connect[server.id][user.id]:
                    age = connect[server.id][user.id]["Age"]
                    data.add_field(name="Age:", value=age)
                else:
                    pass
                if "Site" in connect[server.id][user.id]:
                    site = connect[server.id][user.id]["Site"]
                    data.add_field(name="Website:", value=site)
                else:
                    pass
                if "About" in connect[server.id][user.id]:
                    about = connect[server.id][user.id]["About"]
                    data.add_field(name="About:", value=about)
                else:
                    pass
                if "Gender" in connect[server.id][user.id]:
                    gender = connect[server.id][user.id]["Gender"]
                    data.add_field(name="Gender:", value=gender)
                else:
                    pass 
                if "Job" in connect[server.id][user.id]:
                    job = connect[server.id][user.id]["Job"]
                    data.add_field(name="Profession:", value=job)
                else:
                    pass
                if "Email" in connect[server.id][user.id]:
                    email = connect[server.id][user.id]["Email"]
                    data.add_field(name="Email Address:", value=email)
                else:
                    pass
                if "Other" in connect[server.id][user.id]:
                    other = connect[server.id][user.id]["Other"]
                    data.add_field(name="Other:", value=other)
                else:
                    pass
                if user.avatar_url:
                    name = str(user)
                    name = " ~ ".join((name, user.nick)) if user.nick else name
                    data.set_author(name=name, url=user.avatar_url)
                    data.set_thumbnail(url=user.avatar_url)
                else:
                    data.set_author(name=user.name)

                await self.bot.say(embed=data)
            else:
                prefix = ctx.prefix
                data = discord.Embed(colour=user.colour)
                data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
                await self.bot.say(embed=data)
        else:
            connect = fileIO(self.profile, "load")
            server = ctx.message.server
            if user.id in connect[server.id]:
                data = discord.Embed(description="{}".format(server), colour=user.colour)
                if "Age" in connect[server.id][user.id]:
                    town = connect[server.id][user.id]["Age"]
                    data.add_field(name="Age", value=town)
                else:
                    pass
                if "Site" in connect[server.id][user.id]:
                    site = connect[server.id][user.id]["Site"]
                    data.add_field(name="Website:", value=site)
                else:
                    pass
                if "About" in connect[server.id][user.id]:
                    about = connect[server.id][user.id]["About"]
                    data.add_field(name="About:", value=about)
                else:
                    pass
                if "Gender" in connect[server.id][user.id]:
                    gender = connect[server.id][user.id]["Gender"]
                    data.add_field(name="Gender:", value=gender)
                else:
                    pass 
                if "Job" in connect[server.id][user.id]:
                    job = connect[server.id][user.id]["Job"]
                    data.add_field(name="Profession:", value=job)
                else:
                    pass
                if "Email" in connect[server.id][user.id]:
                    email = connect[server.id][user.id]["Email"]
                    data.add_field(name="Email Address:", value=email)
                else:
                    pass
                if "Other" in connect[server.id][user.id]:
                    other = connect[server.id][user.id]["Other"]
                    data.add_field(name="Other:", value=other)
                else:
                    pass
                if user.avatar_url:
                    name = str(user)
                    name = " ~ ".join((name, user.nick)) if user.nick else name
                    data.set_author(name=name, url=user.avatar_url)
                    data.set_thumbnail(url=user.avatar_url)
                else:
                    data.set_author(name=user.name)

                await self.bot.say(embed=data)
            else:
                data = discord.Embed(colour=user.colour)
                data.add_field(name="Error:warning:",value="{} doesn't have an account at the moment, sorry.".format(user.mention))
                await self.bot.say(embed=data)

    @commands.group(name="update", pass_context=True, invoke_without_command=True, no_pm=True)
    async def update(self, ctx):
        """Update your TPC"""
        await send_cmd_help(ctx)

    @update.command(pass_context=True, no_pm=True)
    async def about(self, ctx, *, about):
        """Tell us about yourself"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass
        
        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"About" : about})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have updated your About Me to{}".format(about))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def website(self, ctx, *, site):
        """Do you have a website?"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix
        
        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"Site" : site})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Website to {}".format(site))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def age(self, ctx, *, age):
        """How old are you?"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"Age" : age})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your age to {}".format(age))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def job(self, ctx, *, job):
        """Do you have a job?"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"Job" : job})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Job to {}".format(job))
            await self.bot.say(embed=data)
    
    @update.command(pass_context=True, no_pm=True)
    async def gender(self, ctx, *, gender):
        """What's your gender?"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix
                
        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"Gender" : gender})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Gender to {}".format(gender))
            await self.bot.say(embed=data)
 
    @update.command(pass_context=True, no_pm=True)
    async def email(self, ctx, *, email):
        """What's your email address?"""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"email" : email})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Email to {}".format(email))
            await self.bot.say(embed=data)

    @update.command(pass_context=True, no_pm=True)
    async def other(self, ctx, *, other):
        """Incase you want to add anything else..."""

        connect = fileIO(self.profile, "load")
        server = ctx.message.server
        user = ctx.message.author
        prefix = ctx.prefix

        if server.id not in connect:
            connect[server.id] = {}
        else:
            pass

        if user.id not in connect[server.id]:
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Error:warning:",value="Sadly, this feature is only available for people who had registered for an account. \n\nYou can register for a account today for free. All you have to do is say `{}signup` and you'll be all set.".format(prefix))
            await self.bot.say(embed=data)
        else:
            connect[server.id][user.id].update({"Other" : other})
            fileIO("data/account/accounts.json","save",connect)
            data = discord.Embed(colour=user.colour)
            data.add_field(name="Congrats!:sparkles:",value="You have set your Other to {}".format(other))
            await self.bot.say(embed=data)

def check_folder():
    if not os.path.exists("data/account"):
        print("Creating data/account folder...")
        os.makedirs("data/account")

def check_file():
    data = {}
    f = "data/account/accounts.json"
    if not fileIO(f, "check"):
        print("Creating default account's account.json...")
        fileIO(f, "save", data)

def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(Account(bot))
