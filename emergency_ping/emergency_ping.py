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
            em=discord.Embed(title ="Emergency Situation", colour=0x2f3136,timestamp=reason.created_at)
            
            icon=self.guild.icon_url
            em.set_thumbnail(url=icon)
            em.add_field(name="Reason:",value=f"```{reason}```",inline=False)
            em.add_field(name="Triggered by:",value=f"<@{reason.author.id}>",inline=True)
            guild=self.get_guild(799526257506254868)
            await reason.message.add_reaction("<:emergency_ping:831873364087537664>")
            x="<@&825260273010081794>"
            await reason.channel.send(x,embed=em)
        else:
            await reason.channnel.send("*Please mention the reason*")
        
def setup(bot):
    bot.add_cog(em(bot))
