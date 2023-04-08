import discord
from discord.ext import commands
#from keep_alive import keep_alive
from keep_alive import awake
import os

client = discord.Client()

bot = commands.Bot(command_prefix = '>', help_command = commands.MinimalHelpCommand( no_category = 'Others'))

@bot.event
async def on_message(message):
  if message.content == ">help":
    await message.channel.send("Check out the Help Manual: https://sites.google.com/view/amazoo-help/home")

  await bot.process_commands(message)

#log
@bot.event
async def on_ready():
  print('Logged in as '+ str(bot.user.name))
  print('-------')
  print('Servers connected to:')
  for guild in bot.guilds:
    print(guild.name)

#error_handler
@bot.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.CommandOnCooldown):
    message = f"The :eye: has to blink (Please try again after {round(error.retry_after, 1)} seconds.)"
  elif isinstance(error, commands.MissingPermissions):
    message = "You are missing the required permissions to run this command!"
  elif isinstance(error, commands.MissingRequiredArgument):
    message = f"Missing a required argument: `{error.param}`"
  elif isinstance(error, commands.ConversionError):
    message = str(error)
  elif isinstance(error, commands.CommandNotFound):
    message = str(error)
  else:
    message = "Oh no! Something went wrong while running the command!"
    print(error)
  
  await ctx.send(message)

#command - servers
@bot.command()
async def servers(ctx):
    await ctx.send(f"At the moment Eye of Amazoo is a part of `{len(bot.guilds)}` servers")

#Loading cogs
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

awake("https://Amazoo.siddheshumarjee.repl.co", False)
#keep_alive()

try:
  bot.run(os.environ['TOKEN'])
except discord.errors.HTTPException:
  print("flag")
  print("\n Blocked by ratelimits restarting now" )
  os.system('kill 1')
  print("killed1")
  os.system("python restarter.py")