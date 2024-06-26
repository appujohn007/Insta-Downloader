from pyrogram import filters,Client as Mbot
from bot import LOG_GROUP,DUMP_GROUP
import os,re,asyncio,bs4
import requests,wget,traceback

@Mbot.on_message(filters.regex(r'https?://.*twitter[^\s]+') & filters.incoming | filters.regex(r'https?://(?:www\.)?x\.com/\S+') & filters.incoming,group=-5)
async def twitter_handler(Mbot, message):
   try:            
      link=message.matches[0].group(0)
      if "x.com" in link:
         link=link.replace("x.com","fxtwitter.com")
      elif "twitter.com" in link:
         link = link.replace("twitter.com","fxtwitter.com")
      m=await message.reply_sticker("CAACAgIAAxkBATWhF2Qz1Y-FKIKqlw88oYgN8N82FtC8AAJnAAPb234AAT3fFO9hR5GfHgQ")
      try:
          dump_file = await message.reply_video(link,caption="✦ ᴋɪɴᴅʟʏ ᴊᴏɪɴ [•𝖎𝖔 𝕯𝖊𝖛𝖘](https://t.me/botio_devs)")
      except Exception as e:
          print(e)
          try:
             snd_message=await message.reply(link)
             await asyncio.sleep(1)
             dump_file = await message.reply_video(link,caption="✦ ᴋɪɴᴅʟʏ ᴊᴏɪɴ [•𝖎𝖔 𝕯𝖊𝖛𝖘](https://t.me/botio_devs)")
             await snd_message.delete()
          except Exception as e:
              print(e)
              await snd_message.delete()
              get_api=requests.get(link).text
              soup=bs4.BeautifulSoup(get_api,"html.parser")
              meta_tag= soup.find("meta", attrs = {"property": "og:video"})
              if not meta_tag:
                  meta_tag = soup.find("meta", attrs={"property": "og:image"})
              content_value  = meta_tag['content']
              try:
                  dump_file = await message.reply_video(content_value,caption="✦ ᴋɪɴᴅʟʏ ᴊᴏɪɴ [•𝖎𝖔 𝕯𝖊𝖛𝖘](https://t.me/botio_devs)")
              except Exception as e:
                  print(e)
                  try:
                     snd_msg=await message.reply(content_value)
                     await asyncio.sleep(1)
                     await message.reply_video(content_value,caption="✦ ᴋɪɴᴅʟʏ ᴊᴏɪɴ [•𝖎𝖔 𝕯𝖊𝖛𝖘](https://t.me/botio_devs)")
                     await snd_msg.delete()
                  except Exception as e:
                      print(e)
                      await message.reply("Oops Invalid link or Media Is Not Available:)")
   except Exception as e:
        print(e)
        if LOG_GROUP:
           await Mbot.send_message(LOG_GROUP,f"{e} {message.chat.id}")
           await Mbot.send_message(LOG_GROUP,traceback.format_exc())
   finally:
       if DUMP_GROUP:
          if "dump_file" in locals():
             await dump_file.copy(DUMP_GROUP)
       await m.delete()

            
