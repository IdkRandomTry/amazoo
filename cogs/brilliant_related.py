import discord
from discord.ext import commands

from bs4 import BeautifulSoup
import requests


class Brilliant_related(commands.Cog):

  def __init__(self,bot):
    self.bot = bot

  #briki
  @commands.hybrid_command(help ='Links to brilliant wiki closest to your query.e.g. >briki eulerian path')
  async def briki(self,ctx,*,query:str):
    page = requests.get("https://www.google.com/search?q=brilliant wiki "+query+"&num=1")
    soup = BeautifulSoup(page.content, "html5lib")
    links = soup.findAll("a")
    for link in links:
      daURL = "empty"
      link_href = link.get('href')
      if "url?" and "brilliant.org" in link_href:
        daURL = "https://www.google.com/" + link_href
        briki_page = requests.get(daURL)
        soup = BeautifulSoup(briki_page.content, "html5lib")

        title = soup.find("title").text
        daURL = soup.find(class_  = "wiki-self-citation").find("a").get('href')
        summary = soup.find(class_ = "summary wiki-content").find("p").text
        contents = soup.find(class_ = "toc wiki-toc").findAll("li")
        toc = ""
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

  #mobile view
  @commands.hybrid_command(help = 'Gives you the link to go to brilliant.org mobile view.')
  async def mobview(self,ctx):
    await ctx.send("It really bugged me as well when I couldn't go to mobile view from full site view. Here's the link for the switch: https://brilliant.org/?flavour=mobile")

  #full site view
  @commands.hybrid_command(help = 'Gives you the link to go to brilliant.org full view.')
  async def fullview(self,ctx):
    await ctx.send("Here's the link for the switch: https://brilliant.org/?flavour=full")

async def setup(bot):
  await bot.add_cog(Brilliant_related(bot))