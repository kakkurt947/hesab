# Dızlar Dızlar Dızlar bot
import re, os, random, asyncio, html,configparser,pyrogram, subprocess, requests, time, traceback, logging, telethon, csv, json, sys
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from asyncio.exceptions import TimeoutError
from pyrogram.errors import SessionPasswordNeeded, FloodWait, PhoneNumberInvalid, ApiIdInvalid, PhoneCodeInvalid, PhoneCodeExpired, UserNotParticipant
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from telethon.client.chats import ChatMethods
from csv import reader
from telethon.sync import TelegramClient
from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError
from telethon.sessions import StringSession
from pyrogram import Client,filters
from pyromod import listen
from sql import add_user, query_msg
from support import users_info
from datetime import datetime, timedelta,date
import csv
 #add_user= query_msg= users_info=0
if not os.path.exists('./sessions'):
    os.mkdir('./sessions')
if not os.path.exists(f"Users/5494033825/phone.csv"):
   os.mkdir('./Users')
   os.mkdir(f'./Users/5494033825')
   open(f"Users/5494033825/phone.csv","w")
if not os.path.exists('data.csv'):
    open("data.csv","w")
APP_ID =  9544149
API_HASH = "ec6038735b49819f89c26567dc43b161"
BOT_TOKEN = "5585398169:AAE-Hrc4ngc0ywPgiGi8RQACZoRrwZgpJ_4"
UPDATES_CHANNEL = "tutkudestek"
OWNER = [5494033825,5377241809]
PREMIUM = [5494033825,5377241809]
app = pyrogram.Client("app", api_id=APP_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))



with open("data.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    ishan=[]
    for row in rows:
        d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
        r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-11-03", '%Y-%m-%d')
        if d<=r:
            PREMIUM.append(int(row[1]))

# ------------------------------- Subscribe --------------------------------- #
async def Subscribe(lel, message):
   update_channel = UPDATES_CHANNEL
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.chat.id)
         if user.status == "kicked":
            await app.send_message(chat_id=message.chat.id,text="Üzgünüm efendim, yasaklandınız. İletişim [Destek Grubu](https://t.me/tutkudestek).", parse_mode="markdown", disable_web_page_preview=True)
            return 1
      except UserNotParticipant:
         await app.send_message(chat_id=message.chat.id, text="**Lütfen Beni Kullanmak İçin Güncel Kanalıma Katılın!\n ve Kontrol etmek için tıklayın /start**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 Güncelleme Kanalına Katılın 🤖", url=f"https://t.me/tutkudestek")]]), parse_mode="markdown")
         return 1
      except Exception:
         await app.send_message(chat_id=message.chat.id, text="**Bir şeyler ters gitti. İletişim [Destek Grubu](https://t.me/tutkudestek).**", parse_mode="markdown", disable_web_page_preview=True)
         return 1




# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["start"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   id = message.from_user.id
   user_name = '@' + message.from_user.username if message.from_user.username else None
   await add_user(id, user_name)
   but = InlineKeyboardMarkup([[InlineKeyboardButton("Login ✅", callback_data="Login"), InlineKeyboardButton("Group Ekle 💯", callback_data="Adding") ],[InlineKeyboardButton("Telefon Ekle ⚙️", callback_data="Edit"), InlineKeyboardButton("Telefonlar 💕", callback_data="Ish")],[InlineKeyboardButton("Telefon Kaldır ⚙️", callback_data="Remove"), InlineKeyboardButton("Yönetim paneli", callback_data="Admin")]])
   await message.reply_text(f"**Merhaba** `{message.from_user.first_name}` **!\n\nBen üye çekmek için tasarlanmış botum. \nÜcretsiz üye çekmek için tasarlandım,\nSizler için en iyisi.\n\n💬 Yardım Grubu @tutkudestek**", reply_markup=but)



