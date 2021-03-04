from discord.ext import commands
import utils

print('Loading config file')
cfg = utils.load_config('Config.json')

print('Creating bot')
bot = commands.Bot('.', case_insensitive=True)

@bot.event
async def on_ready():
	print('=================')
	print('Loaded up and ready to roll!')
	print(f'Username: {bot.user.name}')
	print('=================')

print('Starting bot')
bot.run(cfg.token)