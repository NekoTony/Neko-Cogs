import discord
from discord.ext import commands
import time
from random import choice, sample 
import os
from .utils.dataIO import dataIO

class Q20:
    """Play 20 Questions"""

    def __init__(self, bot):
        self.bot = bot
        self.q = "data/q20/settings.json"
        self.q20 = dataIO.load_json(self.q)

    @commands.command(pass_context=True)
    async def play(self, ctx, questions=None):
        """Play 20 questions!"""

        author = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.server

        maxq = self.q20["maxq"]
        try:
            questions = maxq if not questions else int(questions)
        except:
            await self.bot.say("Sorry, but the number you provided must be an actual number.")
            return
        
        if questions > self.q20["maxq"]:
            return await self.bot.say("The max amount of questions is {}, sorry.".format(self.q20["maxq"]))
            return

        userz = []
        await self.bot.say("Want to join? Well say `join` to participate in this round! Total Questions: {}".format(questions))
        timez = self.q20["time"]
        while True:
            answer = await self.bot.wait_for_message(channel=channel)
            picked = self.q20["picked"]
            user = answer.author
            
            if answer.content.lower() == "join" and user.id != author.id:
                if user.id not in userz:
                    userz.append(user)
            
            if timez == 0:
                await self.bot.say("Times up!")
                break
            
            if len(userz) == picked:
                await self.bot.say("Max characters has joined!")
                break
            
            time.sleep(1)
            timez = timez - 1

        userz = sample(userz, len(userz))

        await self.bot.send_message(author, "Well there bud, you got {} people joining your game. Now let me ask you, what is the answer people need to guess?".format(len(userz)))
        answer = await self.bot.wait_for_message(author=author, timeout=self.q20["time"], check=self.check)

        if answer is None:
            await self.bot.send_message(author, "You too too long to reply")
            await self.bot.say("{}, didn't provide me with a answer.".format(author))
            return
        else:
            ans = answer.content
            await self.bot.send_message(author, "Perfect! Now tell me, what is the theme for the world you provide?")

        answer2 = await self.bot.wait_for_message(author=author, timeout=self.q20["time"], check=self.check)

        if answer2 is None:
            await self.bot.send_message(author, "You too too long to reply")
            await self.bot.say("{}, didn't provide me with a theme.".format(author))
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
            
            user = userz[0]
            await self.bot.say("{}, would you like to ask a `question` or `guess`.".format(user.mention))
            saying = await self.bot.wait_for_message(author=user, timeout=120)
            
            if saying is None:
                await self.bot.say("You took too long to respond")
                userz.append(userz.pop(userz.index(userz[0])))
            elif saying.content.lower() == "question":
                await self.bot.say("Ok then, what's your question?")
                question = await self.bot.wait_for_message(author=user, timeout=120)
                await self.bot.say("Kool! {}, you can only reply with `yes`,`no`,`sometimes`, or `idk`. So, what is it??".format(author.mention))
                tf = await self.bot.wait_for_message(author=author, timeout=120)
                if tf is None:
                    await self.bot.say("Sorry, but your time is up!")
                    userz.append(userz.pop(userz.index(userz[0])))
                elif tf.content.lower() in ("yes", "y"):
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz.append(userz.pop(userz.index(userz[0])))
                    questions = questions - 1
                elif tf.content.lower() in ("no", "n"):
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz.append(userz.pop(userz.index(userz[0])))
                    questions = questions - 1
                elif tf.content.lower() == "idk":
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz.append(userz.pop(userz.index(userz[0])))
                    questions = questions - 1
                elif tf.content.lower() == "sometimes":
                    add = '{} asked the question "{}" and got the answer was "{}"'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    userz.append(userz.pop(userz.index(userz[0])))
                    questions = questions - 1
            elif saying.content.lower() == "guess":
                await self.bot.say("Ok, what is your guess?")
                guess = await self.bot.wait_for_message(author=user, timeout=120)

                if guess.content.lower() == ans.lower():
                    await self.bot.say("{}, you got it right!".format(user.display_name))
                    return
                elif guess is None:
                    await self.bot.say("You took too long to respond.")
                    userz.append(userz.pop(userz.index(userz[0])))
                else:
                    await self.bot.say("Sorry, but that guess was incorrect")
                    add = "{} guessed <{}>".format(user.display_name, guess.content)
                    quz.append(add)
                    userz.append(userz.pop(userz.index(userz[0])))
                    questions = questions - 1

            else:
                await self.bot.say("Sorry but you must either choosed guess or question. Your turn has been skipped.")

            string = "\n".join(quz)
            await self.bot.say("List of Questions:\n```{}```\n{} questions left!".format(string, questions))

        maxfg = self.q20["maxfg"]
        count = 0
        userz = sample(userz, len(userz))
        if maxfg != 0:
            for x in userz:
                user = x
                await self.bot.say("What is your final guess, {}?".format(user.mention))
                zzz = await self.bot.wait_for_message(author=user)

                if zzz.content.lower() == ans.lower():
                    await self.bot.say("You got it right!")
                    return
                else:
                    await self.bot.say("Sorry but that was incorrect")

                count = count + 1

                if count == maxfg:
                    await self.bot.say("Seems like no one got it! The answer was **{}**".format(ans.title()))
                    return
    
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
        "time" : 160,
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
