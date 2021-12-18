import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time
from threading import Thread

# setting up thingz
timeloop = True
sec = 0
bot = commands.Bot(command_prefix = '!', case_insensitive = True) # you can change the prefix here
game = discord.Game(name = 'game name') # replace game name with, well, the game name
TOKEN = 'ODY3NDI1NjQ3MzIwMjM2MDMz.YYT6ng.HC1nMZd3q8qWxnswLFYE_WMf-QQ' # put bot token here

# timer function
def timer():
	global sec
	while timeloop:
		time.sleep(1)
		sec += 1

background_thread = Thread(target=timer)
background_thread.start()

@bot.event
async def on_ready():
	await bot.change_presence(activity = game)
	print("Bot is online and connected to Discord")

# functions for attack command
# you need to make four txt files called bosshealth, defeatedtimes, bossname, and totalhealth
# and set the first boss' stats in those

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

@bot.command()
async def attack():
	global sec
	if sec < 5: # you can customize how many seconds you want in between to allow people to attack
		await bot.say('You cannot attack for another ' + str(5-sec) + ' seconds.')
		return
	sec = 0
	health = int(getBossHealth())
	boss = ['list of names']
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
		
#running the bot
bot.run(TOKEN)
