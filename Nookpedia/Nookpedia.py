import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
from .utils.chat_formatting import *
import aiohttp
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False

class Nookpedia:
    """Get Animal Crossing Info from Nookpedia"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="acnl", pass_context=True, invoke_without_command=True)
    async def acnl(self, ctx):
        """Get creature Stats"""
        await send_cmd_help(ctx)

    @acnl.command(pass_context=True)
    async def fish(self, ctx, *, creature):
        """Get information about a certain fish, supported by NookPedia"""

        link = "https://nookipedia.com/w/api.php?action=query&list=categorymembers&cmtitle=Category:Fish&cmlimit=500&format=json"
        async with aiohttp.get(link) as t:
            result = await t.json()
            foundCheck = False
            for list in result["query"]["categorymembers"]:
                if creature.lower() == list["title"].lower():
                    bug2 = creature.replace(" ", "_")
                    url = "https://nookipedia.com/wiki/{}".format(bug2.title())
                    async with aiohttp.get(url) as response:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        try:
                            tds = soup.find(id="Infobox-fish").find_all('td')
                            ths = soup.find(id="Infobox-fish").find_all('th')
                            img = soup.find(id="Infobox-fish").find('img').get('src')
                            td1 = tds[2]
                            th1 = ths[0]
                            td2 = tds[3]
                            th2 = ths[1]
                            th3 = ths[2]
                            td3 = tds[4]
                            th4 = ths[3]
                            td4 = tds[5]
                            th5 = ths[4]
                            td5 = tds[6]
                            th6 = ths[5]
                            td6 = tds[7]                            
                            th7 = ths[6]
                            td7 = tds[8]
                            th8 = ths[7]
                            td8 = tds[9]
                            th9 = ths[8]
                            td9 = tds[10]
                            th10 = ths[9]
                            td10 = tds[11]
                            data = discord.Embed(colour=discord.Colour.green(), title="{} - Encyclopedia".format(creature.title()))
                            data.set_thumbnail(url="https://nookipedia.com/{}".format(img))
                            data.add_field(name=th1.get_text().strip(), value=td1.get_text().strip())
                            data.add_field(name=th2.get_text().strip(), value=td2.get_text().strip())
                            data.add_field(name=th3.get_text().strip(), value=td3.get_text().strip())
                            data.add_field(name=th4.get_text().strip(), value=td4.get_text().strip())
                            data.add_field(name=th5.get_text().strip(), value=td5.get_text().strip())
                            data.add_field(name=th6.get_text().strip(), value=td6.get_text().strip())
                            data.add_field(name=th7.get_text().strip(), value=td7.get_text().strip())
                            data.add_field(name=th8.get_text().strip(), value=td8.get_text().strip())
                            data.add_field(name=th9.get_text().strip(), value=td9.get_text().strip().replace(")", ")\n"))
                            data.add_field(name=th10.get_text().strip(), value=td10.get_text().strip().replace(",", "\n"))
                            data.set_footer(text=" Learn more at: {}".format(url))
                            await self.bot.say(embed=data)
                        except:
                            await self.bot.say("Can't get the content from {}".format(url))
                    foundCheck = True
                    return
            if not foundCheck:
                await self.bot.say("Please provide a valid fish name!")
                return
            else:
                await self.bot.say("Error")

    @acnl.command(pass_context=True)
    async def deepsea(self, ctx, *, creature):
        """Get information about a certain deep sea creature, supported by NookPedia"""

        link = "https://nookipedia.com/w/api.php?action=query&list=categorymembers&cmtitle=Category:Deep_sea_creatures&cmlimit=500&format=json"
        async with aiohttp.get(link) as t:
            result = await t.json()
            foundCheck = False
            for list in result["query"]["categorymembers"]:
                if creature.lower() == list["title"].lower():
                    bug2 = creature.replace(" ", "_")
                    url = "https://nookipedia.com/wiki/{}".format(bug2.title())
                    async with aiohttp.get(url) as response:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        try:
                            tds = soup.find(id="Infobox-fish").find_all('td')
                            ths = soup.find(id="Infobox-fish").find_all('th')
                            img = soup.find(id="Infobox-fish").find('img').get('src')
                            td1 = tds[2]
                            th1 = ths[0]
                            td2 = tds[3]
                            th2 = ths[1]
                            th3 = ths[2]
                            td3 = tds[4]
                            th4 = ths[3]
                            td4 = tds[5]
                            th5 = ths[4]
                            td5 = tds[6]
                            th6 = ths[5]
                            td6 = tds[7]                            
                            th7 = ths[6]
                            td7 = tds[8]
                            th8 = ths[7]
                            td8 = tds[9]
                            th9 = ths[8]
                            td9 = tds[10]
                            th10 = ths[9]
                            td10 = tds[11]
                            data = discord.Embed(colour=discord.Colour.green(), title="{} - Encyclopedia".format(creature.title()))
                            data.set_thumbnail(url="https://nookipedia.com/{}".format(img))
                            data.add_field(name=th1.get_text().strip(), value=td1.get_text().strip())
                            data.add_field(name=th2.get_text().strip(), value=td2.get_text().strip())
                            data.add_field(name=th3.get_text().strip(), value=td3.get_text().strip())
                            data.add_field(name=th4.get_text().strip(), value=td4.get_text().strip())
                            data.add_field(name=th5.get_text().strip(), value=td5.get_text().strip())
                            data.add_field(name=th6.get_text().strip(), value=td6.get_text().strip())
                            data.add_field(name=th7.get_text().strip(), value=td7.get_text().strip())
                            data.add_field(name=th8.get_text().strip(), value=td8.get_text().strip())
                            data.add_field(name=th9.get_text().strip(), value=td9.get_text().strip())
                            data.add_field(name=th10.get_text().strip(), value=td10.get_text().strip().replace(",", "\n"))
                            data.set_footer(text=" Learn more at: {}".format(url))
                            await self.bot.say(embed=data)
                        except:
                            await self.bot.say("Can't get the content from {}".format(url))
                    foundCheck = True
                    return
            if not foundCheck:
                await self.bot.say("Please provide a valid deep sea creature name!")
                return
            else:
                await self.bot.say("Error")


    @acnl.command(pass_context=True)
    async def bug(self, ctx, *, bug):
        """Get information about a certain bug, supported by NookPedia"""

        link = "https://nookipedia.com/w/api.php?action=query&list=categorymembers&cmtitle=Category:Insect&cmlimit=500&format=json"
        async with aiohttp.get(link) as t:
            result = await t.json()
            foundCheck = False
            for list in result["query"]["categorymembers"]:
                if bug.lower() == list["title"].lower():
                    bug2 = bug.replace(" ", "_")
                    url = "https://nookipedia.com/wiki/{}".format(bug2.title())
                    async with aiohttp.get(url) as response:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        try:
                            tds = soup.find(id="Infobox-bug").find_all('td')
                            ths = soup.find(id="Infobox-bug").find_all('th')
                            img = soup.find(id="Infobox-bug").find('img').get('src')
                            td1 = tds[2]
                            th1 = ths[0]
                            td2 = tds[3]
                            th2 = ths[1]
                            th3 = ths[2]
                            td3 = tds[4]
                            th4 = ths[3]
                            td4 = tds[5]
                            th5 = ths[4]
                            td5 = tds[6]
                            th6 = ths[5]
                            td6 = tds[7]                            
                            th7 = ths[6]
                            td7 = tds[8]
                            th8 = ths[7]
                            td8 = tds[9]
                            th9 = ths[8]
                            td9 = tds[10]
                            data = discord.Embed(colour=discord.Colour.green(), title="{} - Encyclopedia".format(bug.title()))
                            data.set_thumbnail(url="https://nookipedia.com/{}".format(img))
                            data.add_field(name=th1.get_text().strip(), value=td1.get_text().strip())
                            data.add_field(name=th2.get_text().strip(), value=td2.get_text().strip())
                            data.add_field(name=th3.get_text().strip(), value=td3.get_text().strip())
                            data.add_field(name=th4.get_text().strip(), value=td4.get_text().strip())
                            data.add_field(name=th5.get_text().strip(), value=td5.get_text().strip())
                            data.add_field(name=th6.get_text().strip(), value=td6.get_text().strip())
                            data.add_field(name=th7.get_text().strip(), value=td7.get_text().strip())
                            data.add_field(name=th8.get_text().strip(), value=td8.get_text().strip())
                            data.add_field(name=th9.get_text().strip(), value=td9.get_text().strip().replace(",", "\n"))
                            data.set_footer(text=" Learn more at: {}".format(url))
                            await self.bot.say(embed=data)
                        except:
                            await self.bot.say("Can't get the content from {}".format(url))
                    foundCheck = True
                    return
            if not foundCheck:
                await self.bot.say("Please provide a valid bug name!")
                return
            else:
                await self.bot.say("Error")

    @acnl.command(pass_context=True)
    async def villager(self, ctx, *, villager):
        """Get information about a certain Villager, supported by NookPedia"""

        link = "https://nookipedia.com/w/api.php?action=query&list=categorymembers&cmtitle=Category:Villagers&cmlimit=500&format=json"
        async with aiohttp.get(link) as t:
            result = await t.json()
            foundCheck = False
            for list in result["query"]["categorymembers"]:
                if villager.lower() == list["title"].lower():
                    bug2 = villager.replace(" ", "_")
                    url = "https://nookipedia.com/wiki/{}".format(bug2.title())
                    async with aiohttp.get(url) as response:
                        soup = BeautifulSoup(await response.text(), "html.parser")
                        try:
                            tds = soup.find(id="Infobox-villager").find_all('td')
                            ths = soup.find(id="Infobox-villager").find_all('th')
                            img = soup.find(id="Infobox-villager").find('img').get('src')
                            data = discord.Embed(colour=discord.Colour.green(), title="{} - Encyclopedia".format(villager.title()))
                            data.set_thumbnail(url="https://nookipedia.com/{}".format(img))
                            if tds[1]:
                                td1 = tds[2]
                                th1 = ths[1]
                                data.add_field(name=th1.get_text().strip(), value=td1.get_text().strip())
                            elif tds[2]:
                                td2 = tds[3]
                                th2 = ths[2]
                                data.add_field(name=th2.get_text().strip(), value=td2.get_text().strip())
                            elif tds[3]:
                                th3 = ths[3]
                                td3 = tds[4]
                                data.add_field(name=th3.get_text().strip(), value=td3.get_text().strip())
                            elif tds[4]:
                                th4 = ths[4]
                                td4 = tds[5]
                                data.add_field(name=th4.get_text().strip(), value=td4.get_text().strip())
                            elif tds[5]:
                                th5 = ths[5]
                                td5 = tds[6]
                                data.add_field(name=th5.get_text().strip(), value=td5.get_text().strip())
                            elif tds[6]:
                                th6 = ths[6]
                                td6 = tds[7]
                                data.add_field(name=th6.get_text().strip(), value=td6.get_text().strip())
                            elif tds[7]:                            
                                th7 = ths[7]
                                td7 = tds[8]
                                data.add_field(name=th7.get_text().strip(), value=td7.get_text().strip().replace(")", "\n"))
                            elif tds[8]:
                                th8 = ths[8]
                                td8 = tds[9]
                                data.add_field(name=th8.get_text().strip(), value=td8.get_text().strip())
                            elif tds[8]:
                                th9 = ths[9]
                                td9 = tds[10]
                                data.add_field(name=th9.get_text().strip(), value=td9.get_text().strip().replace(",", "\n"))
                            data.set_footer(text=" Learn more at: {}".format(url))
                            await self.bot.say(embed=data)
                        except:
                            await self.bot.say("Can't get the content from {}".format(url))
                    foundCheck = True
                    return
            if not foundCheck:
                await self.bot.say("Please provide a valid Villager name!")
                return
            else:
                await self.bot.say("Error")

def setup(bot):
    if soupAvailable:
        bot.add_cog(Nookpedia(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
