import discord
from discord.ext import commands
import os

# Создаем бота
bot = commands.Bot(command_prefix='!')

# Загружаем классы
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Событие готовности бота
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Запуск бота
bot.run('YOUR_BOT_TOKEN')
