import discord
from discord import app_commands
from discord.ext import commands


class TemplateCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(__name__)

    @app_commands.command()
    async def command(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("message")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TemplateCog(bot))
