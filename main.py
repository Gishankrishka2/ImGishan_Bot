import logging

from pyrogram import Client, idle

from vars import var

logging.getLogger("pyrogram").setLevel(logging.INFO)

PmBot = Client(
    "Pm Bot",
    api_id=var.API_ID,
    api_hash=var.API_HASH,
    bot_token=var.BOT_TOKEN,
    plugins=dict(root="plugins"),
)

PmBot.start()
uname = (PmBot.get_me()).username
print(f"""
╭━━╮╱╱╱╭━━━┳╮
╰┫┣╯╱╱╱┃╭━╮┃┃
╱┃┃╭╮╭╮┃┃╱┃┃┃╭┳╮╭┳━━╮
╱┃┃┃╰╯┃┃╰━╯┃┃┣┫╰╯┃┃━┫
╭┫┣┫┃┃┃┃╭━╮┃╰┫┣╮╭┫┃━┫
╰━━┻┻┻╯╰╯╱╰┻━┻╯╰╯╰━━╯

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖
{uname} has been deployed!
➖➖➖➖➖➖➖➖➖➖
Support: @ImGishan
➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

idle()
