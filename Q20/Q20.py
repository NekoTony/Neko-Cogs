import discord
from discord.ext import commands
import time
from random import choice

class Q20:
    """Play 20 Questions"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def play20(self, ctx, questions=None):
        """Play 20 questions!"""

        author = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.server

        try:
            q = 20 if not questions else int(questions)
        except:
            await self.bot.say("Sorry, but the number you provided must be an actual number.")
            return
        
        if q > 20:
            return await self.bot.say("The max amount of questions is 20, sorry.")
            return

        userz = []
        await self.bot.say("Want to join? Well say `join` to participate in this round! Total Questions: {}".format(q))
        timez = time.time() + 60
        while True:
            answer = await self.bot.wait_for_message(channel=channel)
            picked = 4
            user = answer.author
            if answer.content.lower() == "join" and user.id != author.id:
                if user.id not in userz:
                    userz.append(user.id)
            
            if timez <= 0 or time.time() >= timez:
                await self.bot.say("Times up!")
                break
            
            if len(userz) >= picked:
                await self.bot.say("Max characters has joined!")
                break
            
            timez = timez - 1
            
        totalusers = len(userz)
        
        if totalusers <= 0:
            await self.bot.say("Sorry but you need atleast 1 person to play.")
            return

        await self.bot.send_message(author, "Well there bud, you got {} people joining your game. Now let me ask you, what is the theme?".format(totalusers))
        answer = await self.bot.wait_for_message(author=author, timeout=120)

        if answer is None:
            await self.bot.send_message(author, "You too too long to reply")
            await self.bot.say("Didn't provide me an answer")
            return
        else:
            ans = answer.content
            await self.bot.send_message(author, "Perfect! Now tell me, what is the theme for the world you provide?")

        answer2 = await self.bot.wait_for_message(author=author, timeout=120)

        if answer2 is None:
            await self.bot.send_message(author, "You too too long to reply")
            await self.bot.say("Didn't provide me with a theme")
            return
        else:
            theme = answer2.content
            await self.bot.send_message(author, "Ok, let's get this showboat on a row!")

        await self.bot.say("Hey Guys! Let's begin {} questions! The theme is **{}**".format(q, theme.title()))
        quz = []
        while True:
            string = "None Yet"
            if q <= 0:
                await self.bot.say("Questions are done, time for final guesses!")
                break
            
            idz = choice(userz)
            user = server.get_member(idz)

            await self.bot.say("{}, would you like to ask a `question` or `guess`.".format(user.mention))
            saying = await self.bot.wait_for_message(author=user, timeout=120)
            
            if saying is None:
                await self.bot.say("You took too long to respond")
            elif saying.content.lower() == "question":
                await self.bot.say("Ok then, what's your question?")
                question = await self.bot.wait_for_message(author=user, timeout=120)
                await self.bot.say("Kool! {}, you can only reply with `yes`,`no`,`sometimes`, or `idk`. So, what is it??".format(author.mention))
                tf = await self.bot.wait_for_message(author=author, timeout=120)
                if tf is None:
                    await self.bot.say("Sorry, but your time is up!")
                elif tf.content.lower() in ("yes", "y"):
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    q = q - 1
                elif tf.content.lower() in ("no", "n"):
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    q = q - 1
                elif tf.content.lower() == "idk":
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    q = q - 1
                elif tf.content.lower() == "sometimes":
                    add = '{} asked the question "{}" and got the answer was <{}>'.format(user.display_name, question.content, tf.content)
                    quz.append(add)
                    q = q - 1
            elif saying.content.lower() == "guess":
                await self.bot.say("Ok, what is your guess?")
                guess = await self.bot.wait_for_message(author=user, timeout=120)

                if guess.content.lower() == ans.lower():
                    await self.bot.say("CONGRATS, {}!! YOU GOT IT RIGHT".format(user.display_name))
                    return
                elif guess is None:
                    await self.bot.say("You took too long to respond.")
                else:
                    await self.bot.say("Sorry, but that guess was incorrect")
                    add = "{} guessed <{}>".format(user.display_name, guess.content)
                    quz.append(add)
                    q = q - 1

            else:
                await self.bot.say("Sorry but you must either choosed guess or question. Your turn has been skipped.")

            string = "\n".join(quz)
            await self.bot.say("List of Questions:\n```{}```\n{} questions left!".format(string, q))

        quz = []
        for x in userz:
            user = server.get_member(x)
            await self.bot.say("What is your final guess, {}?".format(user.display_name))
            zzz = await self.bot.wait_for_message(author=user)

            if zzz.content.lower() == ans.lower():
                await self.bot.say("You got it right!")
                return
            else:
                await self.bot.say("Sorry but that was incorrect")

        await self.bot.say("Seems like no one got it! The answer was **{}**".format(ans.title()))




def setup(bot):
    bot.add_cog(Q20(bot))
