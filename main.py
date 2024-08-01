import discord
import random
import time
import re
import json


class Client(discord.Client):
    greetings = [
        "welcome*",
        "hai*",
        "hello*",
        "hi*hi*",
        "hi*",
        "hi*e*",
    ]

    emotions = [
        " ^.^",
        "!*",
        " :3",
        " >:3",
        " ^-^",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open("config.json") as cfg_file:
            self.config = json.load(cfg_file)

        self.channel = self.get_channel(self.config["server"]["watch_channel"])
        self.reply_counter = self.reset_counter()

    def add_repititions(self, input: str) -> str:
        while (i := input.find("*")) >= 0:
            input = input.replace("*", input[i - 1] * random.randint(1, 20), 1)

        return input

    def gen_message(self) -> str:
        random.seed(time.time_ns())
        ret = random.choice(self.greetings) + random.choice(self.emotions)
        ret = self.add_repititions(ret)

        return ret

    def reset_counter(self) -> int:
        rand_cfg = self.config["bot"]["random"]
        self.reply_counter = (
            random.randint(rand_cfg["min"], rand_cfg["max"])
            if rand_cfg["enabled"]
            else self.config["bot"]["fixed"]
        )

        return self.reply_counter


intents = discord.Intents.default()
intents.message_content = True
bot = Client(intents=intents)


@bot.event
async def on_ready():
    print(f"🪵'd (Logged)  in as {bot.user}")

    if not bot.channel:
        bot.channel = await bot.fetch_channel(bot.config["server"]["watch_channel"])

    # TODO: Once discord.py has application emoji support
    # emotions.append([i if i.available else None for i in client.emojis])


@bot.event
async def on_message(message: discord.Message):
    if (
        message.author == bot.user
        or message.channel != bot.channel
        or str(message.author.id) != bot.config["server"]["watch_user"]
    ):  # sad face :3
        return

    bot.reply_counter -= 1

    if bot.reply_counter == 0:
        send_msg = bot.gen_message()

        await bot.channel.send(send_msg)

        bot.reset_counter()
        return


bot.run(bot.config["bot"]["token"])
