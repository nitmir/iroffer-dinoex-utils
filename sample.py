#!/usr/bin/env python
# -*- coding: utf-8 -*-
from iroffer import config

path="/iroffer"
nickserv_pass="password1"
server_list=[("irc.example.net", 6667)]
chan_list=["#channel"]
filedir_list=['/download/']
autosend_list=[(-1, '!list', "XDCC listing")]
adminhost=[
 "telnet!*@telnet",
 "*!*@example.fr",
]
hadminhost=[
 "*!~user@domain.tld",
]
adminpass="password2"
hadminpass="password3"

mybot = "sample"
nick = "[XDCC]`%s" % mybot
headline="Listing disponible en pack #-1 ou ici: http://xdcc.listing.tld/%5BXDCC%5D%60MyBot/"
restrictprivlistmsg=headline
telnet_port = ((sum(ord(i) for i in mybot) % 100) + 2323)

config(mybot, nick, path, nickserv_pass, server_list, chan_list, filedir_list, autosend_list, headline, adminpass, adminhost, hadminpass, hadminhost, telnet_port, restrictprivlistmsg)
