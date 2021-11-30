import discord
from keep_alive import keep_alive
import os
from discord.ext import commands

from bs4 import BeautifulSoup
import requests

client = discord.Client()

bot = commands.Bot(command_prefix = '>')

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
    message = f"Missing a required argument: {error.param}"
  elif isinstance(error, commands.ConversionError):
    message = str(error)
  else:
    message = "Oh no! Something went wrong while running the command!"
  
  await ctx.send(message)

#personal use
bot.flagcount  = 0
def flag(f:str = ""):
  print(str(bot.flagcount) + f)
  bot.flagcount+=1

@bot.command(help = "basic command")
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type ">ping" the bot will respond with "pong!"

#briki
@bot.command(help = 'Links to brilliant wiki closest to your query. \n e.g. >briki eulerian path')
async def briki(ctx,*,query:str):
  page = requests.get("https://www.google.com/search?q=brilliant wiki "+query+"&num=1") #top result for Gsearch
  soup = BeautifulSoup(page.content, "html5lib")
  links = soup.findAll("a")
  for link in links:
    daURL = "empty"
    link_href = link.get('href')
    if "url?" and "brilliant.org" in link_href: #is it really a brilliant wiki?
      daURL = "https://www.google.com/" + link_href
      briki_page = requests.get(daURL)
      soup = BeautifulSoup(briki_page.content, "html5lib")
      
      title = soup.find("title").text
      daURL = soup.find(class_  = "wiki-self-citation").find("a").get('href')
      summary = soup.find(class_ = "summary wiki-content").find("p").text
      contents = soup.find(class_ = "toc wiki-toc").findAll("li")
      toc = "" #table of content
      for content in contents:
        toc = toc + "• " + str(content.text).replace("\n", "").replace("  ","") + "\n"
    
      res = discord.Embed(title = title, url = daURL, description = "Click on title for complete wiki", color = 000000)
      res.add_field(name="Summary", value=summary + "...", inline=False)
      res.add_field(name="Content of the Wiki", value = toc,inline = False)
      res.set_footer(text="wiki provided by Brilliant \nrequested by: {}".format(ctx.author.display_name))
  
      await ctx.send(embed = res)
      break
      

  if daURL == "empty":
    await ctx.send("The :eye: of Amazoo could not find Brilliant wiki similar to your query...")

keep_alive()
bot.run(os.getenv("TOKEN"))
