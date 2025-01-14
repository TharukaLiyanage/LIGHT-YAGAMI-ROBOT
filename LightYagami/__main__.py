import importlib
import time
import re
from sys import argv
from typing import Optional

from LightYagami import (ALLOW_EXCL, CERT_PATH, DONATION_LINK, LOGGER,
                          OWNER_ID, PORT, SUPPORT_CHAT, TOKEN, URL, WEBHOOK,
                          SUPPORT_CHAT, dispatcher, StartTime, telethn, updater, pgram)
# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from LightYagami.modules import ALL_MODULES
from LightYagami.modules.helper_funcs.chat_status import is_user_admin
from LightYagami.modules.helper_funcs.misc import paginate_modules
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.error import (BadRequest, ChatMigrated, NetworkError,
                            TelegramError, TimedOut, Unauthorized)
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          Filters, MessageHandler)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


PM_START_TEXT = """
𝙸 𝙰𝙼 𝙰 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿 𝙼𝙰𝙽𝙰𝙶𝙴𝙼𝙴𝙽𝚃 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝚂𝙾𝙼𝙴 𝙰𝙽𝙸𝙼𝙴 𝙵𝚄𝙽.
𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙵𝙾𝚁 𝚂𝙿𝙰𝙼 𝙵𝚁𝙴𝙴 𝚁𝚄𝙽𝙽𝙸𝙽𝙶.
================================
>> 𝚃𝙾 𝚂𝙴𝙴 𝙻𝙸𝚂𝚃 𝙾𝙵 𝙰𝙻𝙰𝙸𝙻𝙰𝙱𝙻𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙷𝙸𝚃 /Help.
================================
"""

HELP_STRINGS = """
😈 𝙺𝙸𝚁𝙰 [😈](https://telegra.ph/file/c6fd956f3ea3974020439.jpg) 𝙸𝚂 𝙷𝙴𝚁𝙴
𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁 𝚆𝙸𝚃𝙷 𝚃𝙷𝙴𝚂𝙴 𝙿𝙾𝚆𝙴𝚁
𝙸 𝚆𝙸𝙻𝙻 𝙼𝙰𝙽𝙰𝙶𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿
𝙰𝙽𝙳 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙻𝙸𝙶𝙷𝚃 𝚈𝙰𝙶𝙰𝙼𝙸 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿
✪ /Start : 𝚂𝚃𝙰𝚁𝚃𝚂 𝙼𝙴! 𝚈𝙾𝚄'𝚁𝙴 𝙿𝚁𝙾𝙱𝙰𝙱𝙻𝚈 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝚄𝚂𝙴𝙳 𝚃𝙷𝙸𝚂. 
✪ /Help : 𝙲𝙻𝙸𝙲𝙺 𝚃𝙷𝙸𝚂, 𝙸'𝙻𝙻 𝙻𝙴𝚃 𝚈𝙾𝚄 𝙺𝙽𝙾𝚆 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈𝚂𝙴𝙻𝙵! 
✪ /Settings : 
     ◔ 𝙸𝙽 𝙿𝙼: 𝚆𝙸𝙻𝙻 𝚂𝙴𝙽𝙳 𝚈𝙾𝚄 𝚈𝙾𝚄𝚁 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂 𝙵𝙾𝚁 𝙰𝙻𝙻 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝙴𝙳 𝙼𝙾𝙳𝚄𝙻𝙴𝚂. 
       ◔ 𝙸𝙽 𝙰 𝙶𝚁𝙾𝚄𝙿: 𝚆𝙸𝙻𝙻 𝚁𝙴𝙵𝙻𝙴𝙲𝚃 𝚈𝙾𝚄 𝚃𝙾 𝙿𝙼, 𝚆𝙸𝚃𝙷 𝙰𝙻𝙻 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃'𝚂 𝚂𝙴𝚃𝚃𝙸𝙽𝙶𝚂.
""".format(
    dispatcher.bot.first_name, ""
    if not ALLOW_EXCL else "\nᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ᴇɪᴛʜᴇʀ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ / ᴏʀ !.\n")

SAITAMA_IMG = "https://telegra.ph/file/ec96ed00f0762e47ba35b.jpg"
LIGHT_IMG = "https://telegra.ph/file/04187c8699b523c6e796f.mp4"

