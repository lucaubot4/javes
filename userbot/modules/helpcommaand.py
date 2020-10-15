from userbot.events import javes05, rekcah05
from userbot import bot as javes, CMD_HELP
import os

IN = os.environ.get("INLINE_MODE", None)


if not IN:
 @javes05(outgoing=True, pattern="^!help(?: |$)(.*)")
 async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`Tipo di modulo sconosciuto! help per vedere tutti i moduli`")
    else:
        await event.edit(" Ubot di @DarkLukeclapyou")
        string = (f"`Usa !help <module_name>`\n\n**Attualmente caricato [{len(CMD_HELP)}] Moduli **\n")
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
 




@javes.on(rekcah05(pattern=f"help(?: |$)(.*)", allow_sudo=True))
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.reply(str(CMD_HELP[args]))
        else:
            await event.reply("`Tipo di modulo sconosciuto! help per vedere tutti i moduli`")
    else:
        await event.reply("Ubot di @DarkLukeclapyou")
        string = (f"`Usa .help <module_name>`\n\n**Attualmente caricato [{len(CMD_HELP)}] Moduli **\n")
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)





        







CMD_HELP.update({
    "locks":
    "!lock <all (or) type(s)> or !unlock <all (or) type(s)>\
\nUsage: Ti consente di bloccare / sbloccare alcuni tipi di messaggi comuni nella chat. \ [NOTA: richiede i diritti di amministratore appropriati nella chat !!] \ \ n \ nI tipi di messaggi disponibili da bloccare / sbloccare sono: \
\n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`"
})


CMD_HELP.update({
    "chat":
    "!chatid\
\nUsage: Recupera l'ID della chat corrente \
\n\n!userid\
\nUsage: Recupera l'ID dell'utente in risposta, se è un messaggio inoltrato, trova l'ID dell'origine.\
\n\n!chatinfo\
\nUsage: Recupera le informazioni del gruppo\
\n\n!log\
\nUsage: Inoltra il messaggio a cui hai risposto nel tuo gruppo di log del bot.\
\n\n!invite\
\nUsage: !invite <username> invitare l'utente al gruppo.\
\n\n!kickme\
\nUsage: Parti da un gruppo mirato.\
\n\n!link <username/userid> : <testo facoltativo> (o) rispondi al messaggio di qualcuno con! link <testo facoltativo> \ \ nUtilizzo: genera un collegamento permanente al profilo dell'utente con testo personalizzato facoltativo. " })

CMD_HELP.update({
    "filter":
    "!checkfilter\
    \nUsage:Elenca tutti i filtri userbot attivi in ​​una chat.\
    \n\n!savefilter rispondi a un messaggio con! savefilter <tastiera>\
    \nUsage: Salva il messaggio con risposta come risposta alla 'parola chiave'.\
    \nIl bot risponderà al messaggio ogni volta che viene menzionata 'parola chiave'. \
     \ nFunziona con qualsiasi cosa, dai file agli adesivi. \
    \n\n!clearfilter <filtro>\
    \nUsage: Arresta il filtro specificato. \
    \n\n!clearallfilter \
    \nUsage: Stoppa tutti i filtri.\
    \n\n!savefilter2 ,  !checkfilter2,  clearfilter2\
    \nUsage: uguale al filtro "
})


CMD_HELP.update({
    "stickers":
    "!kang\
\nUsage: Rispondi! Kang a un adesivo o un'immagine per associarlo al tuo pacchetto userbot. \
 \ n \ n! kang [emoji ('s)] \
\nUsage: Funziona proprio come! Kang ma usa le emoji che hai scelto. \
 \ n \ n! kang [numero] \
\nUsage: Kang è l'adesivo / immagine per il pacchetto specificato \
 \ n \ n! kang [emoji ('s)] [numero] \
\nUsage:Kang è l'adesivo / immagine per il pacchetto specificato e utilizza le emoji che hai scelto. \
 \ n \ n! stickerinfo \
\nUsage: Ottiene informazioni sul pacchetto di adesivi. \
 \ n \ n! ss \
\nUsage: converti il ​​testo dell'utente in un adesivo come lo screenshot di un adesivo \
\ n \ n! ss2 \
\nUsage: Converti immagine in adesivo \
\ n \ n! testo \
\nUsage: testo sull'adesivo \ \ n \ n! text2 \
\nUsage: uguale a! text ma può usare caratteri personalizzati come! text font | messaggio ex -! text2 font | lol \ \ n \ n! friggere \
\nUsage: rendere divertente la data immagine \
"
})



CMD_HELP.update({
    "beta":
    "!mail\
\nUsage: Crea un falso principale ed elencalo \
\ n \ n! ushort \
\nUsage: accorcia l'URL. \
\ n \ n! song2 \
\nUsage: trova la canzone di destinazione \
\ n \ n! lyrics2 [emoji ('s)] [numero] \
\nUsage: ottieni il testo della canzone \
\ n \ n!mask\
\nUsage: crea una maschera per foto / adesivo taggato \
"
})



CMD_HELP.update({
    "blacklist":
    "!checkblacklist\
    \nUsage:Elenca tutte le blacklist di userbot attive in una chat. \
    \n \n! saveblacklist <keyword> <reply text> o rispondi a un messaggio con! saveblacklist <keyword> \
    \nUsage: Elimina quindi i reparti nella lista nera dei non amministratori. \
     \n \n!clearblacklist <ward> \
    \nUsage: Arresta il reparto della lista nera specificato."
})


CMD_HELP.update({
    "sudo":
  "se attivi sudo, gli utenti sudo possono controllare i tuoi javes come se tu controllassi i bot di gestione del gruppo \
  \npuoi attivare sudo con! set var SUDO_USERS <id del tuo utente sudo> \
   \n \npuoi attivare più utenti sudo in base allo spazio tra ogni ID \
   \ncheck sudo di .sudo nell'account utente sudo \
    \n video di esempio: - https://t.me/javes05/116 \
     \n (!) comando per il proprietario del bot, (.) comando per gli utenti sudo come! ban per il proprietario, .ban per gli utenti sudo \
      \n \n sudo normale disabilitato per alcuni comandi a causa della privacy, se desideri l'accesso completo a sudo puoi impostare FULL_SUDO come True in herolu var \
"
})




CMD_HELP.update({
    "others":
    "comming soon!\
    \n stanno arrivando\
"
})

