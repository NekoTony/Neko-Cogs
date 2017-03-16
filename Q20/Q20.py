import discord
from discord.ext import commands
import time
from random import choice, sample 
import os
from __main__ import send_cmd_help
from .utils.dataIO import dataIO
from .utils import checks

userz = {}
class Q20:
    """Play 20 Questions"""

    def __init__(self, bot):
        self.bot = bot
        self.q = "data/q20/settings.json"
        self.q20 = dataIO.load_json(self.q)

    @commands.group(pass_context=True, invoke_without_command=True)
    async def twentyq(self, ctx):
        """20 Questions commands.."""
        
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @checks.is_owner()
    @twentyq.command(pass_context=True)
    async def settime(self, ctx, timeout):
        """Set the timeout limit. Make sure it's in seconds"""

        try:
            timeout = int(timeout)
        except:
            return await self.bot.say("Sorry, but {} needs to be a number.".format(timeout))
        
        self.q20["time"] = int(timeout)
        dataIO.save_json(self.q, self.q20)
        await self.bot.say("The timeout limit has been set to {} seconds.".format(timeout))

    @checks.is_owner()
    @twentyq.command(pass_context=True)
    async def setmaxp(self, ctx, maxp):
        """Set the timeout limit. Make sure it's in seconds"""

        try:
            maxp = int(maxp)
        except:
            return await self.bot.say("Sorry, but {} needs to be a number.".format(maxp))
        
        self.q20["picked"] = int(maxp)
        dataIO.save_json(self.q, self.q20)
        await self.bot.say("The max people who can play in a game has been set to {}.".format(maxp))

    @checks.is_owner()
    @twentyq.command(pass_context=True)
    async def setmaxq(self, ctx, maxq):
        """Set the max amount of questions a game can have."""

        try:
            maxq = int(maxq)
        except:
            return await self.bot.say("Sorry, but {} needs to be a number.".format(maxq))
        
        self.q20["maxq"] = int(maxq)
        dataIO.save_json(self.q, self.q20)
        await self.bot.say("The max amount of questions has been set to {}.".format(maxq))
    
    @checks.is_owner()
    @twentyq.command(pass_context=True)
    async def setprize(self, ctx, amount):
        """COMING SOON - Set the amount of Credits rewarded if they guess it right.."""

        try:
            amount = int(amount)
        except:
            return await self.bot.say("Sorry, but {} needs to be a number.".format(amount))
        
        self.q20["amount"] = int(amount)
        dataIO.save_json(self.q, self.q20)
        await self.bot.say("The amount of taunts rewared is set to {}.".format(amount))

    @checks.is_owner()
    @twentyq.command(pass_context=True)
    async def setmaxfg(self, ctx, maxfg):
        """Set the max amount of final guesses from people."""

        try:
            maxfg = int(maxfg)
        except:
            return await self.bot.say("Sorry, but {} needs to be a number.".format(maxfg))
        
        self.q20["maxfg"] = int(maxfg)
        dataIO.save_json(self.q, self.q20)
        await self.bot.say("The max finl guesses has been set to {}.".format(maxfg))

    @twentyq.command(pass_context=True)
    async def play(self, ctx, questions=None):
        """Play 20 questions!"""

        author = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.server
        global userz

        maxq = self.q20["maxq"]
        try:
            questions = maxq if not questions else int(questions)
        except:
            await self.bot.say("Sorry, but the number you provided must be an actual number.")
            return
        
        if questions > self.q20["maxq"]:
            return await self.bot.say("The max amount of questions is {}, sorry.".format(self.q20["maxq"]))
            return


        await self.bot.say("Want to join? Well say `join` to participate in this round! Total Questions: {}".format(questions))
        timez = self.q20["time"]
        await self.bot.wait_for_message(channel=channel, timeout=timez, check=self.check2)

        sample(userz[channel.id], len(userz[channel.id]))

        if len(userz[channel.id]) == 0:
            return await self.bot.say("You can't play by yourself.")
        await self.bot.send_message(author, "Well there bud, you got {} people joining your game. Now let me ask you, what is the answer people need to guess?".format(len(userz[channel.id])))
        answer = await self.bot.wait_for_message(author=author, timeout=self.q20["time"], check=self.check)
        if answer is None:
            await self.bot.send_message(author, "You too too long to reply")
            await self.bot.say("{}, didn't provide me with a answer.".format(author))
            del userz[channel.id]
            return
        else:
            ans = answer.content
            await self.bot.send_message(author, "Perfect! Now tell me, what is the theme for the world you provide?")

        answer2 = await self.bot.wait_for_message(author=author, timeout=self.q20["time"], check=self.check)

        if answer2 is None:
            await self.bot.send_message(author, "You too too long to reply")
            await self.bot.say("{}, didn't provide me with a theme.".format(author))
            del userz[channel.id]
            return
        else:
            theme = answer2.content
            await self.bot.send_message(author, "Ok, let's get this showboat on a row!")

        await self.bot.say("Hey Guys! Let's begin {} questions! The theme is **{}**".format(questions, theme.title()))
        quz = []
        string = "No questions Yet"
        while True:
            if questions == 0:
                await self.bot.say("Questions are done, time for final guesses!")
                break
            
            user = userz[channel.id][0]
            await self.bot.say("{}, would you like to ask a `question` or `guess`.".format(user.mention))
            saying = await self.bot.wait_for_message(author=user, timeout=self.q20["time"])
            
            if saying is None:
                await self.bot.say("You took too long to respond")
                userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
            elif saying.content.lower() == "question":
                await self.bot.say("Ok then, what's your question? Make sure it's a yes or no question only.")
                question = await self.bot.wait_for_message(author=user, timeout=self.q20["time"])
                if question is None:
                    await self.bot.say("{} took too long to answer a question, next person.")
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                    continue
                await self.bot.say("Kool! {}, you can only reply with `yes`,`no`,`sometimes`, or `idk`. So, what is it??".format(author.mention))
                tf = await self.bot.wait_for_message(author=author, timeout=self.q20["time"])
                if tf is None:
                    await self.bot.say("Sorry, but the {} took too long to reply, should we try it again?!".format(author))
                    continue
                elif tf.content.lower() in ("yes", "y"):
                    add = '{} asked the question "{}" and got the answer was "{}".'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                    questions = questions - 1
                elif tf.content.lower() in ("no", "n"):
                    add = '{} asked the question "{}" and got the answer was "{}".'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                    questions = questions - 1
                elif tf.content.lower() == "idk":
                    add = '{} asked the question "{}" and got the answer was "{}".'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                    questions = questions - 1
                elif tf.content.lower() == "sometimes":
                    add = '{} asked the question "{}" and got the answer was "{}".'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                    questions = questions - 1
            elif saying.content.lower() == "guess":
                await self.bot.say("Ok, what is your guess?")
                guess = await self.bot.wait_for_message(author=user, timeout=self.q20["time"])

                if guess is None:
                    await self.bot.say("You took too long to respond.")
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                elif guess.content.lower() == ans.lower():
                    await self.bot.say("{}, you got it right!".format(user.display_name))
                    del userz[channel.id]
                    return
                else:
                    await self.bot.say("Sorry, but that guess was incorrect.")
                    add = "{} guessed <{}>".format(user.display_name, guess.content)
                    quz.append(add)
                    userz[channel.id].append(userz[channel.id].pop(userz[channel.id].index(userz[channel.id][0])))
                    questions = questions - 1

            else:
                await self.bot.say("Sorry but you must either choosed guess or question. Your turn has been skipped.")

            string = "\n".join(quz)
            await self.bot.say("List of Questions:\n```{}```\n{} questions left!".format(string, questions))

        maxfg = self.q20["maxfg"]
        count = 0
        userz = sample(userz[channel.id], len(userz[channel.id]))
        if maxfg != 0:
            for x in userz:
                user = x
                await self.bot.say("What is your final guess, {}?".format(user.mention))
                zzz = await self.bot.wait_for_message(author=user)

                if zzz.content.lower() == ans.lower():
                    await self.bot.say("You got it right!")
                    del userz[channel.id]
                    return
                else:
                    await self.bot.say("Sorry but that was incorrect.")

                count = count + 1

                if count == maxfg:
                    await self.bot.say("Seems like no one got it! The answer was **{}**".format(ans.title()))
                    del userz[channel.id]
                    return

        await self.bot.say("Seems like no one got it! The answer was **{}**".format(ans.title()))
                
    def check2(self, msg):
        global userz
        picked = self.q20["picked"]
        user = msg.author
        channel = msg.channel
        if channel.id not in userz:
            userz[channel.id] = []
        if msg.content.lower() == "join":
            if user not in userz[channel.id]:
                userz[channel.id].append(user)
                print("{} has joined!".format(user))

        return len(userz[channel.id]) == picked
    
    def check(self, msg):
        return msg.channel.is_private
    
                
    
        
def check_folders():
    if not os.path.exists("data/q20"):
        print("Creating the Q20 folder, so be patient...")
        os.makedirs("data/q20")
        print("Finish!")

def check_files():
    twentysix = "data/q20/settings.json"
    json = {
        "maxq" : 20,
        "time" : 120,
        "amount" : 150,
        "maxfg" : 3,
        "picked" : 15,
    }

    if not dataIO.is_valid_json(twentysix):
        dataIO.save_json(twentysix, json)
        print("Created json.json!")

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Q20(bot))
