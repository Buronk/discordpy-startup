from discord.ext import commands
import discord
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()


@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 605720617924165646 and (before.channel != after.channel):
        alert_channel = client.get_channel(605720617924165644)
        if before.channel is None: 
            msg = {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

client.run(TOKEN)
