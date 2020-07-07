# JustSaysInMiceBot

A Discord bot that lets you have your own, personal <https://twitter.com/justsaysinmice>. Pretty much nothing to it. Says "IN MICE" when someone says `/(?!)in.*mice/`.


## Run locally

Requires Python >= 3.8, [discord.py](https://github.com/Rapptz/discord.py), and a Discord app token.

```
pip install -r requirements.txt
export JUSTSAYSINMICEBOT_TOKEN='<discord app token>'
python justsaysinmicebot.py
```

## Run with Docker

First

```
cp template.env .env
```

then fill in `JUSTSAYSINMICEBOT_TOKEN` in `.env`. Then

```
docker-compose up
```
