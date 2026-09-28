import asyncio
import os
from pathlib import Path

import discord
from discord.ext import commands

from cli.mc import is_running


class Bot(commands.Bot):
    @commands.Cog.listener()
    async def on_ready(self) -> None:
        await self.change_presence(
            activity=discord.Activity(
                name="Loading...",
                type=discord.ActivityType.competing,
            ),
            status=discord.Status.idle,
        )
        await self.tree.sync()
        await self.change_presence(
            activity=discord.Activity(
                name="Running...",
                type=discord.ActivityType.playing,
            ),
        )

    @staticmethod
    def _cogs(dir: str) -> list[str]:
        cogs: list[str] = []

        dir_path = Path(dir)
        if not (dir_path.exists() and dir_path.is_dir()):
            return cogs

        for file_path in dir_path.iterdir():
            if file_path.name.startswith("_"):
                continue

            dir_name = file_path.parent.name
            file_name = file_path.name.split(".")[0]
            cogs.append(f"{dir_name}.{file_name}")

        return cogs

    def setup_cog(self, cog_dir: str = "src/cogs/") -> None:
        if not os.path.exists(cog_dir):
            return

        for cog in Bot._cogs(cog_dir):
            asyncio.run(self.load_extension(cog))

    def __token(self, key: str) -> str:
        try:
            import dotenv

            dotenv.load_dotenv()
            return os.environ[key]
        except KeyError:
            print(f'"{key}" not found.')
            raise

    async def setup_hook(self) -> None:
        await self.tree.sync()

    def boot(self, key: str = "TOKEN") -> None:
        super().run(self.__token(key))


if __name__ == "__main__":
    print(f"is_running: {is_running()}")

    bot = Bot(command_prefix=[], intents=discord.Intents.all())
    bot.setup_cog()
    bot.boot()
