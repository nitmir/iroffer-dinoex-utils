#!/usr/bin/env python
# -*- coding: utf-8 -*-
from iroffer import config

path="/iroffer"
nickserv_pass="password1"
server_list=[("irc.example.net", 6667)]
chan_list=["#channel"]
filedir_list=['/download/']
uploaddir=[]
downloadhost_list=[] # everyone if empty
uploaddir=[] # nobody if empty
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

config(
 mybot=mybot,
 nick=nick,
 path=path,
 nickserv_pass=nickserv_pass,
 server_list=server_list,
 chan_list=chan_list,
 filedir_list=filedir_list,
 autosend_list=autosend_list,
 headline=headline,
 adminpass=adminpass,
 adminhost=adminhost,
 hadminpass=hadminpass,
 hadminhost=hadminhost,
 telnet_port=telnet_port,
 restrictprivlistmsg=restrictprivlistmsg,
 uploaddir=uploaddir,
 uploadhost=uploadhost,
 downloadhost_list=downloadhost_list
)
