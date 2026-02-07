import discord
from discord import app_commands
from discord.ext import commands
from keep_alive import keep_alive
import os

# تشغيل سيرفر الويب للبقاء حياً
keep_alive()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} đã sẵn sàng!")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Đã đồng bộ {len(synced)} lệnh slash (/)")
    except Exception as e:
        print(f"Lỗi sync lệnh: {e}")

@bot.tree.command(name="becam", description="Bot vào kênh voice của bạn 🎧")
async def becam(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        if not interaction.guild.voice_client:
            await channel.connect()
            await interaction.response.send_message(f"✅ Be Cam đã vào kênh **{channel.name}**", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ Be Cam đang ở trong một kênh khác.", ephemeral=True)
    else:
        await interaction.response.send_message("❌ Bạn chưa ở trong kênh voice nào!", ephemeral=True)

@bot.tree.command(name="out", description="Bot rời khỏi kênh voice ❌")
async def out(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("🚪 Be Cam đã rời khỏi kênh voice.", ephemeral=True)
    else:
        await interaction.response.send_message("❌ Be Cam không ở trong kênh voice nào.", ephemeral=True)

# قراءة التوكن من Environment Variables في Render
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
