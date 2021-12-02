import discord
from discord.ext import commands

class General(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  @commands.command(help = 'Basic Command')
  async def ping (ctx):
    ctx.send("Pong!")


def setup(bot):
  bot.add_cog(General(bot))