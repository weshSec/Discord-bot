#Nao_Bot
import discord
import asyncio
import pytz
from discord import Emoji
from datetime import datetime
from pytz import timezone


client = discord.Client()


@client.event

async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='help!'))
    print('------')


@client.event
async def on_message(message):

    #if message.content.startswith(''):

	
    if message.content.startswith('help!'):
        embed = discord.Embed(title="**Nao**", description="A bot under development.", colour=0xff00b8)
        embed.set_thumbnail(url='https://wiki.mabinogiworld.com/images/thumb/0/07/Nao.png/215px-Nao.png')
        embed.add_field(name=":alarm_clock: Time", value="``time!``", inline=True)
        embed.add_field(name=":speech_balloon: Spam", value="``spam! | spam! s``" , inline=True)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('test!'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    if message.content.startswith('spam!'):
        if message.author.id != client.user.id:
            await client.delete_message(message)
            spam = ""
            string = message.content.split()
            times = int(string[len(string)-1])
            if string[1] == "s":
                for i in range(len(string)):
                    if not(i<2 or i==len(string)-1):
                        spam += " "+string[i]
                        if "554324647710294026" in [role.id for role in message.author.roles]:
                            if times <= 50:
                                for i in range(times):
                                    await asyncio.sleep(1)
                                    if not(i==times-1):
                                        await client.send_message(message.channel, spam)
                                        async for m in client.logs_from(message.channel, limit=1):
                                            check = str(message.content.split()[2:3])
                                            if check[2:3] in spam:
                                                await client.delete_message(m)
                                    else:
                                        await client.send_message(message.channel, spam)
                            else:
                                for i in range(50):
                                    await asyncio.sleep(1)
                                    if not(i==times-1):
                                        await client.send_message(message.channel, spam)
                                        async for m in client.logs_from(message.channel, limit=1):
                                            check = str(message.content.split()[2:3])
                                            if check[2:3] in spam:
                                                await client.delete_message(m)
                                    else:
                                        await client.send_message(message.channel, spam)
                        else:
                            if times <= 20:
                                for i in range(times):
                                    await asyncio.sleep(1)
                                    if not(i==times-1):
                                        await client.send_message(message.channel, spam)
                                        async for m in client.logs_from(message.channel, limit=1):
                                            check = str(message.content.split()[2:3])
                                            if check[2:3] in spam:
                                                await client.delete_message(m)
                                    else:
                                        await client.send_message(message.channel, spam)
                            else:
                                for i in range(20):
                                    await asyncio.sleep(1)
                                    if not(i==times-1):
                                        await client.send_message(message.channel, spam)
                                        async for m in client.logs_from(message.channel, limit=1):
                                            check = str(message.content.split()[2:3])
                                            if check[2:3] in spam:
                                                await client.delete_message(m)
                                    else:
                                        await client.send_message(message.channel, spam)
            else:
                for i in range(len(string)):
                    if not(i==0 or i==len(string)-1):
                        spam += " "+string[i]
                if "554324647710294026" in [role.id for role in message.author.roles]:
                    if times <= 50:
                        for i in range(times):
                            await asyncio.sleep(1)
                            await client.send_message(message.channel, spam)
                    else:
                        for i in range(50):
                            await asyncio.sleep(1)
                            await client.send_message(message.channel, spam)
                elif times <= 20:
                    for i in range(times):
                        await asyncio.sleep(1)
                        await client.send_message(message.channel, spam)
                else:
                    for i in range(20):
                        await asyncio.sleep(1)
                        await client.send_message(message.channel, spam)

    if message.content.startswith('clear!'):
        if "554324647710294026" in [role.id for role in message.author.roles]:
            await client.delete_message(message)
            command = message.content.split()
            times = int(command[1])
            if times <= 100:
                async for m in client.logs_from(message.channel, limit=times):
                    try:
                        await client.delete_message(m)
                    except:
                        pass


    if message.content.startswith('time!'):
    	embed = discord.Embed(title="**Time**", description="Server Time[24hours] Erinn Time[12hours]", colour=0xff00b8)
    	embed.set_thumbnail(url='https://wiki.mabinogiworld.com/images/thumb/2/28/Tarlach.png/166px-Tarlach.png')
    	embed.add_field(name=":desktop: Server Time", value="``"+Server_Time()[:5]+"``", inline=True)
    	embed.add_field(name=":star: Erinn Time", value="``"+Erinn_Time()+"``", inline=True)
    	await client.send_message(message.channel, embed=embed)

def Server_Time():
    date_format='%H:%M:%S'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('America/Los_Angeles'))
    date_real = date.strftime(date_format)
    return date_real

def Erinn_Time():
    date_real = Server_Time()
    date_erinn = date_real
    date_erinn = int(date_erinn[:2])
    if date_erinn > 12:
        date_erinn -= 12
        if date_erinn<10:
            date_erinn = "0" + str(date_erinn) + ":" + date_real[3:] 
    else:
        date_erinn = date_real


    # Erinn DataBase
    h = 12
    m = 0
    times = []
    while len(times)<41:
        if m >= 60:
            m -= 60
            h += 1
        if h > 12:
            h = 1
        if len(str(m))<2:
            m = "0"+str(m)
        if len(str(h))<2:
            h = "0"+str(h)
        erinn_times = str(h)+":"+str(m)+":00"
        h = int(h)
        m = int(m)
        m += 18
        times.append(erinn_times)

    # Checker
    if date_erinn in times:
        if (times.index(date_erinn)+1)%2 == 0:
            print("Midnight")
        else:
            print("Noon")


    # Conversor
    am_pm = "AM"
    date_erinn_hour = int(date_erinn[:2])*3600
    date_erinn_minute = int(date_erinn[3:5])*60
    date_erinn_second = int(date_erinn[6:8])
    date_erinn_total = (date_erinn_hour + date_erinn_minute + date_erinn_second)*40
    counter = 0
    while date_erinn_total>86400:
        date_erinn_total -= 86400
        counter += 1
    date_erinn_hour = (date_erinn_total/3600)
    date_erinn_minute = (date_erinn_hour - int(date_erinn_hour ))*60
    date_erinn_hour = int(date_erinn_hour)
    date_erinn_minute = int(date_erinn_minute)
    if len(str(date_erinn_minute)) < 2:
        date_erinn_minute = "0" + str(date_erinn_minute)
    if int(date_erinn_hour) > 12:
        date_erinn_hour -= 12 
        am_pm = "PM"
    date_erinn = str(date_erinn_hour)+ ":" + str(date_erinn_minute) + " " + am_pm
    return date_erinn


client.run('TOKEN')
