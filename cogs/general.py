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

  @commands.command(help = "links to top.gg page")
  async def about(self,ctx):
    msg = discord.Embed(title="Eye of Amazoo", url = 'https://top.gg/bot/911989367524950057', description = "click on title for top.gg site")
    msg.set_image(url = 'https://top.gg/api/widget/911989367524950057.svg')
    msg.add_field(name = "prefix", value = "\'>\'")
    msg.add_field(name = "latest additions", value = "• >mean, >mode and >median commands")
    msg.add_field(name = "Cool stuff to do", value = "Check out >magsqr !!", inline = False)
    await ctx.send(embed = msg)

  

def setup(bot):
  bot.add_cog(General(bot))