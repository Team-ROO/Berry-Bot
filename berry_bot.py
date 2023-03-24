import discord
import asyncio
import datetime
from discord.ext import commands

# Initialize intents and bot
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize reminders dictionary
reminders = {}

# Callback functions for reminders
async def remind_leppa(member):
    await asyncio.sleep(60)
    await member.send(f'{member.mention} time to harvest your Leppa Berries!')
    if member.id in reminders:
        reminders[member.id].remove("leppa")

async def remind_gracidea(member):
    await asyncio.sleep(60)
    await member.send(f'{member.mention} time to harvest your Gracidea Flowers!')
    if member.id in reminders:
        reminders[member.id].remove("gracidea")

# Function to schedule reminders
async def schedule_reminder(member, delay, callback, reminder_name):
    await asyncio.sleep(delay)
    await callback(member)

    if member.id in reminders and reminder_name in reminders[member.id]:
        reminders[member.id].remove(reminder_name)

# Event to print bot's login name
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to set a Leppa Berry reminder
@bot.command()
async def leppa(ctx):
    delay = 0.01 * 60 * 60 # 20 hours in seconds
    member = ctx.author
    await ctx.send(f"Reminding {member.mention} to harvest Leppa Berry in 20 hours")
    if member.id not in reminders:
        reminders[member.id] = []
    reminders[member.id].append("leppa")
    await schedule_reminder(member, delay, remind_leppa, "leppa")

# Command to set a Gracidea Flower reminder
@bot.command()
async def gracidea(ctx):
    delay = 44 * 60 * 60 # 44 hours in seconds
    member = ctx.author
    await ctx.send(f"Reminding {member.mention} to harvest Gracidea Flower in 44 hours")
    if member.id not in reminders:
        reminders[member.id] = []
    reminders[member.id].append("gracidea")
    await schedule_reminder(member, delay, remind_gracidea, "gracidea")

# Command to set a custom water reminder
@bot.command()
async def water(ctx, duration: int):
    delay = duration * 60 * 60 # Convert hours to seconds
    member = ctx.author
    await ctx.send(f"Reminding {member.mention} to water their berries in {duration} hours")
    if member.id not in reminders:
        reminders[member.id] = []
    reminders[member.id].append("water")
    await schedule_reminder(member, delay, lambda m: m.send(f"{m.mention} it's time to water your berries!"), "water")

# Command to list all active reminders
@bot.command(name='reminders', help='Lists all the active reminders')
async def list_reminders(ctx):
    member = ctx.author
    if member.id in reminders:
        reminders_str = "\n".join(reminders[member.id])
        await ctx.send(f"{member.mention}, you have the following active reminders:\n{reminders_str}")
    else:
        await ctx.send(f"{member.mention}, you have no active reminders.")

# Command to cancel all of a user's reminders
@bot.command(name='cancel', help='Cancels the specified user\'s reminder')
async def cancel(ctx, member: discord.Member):
    if member.id in reminders:
        del reminders[member.id]
        await ctx.send(f"{member.mention}, all of your reminders have been cancelled.")
    else:
        await ctx.send(f"{member.mention}, you have no active reminders.")

# Run the bot
bot.run("MTA4Nzc3NjgwMTI1MTY3NjE3MA.GkQkka.4XNUcvIjo3_ja2hVq90pEeyaZNX460G884XGVA")

