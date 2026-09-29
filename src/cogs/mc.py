import asyncio

import discord
from discord import app_commands
from discord.ext import commands

import cli.mc
from cli.result import Result


class McCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(__name__)

    @app_commands.command()
    async def mc_boot(self, interaction: discord.Interaction):
        await interaction.response.send_message("booting...")

        match await cli.mc.boot():
            case Result.AlreadyBoot:
                embed = discord.Embed(
                    colour=discord.Colour.red(),
                    title="Failed to boot the server",
                    description="it's already running.",
                )
                return await interaction.edit_original_response(embed=embed)
            case _:  # Ok
                pass

        await interaction.edit_original_response(content="success!")

    @app_commands.command()
    async def mc_reboot(self, interaction: discord.Interaction):
        await interaction.response.send_message("rebooting...")

        match await cli.mc.reboot():
            case Result.NotBoot:
                embed = discord.Embed(
                    colour=discord.Colour.red(),
                    title="Failed to reboot the server",
                    description="it's not booting.",
                )
                return await interaction.edit_original_response(embed=embed)
            case _:  # Ok
                pass

        await interaction.edit_original_response(content="success!")

    @app_commands.command()
    async def mc_shutdown(self, interaction: discord.Interaction):
        await interaction.response.send_message("rebooting...")

        match await cli.mc.reboot():
            case Result.NotBoot:
                embed = discord.Embed(
                    colour=discord.Colour.red(),
                    title="Failed to shutdown the server",
                    description="it's not booting.",
                )
                return await interaction.edit_original_response(embed=embed)
            case _:  # Ok
                pass

        await interaction.edit_original_response(content="success!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(McCog(bot))
