import asyncio
import subprocess

from cli.result import Result


def is_running(port: int = 25565) -> bool:
    cmd = f'netstat -ano | find ":{port}" | length'
    res = subprocess.run(["nu", "-c", cmd], capture_output=True, text=True)
    count = int(res.stdout.strip())
    return count > 0


async def boot() -> Result:
    if is_running():
        return Result.AlreadyBoot

    await asyncio.sleep(3)
    print("boot")

    return Result.Ok


async def reboot() -> Result:
    if not is_running():
        return Result.NotBoot

    await asyncio.sleep(3)
    print("reboot")

    return Result.Ok


async def shutdown():
    if not is_running():
        return Result.NotBoot

    await asyncio.sleep(3)
    print("shutdown")

    return Result.Ok
