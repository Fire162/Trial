from telethon.sync import TelegramClient, events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.contacts import UnblockRequest
import time
from telethon.sync import TelegramClient
from telethon import functions, types
from asyncio import sleep
running_from = time.time()
API_ID = 25032788
API_HASH = 'e79f7cb7edf4014b71d6158f5790d441'
approved = []
blocked = []
client = TelegramClient('session_name', API_ID, API_HASH)
@client.on(events.NewMessage(outgoing=True))
async def echo_messages(event):
    if 0 == 0:   
        me = await client.get_me()  
        mention = f"<a href='tg://user?id={me.id}'>{me.first_name}</a>"          
        msg = event.text
        message_id = event.message.id
        chat_id = event.chat_id        
        if msg == '.ping' or msg == '!ping' or msg == '/ping':
            start_time = time.time()
            # Send initial "Ping Pong" message
            sent_message = await client.edit_message(chat_id,message_id,"•• Pᴏɴɢ ••")                        
            end_time = time.time()
            ex = round(end_time - start_time, 3)
            running_time = time.time() - running_from
            hours, remainder = divmod(running_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            run = f"⏳ Uᴘᴛɪᴍᴇ - {int(hours)}ʜ:{int(minutes)}ᴍ:{int(seconds)}s."                               
            # Edit the message to include ping time and uptime
            await client.edit_message(sent_message, f"•• Pᴏɴɢ ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ: {str(ex)}ᴍs\n{run}\n👑 Oᴡɴᴇʀ : {mention}",parse_mode='HTML')
        elif msg == '.hello' or msg == '!hello' or msg == '/hello':
            await client.edit_message(event.chat_id, event.message.id, '╔┓┏╦━━╦┓╔┓╔━━╗ ║┗┛║┗━╣┃║┃║╯╰║ ║┏┓║┏━╣┗╣┗╣╰╯║ ╚┛┗╩━━╩━╩━╩━━╝')
        elif msg == '.info' or msg == '!info' or msg == '/info':
            await client.edit_message(event.chat_id, event.message.id, 'Repo Disconnected 🍓')
        elif msg.startswith('/math'):
            await event.reply("😢 Disabled ")
        elif msg == '.help':
        	await event.reply('ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı')
        elif msg == '.addsudo':
        	if event.is_reply:
        	   user_id = (await event.get_reply_message()).sender_id
        	   if user_id not in approved:
        	   	approved.append(user_id)  
        	   await event.reply('Successfully Added')
        elif msg == '.rmsudo':
        	if event.is_reply:
        	   user_id = (await event.get_reply_message()).sender_id
        	   print(user_id)    
        	   if user_id in approved:
        	   	approved.remove(user_id)  
        	   await event.reply('Successfully Removed')
        elif msg == '.restart':
            sent = await event.reply('Rᴇʙᴏᴏᴛɪɴɢ ʙᴏᴛ...\n\nWᴀɪᴛ ғᴏʀ ᴀ ᴡʜɪʟᴇ ᴛᴏ ᴜsᴇ ɪᴛ ᴀɢᴀɪɴ.')  
            time.sleep(5)        
            await client.edit_message(sent,'Rᴇsᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟ')	 
        elif msg.startswith('.join'):
            await event.reply('🚫 Cᴜʀʀᴇɴᴛʟʏ Dɪsᴀʙʟᴇᴅ')
            return
            username = msg.replace('.join', '')  
            sent = await event.reply('Roger that...\nI\'m on it.') 
            try:
                await client.join_channel(username)    
                await client.edit_message(sent, 'Joined the chat successfully Over!')
            except Exception as e:
                await client.reply(f'**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nError: {str(e)}\n\nUse: ```.help``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs.')
        elif msg.startswith('.sg'):
            res = None
            if event.is_reply:
                user_id = (await event.get_reply_message()).sender_id
                sent_message = await client.send_message('@SangMata_beta_bot', str(user_id))  # Convert user_id to string
                async for message in client.iter_messages('@SangMata_beta_bot', limit=1):
                    if message.id != sent_message.id:
                        res = message.text
                        break
                if '@SangMata_BOT' in str(res):
                    await event.reply('Sorry')                    
                else:  
                    await event.reply(res)
        elif msg.startswith('.poll'):
            msg = msg.replace('.poll',"")          
            results = await client.inline_query('like',msg)
            message = await results[0].click(event.chat_id)  
        elif msg == '.welcome':
            try:
                await client.edit_message(event.chat_id, event.message.id,'''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')     
            except:
                  await event.reply('''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')  
        elif msg == '.abhinav':
          await client.edit_message(event.chat_id, event.message.id,'''╭━╮╭━╮
┃┃╰╯┃┃
┃╭╮╭╮┣━╮
┃┃┃┃┃┃╭╯
┃┃┃┃┃┃┃
╰╯╰╯╰┻╯


╭━━━┳╮╱╭╮
┃╭━╮┃┃╱┃┃
┃┃╱┃┃╰━┫╰━┳┳━╮╭━━┳╮╭╮
┃╰━╯┃╭╮┃╭╮┣┫╭╮┫╭╮┃╰╯┃
┃╭━╮┃╰╯┃┃┃┃┃┃┃┃╭╮┣╮╭╯
╰╯╱╰┻━━┻╯╰┻┻╯╰┻╯╰╯╰╯


╭━━━╮
┃╭━╮┃
┃╰━╯┣━┳━━╮
┃╭━━┫╭┫╭╮┃
┃┃╱╱┃┃┃╰╯┃
╰╯╱╱╰╯╰━━╯''')
        elif msg == '.fire':
          await client.edit_message(event.chat_id, event.message.id,'''█▀▀ █ █▀█ █▀▀
█▀░ █ █▀▄ ██▄''')
        elif msg == '.dad':
            await client.edit_message(event.chat_id,event.message.id,"""██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗
██║░░██║███████║██║░░██║
██║░░██║██╔══██║██║░░██║
██████╔╝██║░░██║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░""")  
        elif msg == '.back':
            await client.edit_message(event.chat_id,event.message.id,"""
█▀█ ▄▀█ █▀█ ▄▀█
█▀▀ █▀█ █▀▀ █▀█

█▄▄ ▄▀█ █▀▀ █▄▀
█▄█ █▀█ █▄▄ █░█""")    
        elif msg == '.block':                                     
            try:
                user_id = (await event.get_reply_message()).sender_id
            except:
                user_id = event.chat_id
            blocked.append(user_id)
            user_entity = await client.get_entity(user_id)
            await client(BlockRequest(user_entity))          
        elif msg == '.unblock':
            user_id = (await event.get_reply_message()).sender_id
            if user_id in blocked:
                blocked.remove(user_id)    
            #await client.send_message(user_id,'✅ You Are Allowed To Message Me') 
            user_entity = await client.get_entity(user_id)
            await client(UnblockRequest(user_entity))     
        elif msg == '.save':
            to_chat_id = event.sender_id
            reply_message = await event.get_reply_message()
            await client(ForwardMessagesRequest(
    from_peer=reply_message.chat_id,
    id=[reply_message.id],
    to_peer=to_chat_id)) 
            await client.edit_message(event.chat_id,event.message.id,'''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━━┳╮╭┳━━┳━╯┃
╰━━╮┃╭╮┃╰╯┃┃━┫╭╮┃
┃╰━╯┃╭╮┣╮╭┫┃━┫╰╯┃
╰━━━┻╯╰╯╰╯╰━━┻━━╯''') 
        elif msg == '.forward':
            to_chat_id = event.chat_id
            reply_message = await event.get_reply_message()
            await client(ForwardMessagesRequest(
    from_peer=reply_message.chat_id,
    id=[reply_message.id],
    to_peer=to_chat_id))    
        elif msg == '.copy':
            reply_message = await event.get_reply_message()
            await event.client.send_message(event.chat_id, reply_message)  
        elif msg == 'upi' or msg == '.upi' or msg == 'UPI':
            await event.reply('''╭╮╱╭┳━━━┳━━╮
┃┃╱┃┃╭━╮┣┫┣╯
┃┃╱┃┃╰━╯┃┃┃
┃┃╱┃┃╭━━╯┃┃    ---  anurag6672@axl
┃╰━╯┃┃╱╱╭┫┣╮
╰━━━┻╯╱╱╰━━╯''') 
        elif msg == '+1':
            await client.edit_message(event.chat_id,event.message.id,'''
░░░░░░░░░███╗░░
░░██╗░░░████║░░
██████╗██╔██║░░
╚═██╔═╝╚═╝██║░░
░░╚═╝░░███████╗
░░░░░░░╚══════╝''')        
        elif msg == '-1':
            await client.edit_message(event.chat.id,event.message.id,"""
░░░░░░░░███╗░░
░░░░░░░████║░░
█████╗██╔██║░░
╚════╝╚═╝██║░░
░░░░░░███████╗
░░░░░░╚══════╝""")     
        elif msg == '.💀':
            await client.edit_message(event.chat.id,event.message.id,'''███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
''')
        elif msg == '.love':
            await client.edit_message(event.chat.id,event.message.id,'''▀██▀─▄███▄─▀██─██▀██▀▀█
─██─███─███─██─██─██▄█
─██─▀██▄██▀─▀█▄█▀─██▀█
▄██▄▄█▀▀▀─────▀──▄██▄▄█
''')
        elif msg == '.wtf':
            await client.edit_message(event.chat_id,event.message.id,'''┏┓┏┓┏┳━━━━┳━━━┓
┃┃┃┃┃┣━┓┏━┫┏━━┛
┃┃┃┃┃┃╱┃┃╱┃┗━┓╱
┃╰┛╰┛┃╱┃┃╱┃┏━┛╱
╰━━━━┛╱┗┛╱┗┛╱╱╱
''') 
        elif msg == '.h':
            heart_sequence = ['💝', '❤️', '🧡', '♥️', '❤️‍🩹', '🤍', '💚', '💙', '💜', '🖤', '❤️‍🔥']
            for heart in heart_sequence:
                time.sleep(1)
                if heart == '🖤' or heart == '💝':
                    time.sleep(1)
                await client.edit_message(event.chat_id, event.message.id,heart)
        elif msg.startswith('.q'):
            if event.message.reply_to:
                reply_message = await event.message.get_reply_message()
                await client(ForwardMessagesRequest(
    from_peer=reply_message.chat_id,
    id=[reply_message.id],
    to_peer='@Quotlybot'))     
                await client.edit_message(event.chat_id, event.message.id,'<b>𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈<b>',parse_mode='HTML')
                time.sleep(5)             
                response = await client.get_messages('@QuotLyBot', limit=1)
                hi = await client.forward_messages(event.chat_id, response)             
            else:
                user_id = event.text.replace('.q', '').strip()
                sent_message = await client.send_message('@QuotLyBot',user_id)   
                await client.edit_message(event.chat_id, event.message.id,'<b>𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈<b>',parse_mode='HTML')
                time.sleep(5)             
                response = await client.get_messages('@QuotLyBot', limit=1)
                if response.message_id == event.message_id:
                    time.sleep(2) 
                    response = await client.get_messages('@QuotLyBot', limit=1)    
                    hi = await client.forward_messages(event.chat_id, response)                  
                else:
                    hi = await client.forward_messages(event.chat_id, response)   
                    await event.reply(sticker=event.message.sticker)
        elif msg == '.no':
            await client.edit_message(event.chat_id,event.message.id,'''
███╗░░██╗░█████╗░
████╗░██║██╔══██╗
██╔██╗██║██║░░██║
██║╚████║██║░░██║
██║░╚███║╚█████╔╝
╚═╝░░╚══╝░╚════╝░''')  
        elif msg == '.ind':
            await client.edit_message(event.chat_id,event.message.id,'''ㅤㅤㅤㅤ⬛️🟧🟧🟧🟧🟧🟧🟧🟧🟧
               ⬛️🟧🟧🟧🟧🟧🟧🟧🟧🟧
               ⬛️⬜️⬜️⬜️🟦🟦⬜️⬜️⬜️⬜️
               ⬛️⬜️⬜️⬜️🟦🟦⬜️⬜️⬜️⬜️
               ⬛️🟩🟩🟩🟩🟩🟩🟩🟩🟩
               ⬛️🟩🟩🟩🟩🟩🟩🟩🟩🟩
               ⬛️
               ⬛️
         ⬛️⬛️⬛️⬛️
     ⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️''')
        elif msg == ".pro":
            await client.edit_message(event.chat_id,event.message.id,'''
██████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗
██████╔╝██████╔╝██║░░██║
██╔═══╝░██╔══██╗██║░░██║
██║░░░░░██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░''')
        elif msg == '.approve':
            result = client(functions.messages.HideAllChatJoinRequestsRequest(
        peer='@mr_abhinav_pro',
        approved=True,
        link='https://t.me/+8MqwUI4eKMlmODE1'
    ))
            print(result.stringify())                        
@client.on(events.NewMessage(incoming=True))
async def echo_messages(event):
        me = await client.get_me()
        mention = f"<a href='tg://user?id={me.id}'>{me.first_name}</a>"
        if event.sender_id not in approved:
        	return    
        msg = event.text
        #print(event.sender_id)
        if msg == '.ping' or msg == '!ping' or msg == '/ping':
            start_time = time.time()
            # Send initial "Ping Pong" message
            sent_message = await event.reply("•• Pᴏɴɢ ••")                        
            end_time = time.time()
            ex = round(end_time - start_time, 3)
            running_time = time.time() - running_from
            hours, remainder = divmod(running_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            run = f"⏳ Uᴘᴛɪᴍᴇ - {int(hours)}ʜ:{int(minutes)}ᴍ:{int(seconds)}s."
            
            # Edit the message to include ping time and uptime
            await client.edit_message(sent_message, f"•• Pᴏɴɢ ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ: {str(ex)}ᴍs\n{run}\n👑 Oᴡɴᴇʀ : {mention}",parse_mode='HTML')
        elif msg == '.hello' or msg == '!hello' or msg == '/hello':
            await event.reply('╔┓┏╦━━╦┓╔┓╔━━╗ ║┗┛║┗━╣┃║┃║╯╰║ ║┏┓║┏━╣┗╣┗╣╰╯║ ╚┛┗╩━━╩━╩━╩━━╝')
        elif msg == '.info' or msg == '!info' or msg == '/info':
            await client.edit_message(event.chat_id, event.message.id, 'Repo Disconnected 🍓')
        elif msg.startswith('/math'):
            await event.reply("😢 Disabled ")
        elif msg == '.help':
        	await event.reply('ıllıllı★ 𝙷𝚎𝚕𝚙 𝙼𝚎𝚗𝚞 ★ıllıllı')
        elif msg == '.restart':
            sent = await event.reply('Rᴇʙᴏᴏᴛɪɴɢ ʙᴏᴛ...\n\nWᴀɪᴛ ғᴏʀ ᴀ ᴡʜɪʟᴇ ᴛᴏ ᴜsᴇ ɪᴛ ᴀɢᴀɪɴ.')   
            time.sleep(5)        
            await client.edit_message(sent,'Rᴇsᴛᴀʀᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟ')	 
        elif msg.startswith('.join'):
            await event.reply('🚫 Cᴜʀʀᴇɴᴛʟʏ Dɪsᴀʙʟᴇᴅ')
            return
            username = msg.replace('.join', '')  
            sent = await event.reply('Roger that...\nI\'m on it.') 
            try:
                await client.join_channel(username)    
                await client.edit_message(sent, 'Joined the chat successfully Over!')
            except Exception as e:
                await client.reply(f'**🧿Wʀᴏɴɢ Usᴀɢᴇ🧿**\n\nError: {str(e)}\n\nUse: ```.help``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs.')
        elif msg.startswith('.sg'):
            if event.is_reply:
                user_id = (await event.get_reply_message()).sender_id
                sent_message = await client.send_message('@SangMata_beta_bot', str(user_id))  # Convert user_id to string
                async for message in client.iter_messages('@SangMata_beta_bot', limit=1):
                    if message.id != sent_message.id:
                        res = message.text
                        break   
                await event.reply(res)
        elif msg.startswith('.poll'):
            msg = msg.replace('.poll',"")          
            results = await client.inline_query('like',msg)
            message = await results[0].click(event.chat_id)    
        elif msg == '.welcome':
            try:
                await client.edit_message(event.chat_id, event.message.id,'''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')     
            except:
                  await event.reply('''───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')  
        elif msg == '.abhinav':
            await event.reply('''╭━╮╭━╮
┃┃╰╯┃┃
┃╭╮╭╮┣━╮
┃┃┃┃┃┃╭╯
┃┃┃┃┃┃┃
╰╯╰╯╰┻╯


╭━━━┳╮╱╭╮
┃╭━╮┃┃╱┃┃
┃┃╱┃┃╰━┫╰━┳┳━╮╭━━┳╮╭╮
┃╰━╯┃╭╮┃╭╮┣┫╭╮┫╭╮┃╰╯┃
┃╭━╮┃╰╯┃┃┃┃┃┃┃┃╭╮┣╮╭╯
╰╯╱╰┻━━┻╯╰┻┻╯╰┻╯╰╯╰╯


╭━━━╮
┃╭━╮┃
┃╰━╯┣━┳━━╮
┃╭━━┫╭┫╭╮┃
┃┃╱╱┃┃┃╰╯┃
╰╯╱╱╰╯╰━━╯''') 
        elif msg == '.fire':
          await event.reply('''█▀▀ █ █▀█ █▀▀
█▀░ █ █▀▄ ██▄''')
        elif msg == '.dad':
            await event.reply("""██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗
██║░░██║███████║██║░░██║
██║░░██║██╔══██║██║░░██║
██████╔╝██║░░██║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░""")  
        elif msg == '.back':
            await event.reply("""
█▀█ ▄▀█ █▀█ ▄▀█
█▀▀ █▀█ █▀▀ █▀█

█▄▄ ▄▀█ █▀▀ █▄▀
█▄█ █▀█ █▄▄ █░█""")    
        elif msg == '.block':                                     
            user_id = (await event.get_reply_message()).sender_id
            blocked.append(user_id)        
            await client.block_user(user_id)
        elif msg == '.unblock':
            user_id = (await event.get_reply_message()).sender_id
            if user_id in blocked:
                blocked.remove(user_id)             
            user_entity = await client.get_entity(user_id)
            await client(UnblockRequest(user_entity))                
        elif msg == '.save':
            to_chat_id = event.sender_id
            reply_message = await event.get_reply_message()
            await client(ForwardMessagesRequest(
    from_peer=reply_message.chat_id,
    id=[reply_message.id],
    to_peer=to_chat_id)) 
            await event.reply('''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━━┳╮╭┳━━┳━╯┃
╰━━╮┃╭╮┃╰╯┃┃━┫╭╮┃
┃╰━╯┃╭╮┣╮╭┫┃━┫╰╯┃
╰━━━┻╯╰╯╰╯╰━━┻━━╯''')
        elif msg == '.forward':
            to_chat_id = event.chat_id
            reply_message = await event.get_reply_message()
            await client(ForwardMessagesRequest(
    from_peer=reply_message.chat_id,
    id=[reply_message.id],
    to_peer=to_chat_id))    
        elif msg == '.copy':
            reply_message = await event.get_reply_message()
            await event.client.send_message(event.chat_id, reply_message)  
        elif msg == 'upi' or msg == '.upi' or msg == 'UPI':
            await event.reply('''╭╮╱╭┳━━━┳━━╮
┃┃╱┃┃╭━╮┣┫┣╯
┃┃╱┃┃╰━╯┃┃┃
┃┃╱┃┃╭━━╯┃┃    ---  anurag6672@axl
┃╰━╯┃┃╱╱╭┫┣╮
╰━━━┻╯╱╱╰━━╯''') 
        elif msg == '+1':
            await event.reply('''
░░░░░░░░░███╗░░
░░██╗░░░████║░░
██████╗██╔██║░░
╚═██╔═╝╚═╝██║░░
░░╚═╝░░███████╗
░░░░░░░╚══════╝''')     
        elif msg == '-1':
            await event.reply('''
░░░░░░░░███╗░░
░░░░░░░████║░░
█████╗██╔██║░░
╚════╝╚═╝██║░░
░░░░░░███████╗
░░░░░░╚══════╝''')  
        elif msg == '.💀':
            await event.reply('''███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
''')  
        elif msg == '.love':
            await event.reply('''▀██▀─▄███▄─▀██─██▀██▀▀█
─██─███─███─██─██─██▄█
─██─▀██▄██▀─▀█▄█▀─██▀█
▄██▄▄█▀▀▀─────▀──▄██▄▄█
''')   
        elif msg == '.wtf':
            await event.reply('''┏┓┏┓┏┳━━━━┳━━━┓
┃┃┃┃┃┣━┓┏━┫┏━━┛
┃┃┃┃┃┃╱┃┃╱┃┗━┓╱
┃╰┛╰┛┃╱┃┃╱┃┏━┛╱
╰━━━━┛╱┗┛╱┗┛╱╱╱
''')   
        elif msg == '.h':
            heart_sequence = ['💝', '❤️', '🧡', '♥️', '❤️‍🩹', '🤍', '💚', '💙', '💜', '🖤', '❤️‍🔥']
            for heart in heart_sequence:
                time.sleep(1)
                if heart == '🖤' or heart == '💝':
                    time.sleep(1)
                await client.edit_message(event.chat_id, event.message.id,heart) 
        elif msg == '.no':
            await event.reply('''
███╗░░██╗░█████╗░
████╗░██║██╔══██╗
██╔██╗██║██║░░██║
██║╚████║██║░░██║
██║░╚███║╚█████╔╝
╚═╝░░╚══╝░╚════╝░''')   
        elif msg == '.ind':
            await event.reply('''ㅤㅤㅤㅤ⬛️🟧🟧🟧🟧🟧🟧🟧🟧🟧
               ⬛️🟧🟧🟧🟧🟧🟧🟧🟧🟧
               ⬛️⬜️⬜️⬜️🟦🟦⬜️⬜️⬜️⬜️
               ⬛️⬜️⬜️⬜️🟦🟦⬜️⬜️⬜️⬜️
               ⬛️🟩🟩🟩🟩🟩🟩🟩🟩🟩
               ⬛️🟩🟩🟩🟩🟩🟩🟩🟩🟩
               ⬛️
               ⬛️
         ⬛️⬛️⬛️⬛️
     ⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️''')   

async def main():
    await client.start()
    await client.run_until_disconnected()
if __name__ == '__main__':
    client.loop.run_until_complete(main())