# ------------------------------- numara kaydetme --------------------------------- #
@app.on_message(filters.private & filters.command(["phone"]))
async def phone(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return 
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı Değilsiniz\nLütfen bir Alt Yazıya Sahip Olun\n200rs ayda\nPm @tommy47shelby**")
      return'''
   if not os.path.exists(f"Users/{message.from_user.id}/phone.csv"):
      os.mkdir(f'./Users/{message.from_user.id}')
      open(f"Users/{message.from_user.id}/phone.csv","w")
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
      str_list = [row[0] for row in csv.reader(f)]
      NonLimited=[]
      a=0
      for pphone in str_list:
         a+=1
         NonLimited.append(str(pphone))
      number = await app.ask(chat_id=message.chat.id, text="**Giriş yapmak için hesap sayısını girin (1, 2, 3, 4 ,5)\n\nYardım için @tutkudestek**")
      n = int(number.text)
      a+=n
      if n<1 :
         await app.send_message(message.chat.id, """**Geçersiz Biçim 1'den az Yeniden deneyin\n\nİletişim @tommy47shelby**""")
         return
      if a>500:
         await app.send_message(message.chat.id, f"**Yalnızca şunları ekleyebilirsiniz: {100-a} Telefon no \n\nSohbet destek ❤️ @tutkudestek**")
         return
      for i in range (62,n+62):
         number = await app.ask(chat_id=message.chat.id, text="**Şimdi Telegram Hesabınızın Telefon Numarasını Uluslararası Biçimde Gönderin. \nDahil **Ülke Kodu**. \nÖrnek: **+6283853200954 = 6283853200954 işaret olmadan +**\n\nDestek 🇹🇷 @tutkudestek**")
         phone = number.text
         if "+" in phone:
            await app.send_message(message.chat.id, """**Alan kodu için + dahil değildir.\n\nBilgi için ❤️ @tommy47shelby**""")
         elif len(phone)==20 or len(phone)==1:
            Singla = str(phone)
            NonLimited.append(Singla)
            await app.send_message(message.chat.id, f"**{n}). Telefon: {phone} Başarılı oldu ✅\n\nBilgi için @tommy47shelby**")
         else:
            await app.send_message(message.chat.id, """**Geçersiz Sayı Biçimi Yeniden deneyin\n\nBilgi için 🇹🇷 @tommy47shelby**""") 
      NonLimited=list(dict.fromkeys(NonLimited))
      with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
         writer = csv.writer(writeFile, lineterminator="\n")
         writer.writerows(NonLimited)
      with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
         for line in infile:
            outfile.write(line.replace(",", ""))
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nBilgi @tommy47shelby**")
   return



# ------------------------------- Acc Login --------------------------------- #
@app.on_message(filters.private & filters.command(["login"]))
async def login(lel, message):
 try:
   await message.delete()
   a= await Subscribe(lel, message)
   if a==1:
      return 
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı Değilsiniz\nLütfen bir Alt Yazıya Sahip Olun\n200rs ayda\n\nResmi Kanal @tutkudestek**")
      return'''
   with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
    r=[]
    l=[]
    str_list = [row[0] for row in csv.reader(f)]
    po = 0
    s=0
    for pphone in str_list:
     try:
      phone = int(utils.parse_phone(pphone))
      client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
      await client.connect()
      if not await client.is_user_authorized():
         try:
            await client.send_code_request(phone)
         except FloodWait as e:
            await message.reply(f"Flood {e.x} Saniye")
            return
         except PhoneNumberInvalidError:
            await message.reply("Telefon Numaranız Geçersiz.\n\nBasın /start yeniden başlamak için!")
            return
         except PhoneNumberBannedError:
            await message.reply(f"{phone} Yasaklandı")
            continue
         try:
            otp = await app.ask(message.chat.id, ("Telefon numaranıza bir Kod gönderilir, \nLütfen Kodu `1 2 3 4 5` gibi boşluk bırakarak yazalım. __(Her sayı arasındaki boşluk!)__ \n\nBot Kod göndermiyorsa, deneyin /restart ve Görevi yeniden başlatın /start Bot'a komut.\nBasın /cancel iptal etmek için."), timeout=300)
         except TimeoutError:
            await message.reply("5 Dakikalık Ulaşılan Süre Sınırı.\nBasın /start yeniden başlamak için!")
            return
         otps=otp.text
         try:
            await client.sign_in(phone=phone, code=' '.join(str(otps)))
         except PhoneCodeInvalidError:
            await message.reply("Geçersiz Kod.\n\nBasın /start yeniden başlamak için!")
            return
         except PhoneCodeExpiredError:
            await message.reply("Kodun Süresi Doldu.\n\nPress /start yeniden başlamak için!")
            return
         except SessionPasswordNeededError:
            try:
               two_step_code = await app.ask(message.chat.id,"Hesabınızda iki adımlı doğrulama var.\nLütfen Şifrenizi Girin.",timeout=300)
            except TimeoutError:
               await message.reply("`5 Dakikalık Ulaşılan Süre Sınırı.\n\nBasın /start yeniden başlamak için!`")
               return
            try:
               await client.sign_in(password=two_step_code.text)
            except Exception as e:
               await message.reply(f"**ERROR:** `{str(e)}`")
               return
            except Exception as e:
               await app.send_message(message.chat.id ,f"**ERROR:** `{str(e)}`")
               return
      with open("Users/5494033825/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         NonLimited=[]
         for pphone in str_list:
            NonLimited.append(str(pphone))
         Singla = str(phone)
         NonLimited.append(Singla)
         NonLimited=list(dict.fromkeys(NonLimited))
         with open('1.csv', 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(NonLimited)
         with open("1.csv") as infile, open(f"Users/5494033825/phone.csv", "w") as outfile:
            for line in infile:
                outfile.write(line.replace(",", ""))
      os.remove("1.csv")
      await client(functions.contacts.UnblockRequest(id='@SpamBot'))
      await client.send_message('SpamBot', '/start')
      msg = str(await client.get_messages('SpamBot'))
      re= "bird"
      if re in msg:
         stats="İyi haber, şu anda hesabınıza herhangi bir sınır uygulanmıyor. Bir kuş gibi özgürsün!"
         s+=1
         r.append(str(phone))
      else:
         stats='you are limited'
         l.append(str(phone))
      me = await client.get_me()
      await app.send_message(message.chat.id, f"Başarıyla Giriş Yapın ✅ Yapılmış.\n\n**İsim:** {me.first_name}\n**Kullanıcı adı:** {me.username}\n**Telefon:** {phone}\n**SpamBot İstatistikleri:** {stats}\n\n**İrtibat @tommy47shelby**")     
      po+=1
      await client.disconnect()
     except ConnectionError:
      await client.disconnect()
      await client.connect()
     except TypeError:
      await app.send_message(message.chat.id, "**Telefon numarasını girmediniz \nlütfen Bilgileri ⚙️ düzenleyiniz. /start.\n\nYardım için @tutkudestek**")  
     except Exception as e:
      await app.send_message(message.chat.id, f"**Hata: {e}\n\nYardım için @tutkudestek**")
    for ish in l:
      r.append(str(ish))
    with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
      writer = csv.writer(writeFile, lineterminator="\n")
      writer.writerows(r)
    with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
      for line in infile:
         outfile.write(line.replace(",", "")) 
    await app.send_message(message.chat.id, f"**Tüm Kayıtlı Numara Girişleri {s} Kullanılabilir Hesap {po} \n\nBilgi için @tutkudestek**") 
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nEditör 🇹🇷 @tutkudestek**")
   return
                          


# ------------------------------- Acc Private Adding --------------------------------- #
@app.on_message(filters.private & filters.command(["adding"]))
async def to(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı Değilsiniz\nLütfen Ara ara çekim yapınız.**")
      return'''
   number = await app.ask(chat_id=message.chat.id, text="**Şimdi Üye Alınacak Grubun Kullanıcı Adını Başında @ Olmadan yazın ve Gönderin")
   From = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Şimdi Kendi Grubunun Kullanıcı Adını Başında @ Olacak şekilde yazın ve Gönderin**")
   To = number.text
   number = await app.ask(chat_id=message.chat.id, text="**Kaç numara eklediysen hesap olarak 1 veya 2 veya 3 gibi rakam yazınız.**")
   a = int(number.text)
   di=a
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         for pphone in str_list:
            peer=0
            ra=0
            dad=0
            r="**Adding Start**\n\n"
            phone = utils.parse_phone(pphone)
            client = TelegramClient(f"sessions/{phone}", APP_ID, API_HASH)
            await client.connect()
            await client(JoinChannelRequest(To))
            await app.send_message(chat_id=message.chat.id, text=f"**Üyeler Dızlanıyor Şefim....**")
            async for x in client.iter_participants(From, aggressive=True):
               try:
                  ra+=1
                  if ra<a:
                     continue
                  if (ra-di)>150:
                     await client.disconnect()
                     r+="**\nBotdestek @tutkudestek**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(message.chat.id, f"**Hata: {phone} Bazı Hatalar Nedeniyle Sonrakne Taşınıyor**")
                     break
                  if dad>40:
                     r+="**\nPm 💬 @tommy47shelby**"
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     r="**Adding Start**\n\n"
                     dad=0
                  await client(InviteToChannelRequest(To, [x]))
                  status = 'DONE'
               except errors.FloodWaitError as s:
                  status= f'FloodWaitError for {s.seconds} sec'
                  await client.disconnect()
                  r+="**\nPm 💬 @tutkudestek**"
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  await app.send_message(chat_id=message.chat.id, text=f'**FloodWaitError için {s.seconds} sec\nSonraki Numaraya Geçiniz**')
                  break
               except UserPrivacyRestrictedError:
                  status = 'PrivacyRestrictedError'
               except UserAlreadyParticipantError:
                  status = 'ALREADY'
               except UserBannedInChannelError:
                  status="User Banned"
               except ChatAdminRequiredError:
                  status="To Add Admin Required"
               except ValueError:
                  status="Girişte Hatavar"
                  await client.disconnect()
                  await app.send_message(chat_id=message.chat.id, text=f"{r}")
                  break
               except PeerFloodError:
                  if peer == 20:
                     await client.disconnect()
                     await app.send_message(chat_id=message.chat.id, text=f"{r}")
                     await app.send_message(chat_id=message.chat.id, text=f"**Çok Fazla PeerFloodError\nSonraki Numaraya Geçiniz**")
                     break
                  status = 'Hata... Tekrar deneyiniz.'
                  peer+=1
               except ChatWriteForbiddenError as cwfe:
                  await client(JoinChannelRequest(To))
                  continue
               except errors.RPCError as s:
                  status = s.__class__.__name__
               except Exception as d:
                  status = d
               except:
                  traceback.print_exc()
                  status="Unexpected Error"
                  break
               r+=f"{a-di+1}). **{x.first_name}**   ⟾   **{status}**\n"
               dad+=1
               a+=1
   except Exception as e:
      await app.send_message(chat_id=message.chat.id, text=f"Hata: {e} n\n\ @tutkudestek")
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nBilgi için @tommy47shelby**")
   return



# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["phonesee"]))
async def start(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı Değilsiniz\nLütfen bir Alt Yazıya Sahip Olun\n200rs ayda tahmini ortalama\nPm 💬 @tommy47shelby**")
      return'''
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         de="**Telefon Numaralarınız**\n\n"
         da=0
         dad=0
         for pphone in str_list:
            dad+=1
            da+=1
            if dad>40:
               de+="**\nİletişim ❤️ By @tutkudestek**"
               await app.send_message(chat_id=message.chat.id, text=f"{de}")
               de="**Your Phone Numbers are**\n\n"
               dad=0 
            de+=(f"**{da}).** `{int(pphone)}`\n")
         de+="**\nİletişim ❤️ By @tommy47shelby**"
         await app.send_message(chat_id=message.chat.id, text=f"{de}")

   except Exception as a:
      pass


# ------------------------------- Start --------------------------------- #
@app.on_message(filters.private & filters.command(["remove"]))
async def start(lel, message):
 try:
   a= await Subscribe(lel, message)
   if a==1:
      return
   '''if message.from_user.id not in PREMIUM:
      await app.send_message(message.chat.id, f"**Artık Premium Kullanıcı Değilsiniz\nLütfen bir Alt Yazıya Sahip Olun\n200rs ortalama\nPm 💬 @tommy47shelby**")
      return'''
   try:
      with open(f"Users/{message.from_user.id}/phone.csv", 'r')as f:
         str_list = [row[0] for row in csv.reader(f)]
         f.closed
         number = await app.ask(chat_id=message.chat.id, text="**Kaldırılacak Numarayı Gönder\n\nİletişim için Sahibime yazın @tommy47shelby**")
         print(str_list)
         str_list.remove(number.text)
         with open(f"Users/{message.from_user.id}/1.csv", 'w', encoding='UTF-8') as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(str_list)
         with open(f"Users/{message.from_user.id}/1.csv") as infile, open(f"Users/{message.from_user.id}/phone.csv", "w") as outfile:
            for line in infile:
               outfile.write(line.replace(",", ""))
         await app.send_message(chat_id=message.chat.id,text="Başarıyla Tamamlandı")
   except Exception as a:
      pass
 except Exception as e:
   await app.send_message(message.chat.id, f"**Hata: {e}\n\nEditör 🇹🇷 @tutkudestek**")
   return

# ------------------------------- Admin Pannel --------------------------------- #
@app.on_message(filters.private & filters.command('ishan'))
async def subscribers_count(lel, message):
   a= await Subscribe(lel, message)
   if a==1:
      return
   if message.from_user.id in OWNER:
      but = InlineKeyboardMarkup([[InlineKeyboardButton("Kullanıcı ✅", callback_data="Users")], [InlineKeyboardButton("Broadcast 💯", callback_data="Broadcast")],[InlineKeyboardButton("Kullanıcı Ekle", callback_data="New")], [InlineKeyboardButton("Kullanıcıları Kontrol Et", callback_data="Check")]])
      await app.send_message(chat_id=message.chat.id,text=f"**Hi** `{message.from_user.first_name}` **!\n\nİrregular Bot İLE TEKNOLOJİNİN Yönetici Paneline Hoş Geldiniz\n\nİletişim ❤️ By @tutkudestek**", reply_markup=but)
   else:
      await app.send_message(chat_id=message.chat.id,text="**Bot'un sahibi değilsiniz\n\nBotun Sahibi 🇹🇷 @tommy47shelby ulaşabilirsiniz**")



# ------------------------------- Buttons --------------------------------- #
@app.on_callback_query()
async def button(app, update):
   k = update.data
   if "Login" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yardım için burdayım..!\nSadece tıklayın /login Giriş yapmak ve Hesap istatistiklerini kontrol etmek için**""") 
   elif "Ish" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yardım için burdayım..!\nSadece tıklayın /phonesee Giriş yapmak ve Hesap istatistiklerini kontrol etmek için.**""") 
   elif "Remove" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yardım için burdayım..!\nSadece tıklayın /remove Giriş yapmak ve Hesap istatistiklerini kontrol etmek için.**""") 
   elif "Adding" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yardım için burdayım..!\nSadece tıklayın /adding Giriş'ten eklemeye başlamak için ✅**""") 
   elif "Edit" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yardım için burdayım..!\nSadece tıklayın /phone Giriş yapmak ve Hesap istatistiklerini kontrol etmek için.**""") 
   elif "Home" in k:
      await update.message.delete()
      await app.send_message(update.message.chat.id, """**Yardım için burdayım..!\nSadece tıklayın /start Eve Gitmek için.**""") 
   elif "Users" in k:
      await update.message.delete()
      msg = await app.send_message(update.message.chat.id,"Lütfen bekleyin...")
      messages = await users_info(app)
      await msg.edit(f"Total:\n\nUsers - {messages[0]}\nBlocked - {messages[1]}")
   elif "New" in k:
      await update.message.delete()
      number = await app.ask(chat_id=update.message.chat.id, text="**Yeni Kullanıcının Kullanıcı Kimliğini Gönderiniz.**")
      phone = int(number.text)
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         f.closed
         f = open("data.csv", "w", encoding='UTF-8')
         writer = csv.writer(f, delimiter=",", lineterminator="\n")
         writer.writerow(['sr. no.', 'user id', "Date"])
         a=1
         for i in rows:
            writer.writerow([a, i[1],i[2]])
            a+=1
         writer.writerow([a, phone, date.today() ])
         PREMIUM.append(int(phone))
         await app.send_message(chat_id=update.message.chat.id,text="Başarıyla Tamamlandı")

   elif "Check" in k:
      await update.message.delete()
      with open("data.csv", encoding='UTF-8') as f:
         rows = csv.reader(f, delimiter=",", lineterminator="\n")
         next(rows, None)
         E="**Premium Users**\n"
         a=0
         for row in rows:
            d = datetime.today() - datetime.strptime(f"{row[2]}", '%Y-%m-%d')
            r = datetime.strptime("2022-12-01", '%Y-%m-%d') - datetime.strptime("2022-11-03", '%Y-%m-%d')
            if d<=r:
               a+=1
               E+=f"{a}). {row[1]} - {row[2]}\n"
         E+="\n\n**Pm için  💬 By @tutkudestek**"
         await app.send_message(chat_id=update.message.chat.id,text=E)

   elif "Admin" in k:
      await update.message.delete()
      if update.message.chat.id in OWNER:
         but = InlineKeyboardMarkup([[InlineKeyboardButton("Kullanıcı ✅", callback_data="Users")], [InlineKeyboardButton("Broadcast 💯", callback_data="Broadcast")],[InlineKeyboardButton("Kullanıcı Ekle", callback_data="New")], [InlineKeyboardButton("Kullanıcıları Kontrol Et", callback_data="Check")]])
         await app.send_message(chat_id=update.message.chat.id,text=f"**İrregular Bot İLE TECH Yönetici Paneline Hoş Geldiniz**", reply_markup=but)
      else:
         await app.send_message(chat_id=update.message.chat.id,text="**Bot'un sahibi değilsiniz \n\nSahibime yazın. By @tutkudestek**")
   elif "Broadcast" in k:
    try:
      query = await query_msg()
      a=0
      b=0
      number = await app.ask(chat_id=update.message.chat.id, text="**Şimdi bana Yayın için mesaj verin**")
      phone = number.text
      for row in query:
         chat_id = int(row[0])
         try:
            await app.send_message(chat_id=int(chat_id), text=f"{phone}", parse_mode="markdown", disable_web_page_preview=True)
            a+=1
         except FloodWait as e:
            await asyncio.sleep(e.x)
            b+=1
         except Exception:
            b+=1
            pass
      await app.send_message(update.message.chat.id,f"Başarıyla Yayınlandı {a} Sohbet\nBaşarısız - {b} Sohbet !")
    except Exception as e:
      await app.send_message(update.message.chat.id,f"**Hata: {e}\n\nYardım için @BotHastanesi**")






print("Üye Ekleme Başarılı Bir Şekilde Başladı........")
app.run()
 
