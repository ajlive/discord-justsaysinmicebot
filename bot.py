#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

import discord  # type: ignore

APP_TOKEN = "JUSTSAYSINMICEBOT_TOKEN"
INMICE_PATTERN = re.compile(r"in.*mice", re.IGNORECASE)

client = discord.Client()


class NoAppToken(Exception):
    pass


@client.event
async def on_ready() -> None:
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    if INMICE_PATTERN.search(message.content):
        await message.channel.send("IN MICE")


def main() -> None:
    def _app_token() -> str:
        try:
            token = os.environ[APP_TOKEN]
            assert token
        except (KeyError, AssertionError) as e:
            raise NoAppToken
        return token

    try:
        token = _app_token()
    except NoAppToken:
        sys.exit(
            (
                "Please expose Discord app token as env var {APP_TOKEN};"
                " if using docker, cp template.env .env, fill in token"
            )
        )
    client.run(token)


if __name__ == "__main__":
    main()
