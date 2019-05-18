import json
import discord

config_file = open('config.json')
TOKEN = json.load(config_file)['token']

client = discord.Client()

@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 533900036917166090:
        print(payload.emoji.name)
        # Find a role corresponding to the Emoji name.
        guild = payload.guild

client.run(TOKEN)