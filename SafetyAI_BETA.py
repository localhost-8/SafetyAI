token = "ок, а теперь напишем 18 bit ключ входа? "
while True:
    import os, time, sys, subprocess
    if len(sys.argv) == 2:
        time.sleep(5)
        print ('track end')
        if sys.platform == 'darwin':
            subprocess.Popen(['say', 'hello'])
    else:
        print ('main begin')
    #try:

        
    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)
    print ('[+] add to startup')
    print("[+] restarting libraries")
    
    #-------------
    #Импорт библиотек
    import json
    import discord # Библиотека дискорда
    import requests 
    import datetime
    from bs4 import BeautifulSoup 
    import asyncio # Библиотека на ожидание.
    from discord.ext import commands, tasks # Импортирование из библиотеке функцию commands, tasks
    #pip3 install discordpy-slash
    #pip install slash-discord.py
    #pip install -U slash-discord.py 
    from discord_slash import SlashCommand
    from discord_slash.utils.manage_commands import create_option
    from discord.utils import get # Импортирование из библиотеке функцию get
    from discord.ext.commands import Bot
    from discord import FFmpegPCMAudio# Импортирование из библиотеке функцию Bot для работы бота.
    import ffmpeg
    import subprocess
    from subprocess import check_call
    import youtube_dl
    import random
    from colorama import init, Fore, Back, Style
    import requests
    import re
    import numpy as np
    from dhooks import Webhook
    from discord.gateway import DiscordWebSocket
    from rule34Py import rule34Py, version
    import winsound
    from bs4 import BeautifulSoup as bs
    
    
    #except:
        #print("[*] > Error in the library, please. restart the system !")
