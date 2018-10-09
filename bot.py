import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix = '.')
token = 'TOKEN'

@bot.event
async def on_ready():
    await bot.change_presence(game = discord.Game(name = 'with my horn'))
    print("Bot is online and connected to Discord")

#functions for attack command
def getBossHealth():
	bosshealthfile_read = open('bosshealth.txt', 'r')
	health = bosshealthfile_read.read()
	bosshealthfile_read.close()
	return health

def changeBossHealth(amount):
	bosshealthfile_write = open('bosshealth.txt', 'w')
	bosshealthfile_write.write(str(amount))
	bosshealthfile_write.close()

def getDefeatedTimes():
	defeatedtimesfile_read = open('defeatedtimes.txt', 'r')
	defeatedtimes = defeatedtimesfile_read.read()
	defeatedtimesfile_read.close()
	return defeatedtimes

def changeDefeatedTimes(amount):
	defeatedtimesfile_write = open('defeatedtimes.txt', 'w')
	defeatedtimesfile_write.write(str(amount))
	defeatedtimesfile_write.close()

def getBossName():
	bossnamefile_read = open('bossname.txt', 'r')
	bossname = bossnamefile_read.read()
	bossnamefile_read.close()
	return bossname

def changeBossName(amount):
	bossnamefile_write = open('bossname.txt', 'w')
	bossnamefile_write.write(str(amount))
	bossnamefile_write.close()

def getTotalHealth():
	totalhealthfile_read = open('totalhealth.txt', 'r')
	totalhealth = totalhealthfile_read.read()
	totalhealthfile_read.close()
	return totalhealth

def changeTotalHealth(amount):
	totalhealthfile_write = open('totalhealth.txt', 'w')
	totalhealthfile_write.write(str(amount))
	totalhealthfile_write.close()

#start of commands
@bot.event
async def ping():
	await bot.say('pong!')

@bot.command()
async def attack():
	health = int(getBossHealth())
	boss = ['Valo', 'Jasper', 'Xoshi', 'Luc', 'Xolia', 'Angle', 'Liam', 'Clarence', 'Gabriel', 'Lem', 'Bow']
	name = getBossName()
	defeatedtimes = int(getDefeatedTimes())
	totalhealth = int(getTotalHealth())
	if health > 0:
		damage = random.randint(1, 20)
		health = health - damage
		changeBossHealth(health)
		if health <= 0:
			defeatedtimes = defeatedtimes + 1
			changeDefeatedTimes(defeatedtimes)
			health = 50 + (20 * defeatedtimes)
			changeBossHealth(health)
			totalhealth = health
			changeTotalHealth(totalhealth)
			name = random.choice(boss)
			changeBossName(name)
			await bot.say('You have defeated the boss!\n\na new enemy appears')
		await bot.say('level %s: %s \n%s / %s HP \n\nYou have done %s damage! ' % (defeatedtimes, name, health, totalhealth, damage))

bot.run(TOKEN)
