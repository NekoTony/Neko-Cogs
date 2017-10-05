import discord
from .utils import checks
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils.chat_formatting import pagify
from __main__ import send_cmd_help
import os


class Customhelp:
    """Allows you to set your own server on_join message!"""

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
        self.file = "data/customhelp/settings.json"
        self.customhelp = dataIO.load_json(self.file)

    @checks.is_owner()
    @commands.group(pass_context=True)
    async def sethelp(self, ctx):
        """Custom Help allows you to create your very own help message for your own Red-DiscordBot"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def embedauthor(self, ctx):
        """Allows you to decide if you want the bot in the embed message."""

        if self.customhelp["embedAuthor"] is False:
            self.customhelp["embedAuthor"] = True
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("The author for embed have been turned on!")
        else:
            self.customhelp["embedAuthor"] = False
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("The author for embed have been turned off!")

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def embedtoggle(self, ctx):
        """Turn on or off the ability to make the help mesaged embed"""

        if self.customhelp["embedToggle"] is False:
            self.customhelp["embedToggle"] = True
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("The embed have been turned on!")
        else:
            self.customhelp["embedToggle"] = False
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("The embed have been turned off!")

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def privateset(self, ctx):
        """Turn on or off the ability to make help messages in direct message."""

        if self.customhelp["helpPrivate"] is False:
            self.customhelp["helpPrivate"] = True
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("The help message will be now sent to direct message!")
        else:
            self.customhelp["helpPrivate"] = False
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("The help message will not be set within the channel it has been said in??!")

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def setmsg(self, ctx):
        """Set the help message"""

        author = ctx.message.author
        channel = ctx.message.channel
        if "amount" not in self.customhelp:
            self.customhelp["amount"] = 5
            dataIO.save_json(self.file, self.customhelp)
        await self.add_message(author, channel)

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def settitle(self, ctx):
        """Set the help embed title"""

        author = ctx.message.author
        channel = ctx.message.channel
        await self.bot.say("Take your time and tell me, what do you want in your help embed title!")

        message = await self.bot.wait_for_message(channel=channel, author=author)

        if message is not None:
            self.customhelp["embedTitle"] = message.content
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("Congrats, the help embed title has been set to: ```{}```".format(message.content))
        else:
            await self.bot.say("There was an error.")

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def setfooter(self, ctx):
        """Set the help embed footer"""

        author = ctx.message.author
        channel = ctx.message.channel
        await self.bot.say("Take your time and tell me, what do you want in your help embed footer!")

        message = await self.bot.wait_for_message(channel=channel, author=author)

        if message is not None:
            self.customhelp["embedFooter"] = message.content
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("Congrats, the help embed footer has been set to: ```{}```".format(message.content))
        else:
            await self.bot.say("There was an error.")

    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def setcolor(self, ctx):
        """Set the help embed color"""

        author = ctx.message.author
        channel = ctx.message.channel
        await self.bot.say(
            "Take your time and tell me, what do you want in your help embed color! Make sure it's like 0xfffff or 0x000000 for assign colors or else it won't work.")

        message = await self.bot.wait_for_message(channel=channel, author=author)

        if message is not None:
            self.customhelp["embedColor"] = message.content
            dataIO.save_json(self.file, self.customhelp)
            await self.bot.say("Congrats, the help embed color has been set to: ```{}```".format(message.content))
        else:
            await self.bot.say("There was an error.")

    @commands.command(pass_context=True)
    async def help(self, ctx, *, command=None):
        if command is not None:
            ctx.command = self.bot.get_command(command)
            await send_cmd_help(ctx)
            return
        
        author = ctx.message.author

        if self.customhelp["helpPrivate"]:
            channel = author
        else:
            channel = ctx.message.channel

        msg = self.customhelp["helpMessage"]
        msg = "\n".join(msg)
        if self.customhelp["embedToggle"]:
            try:
                color = int(self.customhelp["embedColor"], 16)
            except:
                color = 0x898a8b
            for page in pagify(msg):
                title = self.customhelp["embedTitle"]
                footer = self.customhelp["embedFooter"]
                auth = self.customhelp["embedAuthor"]
                embed = discord.Embed(colour=color, title=title, description=page)
                if auth:
                    embed.set_author(name=self.bot.user.name, url=self.bot.user.avatar_url)
                embed.set_footer(text=footer)
                try:
                    await self.bot.send_message(channel, embed=embed)
                except discord.HTTPException:
                    await self.bot.say("Sorry, i need embed permissions or couldn't send message.")
        else:
            try:
                for page in pagify(msg):
                    await self.bot.send_message(channel, page)
            except discord.HTTPException:
                await self.bot.say("Couldn't send the message.")

    async def add_message(self, author, channel):
        amount = self.customhelp["amount"]
        messages = []
        for x in range(amount):
            await self.bot.say(
                "Hi, you got {} _____ to update left. What do you want to say in your {} message. Say `break` to end it".format(
                    amount - x, x))
            message = await self.bot.wait_for_message(author=author, channel=channel)

            if message.content.lower() == "break":
                break
            if message is not None:
                messages.append(message.content)
            else:
                return await self.bot.say("There was an error")

        self.customhelp["helpMessage"] = messages
        dataIO.save_json(self.file, self.customhelp)
        await self.bot.say("Saved! Here's your message")
        for x in self.customhelp["helpMessage"]:
            await self.bot.say(x)


def check_folders():
    if not os.path.exists("data/customhelp"):
        print("Creating the on_join folder, so be patient...")
        os.makedirs("data/customhelp")
        print("Finish!")


def check_files():
    twentysix = "data/customhelp/settings.json"
    json = {
        "helpMessage": ["Meep, to change help message, say `[p]sethelp setmsg`"],
        "helpPrivate": False,
        "embedColor": "0xFFFFFF",
        "embedFooter": "This is your footer!",
        "embedToggle": False,
        "embedTitle": "This is your title!",
        "embedAuthor": False,
        "amount": 5
    }

    if not dataIO.is_valid_json(twentysix):
        print("Derp Derp Derp...")
        dataIO.save_json(twentysix, json)
        print("Created settings.json!")


def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Customhelp(bot))
