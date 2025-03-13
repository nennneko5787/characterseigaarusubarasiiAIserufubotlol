import os

import dotenv
from discord.ext import commands

bot = commands.Bot(
    [
        "otoha#",
        "otoha♪",
        "otohasayaka#",
        "otohasayaka♪",
        "音葉#",
        "音葉♪",
        "音葉さやか#",
        "音葉さやか♪",
    ],
    description="音葉さやかだよ♪よろしくね♪",
)


@bot.event
async def setup_hook():
    await bot.load_extension("cogs.aichat")


dotenv.load_dotenv()
bot.run(os.getenv("discord"))
