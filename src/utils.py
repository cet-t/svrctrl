from typing import Literal


def create_link(
    type: Literal[
        "command",
        "user",
        "text",
        "voice",
    ],
    **args,
):
    match type:
        case "command":
            return f"</{args["name"]}:{args["id"]}>"
        case "user":
            return f"<@{args["id"]}>"
        case "text":
            return f"<#{args["id"]}>"
        case "voice":
            return (
                f"https://discord.com/channels/{args["guild_id"]}/{args["channel_id"]}"
            )
