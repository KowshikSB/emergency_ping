from discord.ext import commands
from discord import channel, utils
import discord
import asyncio

from discord.ext.commands import bot

import discord
from discord.ext import commands
class em(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    
    @commands.command()
    async def emergency(self,ctx,*,reason=None):
        if reason is not None:
            em=discord.Embed(title ="Emergency Ping", colour=0x2f3136)
            
            
            em.add_field(name="Reason:",value=f"```{reason}```",inline=False)
            em.add_field(name="Triggered by:",value=f"<@{ctx.author.id}> - `{ctx.author.id}`",inline=True)
            em.set_footer(text='Kek')
            
            
            await ctx.message.add_reaction("<:emergency_ping:831873364087537664>")
            x="<@&825260273010081794>"
            await ctx.channel.send(x,embed=em)
        else:
            
            
            await ctx.channel.send("*Please mention the reason*")
        
def setup(bot):
    bot.add_cog(em(bot))
