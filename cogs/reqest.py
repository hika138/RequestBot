import discord
import os
from discord import app_commands
from discord.ext import commands
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
guild_id = int(os.environ.get("GUILD_ID"))
class request(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot