import discord
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive
import os

keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} ")
    try:
        synced = await bot.tree.sync()
        print(f"🔁  {len(synced)}  (/)")
    except Exception as e:
        print(f"h: {e}")

@bot.tree.command(name="becam", description=" 🎧")
async def becam(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        if not interaction.guild.voice_client:
            await channel.connect()
            await interaction.response.send_message(f"✅  **{channel.name}**", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ .", ephemeral=True)
    else:
        await interaction.response.send_message("❌ !", ephemeral=True)

@bot.tree.command(name="out", description="  ❌")
async def out(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("🚪 .", ephemeral=True)
    else:
        await interaction.response.send_message("❌ .", ephemeral=True)


token = os.getenv('DISCORD_TOKEN')
bot.run(token)

