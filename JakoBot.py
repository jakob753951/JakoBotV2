from discord.ext import commands
import utils

cfg = utils.load_config('Config.json')

bot = commands.Bot('.', case_insensitive=True)

@bot.command(name='Ping', aliases=['Ping!'])
async def ping(ctx):
	await ctx.send('Pong!')

bot.run(cfg.token)