import discord
from discord.ext import commands

import math

class Solvers(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  #n choose k
  @commands.command(help = ":For solving combinatrics(combinations) problems(n choose k). Remember to follow convention nCk")
  async def choose(self, ctx, n:float, ki:float):
    if round(n)-n!=0 or round(ki)-ki != 0 or n < 0 or ki < 0 or ki > n:
      ans = "You can't choose "+ str(ki) + " from"+ str(n)
    else:
      res = 1
      try:
        k = ki
        if k > (n-k):
          k = n-k
        for i in range (int(k)):
          res = res * (n-i)
        res = res/math.factorial(k)
        ans = "There are `"+str(int(res))+"` ways to choose "+str(int(ki))+" objects from "+str(int(n))    
      except:
        ans = "The answer is MIND-BOGGLINGLY big."

    await ctx.send(ans)

  #n perm k
  @commands.command(help = ":For solving combinatrics (permutation) problems(n perm k). Remember to follow convention: nPk")
  async def perm(self, ctx, n:float, k:float):
    if round(n)-n !=0 or round(k)-k != 0 or n < 0 or k < 0 or k > n:
      ans = "You cant choose "+str(k)+" from "+ str(n) + " let alone arrange/permute them"
    else:
      res = 1
      try:
        for i in range (int(k)):
          res = res * (n-i)
        ans = "There are "+str(int(res))+" ways to arrange/permute "+str(int(k))+" objects from "+str(int(n))
      except:
        ans = "The answer is MIND-BOGGLINGLY big."

    await ctx.send(ans)

def setup(bot):
  bot.add_cog(Solvers(bot))