import discord
from discord.ext import commands

class General(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command(help = 'Basic Command')
  async def ping (self,ctx):
    await ctx.send("Pong!")
  
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

  

def setup(bot):
  bot.add_cog(General(bot))