# JustSaysInMiceBot

<img alt='justsaysinmicebot in glorious action' src='README-justsaysinmicebot.png' width='50%' height='50%'>

A Discord bot that lets you have your own, personal <https://twitter.com/justsaysinmice>. Pretty much nothing to it. Says "IN MICE" when someone says `/(?!)in.*mice/`.

Add it to your server with [this link](https://discord.com/api/oauth2/authorize?client_id=729787035136557137&permissions=67584&scope=bot) _(permissions: 67584 Send Messages, Read Message History)_.


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
