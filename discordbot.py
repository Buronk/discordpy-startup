from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))

channel_bot_test = [channel for channel in client.get_all_channels() if channel.name == 'test'][0]
await client.send_message(channel_bot_test, '勝手に喋るよ')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
