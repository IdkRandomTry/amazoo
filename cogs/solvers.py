import discord
from discord.ext import commands

import math
import cmath
import statistics as stat

class Solvers(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  #n choose k
  @commands.hybrid_command(help = "For solving combinatrics(combinations) problems(n choose k). Remember to follow convention nCk")
  async def choose(self, ctx, n:float, k:float):
    ki = k
    if round(n)-n!=0 or round(ki)-ki != 0 or n < 0 or ki < 0 or ki > n:
      ans = f'You can\'t choose {str(ki)} from {str(n)}'
    else:
      res = 1
      try:
        k = ki
        if k > (n-k):
          k = n-k
        for i in range (int(k)):
          res = res * (n-i)
        res = res/math.factorial(k)
        ans = f'There are `{str(int(res))}` ways to choose {str(int(ki))} objects from {str(int(n))}'    
      except:
        ans = "The answer is MIND-BOGGLINGLY big."

    await ctx.send(ans)

  #n perm k
  @commands.hybrid_command(help = "For solving combinatrics (permutation) problems(n perm k). Remember to follow convention: nPk")
  async def perm(self, ctx, n:float, k:float):
    if round(n)-n !=0 or round(k)-k != 0 or n < 0 or k < 0 or k > n:
      ans = f'You cant choose {str(k)} from {str(n)} let alone arrange/permute them'
    else:
      res = 1
      try:
        for i in range (int(k)):
          res = res * (n-i)
        ans = f'There are `{str(int(res))}` ways to arrange/permute {str(int(k))} objects from {str(int(n))}'
      except:
        ans = "The answer is MIND-BOGGLINGLY big."

    await ctx.send(ans)

  #qudratic equation solver
  @commands.hybrid_command(help = "Solving Quadratic equations. (Don't forget to follow general form: ax²+ bx + c = 0)")
  async def quad(self, ctx, a: float, b:float, c:float):
    msg = discord.Embed(title = "Amazoo's Quadratic Equation Solver...", color =  000000)

    if a == 0:
      msg.add_field(name = "Please check data", value = "Coefficient of x² term is 0",inline = False)
      
    else:
      eqn = f'{a} x² + {b}x + {c} = 0'
      msg.add_field(name = "The standard form of equation looks like:",value = eqn)
      D = b*b-4*a*c #discriminant
      if D == 0:
        msg.add_field(name = "Nature of roots", value = "Yay!! The roots are real and equal",inline = False)
        res = (-b/(2*a))
        msg.add_field(name = "Roots",value = f'```css\n{res} and {res}```' ,inline = False)
      
      else:
        if D<0:
          msg.add_field(name = "Nature of roots", value = "Uh-Oh!! The roots are not real",inline = False)
          x1 = (-b + cmath.sqrt(D))/(2*a)
          x2 = (-b - cmath.sqrt(D))/(2*a)
       
        if D>0:
          msg.add_field(name = "Nature of roots", value = "The roots are real and distinct",inline = False)
          x1 = (-b + math.sqrt(D))/(2*a)
          x2 = (-b - math.sqrt(D))/(2*a)

        sqrtform = f'({-b} +- sqrt({str(D)}) )/{2*a}'

        res = str(x1)+" & "+ str(x2)
        msg.add_field(name = "Roots",value = f'```css\n{sqrtform}```\nwhich is simplified to\n```css\n{res}```' ,inline = False)

    msg.set_footer(text=f'Answered using Formula to solve quadratic equations \nrequested by: {ctx.author.display_name}')

    await ctx.send(embed = msg)

  #Mean
  @commands.hybrid_command(help = "enter data separated by space. \n\n eg. >mean 1 2 3 4 5 ...")
  async def mean (self, ctx, *, data_str):
    data = [float(idx) for idx in data_str.split(' ')]
    await ctx.send(f'Mean of given data is {stat.mean(data)}')

  #Median
  @commands.hybrid_command(help = "enter data separated by space. \n\n eg. >median 1 2 3 4 5 ...")
  async def median (self, ctx, *, data_str):
    data = [float(idx) for idx in data_str.split(' ')]
    await ctx.send(f'Median of given data is {stat.median(data)}')

  #Mode
  @commands.hybrid_command(help = "enter data separated by space. \n\n eg. >mode 1 2 2 4 5 ...")
  async def mode (self, ctx, *, data_str):
    data = [float(idx) for idx in data_str.split(' ')]
    mode = stat.multimode(data)
    if len(mode)==1:
      await ctx.send(f'Mode of given data is {stat.multimode(data)}')
    else:
      await ctx.send(f'Modes of given data are {stat.multimode(data)}')

async def setup(bot):
  await bot.add_cog(Solvers(bot))