DONATE_STRING = """ɴᴏ ɴᴇᴇᴅ ɪ'ᴍ ʀɪᴄʜ!
"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("LightYagami.modules." +
                                              module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception(
            "Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_message(
        chat_id=chat_id,
        text=text,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=False,
        reply_markup=keyboard)


@run_async
def test(update: Update, context: CallbackContext):
    # pprint(eval(str(update)))
    # update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("This person edited a message")
    print(update.effective_message)


@run_async
def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split('_', 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id, HELPABLE[mod].__help__,
                    InlineKeyboardMarkup([[
                        InlineKeyboardButton(
                            text="Back", callback_data="help_back")
                    ]]))
            elif args[0].lower() == "markdownhelp":
                IMPORTED["extras"].markdown_help_sender(update)
            elif args[0].lower() == "disasters":
                IMPORTED["disasters"].send_disasters(update)
            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(
                        match.group(1), update.effective_user.id, False)
                else:
                    send_settings(
                        match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_photo(
                SAITAMA_IMG,
                PM_START_TEXT.format(
                    escape_markdown(first_name),
                    escape_markdown(context.bot.first_name)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="➕ α∂∂ мє тσ уσυя gяσυρ ➕",
                            url="t.me/LIGHT_YAGAMI_ROBOT?startgroup=true".format(context.bot.username))
                    ],
                     [
                         InlineKeyboardButton(
                             text="🎯 ѕυρρσят gяσυρ 🎯",
                             url=f"https://t.me/KIRASUPPORT"),
                         InlineKeyboardButton(
                             text="🔀 ʝσιη ƒσя υρ∂αтєѕ 🔀",
                             url="https://t.me/KIRAUPDATESS")
                     ],
                    
                    [
                         InlineKeyboardButton(
                             text="🔴 ѕσυя¢є ¢σ∂є 🔴",
                             url="https://github.com/ITZ-DEVIL-OP/LIGHT-YAGAMI-ROBOT"),
                         InlineKeyboardButton(
                             text="🇮🇳 уαgαмι ∂єνѕ 🇮🇳",
                             url="t.me/KIRA_DEVS")
                     ],[
                        InlineKeyboardButton(
                            text="👻 нєℓρ αη∂ ¢σммαη∂ѕ 👻",
                            url="t.me/light_yagami_robot?start=help".format(context.bot.username))
                    ]]))
    else:
        update.effective_message.reply_video(
                LIGHT_IMG, caption=f"======❤ 𝐇𝐞𝐥𝐥𝐨 𝐈'𝐌 𝐊𝐢𝐫𝐚 😈 𝐋𝐞𝐭'𝐬 𝐊𝐢𝐥𝐥 𝐁𝐚𝐝 𝐏𝐞𝐨𝐩𝐥𝐞𝐬\n𝐁𝐲 𝐖𝐫𝐢𝐭𝐢𝐧𝐠 𝐓𝐡𝐨𝐬𝐞 𝐍𝐚𝐦𝐞 𝐎𝐧 𝐃𝐞𝐚𝐭𝐡 𝐍𝐨𝐭𝐞 ❤======")      
# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


@run_async
def help_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = ("Here is the help for the *{}* module:\n".format(
                HELPABLE[module].__mod_name__) + HELPABLE[module].__help__)
            query.message.reply_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="Back", callback_data="help_back")
                ]]))

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")))

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")))

        elif back_match:
            query.message.edit_text(
                text=HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")))

        # ensure no spinny white circle
        context.bot.answer_callback_query(query.id)
        # query.message.delete()

    except BadRequest:
        pass


@run_async
def get_help(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_text(
                f"Contact me in PM to get help of {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="Help",
                        url="t.me/{}?start=ghelp_{}".format(
                            context.bot.username, module))
                ]]))
            return
        update.effective_message.reply_text(
            "ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴘᴏssɪʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    text="🖤 ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴍᴇ ʜᴇʟᴘ 🖤",
                    url="t.me/LIGHT_YAGAMI_ROBOT?start=help".format(context.bot.username))
            ]]))
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = "Here is the available help for the *{}* module:\n".format(HELPABLE[module].__mod_name__) \
               + HELPABLE[module].__help__
        send_help(
            chat.id, text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="𝗚𝗢 𝗕𝗔𝗖𝗞 🔥",
                                       callback_data="help_back")]]))

    else:
        send_help(chat.id, HELP_STRINGS)


def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join("*{}*:\n{}".format(
                mod.__mod_name__, mod.__user_settings__(user_id))
                                   for mod in USER_SETTINGS.values())
            dispatcher.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN)

        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN)

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(
                user_id,
                text="Which module would you like to check {}'s settings for?"
                .format(chat_name),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)))
        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any chat settings available :'(\nSend this "
                "in a group chat you're admin in to find its current settings!",
                parse_mode=ParseMode.MARKDOWN)


@run_async
def settings_button(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* has the following settings for the *{}* module:\n\n".format(escape_markdown(chat.title),
                                                                                     CHAT_SETTINGS[module].__mod_name__) + \
                   CHAT_SETTINGS[module].__chat_settings__(chat_id, user.id)
            query.message.reply_text(
                text=text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="Back",
                        callback_data="stngs_back({})".format(chat_id))
                ]]))

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id)))

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                "Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id)))

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            query.message.reply_text(
                text="Hi there! There are quite a few settings for {} - go ahead and pick what "
                "you're interested in.".format(escape_markdown(chat.title)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)))

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message == "Message is not modified":
            pass
        elif excp.message == "Query_id_invalid":
            pass
        elif excp.message == "Message can't be deleted":
            pass
        else:
            LOGGER.exception("Exception in settings buttons. %s",
                             str(query.data))


@run_async
def get_settings(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ᴛʜɪs ᴄʜᴀᴛ's sᴇᴛᴛɪɴɢs, ᴀs ᴡᴇʟʟ ᴀs ʏᴏᴜʀs."
            msg.reply_text(
                text,
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        text="🖤 ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴍᴇ sᴇᴛᴛɪɴɢs 🖤",
                        url="t.me/LIGHT_YAGAMI_ROBOT?start=stngs_{}".format(
                            context.bot.username, chat.id))
                ]]))
        else:
            text = "ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs."

    else:
        send_settings(chat.id, user.id, True)


@run_async
def donate(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]
    bot = context.bot
    if chat.type == "private":
        update.effective_message.reply_text(
            DONATE_STRING,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True)

        if OWNER_ID != 254318997 and DONATION_LINK:
            update.effective_message.reply_text(
                "You can also donate to the person currently running me "
                "[here]({})".format(DONATION_LINK),
                parse_mode=ParseMode.MARKDOWN)

    else:
        try:
            bot.send_message(
                user.id,
                DONATE_STRING,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)

            update.effective_message.reply_text(
                "I've PM'ed you about donating to my creator!")
        except Unauthorized:
            update.effective_message.reply_text(
                "Contact me in PM first to get donation information.")


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop


def main():

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.sendMessage(f"@YAGAMIBOT_SUPPORT", "Time To Write Names On Death Note")
        except Unauthorized:
            LOGGER.warning(
                "Bot isnt able to send message to support_chat, go and check!")
        except BadRequest as e:
            LOGGER.warning(e.message)

    test_handler = CommandHandler("test", test)
    start_handler = CommandHandler("start", start)

    help_handler = CommandHandler("help", get_help)
    help_callback_handler = CallbackQueryHandler(
        help_button, pattern=r"help_.*")

    settings_handler = CommandHandler("settings", get_settings)
    settings_callback_handler = CallbackQueryHandler(
        settings_button, pattern=r"stngs_")

    donate_handler = CommandHandler("donate", donate)
    migrate_handler = MessageHandler(Filters.status_update.migrate,
                                     migrate_chats)

    # dispatcher.add_handler(test_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(settings_handler)
    dispatcher.add_handler(help_callback_handler)
    dispatcher.add_handler(settings_callback_handler)
    dispatcher.add_handler(migrate_handler)
    dispatcher.add_handler(donate_handler)

    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(
                url=URL + TOKEN, certificate=open(CERT_PATH, 'rb'))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4, clean=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pgram.start()
    main()
