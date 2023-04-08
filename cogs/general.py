import discord
from discord.ext import commands

import random

class General(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command(help = 'Basic Command')
  async def ping (self,ctx):
    await ctx.send("Pong!")

  @commands.command(help = "Let Amazoo suggest a discussion topic as a conversation starter! (You can suggest topics by DMing Sidd_Bourbaki)")
  @commands.cooldown(1,300,commands.BucketType.guild)
  async def discuss(self,ctx):

    viable_topics = [
      ["The Paradox of Free Will: Are we free to do anything we want (:salad:) or we are doing what has been decided for us (:pizza:)?"],
      ["Is mathematics invented (:salad:) or discovered(:pizza:)?"],
      ["What would you do if you build a death ray?"],
      ["What is your favourite mathematical paradox?"],
      ["What is the coolest mathematical fact/theorem that you know off the top of your head?"],
      ["Is AI a threat to humans? Yes(:pizza:) or No(:salad:)"],
      ["What is your favourite myth or any myth you remember..."],
      ["What's your current favorite Maths YouTube video?"],
      ["Do you think technology will pave the way for human to self-destruction (:pizza:), or to advancement(:salad:), or both?"],
      ["ETHICAL DILEMMA: How would you react to the trolley problem? Pull the lever (:salad:) or not (:pizza:)?","https://ed.ted.com/lessons/would-you-sacrifice-one-person-to-save-five-eleanor-nelsen"],
      ["What was the best invention, according to you, of the last 50 years?"],
      ["According to you, what was the best invention of the last 200 years?"],
      ["According to you, what was the best invention of them all?"],
      ["What is the weirdest science concept you have come across"],
      ["Agree (:salad:) or Disagree (:pizza:): Science and Religion can complement each other."],
      ["Do you think Alien Life forms exist? \nYes - :salad:\nNo - :pizza:"],
      ["What are your views on Mary’s Room Experiment? Does she learn something new (:salad:) or not (:pizza:)?","https://ed.ted.com/lessons/mary-s-room-a-philosophical-thought-experiment-eleanor-nelsen"],
      ["Is Fear of Death basically the Fear of Missing Out (FOMO)? \nYes - :salad:\n No - :pizza:"],
      ["Would you like to be immortal?\nYes - :salad:\nno - :pizza: "],
      ["Do you think 'The Anthropic Principle' is significant? \nYes - :salad:\n No - :pizza:"],
      ["Share an lesser-known STEM fact!"],
      ["What is your favourite puzzle game (video or analogue)?"],
      ["What is your all-time favourite Sci-Fi movie (or movie series)"],
      ["What is your all-time favourite Sci-Fi book (or book series)"],
      ["How do you know you are not dreaming?"]
    ]

    topic = random.choice(viable_topics)
    msg = discord.Embed(title = topic[0])
    msg.set_footer(text=f'requested by: {ctx.author.display_name}')
    em = await ctx.send(embed=msg)
    if ":salad:" in topic[0]:
      await em.add_reaction('🥗')
      await em.add_reaction('🍕')
    try:
      await ctx.send(topic[1])
    except:
      return

  @commands.command(help = "Make a suggestion for discussion topics")
  async def addtopic (self,ctx,*,Topic:str):
    TopicBox = open("Topics.txt")
    TopicList = TopicBox.readlines()
    TopicList.append(Topic.replace('\n', '\ n') + f'__BY__  {str(ctx.author)} (server - {str(ctx.guild)})\n')

    TopicStr = "".join(TopicList)

    DroppingTopic = open("Topics.txt", "w")
    DroppingTopic.write(TopicStr)
    DroppingTopic.close()
    await ctx.send(f'{str(ctx.author.mention)}\'s suggested \n`{Topic}`\nas a discussion topic! \nThank you')    

  @commands.command(help = "Make a suggestion for the bot! Please be brief.")
  async def suggest (self,ctx,*,suggestion:str):
    SuggestionBox = open("Suggestions.txt")
    SuggestionList = SuggestionBox.readlines()
    SuggestionList.append(suggestion.replace('\n', '\ n') + f'__BY__  {str(ctx.author)} (server - {str(ctx.guild)})\n')

    SuggestionStr = "".join(SuggestionList)

    DroppingSuggestion = open("Suggestions.txt", "w")
    DroppingSuggestion.write(SuggestionStr)
    DroppingSuggestion.close()
    await ctx.send(f'{str(ctx.author)}\'s suggestion: \n{suggestion}\n has been recorded. \nThank you')

  @commands.command(help = "Try typing it in.")
  async def about(self,ctx):
    msg = discord.Embed(title="Eye of Amazoo", description = "STEM - oriented bot. Type in '>help' for more information.")
    msg.set_author(name = "click here for top.gg page",url = 'https://top.gg/bot/911989367524950057')
    msg.set_image(url = 'https://top.gg/api/widget/911989367524950057.svg')
    msg.set_thumbnail(url = 'https://images.discordapp.net/avatars/911989367524950057/70120c09cd5c095725f498000052d7d0.png?size=512')
    msg.add_field(name = "Prefix", value = "\'>\'")
    msg.add_field(name = "Latest Additions", value = "• >mean, >mode and >median commands")
    msg.add_field(name = "Cool stuff to do", value = "Check out >magsqr !!", inline = False)
    msg.set_footer(text=f'requested by: {ctx.author.display_name}')
    await ctx.send(embed = msg)

  @commands.command(help = "embed msg and return it to make it stand out")
  async def em(self, ctx,*, msg: str):
    author = "by " + str(ctx.author.display_name)
    msg = discord.Embed(title = msg, description = author)
    await ctx.send(embed = msg)  

def setup(bot):
  bot.add_cog(General(bot))