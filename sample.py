#!/usr/bin/env python
# -*- coding: utf-8 -*-
from iroffer import config

path="/etc/iroffer" # path from inside the chroot if chrooted
nickserv_pass="password1"
server_list=[("irc.example.net", 6667)]
chan_list=["#channel"]

filedir_list=[]
uploaddir_list=[]

downloadhost_list=[] # everyone if empty
uploadhost_list=[] # nobody if empty

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
headline="Listing available at pack #-1 or here: http://xdcc.listing.tld/%5BXDCC%5D%60MyBot/"
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
 uploaddir_list=uploaddir_list,
 uploadhost_list=uploadhost_list,
 downloadhost_list=downloadhost_list
)