''' <---- Object Comment
    USE: Thonny/VScode/Pyton IDLE/Komodo/PyCharm
'''
    cmd  = os.system("cls")
    print("[*] trying to connect...") 
    print("[LOADING] Loading program...")
    print("""\033[1;32m
    ---------------------------------------------------------------------------------------
            ____  _ __                               __
           / __ )(_) /_  ____ _____  ____ __________/ /
          / __  / / __ \/ __ `/_  / / __ `/ ___/ __  /
         / /_/ / / / / / /_/ / / /_/ /_/ / /  / /_/ /
        /_____/_/_/ /_/\__,_/ /___/\__,_/_/   \__,_/

                                                  25.7V
                                                                Coded By 𝖆✟ᖴᏬᏒᏒᎩ 𝕯𝖗𝖚𝖓𝖐𝖊𝖗 ✞˞˞ٴٴB#0733
    --------------------------------------------------------------------------------------- 
    """)
    class MyDiscordWebSocket(DiscordWebSocket):
        print("  [-] plug-ins are enabled (0)") 

        async def send_as_json(self, data):
            if data.get('op') == self.IDENTIFY:
                if data.get('d', {}).get('properties', {}).get('$browser') is not None:
                    data['d']['properties']['$browser'] = 'Discord Android'
                    data['d']['properties']['$device'] = 'Discord Android'
            await super().send_as_json(data)


    DiscordWebSocket.from_client = MyDiscordWebSocket.from_client
    user_agents = [ 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
    ]
    user_agent = random.choice(user_agents) 
    headers = {'User-Agent': user_agent}
    try:
        print("[+] start of systems")
        frequency = 1500  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        #Импорт библиотек
        #-------------
        #Настройка бота
        current_time = datetime.date.today()
        songs = asyncio.Queue()
        play_next_song = asyncio.Event()
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
        print("player:" + str(ydl))
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        client = discord.Client()
        nd = datetime.datetime.now() #Переменая в которой содержиться дата и время
        prefixintial = open("prefix.txt", "+a")
        prefixintial = open( "prefix.txt", "r").readline(1)
        import os
        import subprocess
        from subprocess import check_call
        print("\033[1;32m USER:" + os.name)
        print(f"\033[1;32m CONNECT: {current_time}")
        print(os.getpid())
        prefix = prefixintial # Создаем переменую prefix и пишем переменую prefixinitial, нужно для не которых команд
        print("\033[1;32m command:" + str(prefix))
        client = commands.Bot( command_prefix= prefix)
        slash = SlashCommand(client, sync_commands=True) #инициализируем бота префиксом тоесть переменой prefixinitial
        print("\033[1;32m =============================")
        winsound.Beep(frequency, duration)
        frequency2 = 650  # Set Frequency To 2500 Hertz
        duration2 = 50  # Set Duration To 1000 ms == 1 second
        frequency3 = 2500  # Set Frequency To 2500 Hertz
        duration3 = 50  # Set Duration To 1000 ms == 1 second
    except:
        print("[***] > Error with settings, restart the system")
    #Настройка бота
    #-------------
    # Выдача Гендерных ролей
    # Выдача ролей при помощи select menu
    try:
        @slash.slash(description="ai")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def browser(ctx, text:str):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            a = []
            b = []
            c = []
            d = []
            a1 = []
            b1 = []
            c1 = []
            d1 = []

            user_agents = [ 
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
                'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
                'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
            ]
            user_agent = random.choice(user_agents) 
            headers = {'User-Agent': user_agent}

            H = ["Rtsp://","rtsp://","www.","t.me",".pro",".net",".nes",".ru",".org","Hrrp://","hrrp://","Hrrps://","hrrps://","Http://","http://","Https://","https://"]
            f = False
            h = 0
            H1 = [f'https://www.google.ru/search?q={text}',f'https://www.bing.com/search?q={text}']
            for v in H:
                regex = re.compile(v)
                match = re.search(regex, text)
                if match:
                    H1 = re.findall(r'(https://[^\s]+)', text)
                    
            for H2 in H1:
                r = requests.get(str(H2), headers = headers)
                soup = bs(r.content, 'lxml')
                try:
                    a = str(soup.select_one('title').text)
                except:
                    b = str(soup.find_all('title'))
                    print("error!")
                try:
                    b = str(soup.select_one('body').text) 
                except:
                    b = str(soup.find_all('body'))
                    print("error!")
                try:
                    c = str(soup.select_one('h1').text) + ' \ add+ \ '
                except:
                    c = str(soup.find_all('h1')) + ' \ add+ \ '
                    print("error!")
                try:
                    c += str(soup.select_one('h3').text) + ' \ add+ \ '
                except:
                    c += str(soup.find_all('h3')) + ' \ add+ \ '
                    print("error!")
                try:
                   d = str(soup.select_one('span').text)
                except:
                    d = str(soup.find_all('span')) 
                    print("error!")
                try:
                   e = str(soup.select_one('div').text) 
                except:
                    e = str(soup.find_all('div')) 
                    print("error!")
                try:
                    a = str(a[0:120])
                except:
                    print("error!")
                try:
                    b = str(b[0:120])
                except:
                    print("error!")
                try:
                    c = str(c[0:120])
                except:
                    print("error!")
                try:
                    d = str(d[0:120])
                except:
                    print("error!")
                try:
                    e = str(e[0:120])
                except:
                    print("error!")
                    
                inf = discord.Embed(
                    color = setx,
                    title=f"[Title] {a}" ,
                    description= f"\n [Answer] {b} \n [Object] {c} \n [] {d} \n [Model] {e}",
                )
                send2 = await ctx.send(embed=inf)
                await asyncio.sleep(15)
                await send2.delete()
                
        @slash.slash(description="turn off the bot on the server")
        @commands.cooldown(1, 8, commands.BucketType.user)
        async def leave(ctx):
            fp = open("ID-admin.txt", "+a")
            with open("ID-admin.txt", "r") as file1:
                    # итерация по строкам
                for line in file1:
                    print("ID:" + str(ctx.author.id) + " ID:" + str(line.strip()))                                                                                                                                                                        
                    if str(ctx.author.id) == str(line.strip()):
                        print(f"command: Channel Locked.")
                        embed3 = discord.Embed(title=f'[:clock2:]**Bihazard: **',
                                description= f'**The problems were broken:**\n blocked ID: **#{ctx.guild.id}** \n ADMIN: @{ctx.author.name} @{ctx.author.nick} \n ``connect = False`` \n**Reason:** Guild Save Used\n`Please Wait For An Admin/Moderator To Unlock This Channel`\n **Conclusion:** ``search in history.``.',
                                colour=0xff0000)
                        embed3.set_thumbnail(url="https://images.mysafetylabels.com/img/lg/L/biological-hazard-ansi-caution-label-lb-2249.png")
                        await ctx.send(embed=embed3)
                        await ctx.guild.leave()
                    else:
                            embed3 = discord.Embed(title=f'**Bihazard: **',
                                    description= f'``#you dont have the rights to send an attack``',
                                    colour=0xff0000)
                            embed3.set_thumbnail(url="https://images.mysafetylabels.com/img/lg/L/biological-hazard-ansi-caution-label-lb-2249.png")
                            await ctx.send(embed=embed3)       
        
        @slash.slash(description="role")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def remove(ctx, member:discord.Member, role: discord.Role):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите ``member``!** {error_emoji}')
            else:
                if member is None:
                    await ctx.send(f'{error_emoji} **Пожалуйста, укажите ``role``!** {error_emoji}')
                else:
                    await member.remove_roles(role)
                    channel_id = 1038582736266461194
                    channel = client.get_channel(channel_id)
                    inf = discord.Embed(
                        color = setx,
                        title=f"{member} >>> get : {role}",
                        description= role,
                    )
                    await ctx.send(embed=inf)
                    await channel.send(embed=inf)
            
        @slash.slash(description="chat")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def DM(ctx, user_to_dm: discord.Member, arg): 
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if user_to_dm is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            else:
                await user_to_dm.create_dm()
                user = ctx.author.name
                embed3 = discord.Embed(title=f'user: {user} >>> send: { user_to_dm } ',
                                description=f'**loading...**',
                                colour=setx)
                embed3.set_image(url="https://media2.giphy.com/media/44y8gMkXosEm4qvRtF/giphy.gif?cid=790b7611ea3803295fbcd9407d7976ff88543e414e83d7d5&rid=giphy.gif&ct=g")
                embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                embed3.set_thumbnail(url=ctx.guild.icon_url)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                send1 = await ctx.send(embed=embed3)
                embed3 = discord.Embed(title=f'user: {user} >>> send: { user_to_dm } ',
                                description=f'{arg}',
                                colour=setx)
                embed3.set_image(url="https://media2.giphy.com/media/44y8gMkXosEm4qvRtF/giphy.gif?cid=790b7611ea3803295fbcd9407d7976ff88543e414e83d7d5&rid=giphy.gif&ct=g")
                embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                embed3.set_thumbnail(url=ctx.guild.icon_url)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                send2 = await user_to_dm.dm_channel.send(embed=embed3)
                await asyncio.sleep(3)
                await send1.delete()
                await asyncio.sleep(1800)
                await send2.delete()
                

        @slash.slash(description="settings")
        @commands.cooldown(1, 10, commands.BucketType.user)
        @commands.has_permissions(administrator = True)
        async def settings(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            user = ctx.author.name
            guild = ctx.guild
            embed3 = discord.Embed(title=f' ```settings - настройки``` ',
                            description='** 5️⃣ - включить "дополнительные функции" (1)? \n 6️⃣ - включить настройку "реакции" (2)? \n 7️⃣ - включить настройку "блокировки рекламы" (3)? \n 8️⃣ -включить настройку "плохие слова" (4)? \n *️⃣ - отключить все настройки (0)? **',
                            colour=setx)
            embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
            embed3.set_thumbnail(url=ctx.guild.icon_url)
            embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            message = await ctx.send(embed=embed3)
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
            await message.add_reaction('7️⃣')
            await message.add_reaction('8️⃣')
            await message.add_reaction('*️⃣')
            
            def check(reaction, user):
                return user == ctx.author
            
            reaction = None
            

            while True:
                if str(reaction) == '5️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : settings : additional features are included (1) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : settings : additional features are included (1) :✅")
 
                    print(f"user: {user} : settings : additional features are included (1) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(read_messages = True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (1).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (1).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break
                    
                elif str(reaction) == '6️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : settings : the reaction setting is enabled (2) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : settings : the reaction setting is enabled (2) :✅")
                        
                    print(f"user: {user} : settings : the reaction setting is enabled (2) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(connect = True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (2).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (2).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break

                if str(reaction) == '7️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : the ad blocking setting is enabled (3) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : the ad blocking setting is enabled (3) :✅")
                    print(f"user: {user} : settings : the ad blocking setting is enabled (3) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(read_message_history=True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (3).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (3).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break

                elif str(reaction) == '8️⃣':
                    try:
                        send1 = await user.send(f"user: {user} : settings : bad words setting is enabled (4) :✅")
                    except:
                        send1 = await ctx.send(f"user: {user} : settings : bad words setting is enabled (4) :✅")
                    print(f"user: {user} : settings : bad words setting is enabled (4)")
                    perms = discord.Permissions(send_messages = True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (4).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (4).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break

                if str(reaction) == '*️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : the selection has been restarted - cancel all settings (0) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : the selection has been restarted - cancel all settings (0) :✅")
                        
                    print(f"user: {user} : settings : the selection has been restarted - cancel all settings (0) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(connect=False,read_messages=False,read_message_history=False,send_messages=False)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (0).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "cancel all settings (0).",permissions = perms)
                    try: 
                        await user.channel.purge()
                    except:
                        print("channel()")
                    try: 
                        await user.delete_dm()
                    except:
                        print("del_dm()")
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break


                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
                    
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                        
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                
                    try:
                        await send1.delete()
                    except:
                        print("[-] Error delete mess 1.")
                    try:
                        await send1.delete()
                    except:
                        print("[-] Error delete mess 1.")
                except:
                    pass


        @client.command()
        @commands.cooldown(1, 10, commands.BucketType.user)
        @commands.has_permissions(administrator = True)
        async def settings(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            user = ctx.author.name
            guild = ctx.guild
            embed3 = discord.Embed(title=f' ```settings - настройки``` ',
                            description='** 5️⃣ - включить "дополнительные функции" (1)? \n 6️⃣ - включить настройку "реакции" (2)? \n 7️⃣ - включить настройку "блокировки рекламы" (3)? \n 8️⃣ -включить настройку "плохие слова" (4)? \n *️⃣ - отключить все настройки (0)? **',
                            colour=setx)
            embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
            embed3.set_thumbnail(url=ctx.guild.icon_url)
            embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            message = await ctx.send(embed=embed3)
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
            await message.add_reaction('7️⃣')
            await message.add_reaction('8️⃣')
            await message.add_reaction('*️⃣')
            
            def check(reaction, user):
                return user == ctx.author
            
            reaction = None
            

            while True:
                if str(reaction) == '5️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : settings : additional features are included (1) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : settings : additional features are included (1) :✅")
 
                    print(f"user: {user} : settings : additional features are included (1) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(read_messages = True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (1).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (1).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break
                    
                elif str(reaction) == '6️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : settings : the reaction setting is enabled (2) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : settings : the reaction setting is enabled (2) :✅")
                        
                    print(f"user: {user} : settings : the reaction setting is enabled (2) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(connect = True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (2).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (2).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break

                if str(reaction) == '7️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : the ad blocking setting is enabled (3) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : the ad blocking setting is enabled (3) :✅")
                    print(f"user: {user} : settings : the ad blocking setting is enabled (3) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(read_message_history=True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (3).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (3).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break

                elif str(reaction) == '8️⃣':
                    try:
                        send1 = await user.send(f"user: {user} : settings : bad words setting is enabled (4) :✅")
                    except:
                        send1 = await ctx.send(f"user: {user} : settings : bad words setting is enabled (4) :✅")
                    print(f"user: {user} : settings : bad words setting is enabled (4)")
                    perms = discord.Permissions(send_messages = True)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (4).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "installed updates (4).",permissions = perms)
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break

                if str(reaction) == '*️⃣':
                    try:
                        send2 = await user.send(f"user: {user} : the selection has been restarted - cancel all settings (0) :✅")
                    except:
                        send2 = await ctx.send(f"user: {user} : the selection has been restarted - cancel all settings (0) :✅")
                        
                    print(f"user: {user} : settings : the selection has been restarted - cancel all settings (0) :✅") # Записываем плохое слово в Bad.txt
                    perms = discord.Permissions(connect=False,read_messages=False,read_message_history=False,send_messages=False)
                    try:
                        role = discord.utils.get(ctx.guild.roles, name = "pocket")#через айди будет проще искать
                        await role.edit(reason = "installed updates (0).",permissions = perms)
                    except:
                        role = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                        await role.edit(reason = "cancel all settings (0).",permissions = perms)
                    try: 
                        await user.channel.purge()
                    except:
                        print("channel()")
                    try: 
                        await user.delete_dm()
                    except:
                        print("del_dm()")
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                    break


                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
                    
                    try:
                        await message.remove_reaction(reaction, user)
                    except:
                        print("[-] Error delete reaction.")
                        
                    try:
                        await message.delete()
                    except:
                        print("[-] Error delete mess.")
                
                    try:
                        await send1.delete()
                    except:
                        print("[-] Error delete mess 1.")
                    try:
                        await send1.delete()
                    except:
                        print("[-] Error delete mess 1.")
                except:
                    pass


        @slash.slash(description="18+")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def QRULE34(ctx,text2:str ,text3:str):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if ctx.channel.is_nsfw():
                r34Py = rule34Py()
                search = r34Py.search([text2, text3])
                search3 = str(json.dumps(search[0], default=vars))
                embed = discord.Embed(
                    title="🟢 Online:",
                    description= search3,
                    color=setx
                )
                embed.set_image(url="https://api-cdn.rule34.xxx/images/5708/c6891c23beb17b3805d646f335f26bbc.png")
            else:
                embed = discord.Embed(
                    title=":x: Channel Is Not NSFW",
                    color=setx
                )
                embed.set_image(url="https://media0.giphy.com/media/W5C9c8nqoaDJWh34i6/giphy.gif")

            message = await ctx.send(embed=embed)
            await message.add_reaction('🔷')
            await message.add_reaction('🔶')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🔷':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : post 18+ :✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} :  post 18+ :✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} :  post 18+ :✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🔶':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : post 18+ :❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  post 18+ :❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  post 18+ :❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()


        @slash.slash(description="18+")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def RULE34(ctx,text:str):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if ctx.channel.is_nsfw():
                r34Py = rule34Py()
                result_comments = r34Py.get_comments(4153825)
                result_post = r34Py.get_post(4931536)
                result_pool = r34Py.get_pool(17509)
                result_random = r34Py.random_post([text]) # or r34Py.random_post()
                embed = discord.Embed(
                    title="IMG:",
                    color=setx
                )
                embed.set_image(url=result_random.image)
            else:
                embed = discord.Embed(
                    title=":x: Channel Is Not NSFW",
                    color=setx
                )
                embed.set_image(url="https://media0.giphy.com/media/W5C9c8nqoaDJWh34i6/giphy.gif")

            message = await ctx.send(embed=embed)
            await message.add_reaction('🔷')
            await message.add_reaction('🔶')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🔷':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : post 18+ :✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} :  post 18+ :✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} :  post 18+ :✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🔶':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : post 18+ :❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  post 18+ :❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  post 18+ :❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()

        @slash.slash(description="18+")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def nsfw(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            import aiohttp
            if ctx.channel.is_nsfw():
                embed = discord.Embed(title="18+", colour= setx)  
                async with aiohttp.ClientSession() as cs:
                    async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
                        res = await r.json()
                        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            else:
                embed = discord.Embed(
                    title=":x: Channel Is Not NSFW",
                    color=setx
                )
                embed.set_image(url="https://media0.giphy.com/media/W5C9c8nqoaDJWh34i6/giphy.gif")
            message = await ctx.send(embed=embed)
            await message.add_reaction('🔷')
            await message.add_reaction('🔶')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🔷':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : post 18+ :✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} :  post 18+ :✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} :  post 18+ :✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🔶':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : post 18+ :❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  post 18+ :❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  post 18+ :❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()

        @client.command()
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def qlist(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            guild = ctx.guild
            servers = []
            for guild in client.guilds:
                try:
                    invite = await guild.text_channels[0].create_invite(max_age=3600)
                    servers.append(f"\n ** {guild.name} ** - \n [0] {invite.url} \n")
                except:
                    continue

                
            embed = discord.Embed(title='Servers', description='\n'.join(servers), color=setx)
            await ctx.send(embed=embed)

        @client.command(description='webhook management <partner +>')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def webhook(ctx,url:str=None,name:str=None,mess:str=None,text:str=None):
            if url == None:
                hook = await ctx.channel.create_webhook(name=f"{name}")
            else:
                try:
                    webhooklink = str(url)
                    hook = Webhook(webhooklink.replace("app", ""))
                except:
                    hook = await ctx.channel.create_webhook(name=f"{name}")
                    
                
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            embed3 = discord.Embed(title=f'HOST: {mess}',
                            description= text,
                            colour=setx)
            await hook.send(embed=embed3)
            await hook.delete()
        
        @slash.slash(description="post")
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def webhook(ctx,url:str=None,name:str=None,mess:str=None,text:str=None):
            if url == None:
                hook = await ctx.channel.create_webhook(name=f"{name}")
            else:
                try:
                    webhooklink = str(url)
                    hook = Webhook(webhooklink.replace("app", ""))
                except:
                    hook = await ctx.channel.create_webhook(name=f"{name}")
                    
                
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            await asyncio.sleep(3)
            embed3 = discord.Embed(title=f'HOST: {mess}',
                            description= text,
                            colour=setx)
            await hook.send(embed=embed3)
            await hook.delete()


        @client.command(description='webhook2 management <partner +>')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def webhook2(ctx,url:str=None,name:str=None,text:str=None):
            if url == None:
                hook = await ctx.channel.create_webhook(name=f"{name}")
            else:
                try:
                    webhooklink = str(url)
                    hook = Webhook(webhooklink.replace("app", ""))
                except:
                    hook = await ctx.channel.create_webhook(name=f"{name}")
                    
                
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            await hook.send(text)
            await hook.delete()

        @slash.slash(description="messange")
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def webhook2(ctx,url:str=None,name:str=None,text:str=None):
            if url == None:
                hook = await ctx.channel.create_webhook(name=f"{name}")
            else:
                try:
                    webhooklink = str(url)
                    hook = Webhook(webhooklink.replace("app", ""))
                except:
                    hook = await ctx.channel.create_webhook(name=f"{name}")
                    
                
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            await hook.send(text)
            await hook.delete()
                
        @slash.slash(description="Channel Locked..")
        @commands.has_permissions(administrator = True)
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def lockdown(ctx, member:discord.Member):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            avtorMsg = ctx.author.name
            channel_id = ctx.channel.id
            channel = client.get_channel(channel_id)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = False
            overwrite.connect = False
            overwrite.read_message_history= False
            await channel.set_permissions(member, overwrite=overwrite)
            embed3 = discord.Embed(title=f'HOST: {channel}',
                            description= f'**Channel Locked.**\n USER: {member} \n Profile2: {avtorMsg} \n ``read_message_history = False`` \n ``send_messages = False`` \n ``read_messages = False`` \n ``connect = False`` \n cod: ``{overwrite}`` \n**Reason:** Guild Save Used\n`Please Wait For An Admin/Moderator To Unlock This Channel`',
                            colour=setx)
            embed3.set_thumbnail(url=ctx.guild.icon_url)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await channel.set_permissions(member, overwrite=overwrite)
            await ctx.send(embed=embed3)


        @slash.slash(description="Channel opened..")
        @commands.has_permissions(administrator = True)
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def Unlock(ctx, member:discord.Member):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            avtorMsg = ctx.author.name
            channel_id = ctx.channel.id
            channel = client.get_channel(channel_id)
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = True
            overwrite.read_messages = True
            overwrite.read_message_history= True
            overwrite.connect = True
            await channel.set_permissions(member, overwrite=overwrite)
            embed3 = discord.Embed(title=f'HOST: {channel}',
                            description= f'**The channel is open.**\n USER: {member} \n Profile2: {avtorMsg} \n ``read_message_history = True`` \n ``send_messages = True`` \n ``read_messages = True`` \n ``connect = True`` \n cod: ``{overwrite}`` \n **Reason:** Guild Save Used \n `Please write a report to the user later`',
                            colour=setx)
            embed3.set_thumbnail(url="https://thumbs.gfycat.com/TanFailingCoypu-size_restricted.gif")
            embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed=embed3)

            
        @slash.slash(description="type side of square: ")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def square(ctx, side:int ):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            square = side+side+side+side
            perimeter = side**2
            diagonal = np.sqrt(side**2+side**2)
            emb = discord.Embed(title='информация об квадрате:',color=setx)
            emb.add_field(name="[+]perimeter:",value=square,inline=False)
            emb.add_field(name="[+]square:",value=perimeter,inline=False)
            emb.add_field(name='[+]diagonal:',value=diagonal,inline=False)
            emb.set_thumbnail(url='https://i.gifer.com/8Od7.gif')
            message = await ctx.send(embed = emb)
            await message.add_reaction('♥')
            await message.add_reaction('💔')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '♥':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : square:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : square:✅ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                        print(f"user: {user} : square:✅ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                elif str(reaction) == '💔':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : square:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : square:❌ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                            print(f"user: {user} : square:❌ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
                
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="this software is made to calculate circles (write the radius of the circle:)")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def circle(ctx, r:int):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            from art import tprint
            import math, os
            i = 0
            P = 3.14
            tprint('L=r*p*r')
            L = (P*2*float(r))
            S = (float(r)**2*P)
            emb = discord.Embed(title='информация об круг:',color=setx)
            emb.add_field(name="[+]L:",value=L,inline=False)
            emb.add_field(name="[+]S:",value=S,inline=False)
            emb.set_thumbnail(url='https://i.pinimg.com/originals/b8/13/78/b81378741b6aa6cb222f1404aafa126f.gif')
            message = await ctx.send(embed = emb)
            await message.add_reaction('🍃')
            await message.add_reaction('🍒')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🍃':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : circle:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : circle:✅ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                        print(f"user: {user} : circle:✅ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                elif str(reaction) == '🍒':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : circle:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : circle:❌ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                            print(f"user: {user} : circle:❌ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                    
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="- USER")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def qinfo(ctx,member:discord.Member):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0       
            emb = discord.Embed(title='Информация о пользователе',color=setx)
            emb.add_field(name="Когда присоеденился:",value=member.joined_at,inline=False)
            emb.add_field(name="Имя:",value=member.display_name,inline=False)
            t = member.status
            if t == discord.Status.online:
                d = "✅ В сети"

            t = member.status
            if t == discord.Status.offline:
                d = "🔇 Не в сети"

            t = member.status
            if t == discord.Status.idle:
                d = "💫 Не активен"

            t = member.status
            if t == discord.Status.dnd:
                d = "🕐 Не беспокоить"
            emb.add_field(name="Активность:", value=d,inline=False)
            emb.add_field(name="Статус:", value=member.activity,inline=False)
            emb.add_field(name="Роль на сервере:", value=str(member.top_role.mention),inline=False)
            emb.add_field(name='Айди',value=member.id,inline=False)
            emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            message = await ctx.send(embed = emb)
            await message.add_reaction('🍸')
            await message.add_reaction('🍷')
            def check(reaction, user):
                return user == ctx.author

            reaction = None

            while True:
                if str(reaction) == '🍸':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : qinfo:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : qinfo:✅ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                        print(f"user: {user} : qinfo:✅ >> {i} 📈" )# Записываем плохое слово в Bad.txt               
                elif str(reaction) == '🍷':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : qinfo:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : qinfo:❌ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                            print(f"user: {user} : qinfo:❌ >> {i} 📈" )# Записываем плохое слово в Bad.txt
                    
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
            file1.close()
        @slash.slash(description="- list")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def qlvlup(ctx):
            message = await ctx.send(file=discord.File('Up_lvl.txt'))
            await asyncio.sleep(30)
            await ctx.channel.purge(2)
            
        @slash.slash(description="- list")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def qinvite(ctx):
            i = 0
            message = await ctx.send(file=discord.File('Invite.txt'))
            await message.add_reaction('🏳')
            await message.add_reaction('🏴')
            def check(reaction, user):
                return user == ctx.author

            reaction = None

            while True:
                if str(reaction) == '🏳':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : desk (invite):✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : desk (invite):✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : desk (invite):✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🏴':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : desk (invite):❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : desk (invite):❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : desk (invite):❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="history")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def history(ctx):
            i = 0
            message = await ctx.send(file=discord.File('Massage.txt'))
            await message.add_reaction('🌕')
            await message.add_reaction('🌑')
            def check(reaction, user):
                return user == ctx.author

            reaction = None

            while True:
                if str(reaction) == '🌕':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : history:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : history:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : history:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🌑':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : history:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : history:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : history:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()        
        @slash.slash(description='customkey')
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def customkey(ctx, key, number, length, url = None):
            i = 0
            chars = str(key)
            number = int(number)
            length = int(length)
            for n in range(number):
                password =''
                for i in range(length):
                    password += random.choice(chars)
                with open("keygetp.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8
                    if url == None:
                        logmsg.write(password + "\n") # Записываем плохое слово в Bad.txt        message = await ctx.send(file=discord.File('Massage.txt'))
                    else:
                        logmsg.write(url + password + "\n")
            message = await ctx.send(file=discord.File('keygetp.txt'))
            await message.add_reaction('🔥')
            await message.add_reaction('❄')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🔥':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : customkey:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : customkey:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : customkey:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '❄':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : customkey:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : customkey:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : customkey:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await asyncio.sleep(25)
            os.remove("keygetp.txt")
            await message.delete()
        @slash.slash(description="bad_word2")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def bad_word(ctx):
            i = 0
            message = await ctx.send(file=discord.File('Bad word2.txt'))
            await message.add_reaction('🏔')
            await message.add_reaction('🗻')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🏔':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : bad_word:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : bad_word:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : bad_word:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🗻':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : bad_word:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : bad_word:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : bad_word:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="turn off the bot on the server")
        async def alert(ctx,ids):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            fp = open("ID-admin.txt", "+a")
            with open("ID-admin.txt", "r") as file1:
                    # итерация по строкам
                for line in file1:
                    print("ID:" + str(ctx.author.id) + " ID:" + str(line.strip()))                                                                                                                                                                        
                    if str(ctx.author.id) == str(line.strip()):
                        if ids is None:
                            await ctx.send(f'{error_emoji} **Пожалуйста, укажите id_server``!** {error_emoji}')
                        else:
                            with open("ID-server.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                                logmsg.write(str(ids) + f"\n")
                            channel_id = 1046478086188826725
                            channel = client.get_channel(channel_id)
                            print(f"command: Channel Locked.")
                            embed3 = discord.Embed(title=f'**Bihazard: **',
                                    description= f'**The problems were broken:**\n blocked ID: #{ids} \n ADMIN: @{ctx.author.name} @{ctx.author.nick} \n Profile: ``@{user}`` \n ``BAN = True`` \n ``closing chats = True`` \n ``connect = False`` \n**Reason:** Guild Save Used\n`Please Wait For An Admin/Moderator To Unlock This Channel`\n **Conclusion:** ``search in history.``.',
                                    colour=setx)
                            embed3.set_thumbnail(url="https://images.mysafetylabels.com/img/lg/L/biological-hazard-ansi-caution-label-lb-2249.png")
                            await channel.send(embed=embed3)
                            await ctx.send(embed=embed3)
                    else:
                            embed3 = discord.Embed(title=f'**Bihazard: **',
                                    description= f'``#you dont have the rights to send an attack``',
                                    colour=setx)
                            embed3.set_thumbnail(url="https://images.mysafetylabels.com/img/lg/L/biological-hazard-ansi-caution-label-lb-2249.png")
                            await ctx.send(embed=embed3)
            
        @slash.slash(description="json")
        async def img(ctx,url):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            emb = discord.Embed(title = "Picture -> \n картинка:", colour=setx)
            emb.set_image(url = url)
            message = await ctx.send(embed = emb) 
            await message.add_reaction('✔')
            await message.add_reaction('⭕')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '✔':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : img:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : img:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : img:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '⭕':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : img:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : img:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : img:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="json2")          
        async def img2(ctx,url):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            response = requests.get(url) # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON
            embed = discord.Embed(color = setx, title = 'Picture -> \n картинка:') # Создание Embed'a
            embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
            message = await ctx.send(embed = embed) 
            await message.add_reaction('🟩')
            await message.add_reaction('🟥')        
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '🟩':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : img2:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : img2:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : img2:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🟥':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : img2:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : img2:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : img2:❌  >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break


            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="search +h +m +l +i +p")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def search(ctx,word:str,status:str):
            if status == "h":
                file1 = open( "Massage.txt", "r")
            if status == "m":
                file1 = open( "Bad word2.txt", "r")
            if status == "l":
                file1 = open( "Invite.txt", "r")
            if status == "i":
                file1 = open( "Up_lvl.txt", "r")
            if status == "p":
                file1 = open( "prefix.txt", "r")
            i = 0
            txt = file1.readlines()
            print(txt)
            string = word
            for text in txt:
                regex = re.compile(string)
                match = re.search(regex, text)
                if match:
                    with open("file.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(' Found "{}" in "{}"'.format(string, text)) # Записываем плохое слово в Bad.txt
                        text_pos = match.span()
                        logmsg.write(text[match.start():match.end()]) # Записываем плохое слово в Bad.txt
            message = await ctx.send(file=discord.File('file.txt'))
            await message.add_reaction('➕')
            await message.add_reaction('➖')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '➕':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : search:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : search:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : search:✅  >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '➖':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : search:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : search:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : search:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await asyncio.sleep(90)
            await message.delete()
            await asyncio.sleep(90)
            os.remove("file.txt")
            file1.close()
        @slash.slash(description="qhelp")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def qhelp(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            embed = discord.Embed(color=setx, title=f'Commands:', description= "``/square `` - write the properties of a square -> \n написать свойства квадрата \n ``/circle `` - write circle properties -> \n написать свойства круга \n ``/cl_lvlup `` - clear the level -> \n очистить уровень \n ``/cl_bad_word2`` - clear the blacklist -> \n очистить черный список \n ``/cl_history `` - clear history -> \n очистить историю \n ``/cl_index`` - clear the index -> \n очистить индекс \n  ``/qrule34 `` - content for 18+ -> \n контент для 18+ \n  ``/rule34 `` - content for 18+ -> \n контент для 18+ \n ``/nsfw `` - content for 18+ -> \n контент для 18+ \n ``/webhook /webhook2  `` - webhook management -> \n управление веб-перехватчиками \n ``/changestatus  `` - change the status of the bot -> \n изменить статус бота \n  ``/qlvlup  `` - viewing the level of posts. -> \n просмотр уровня постов. \n  ``/qinvite `` - a sheet for checking invites. -> \n лист для проверки приглашений. \n  ``/search`` - search in history. -> \n поиск в истории \n ``/avatar`` - Shows you a users profile picture. -> \n Показывает изображение профиля пользователя \n ``/qhelp`` - Shows you a help embed. -> \n Показывает вам встроенную справку \n``/post`` - publish a post -> \n опубликовать пост \n``📝 /info`` - Shows useful server information.  -> \n полезная информация о сервере. \n``/invite`` - Shows you a list of server invitations  -> \n показывает вам список приглашений на сервер \n``/qinfo`` - Shows you useful information about a user  -> \n показывает полезную информацию о пользователе. \n``/write_prefix`` - new prefix for staff command.  -> \n новый префикс для штабной команды. \n``/dm /tpsend`` - for a personal chat.  -> \nдля личного чата. \n``/qnick`` - quickly change the nickname on the server.  -> \n быстро сменить никнейм на сервере. \n``/report`` - Shows you useful information about a user.  -> \n показывает полезную информацию о пользователе. \n``/clear`` - clear the entire chat in 5-10 seconds.  -> \n счистить весь чат за 5-10 секунд. \n``/qchannel`` - create a new chat.  -> \n создать новый чат. \n``/ban`` - Bans a member.  -> \n создать новый чат. \n``/clears`` - Clears the community from the user.  -> \n счищает сообщество от пользователя. \n``/lockdown`` - Kicks a member.  -> \n закрыть чат для пользователя \n``/unlock`` - Unbans a member.  -> \n открыть чат для пользователя \n``/qchdel`` - isolation channel. -> \n удалить канал. \n ``/remove`` - remove a role from a user. ->\n удалить роль пользователя. \n ``/browser`` - search for information on a subject.  -> \n поиск информации по теме. \n")
            embed.add_field(name='Add to your server -> \n Добавить на свой сервер', value='[⌨](https://discord.com/api/oauth2/authorize?client_id=1020080505384873984&permissions=8&scope=bot%20applications.commands)', inline=False)
            embed.add_field(name='Official bot server -> \n Официальный бот-сервер:', value='[🎛](https://discord.gg/5zRq8kux96)', inline=False)
            embed.add_field(name=' Developer Terms of Service -> \n Условия использования для разработчиков:', value='[🔍](https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service)', inline=False)
            embed.add_field(name=' Discord Developer Policy -> \n Политика Discord для разработчиков:', value='[📋](https://discord.com/developers/docs/policies-and-agreements/developer-policy)', inline=False)
            embed.add_field(name=' Learn more about bot users -> \n Узнайте больше о пользователях-ботах:', value='[📦](https://discord.com/developers/docs/topics/oauth2#bots)', inline=False)
            embed.add_field(name='  𝙢𝙮 𝙘𝙧𝙚𝙖𝙩𝙤𝙧 ', value='[💎](https://discord-tracker.ru/tracker/user/931586817713668177/)', inline=False)
            ping_ = client.latency
            ping = round(ping_ * 1000)
            
            i = 0
            n = 0
                
            embed.add_field(name=f"my ping - мой пинг:", value=f'[{ping}ms 🕐](https://yandex.ru/time?ysclid=l9rqar6ovg84234744)', inline=False)

            embed.set_thumbnail(url="https://cdn.dribbble.com/users/68238/screenshots/5788547/banksy.gif")
            message = await ctx.send(embed=embed)
            await message.add_reaction('🟢')
            await message.add_reaction('🔴')
            def check(reaction, user):
                return user == ctx.author

            reaction = None

            while True:
                if str(reaction) == '🟢':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : help:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : help:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : help:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🔴':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : help:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : help:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : help:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break


            
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
        @slash.slash(description="cat")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def cat(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON
            embed = discord.Embed(color = setx, title = 'Cat: -> \n Кот:') # Создание Embed'a
            embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
            message = await ctx.send(embed = embed) 
            await message.add_reaction('🔆')
            await message.add_reaction('🔅')
            def check(reaction, user):
                return user == ctx.author

            reaction = None

            while True:
                if str(reaction) == '🔆':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : cat:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : cat:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : cat:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🔅':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : cat:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  cat:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  cat:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break



            
            await asyncio.sleep(1800)
            await send1.delete()
            await send2.delete()
            await message.delete()
        @slash.slash(description="dog")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def dog(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON
            embed = discord.Embed(color = setx, title = 'Dog: -> \n Собака:') # Создание Embed'a
            embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
            message = await ctx.send(embed = embed)
            await message.add_reaction('▫')
            await message.add_reaction('🎈')
            
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '▫':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : dog:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} :  dog:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} :  dog:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '🎈':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : dog:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  dog:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  dog:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break


            await asyncio.sleep(1800)
            await send1.delete()
            await send2.delete()
            await message.delete()
        @slash.slash(description="fox")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def fox(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
            json_data = json.loads(response.text) # Извлекаем JSON
            embed = discord.Embed(color = setx, title = 'Fox: -> \n Лис:') # Создание Embed'a
            embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
            message = await ctx.send(embed = embed)
            await message.add_reaction('💹')
            await message.add_reaction('〽')
            
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '💹':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : fox:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : fox:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} : fox:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '〽':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : fox:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  fox:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  fox:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break


            
            await asyncio.sleep(1800)
            await send1.delete()
            await send2.delete()
            await message.delete()
        @slash.slash(description="nick")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def qnick(ctx, member: discord.Member, nick):
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            else:
                await member.edit(nick=nick)
                await ctx.send(f'nickname was changed for {member.mention} -> \n псевдоним был изменен для {member.mention}')
        @client.event
        async def on_message(payload):
            winsound.Beep(frequency2, duration2)
            if payload.user_id != None:
                channel = client.get_channel(payload.channel_id)
                if channel is None: # checking if we are in a DM channel
                    channel = discord.utils.get(client.private_channels, id=payload.channel_id)
                    

        @client.event
        async def on_raw_reaction_add(payload):
            try:
                emoji = payload.emoji # реакция пользователя
                print("emoji_name:", str(emoji))
            except:
                print("emoji_name: [fail1]")
            #await asyncio.sleep(280)
            #try:
            # Получение реакции на сообщение
            guild = client.get_guild(payload.guild_id)
            message_id = payload.message_id # ID сообщения
            channel_id = payload.channel_id # ID канала
            channel = client.get_channel(channel_id) # Получаем канал
            message = await channel.fetch_message(message_id) # Получаем сообщение
            user = message.author
            try:
                emoji = await payload.fetch_message(payload.emoji)
                print("emoji_name:", str(emoji))
            except:
                print("emoji_name: [fail2]")
                
                
            try:
                role = discord.utils.get(message.guild.roles, name = "plugin")#через айди будет проще искать
            except:
                print("return ...")
            perms = discord.Permissions(read_messages = True)
            try:
                nk = role.permissions
            except:
                nk = None
            print(nk," + ",perms)
            try:
                if nk == perms:
                    print("True +")
                    return()
                else:
                    print("False -")

                    try:
                        add_role = [role for role in channel.changed_roles if role.name == emoji]
                        await user.add_roles(add_role[0])
                    except:
                        print("role: [fail 1]")
                    try:
                        add_role = [role for role in channel.changed_roles if role.name == emoji]
                        await client.add_roles(user, add_role[0])
                    except:
                        print("role: [fail 2]")
                    try:
                        role = discord.utils.get(user.server.roles, name == emoji)
                        await user.add_roles(role)
                    except:
                        print("role: [fail 3]")
                    try:
                        role_1 = user.guild.get_role(emoji)
                        await user.add_roles(role_1)
                    except:
                        print("role: [fail 4]")
                        
                    try:
                        role = discord.utils.get(user.server.roles, name == emoji)
                        await client.add_roles(user,role)
                    except:
                        print("role: [fail 5]")
                    try:
                        role_1 = user.guild.get_role(emoji)
                        await client.add_roles(user,role_1)
                    except:
                        print("role: [fail 6]")
                        
                    try:
                        emoji = await channel.fetch_message(payload.emoji)
                        print("emoji:", str(emoji))
                    except:
                        print("emoji: [fail 2]")
                        
                    try:
                        emoji = await message.fetch_message(payload.emoji)
                        print("emoji:", str(emoji))
                    except:
                        print("emoji: [fail 3]")
                        
                    try:
                        emoji = await payload.fetch_message(payload.emoji)
                        print("emoji:", str(emoji))
                    except:
                        print("emoji: [fail 4]")
                    
                    try:
                        await message.add_reaction(str(emoji))
                        print("add reaction ", str(emoji))
                    except:
                        print("add reaction [fail1]")

                    try:
                        await payload.add_reaction(str(emoji))
                        print("add reaction ", str(emoji))
                    except:
                        print("add reaction [fail2]")
                        
                    try:
                        emoji = await channel.add_reaction(str(emoji))
                        print("add reaction", str(emoji))
                    except:
                        print("add reaction [fail3]")
            except:
                print("Error - + ")

        @client.event
        async def on_message(message):
            winsound.Beep(frequency2, duration2)
            if message.author == client.user:
                return
            if message.content.startswith("register"):
                if isinstance(message.channel, discord.DMChannel):
                  await message.author.send("registration mode coming soon!")
                
            if message.content.startswith("$ok"):
                on_member_join()

                
        @slash.slash(description="channel delete?")
        @commands.has_permissions(administrator = True)
        @commands.cooldown(1, 15, commands.BucketType.user)
        async def qchdel(message,seconds:int):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            channel_id = message.channel.id
            avtorMsg = message.author.name
            channel = client.get_channel(channel_id)
            inf2 = discord.Embed(
                color = setx,
                title=f"CHANNEL DELET >> Time: {seconds} -> \n КАНАЛ УДАЛИТЬ >> Время: {seconds} ",
                description= channel_id,
            )
            inf2.set_image(url="https://media2.giphy.com/media/44y8gMkXosEm4qvRtF/giphy.gif?cid=790b7611ea3803295fbcd9407d7976ff88543e414e83d7d5&rid=giphy.gif&ct=g")
            await channel.send(embed=inf2)
            await asyncio.sleep(int(seconds))
            await channel.delete(reason=" {avtorMsg}: delet channel :{channel_id}")
            channel_id = 1038582736266461194
            channel = client.get_channel(channel_id)
            inf = discord.Embed(
                color = setx,
                title=f"{avtorMsg} >> delet channel",
                description= channel_id,
            )
            await channel.send(embed=inf)
            
    # -------------------------------------------------------------------------------------------------------    

        @slash.slash(name='post')
        @commands.cooldown(1, 15, commands.BucketType.user)
        #@commands.has_permissions(administrator=True)
        async def post(ctx, arg):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            user = ctx.author.name
            embed3 = discord.Embed(title=f' ```{arg}``` ',
                            description='***Для того чтобы принять учатие в Host используйте реакцию ниже:***',
                            colour=setx)
            embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
            embed3.set_thumbnail(url=ctx.guild.icon_url)
            embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            message = await ctx.send(embed=embed3)
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '✅':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : post:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} :  post:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                        print(f"user: {user} :  post:✅ >> {i} 📉") # Записываем плохое слово в Bad.txt
                elif str(reaction) == '❌':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : post:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  post:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  post:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
    # -------------------------------------------------------------------------------------------------------

        @slash.slash(description='tpsend')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def tpsend(ctx, member: discord.Member, arg):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            else:
                user = ctx.author.name
                embed3 = discord.Embed(title=f'user: {user} >>> send: { member.name } ',
                                description=f'**loading...**',
                                colour=setx)
                embed3.set_image(url="https://media2.giphy.com/media/44y8gMkXosEm4qvRtF/giphy.gif?cid=790b7611ea3803295fbcd9407d7976ff88543e414e83d7d5&rid=giphy.gif&ct=g")
                embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                embed3.set_thumbnail(url=ctx.guild.icon_url)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                send1 = await ctx.send(embed=embed3)
                embed3 = discord.Embed(title=f'user: {user} >>> send: { member.name } ',
                                description=f'{arg}',
                                colour=setx)
                embed3.set_image(url="https://media2.giphy.com/media/44y8gMkXosEm4qvRtF/giphy.gif?cid=790b7611ea3803295fbcd9407d7976ff88543e414e83d7d5&rid=giphy.gif&ct=g")
                embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                embed3.set_thumbnail(url=ctx.guild.icon_url)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                send2 = await member.send(embed=embed3)
                await asyncio.sleep(3)
                await send1.delete()
                await asyncio.sleep(1800)
                await send2.delete()
            
        @slash.slash(name='qget', description='tp-role')
        @commands.cooldown(1, 25, commands.BucketType.user)
        #@commands.has_permissions(administrator=True)
        async def qget(ctx, member: discord.Member, qid):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите ``member``!** {error_emoji}')
            else:
                if qid is None:
                    await ctx.send(f'{error_emoji} **Пожалуйста, укажите ``qid``!** {error_emoji}')
                else:
                    role_1 = member.guild.get_role(int(qid))# ади роли которую будет получать юзер
                    await member.add_roles(role_1)
                    channel_id = 1038582736266461194
                    channel = client.get_channel(channel_id)
                    inf = discord.Embed(
                        color = setx,
                        title=f"{member} >>> get : {role_1}",
                        description= role_1,
                    )
                    await ctx.send(embed=inf)
                    await channel.send(embed=inf)
            
        @slash.slash(description='tp-role')
        @commands.cooldown(1, 25, commands.BucketType.user)
        #@commands.has_permissions(administrator=True)        
        async def get(ctx, role: discord.Role, member: discord.Member):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите ``member``!** {error_emoji}')
            else:
                if role is None:
                    await ctx.send(f'{error_emoji} **Пожалуйста, укажите ``role``!** {error_emoji}')
                else:
                    await member.add_roles(role)
                    channel_id = 1038582736266461194
                    channel = client.get_channel(channel_id)
                    inf = discord.Embed(
                        color = setx,
                        title=f"{member} >>> get : {role}",
                        description= role,
                    )
                    await ctx.send(embed=inf)


        @slash.slash(description='ban')
        @commands.has_permissions(ban_members=True)
        @commands.has_permissions(administrator=True) 
        async def ban(ctx, member: discord.Member, days=None, arg=None):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            else:
                try:
                    await ctx.guild.ban(member, delete_message_days=0)
                    await ctx.send('User banned for **' + str(days) + ' day(s)**')
                    channel_id = 1038582736266461194
                    channel = client.get_channel(channel_id)
                    embed3 = discord.Embed(
                        color = setx,
                        title=f"banned >>> {member}",
                        description=f"{member} : {arg} : {days}"
                    )
                    embed3.set_image(url="https://i.imgur.com/O3DHIA5.gif")
                    embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                    embed3.set_thumbnail(url=ctx.guild.icon_url)
                    embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                    embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await channel.send(embed=embed3)
                    ban_list.append(member)
                    day_list.append(days * 24 * 60 * 60)
                    server_list.append(ctx.message.server)
                    
                except:
                    await ctx.send('error! user not active')
                await client.kick_chat_member(member.from_user.id)
                await member.send(f"user: {member} >>> {arg} ")
                await message.reply_to_message.reply("users заблокирован")

        @slash.slash(name='report')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def report(ctx, member: discord.Member, arg=None):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            else:
                i = 0
                await ctx.send(f'report: >>> {member} >>> {arg}.')
                embed3 = discord.Embed(
                    color = setx,
                    title=f"report:❓ >>> {member}",
                    description=f' ```{arg}``` '
                )
                embed3.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
                embed3.set_thumbnail(url=ctx.guild.icon_url)
                embed3.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                message = await ctx.send(embed=embed3)
                await message.add_reaction('📈')
                await message.add_reaction('📉')

                def check(reaction, user):
                    return user == ctx.author

                reaction = None

                while True:
                    if str(reaction) == '📈':
                        i = i + 1
                        send2 = await ctx.send(f"user: {user} : report:📈 >>> {member} >> {i} 📈")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} :  report:📈  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} :  report:📈  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            await ctx.channel.create_thread()
                    elif str(reaction) == '📉':
                        i = i - 1
                        send1 = await ctx.send(f"user: {user} : report:📉 >>> {member} >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : report:📉  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : report:📉  >> {i} 📉") # Записываем плохое слово в Bad.txt
                            await ctx.channel.create_thread()
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                        await message.remove_reaction(reaction, user)
                    except:
                        break

                await asyncio.sleep(300)
                await send2.delete()
                await send1.delete()
                await message.delete()
                if i > 3:
                    overwrite = discord.PermissionOverwrite()
                    overwrite.send_messages = False
                    overwrite.read_messages = False
                    overwrite.connect = False
                    await ctx.set_permissions(message.author, overwrite=overwrite)
                    embed3 = discord.Embed(title=f'HOST: {ctx.channel.name}',
                                    description= f'**Channel Locked.**\n USER: {member} : {user} \n ``send_messages = False`` \n ``read_messages = False`` \n ``connect = False`` \n cod: ``{overwrite}`` \n**Reason:** Guild Save Used\n`Please Wait For An Admin/Moderator To Unlock This Channel`',
                                    colour=setx)
                    await ctx.send(embed=embed3)
                    await member.send(f"user: {user} : report:📉 >>> have been banned >> {member} >> {i} 📉")
                else:
                    await ctx.channel.purge()
                    await user.send(f"user: {user} : report:📉 >>> cancellation >> {member} >> {i} 📉")
        @client.event
        async def on_ready():
            now_time = nd.strftime(">> %H:%M:%S >>") #Импорт времени с часами, минутами, секундами.
            date_dm = nd.strftime(" - %d.%m.%y %b -") #Дата с изменёным стилем
            print("\033[1;32m >> Channel >>" + " SYSTEM:✟ℂℂ𝕋𝕍✞ " + (now_time))
            print("\033[1;32m Bot has successfully logged in as: {}".format(client.user))
            print("\033[1;32m Bot ID: {}\n".format(client.user.id))
            winsound.Beep(frequency2, duration2)
            print("[+] the system is restarted...") 
            printer.start()
            
        @slash.slash(description="avatar")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def user(ctx, member: discord.Member):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member == None:#если не упоминать участника тогда выводит аватар автора сообщения
                member = ctx.author
            embed = discord.Embed(color = setx, title = f"Аватар участника - {member.name}", description = f"[Download]({member.avatar_url})")
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)

        @client.event
        async def on_guild_join(guild):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            print("==============================================")
            print("[GUILD]   Бот присоединился к серверу!          ")
            print("[GUILD]   Информация о сервере                  ")
            print("==============================================")
            print(f'[GUILD]  Сервер           - {guild.name}       ')
            print(f'[GUILD]  Владелец сервера - {guild.owner}      ')
            print(f'[GUILD]  ID бота          - {guild.id}         ')
            print(f'[GUILD]  Расположение сервер - {guild.region}  ')
            print("==============================================")
            print(" ")
            overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False,read_message_history=False,connect = False),
            guild.me: discord.PermissionOverwrite(read_messages=True,read_message_history=True,connect = True,send_messages =True)
            }
            try:
                channel2 = discord.utils.get(guild.channel, name = "✟ℂℂ𝕋𝕍✞")
            except:
                channel2 = await guild.create_text_channel(f"✟ℂℂ𝕋𝕍✞", lveres=overwrites, position = 1)
            perms = discord.Permissions(connect=False,read_messages=False,read_message_history=False,send_messages=False)
            try:
                rolep = discord.utils.get(guild.roles, name = "pocket")#через айди будет проще искать
                try:
                    rolep_id = rolep.id
                except:
                    rolep_id = None
            except:
                rolep = await guild.create_role(name= "pocket", permissions=perms, color = setx)
                await rolep.edit(reason = "cancel all settings (0).",permissions = perms)
                try:
                    rolep_id = rolep.id
                except:
                    rolep_id = None
            try:
                perms = discord.Permissions(send_messages=False,read_message_history=False,read_messages=False,administrator = False,connect = False)
                try:
                    role1 = discord.utils.get(guild.roles, name = "Мут")
                except:
                    role1 = await guild.create_role(name=f"Мут", permissions=perms, color = setx)
                role1_id = role1.id
            except:
                role1 = None
                role1_id = role1
            try:
                perms = discord.Permissions(administrator = True,send_messages= True,read_message_history=True,connect = True,read_messages=True)
                try:
                    role2 = discord.utils.get(guild.roles, name = "admin")
                except:
                    role2 = await guild.create_role(name=f"admin", permissions=perms, color = setx)
                role2_id = role2.id
            except:
                role2 = None
                role2_id = role2
            now_times = nd.strftime(" = %H : %M : %S = ") #Время с изменёным стилем
            date_dm = nd.strftime(" - %d.%m.%y %b -") #Дата с изменёным стилем
            embed2 = discord.Embed(color = setx, title = f"✟ℂℂ𝕋𝕍✞ присоединился к серверу {guild.name}")
            embed2.add_field(name='ADMIN: ', value=f"\nIDKey: {role2_id} \n IDBAN: {role1_id} \n ID plugin - {rolep_id} \n ID бота - {guild.id} \n")
            embed2.add_field(name='INFO: ', value=f"\nСервер - {guild.name} \n ID - {guild.id} \n Owner - {guild.owner} \n Disk - {guild.region} \n")
            embed2.add_field(name='Сhannel: ', value=f"\n [overwrites] {overwrites} \n [channel] {channel2} \n [color] {setx} \n")
            embed2.add_field(name='BOT: ', value=f"\n [perms] {perms} \n [channel] {channel2} \n [color] {setx} \n")
            try:
                embed.set_thumbnail(url=guild.icon_url)
            except:
                print("err [photo]")
            await channel2.send(embed=embed2)
            try:
                channel_id = 1038582736266461194
                channel = client.get_channel(channel_id) 
                await channel.send(embed=embed2)
            except:
                print("Err404")
            embed = discord.Embed(color=setx, title=f'Commands:', description= "``/square `` - write the properties of a square -> \n написать свойства квадрата \n ``/circle `` - write circle properties -> \n написать свойства круга \n ``/cl_lvlup `` - clear the level -> \n очистить уровень \n ``/cl_bad_word2`` - clear the blacklist -> \n очистить черный список \n ``/cl_history `` - clear history -> \n очистить историю \n ``/cl_index`` - clear the index -> \n очистить индекс \n  ``/qrule34 `` - content for 18+ -> \n контент для 18+ \n  ``/rule34 `` - content for 18+ -> \n контент для 18+ \n ``/nsfw `` - content for 18+ -> \n контент для 18+ \n ``/webhook /webhook2  `` - webhook management -> \n управление веб-перехватчиками \n ``/changestatus  `` - change the status of the bot -> \n изменить статус бота \n  ``/qlvlup  `` - viewing the level of posts. -> \n просмотр уровня постов. \n  ``/qinvite `` - a sheet for checking invites. -> \n лист для проверки приглашений. \n  ``/search`` - search in history. -> \n поиск в истории \n ``/avatar`` - Shows you a users profile picture. -> \n Показывает изображение профиля пользователя \n ``/qhelp`` - Shows you a help embed. -> \n Показывает вам встроенную справку \n``/post`` - publish a post -> \n опубликовать пост \n``📝 /info`` - Shows useful server information.  -> \n полезная информация о сервере. \n``/invite`` - Shows you a list of server invitations  -> \n показывает вам список приглашений на сервер \n``/qinfo`` - Shows you useful information about a user  -> \n показывает полезную информацию о пользователе. \n``/write_prefix`` - new prefix for staff command.  -> \n новый префикс для штабной команды. \n``/dm /tpsend`` - for a personal chat.  -> \nдля личного чата. \n``/qnick`` - quickly change the nickname on the server.  -> \n быстро сменить никнейм на сервере. \n``/report`` - Shows you useful information about a user.  -> \n показывает полезную информацию о пользователе. \n``/clear`` - clear the entire chat in 5-10 seconds.  -> \n счистить весь чат за 5-10 секунд. \n``/qchannel`` - create a new chat.  -> \n создать новый чат. \n``/ban`` - Bans a member.  -> \n создать новый чат. \n``/clears`` - Clears the community from the user.  -> \n счищает сообщество от пользователя. \n``/lockdown`` - Kicks a member.  -> \n закрыть чат для пользователя \n``/unlock`` - Unbans a member.  -> \n открыть чат для пользователя \n``/qchdel`` - isolation channel. -> \n удалить канал. \n ``/remove`` - remove a role from a user. ->\n удалить роль пользователя. \n ``/browser`` - search for information on a subject.  -> \n поиск информации по теме. \n")
            embed.add_field(name='Add to your server -> \n Добавить на свой сервер', value='[⌨](https://discord.com/api/oauth2/authorize?client_id=1020080505384873984&permissions=8&scope=bot%20applications.commands)', inline=False)
            embed.add_field(name='Official bot server -> \n Официальный бот-сервер:', value='[🎛](https://discord.gg/5zRq8kux96)', inline=False)
            embed.add_field(name=' Developer Terms of Service -> \n Условия использования для разработчиков:', value='[🔍](https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service)', inline=False)
            embed.add_field(name=' Discord Developer Policy -> \n Политика Discord для разработчиков:', value='[📋](https://discord.com/developers/docs/policies-and-agreements/developer-policy)', inline=False)
            embed.add_field(name=' Learn more about bot users -> \n Узнайте больше о пользователях-ботах:', value='[📦](https://discord.com/developers/docs/topics/oauth2#bots)', inline=False)
            embed.add_field(name='  𝙢𝙮 𝙘𝙧𝙚𝙖𝙩𝙤𝙧 ', value='[💎](https://discord-tracker.ru/tracker/user/931586817713668177/)', inline=False)
            ping_ = client.latency
            ping = round(ping_ * 1000)
            
            i = 0
            n = 0
                
            embed.add_field(name=f"my ping - мой пинг:", value=f'[{ping}ms 🕐](https://yandex.ru/time?ysclid=l9rqar6ovg84234744)', inline=False)
                    
            try:
                embed.set_thumbnail(url=guild.icon_url)
            except:
                print("err [photo]")
            await channel2.send(embed=embed)
            
            embed2 = discord.Embed(color=setx, title=f'**did you have a problem? -> \n у вас была проблема? : prefix = $.**', description= "You can turn on the desired settings, write : ``/settings`` \n Вы можете включить нужные настройки, напишите : ``/settings``. \n ")
            await channel2.send(embed=embed2)
            
        @tasks.loop(seconds=12.0) #Создаем повторную типо исполнение указываем seconds=12.0 либо можно minutes=12 ну как то так
        async def printer():
                nds = datetime.datetime.now()
                now_time = nds.strftime(" = %H:%M:%S =")
                await client.change_presence(activity = discord.Activity( type=discord.ActivityType.watching, name = f"Update: {now_time}" ))
                await asyncio.sleep(120)
                await client.change_presence(status = discord.Status.idle,activity = discord.Game (type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))
                await asyncio.sleep(120)
        class MyBot(Bot):

            async def connect(self, *, reconnect: bool = True) -> None:
                print("  [-] plug-ins are enabled (2)")  
                """|coro|

                Creates a websocket connection and lets the websocket listen
                to messages from Discord. This is a loop that runs the entire
                event system and miscellaneous aspects of the library. Control
                is not resumed until the WebSocket connection is terminated.

                Parameters
                -----------
                reconnect: :class:`bool`
                    If we should attempt reconnecting, either due to internet
                    failure or a specific failure on Discord's part. Certain
                    disconnects that lead to bad state will not be handled (such as
                    invalid sharding payloads or bad tokens).

                Raises
                -------
                :exc:`.GatewayNotFound`
                    If the gateway to connect to Discord is not found. Usually if this
                    is thrown then there is a Discord API outage.
                :exc:`.ConnectionClosed`
                    The websocket connection has been terminated.
                """

                backoff = discord.client.ExponentialBackoff()
                ws_params = {
                    'initial': True,
                    'shard_id': self.shard_id,
                }
                while not self.is_closed():
                    try:
                        coro = MyGateway.from_client(self, **ws_params)
                        self.ws = await asyncio.wait_for(coro, timeout=60.0)
                        ws_params['initial'] = False
                        while True:
                            await self.ws.poll_event()
                    except discord.client.ReconnectWebSocket as e:
                        _log.info('Got a request to %s the websocket.', e.op)
                        self.dispatch('disconnect')
                        ws_params.update(sequence=self.ws.sequence, resume=e.resume, session=self.ws.session_id)
                        continue
                    except (OSError,
                            discord.HTTPException,
                            discord.GatewayNotFound,
                            discord.ConnectionClosed,
                            aiohttp.ClientError,
                            asyncio.TimeoutError) as exc:

                        self.dispatch('disconnect')
                        if not reconnect:
                            await self.close()
                            if isinstance(exc, discord.ConnectionClosed) and exc.code == 1000:
                                # clean close, don't re-raise this
                                return
                            raise

                        if self.is_closed():
                            return

                        # If we get connection reset by peer then try to RESUME
                        if isinstance(exc, OSError) and exc.errno in (54, 10054):
                            ws_params.update(sequence=self.ws.sequence, initial=False, resume=True, session=self.ws.session_id)
                            continue

                        # We should only get this when an unhandled close code happens,
                        # such as a clean disconnect (1000) or a bad state (bad token, no sharding, etc)
                        # sometimes, discord sends us 1000 for unknown reasons so we should reconnect
                        # regardless and rely on is_closed instead
                        if isinstance(exc, discord.ConnectionClosed):
                            if exc.code == 4014:
                                raise discord.PrivilegedIntentsRequired(exc.shard_id) from None
                            if exc.code != 1000:
                                await self.close()
                                raise

                        retry = backoff.delay()
                        _log.exception("Attempting a reconnect in %.2fs", retry)
                        await asyncio.sleep(retry)
                        # Always try to RESUME the connection
                        # If the connection is not RESUME-able then the gateway will invalidate the session.
                        # This is apparently what the official Discord client does.
                        ws_params.update(sequence=self.ws.sequence, resume=True, session=self.ws.session_id)

        @client.event
        async def on_command_error(ctx, err):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            embed3 = discord.Embed(title = f"Произошла ошибка: ``{err}``", colour=setx)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

            err = await ctx.send(embed = embed3)
            await asyncio.sleep(8)
            await err.delete()

        @client.event
        async def command_name_error(ctx, error):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            embed3 = discord.Embed(title = f"Произошла ошибка: ``{err}``", colour=setx)
            embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

            err = await ctx.send(embed = embed3)
            await asyncio.sleep(8)
            await err.delete()
            
        @slash.slash(description="add channel +v +t")
        @commands.cooldown(1, 900, commands.BucketType.user)
        async def qchannel(ctx, member: discord.Member,statustype:str,lim= None):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            if statustype is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите statustype!** {error_emoji}')
            else:
                guild = member.guild
                try:
                    perms = discord.Permissions(read_messages = False,connect = False,read_message_history= False,send_messages = False)
                    print("Ok.. ")
                except:
                    print("error (0) [Permissions]")
                try:
                    overwrite = discord.PermissionOverwrite()
                    overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages= False,read_message_history= False,send_messages = False),
                    guild.me: discord.PermissionOverwrite(read_messages=False,read_message_history=False,send_messages = False)
                    }
                    print("Ok.. ")
                except:
                    print("error (1) [Overwrite]")
                try:
                    overwrite.read_messages = False
                    overwrite.connect = False
                    overwrite.read_message_history= False
                    overwrite.send_messages = False
                    print("Ok.. ")
                except:
                    print("error (2) [overwrite]")
                try:
                    await message.channel.set_permissions(message.author, overwrite=overwrite)
                    print("Ok.. ")
                except:
                    print("error (3) [set_permissions]")
                try:
                    role = discord.utils.get(message.guild.roles, name = "@everyone")
                    await role.edit(permissions = perms)
                    print("Ok.. ")
                except:
                    print("error (4) [utils.get]")
                    
                try:
                    role = discord.utils.get(message.guild.roles, name = "@here")
                    await role.edit(permissions = perms)
                    print("Ok.. ")
                except:
                    print("error (5) [utils.get]")
                
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(send_messages = False),
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    guild.default_role: discord.PermissionOverwrite(connect = False),
                    guild.me: discord.PermissionOverwrite(read_messages=True),
                    guild.me: discord.PermissionOverwrite(send_messages=True),
                    guild.me: discord.PermissionOverwrite(connect = True),
                }

                if statustype is "T":
                    channel2 = await guild.create_text_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                if statustype is "V":
                    channel2 = await guild.create_voice_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                if statustype is "+T":
                    channel2 = await guild.create_text_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                if statustype is "+V":
                    channel2 = await guild.create_voice_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)

                if statustype is "t":
                    channel2 = await guild.create_text_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                if statustype is "v":
                    channel2 = await guild.create_voice_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                if statustype is "+t":
                    channel2 = await guild.create_text_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                if statustype is "+v":
                    channel2 = await guild.create_voice_channel(f"𝐂𝐇𝐀𝐓: {member}", ves=overwrites, category=perms, overwrites=overwrites, position = 1, limit = lim)
                channel_id = 1038582736266461194
                channel = client.get_channel(channel_id)
                inf = discord.Embed(
                    color = setx,
                    title=f"✟ℂℂ𝕋𝕍✞>> 𝐂𝐇𝐀𝐓",
                    description=f"user: {user} >> 𝐂𝐇𝐀𝐓: {member}"
                )
                await channel.send(embed=inf)
                await channel2.send(embed=inf)
                embed2 = discord.Embed(color = setx, title = f"✟ℂℂ𝕋𝕍✞ присоединился к  𝐂𝐇𝐀𝐓: {member} ")
                embed2.add_field(name='ADMIN -> \n АДМИНИСТРАТОР: ', value=f"\nIDKey: {member} \n IDKey: {user} \n")
                embed2.add_field(name='INFO -> \n ИНФОРМАЦИЯ: ', value=f"\nСервер - {guild.name} \n ID - {guild.id} \n Owner - {guild.owner} \n Disk - {guild.region} \n")
                embed2.add_field(name='Сhannel -> \n Канал: ', value=f"\n [overwrites] {overwrites} \n [channel] {channel2} \n [color] {setx} \n [Time] 900 seconds \n [limit] {lim} \n")
                embed2.add_field(name='BOT -> \n БОТ: ', value=f"\n [perms] {overwrites} \n [channel] {channel2} \n [color] {setx} \n")
                try:
                    embed.set_thumbnail(url=guild.icon_url)
                except:
                    print("err [photo]")
                await channel2.send(embed=embed2)
                await asyncio.sleep(900) # Ожидание 4 секунду
                await channel2.delete() #Удаление переменой Mas то есть удаление сообщения.           

        @client.event
        async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
                f'Hello, {member.name}!! Welcome to Our Discord Server! -> \n Привет, {member.name}!! Добро пожаловать на наш дискорд сервер!'
            )
                

        @slash.slash(description="cleartp")
        @commands.cooldown(1, 30, commands.BucketType.user)
        async def clears(ctx, user: discord.Member):
            await ctx.channel.purge(limit=None, check=lambda m: m.author==user)
            Mas = await ctx.send(f"clear >>") # Переменая где выводит в чат то что чат очищен в месте с количество указаного вами сообщения 
            await asyncio.sleep(3) # Ожидание 4 секунду
            await Mas.delete() #Удаление переменой Mas то есть удаление сообщения.
        #Очистка чата
        @slash.slash(description='clear')
        #@commands.has_permissions(administrator=True)
        @commands.cooldown(1, 30, commands.BucketType.user)
        async def clear(ctx):
                h = 0
                i = 0
                os.system("cls")
                await asyncio.sleep(1)# amount = 32 - это переменая в которой задано уже 32
                await ctx.channel.purge() # Очистить чат где было указана команда. limit = amount кол-во удаляемых сообщений тут указываеться amount перменая так что сколь вы вы вели столько и будет удалено сообщений. 
                Mas = await ctx.send(f"clear >>") # Переменая где выводит в чат то что чат очищен в месте с количество указаного вами сообщения 
                await asyncio.sleep(3) # Ожидание 4 секунду
                await Mas.delete() #Удаление переменой Mas то есть удаление сообщения.
        #Очистка чата
        @slash.slash(description='qclear')
        #@commands.has_permissions(administrator=True)
        @commands.cooldown(1, 30, commands.BucketType.user)
        async def qclear(ctx,number:int):
            h = 0
            i = 0
            os.system("cls")
            await ctx.channel.purge(limit=number)
            Mas = await ctx.send(f"clear -> \n прозрачный >> {number}")
            await asyncio.sleep(3) # Ожидание 4 секунду
            await Mas.delete() #Удаление переменой Mas то есть удаление сообщения.
            
        @slash.slash(description='-cl index')
        @commands.cooldown(1, 15, commands.BucketType.user)
        async def cl_index(ctx):
            Mas = await ctx.send(f"cl_index -> \n очистка списка приглашенных >>")
            await asyncio.sleep(1)
            os.remove("Invite.txt")
            await Mas.delete()
            
        @slash.slash(description='-cl history')
        @commands.cooldown(1, 15, commands.BucketType.user)
        async def cl_history(ctx):
            Mas = await ctx.send(f"cl_history -> \n очистить список действий >>")
            await asyncio.sleep(1)
            os.remove("Massage.txt")
            await Mas.delete()
            
        @slash.slash(description='-cl lvlup')
        @commands.cooldown(1, 15, commands.BucketType.user)
        async def cl_lvlup(ctx):
            Mas = await ctx.send(f"dlvlup -> \n очистить список голосов >>")
            await asyncio.sleep(1)
            os.remove('Up_lvl.txt')
            await Mas.delete()
            
        @slash.slash(description='-cl bad_word2')
        @commands.cooldown(1, 15, commands.BucketType.user)
        async def cl_bad_word2(ctx):
            Mas = await ctx.send(f"qdel -> \n очистить список заблокированных пользователей >>")
            await asyncio.sleep(1)
            os.remove("Bad word2.txt")
            await Mas.delete()
            

        @slash.slash(description="list+")
        @commands.cooldown(1, 15, commands.BucketType.user)
        async def qlist(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            guild = ctx.guild
            servers = []
            for guild in client.guilds:
                try:
                    invite = await guild.text_channels[0].create_invite(max_age=3600)
                    servers.append(f"\n ** {guild.name} ** - \n [0] {invite.url} \n")
                except:
                    continue
                    
        @slash.slash(description="+")
        @commands.cooldown(1, 10, commands.BucketType.user)
        #@commands.has_permissions(administrator=True) 
        async def invite(ctx, member: discord.Member):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            if member is None:
                await ctx.send(f'{error_emoji} **Пожалуйста, укажите пользователя!** {error_emoji}')
            else:
                guild = member.guild
                i = 0 
                async for entry in guild.audit_logs(limit = 10):
                    if entry.action == discord.AuditLogAction.invite_create:
                        print(f'{entry.user} создал приглашение: {entry.target}')
                        invites = await guild.invites()
                        for invite in invites:
                            i = i + 1
                            print(f'Ссылка: {invite.url} \nСоздатель: {invite.inviter} \n Использования: {invite.uses} \n')
                            with open("Invite.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8
                                logmsg.write(f"{entry.user} создал приглашение: {entry.target} \n")
                                logmsg.write(f"Ссылка: {invite.url} \nСоздатель: {invite.inviter} \n Использования: {invite.uses} \n")
                inf = discord.Embed(
                    color = setx,
                    title=f"✟ℂℂ𝕋𝕍✞ search: {guild.name}",
                    description= f'work completed, results {i} / 10 found.'
                )
                inf.add_field(name='link:', value='[💌](https://discord.gg/KamKsdJ9Bz)', inline=False)
                inf.add_field(name='Rolse:', value='[™](https://discord.gg/WKNR4PxTfy)', inline=False)
                inf.set_image(url="https://media4.giphy.com/media/4edx0TGrxhhnnCTgO4/giphy.gif?cid=ecf05e47yfdn8muafkq1q6hqlg578f4a3i22bvw162lgd5kz&rid=giphy.gif&ct=g")
                inf.set_thumbnail(url=ctx.guild.icon_url)
                inf.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                inf.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                channel_id = 1038582736266461194
                channel = client.get_channel(channel_id)
                Mas = await ctx.send(embed = inf)
                Mas1 = await channel.send(file=discord.File('Invite.txt'))
                await asyncio.sleep(30)
                await Mas.delete()
                await Mas1.delete()

        @slash.slash(description="-server")
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def info(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            guild = ctx.author.guild
            user = ctx.author
            
            role_count = len(ctx.guild.roles)
            staff_roles = ["Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators", "Community Helpers", "Members"]
                
            embed2 = discord.Embed(color = setx, title = "INFO -> \n ИНФОРМАЦИЯ :")
            embed2.add_field(name='Domain -> \n Домен : ', value=f"{ctx.guild.name}", inline=False)
            embed2.add_field(name='Owner -> \n Владелец : ', value=f"{guild.owner}", inline=False)
            embed2.add_field(name='Verification Level -> \n Уровень проверки : ', value=str(ctx.guild.verification_level), inline=False)
            embed2.add_field(name='Highest role -> \n Высшая роль : ', value=ctx.guild.roles[-2], inline=False)
            embed2.add_field(name='Region -> \n Область :', value=f"{guild.region}")  

            for r in staff_roles:
                role = discord.utils.get(ctx.guild.roles, name=r)
                if role:
                    members = '\n'.join([member.name for member in role.members]) or "None"
                    embed2.add_field(name=role.name, value=members)

            embed2.add_field(name='Number of roles -> \n Кол-во ролей : ', value=str(role_count), inline=False)
            embed2.add_field(name='Number Of Members -> \n Кол-во членов : ', value=ctx.guild.member_count, inline=False)
            embed2.add_field(name='Created At: ', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
            embed2.set_thumbnail(url=ctx.guild.icon_url)
            embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

            await ctx.send(embed=embed2)
                
            
    # -------------------------------------------------------------------------------------------------------        
        @client.command()
        @commands.cooldown(1, 10, commands.BucketType.user)
        async def server(ctx):
            colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
            setx = random.choice(colset)
            i = 0
            activeservers = client.guilds
            await ctx.message.delete()
            embed2 = discord.Embed(
                color = setx,
                description= activeservers
            )
            embed2.set_thumbnail(url=ctx.guild.icon_url)
            embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            message = await ctx.send(embed=embed2)
            await message.add_reaction('💲')
            await message.add_reaction('🚷')
            def check(reaction, user):
                return user == ctx.author


            reaction = None

            while True:
                if str(reaction) == '💲':
                    i = i + 1
                    send2 = await user.send(f"user: {user} : server:✅ >> {i} 📈")
                    with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                        logmsg.write(f"user: {user} : server:✅ >> {i} 📈")# Записываем плохое слово в Bad.txt
                        print(f"user: {user} : server:✅ >> {i} 📈")# Записываем плохое слово в Bad.txt
                elif str(reaction) == '🚷':
                    if i > 0:
                        i = i - 1
                        send1 = await user.send(f"user: {user} : server:❌ >> {i} 📉")
                        with open("Up_lvl.txt", "a", encoding = "utf-8") as logmsg: # Открываем файл Massage.txt и декодируем в utf-8 
                            logmsg.write(f"user: {user} : server:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt
                            print(f"user: {user} : server:❌ >> {i} 📉") # Записываем плохое слово в Bad.txt

                
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break
                
            await asyncio.sleep(1800)
            await send2.delete()
            await send1.delete()
            await message.delete()
    # -------------------------------------------------------------------------------------------------------
        @slash.slash(description='change: +g +r +w')
        @commands.cooldown(1, 10, commands.BucketType.user) #Задержка использования 8 секунды
        async def changestatus( ctx, statustype:str = None, *, arg:str = None): #Испртируем ctx, затем встраиваем переменые тип статуса / аргумент
            if statustype is None:  # Проверяем указали ли тип статуса
                await ctx.send( 'Вы не указали тип Статуса' )
            elif arg is None: # Проверяем указали ли аргумент
                await ctx.send( 'Вы не указали нужный аргумент' )
            else: #После проверок 
                if statustype.lower() == 'g': # Играет в
                    await client.change_presence ( status = discord.Status.idle, activity=discord.Game( name = arg) )
                elif statustype.lower() == 'r': # Листает
                    await client.change_presence( status = discord.Status.idle, activity=discord.Activity( type=discord.ActivityType.listening, name = arg) )
                elif statustype.lower() == 'w': # Смотрит
                    await client.change_presence( status = discord.Status.idle, activity=discord.Activity( type=discord.ActivityType.watching, name = arg) )
        @slash.slash(description='prefix')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def write_prefix(ctx, *, prefixsetup = None):
                if prefixsetup == None:
                        massnoprefix = await ctx.send(f"Вы не указали префикс <prefix>")
                        await asyncio.sleep(8)
                        await massnoprefix.delete()
                else:
                        openPrefixFile = open("prefix.txt", "w") # открываем файл prefix.txt метадом write Тоесть записи.
                        writingprefix = openPrefixFile.write(prefixsetup) #Ну а тут мы записываем в открытый файл prefix.txt записываем пременую prefixsetup где мы указали префикс для записи в файл.
                        await ctx.send(f"Префикс изменён на > {prefixsetup} < Что бы применить видите {prefixintial} reload")
                        await client.change_presence(status = discord.Status.idle, activity = discord.Activity( type =discord.ActivityType.watching, name = f"{prefix}reload"))
        @client.command(description='shutdown')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def shutdown(ctx):
                colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
                setx = random.choice(colset)
                inf = discord.Embed(
                    color = setx,
                    title="✟ℂℂ𝕋𝕍✞ > ❌",
                    description="-Перезапуск -Return 25sec.")
                now_times = nd.strftime(" = %H : %M : %S = ") #Время с изменёным стилем
                date_dm = nd.strftime(" - %d.%m.%y %b -") #Дата с изменёным стилем
                embedmas = await ctx.send(embed=inf)
                await asyncio.sleep(25)
                await embedmas.delete()
                await os.execv(sys.executable, ["python"] + sys.argv) #Но тут мы повторно запускаем наш файл то есть бота

        @slash.slash(description='shutdown')
        @commands.cooldown(1, 25, commands.BucketType.user)
        async def shutdown(ctx):
                colset = [0x8A2BE2,0x9b59b6,0x71368a,0x1abc9c,0x2ecc71,0x11806a,0xff0000,0x607d8b,0x1f8b4c,0x48D1CC,0x00FF00,0x3498db]
                setx = random.choice(colset)
                inf = discord.Embed(
                    color = setx,
                    title="✟ℂℂ𝕋𝕍✞ > ❌",
                    description="-Перезапуск -Return 25sec.")
                now_times = nd.strftime(" = %H : %M : %S = ") #Время с изменёным стилем
                date_dm = nd.strftime(" - %d.%m.%y %b -") #Дата с изменёным стилем
                embedmas = await ctx.send(embed=inf)
                await asyncio.sleep(25)
                await embedmas.delete()
                await os.execv(sys.executable, ["python"] + sys.argv) #Но тут мы повторно запускаем наш файл то есть бота


    except:
        print("[****] > operator problems, system restart!")
    #------------
    #Запуск бота
    try:
        print("[+] restarting the client")
        client.run(str(token))
        #Запуск бота (TokenBot) - Это переменая в которой указываеться токен вашего бота.
        subprocess.Popen(['python', os.path.realpath(__file__), '0'], close_fds=True)
        print ('main end')
        print ('[-] remote to startup')
    except:
        print("[**] > Error in the client, please. restart the system !")            
