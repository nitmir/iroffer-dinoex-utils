#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--telnet", type=str, help="parth to telnet port file")

version = "3.30"

def parse_arguments(telnet_port):
    args = parser.parse_args()
    if args.telnet and telnet_port:
        with open(args.telnet, 'w') as f:
            f.write("%s\n" % telnet_port)


def config(mybot, nick, path, nickserv_pass, server_list, chan_list, filedir_list, autosend_list,
           headline, adminpass, adminhost, hadminpass, hadminhost, telnet_port=None, restrictprivlistmsg=None,
           uploaddir_list=[], uploadhost_list=[], downloadhost_list=[]):
    parse_arguments(telnet_port)
##############################################################################
##                       iroffer 1.4.b03 config file                        ##
##            lines starting with "#" or are blank are ignored              ##
##############################################################################

# Version of this file:
#
# $Id$
#

##############################################################################
##                                  FILES                                   ##
##############################################################################

##############################################################################
###                             - pid file -                               ###
### Writes the process id to this file on startup                          ###

    print "pidfile %s/pid/%s.pid" % (path, mybot)

##############################################################################
###                             - log file -                               ###
### Writes logging information to this file.                               ###
    print "logfile %s/log/%s.log" % (path, mybot)

##############################################################################
###                            - log rotate -                              ###
### After the time given here a logfile will be rotated.                   ###
### logrotate can be set to none, 1 - 24 hours, daily, weekly or monthly   ###
    print "logrotate weekly"

##############################################################################
###                         - expire logfiles -                            ###
### After the given number of days the old logfiles are deleted.           ###
### This will only be checked after logrotate.                             ###
### Default: logfiles are not deleted.                                     ###
#expire_logfiles 31

##############################################################################
###                            - log stats -                               ###
### Setting logstats will log statistical information and this will also   ###
###  send this stats to a dcc chat if one is active.                       ###
    print "logstats yes"

##############################################################################
###                             - state file -                             ###
### temporary storage for iroffer state information across restarts        ###
    print "statefile %s/state/%s.state" % (path, mybot)

##############################################################################
###                          - old state file -                            ###
### Writes smaller iroffer statefile by default. Set this option to write  ###
### a statefile that is compatible with old versions.                      ###
### WARNING!!  You need this option for the PHP weblist iroffer-state.php  ###
###            version 2.10 and below.                                     ###
#old_statefile

##############################################################################
###                          - send state file -                           ###
### send statefile every hour via DCC to the specified nick                ###
#send_statefile XDCC|statistik

##############################################################################
###                      - send state file minute -                        ###
### send statefile every hour via when the minute matches                  ###
#send_statefile_minute 0

##############################################################################
###                         - xdcc listing file -                          ###
### if you want to export your xdcc list via a webserver, or other means   ###
### define 'xdcclistfile' and iroffer will write the xdcc list to it when  ###
### needed.                                                                ###
### If xdcclistfileraw is set the file will be written with the IRC        ###
### control characters included (color, formatting, etc..).                ###
    print "xdcclistfile %s/list/%s.txt" % (path, mybot)
#xdcclistfileraw

##############################################################################
###                     - xdcc listing group only  -                       ###
### Export your xdcc list with group and main information only.            ###
### Default output is all packs and no group information.                  ###
#xdcclist_grouponly

##############################################################################
###                         - group seperator -                            ###
### printed between group name and group description.                      ###
### Default: space                                                         ###
#group_seperator " "
    print 'group_seperator " - "'

##############################################################################
###                         - dos text files -                             ###
### Write xdcclistfile as DOS text format, with CRLF als line break.       ###
### Default: no, on CYGWIN Default: yes                                    ###
#dos_text_files yes
#dos_text_files no

##############################################################################
###                          - send listfile -                             ###
### Packnumber of xdcclistfile added to the bot, enables XDCC SEND LIST.   ###
### A value of -1 will send the xdcclistfile without creating a pack.      ###
### Default: off                                                           ###
#send_listfile 1
    print "send_listfile -1"

##############################################################################
###                           - xdcc xml file -                            ###
### if you want to export your packlist in XML define xdccxmlfile.         ###
#xdccxmlfile mybot.xml
    print "xdccxmlfile %s/list/%s.xml" % (path, mybot)

##############################################################################
###                              - charset -                               ###
### This must be set to the encoding of your filenames.                    ###
### The charset in header.html must match to this.                         ###
### Default: UTF-8                                                         ###
#charset UTF-8
#charset iso-8859-1

##############################################################################
###                      - xdcc list by privmsg  -                         ###
### send the result of XDCC LIST by privmsg instead of notice.             ###
### Default: notice                                                        ###
#xdcclist_by_privmsg

##############################################################################
###                         - xdcc remove file -                           ###
### export stats on removed packs for better statistics.                   ###
#xdccremovefile mybot.removed.xdcc

##############################################################################
###                          - admin job file -                            ###
### when defined, read this file for commands and execute them.            ###
#admin_job_file mybot.job

##############################################################################
###                       - admin job done file -                          ###
### Write the output from the commands in "admin_job_file" into this file. ###
### Default: <admin_job_file>.done                                         ###
#admin_job_done_file mybot.done

##############################################################################
###                            - http port -                               ###
### Port for the build-in webserver.                                       ###
### Default: 0 = disabled.                                                 ###
#http_port 8000

##############################################################################
###                         - http access log -                            ###
### If defined, iroffer will log http request in CLF compatible format.    ###
### Default: disabled.                                                     ###
#http_access_log httpd_access.log

##############################################################################
###                            - http vhost -                              ###
### List of up to 2 local IP addresses for the Webserver to run on.        ###
### Use "::" or "0.0.0.0" to allow any IP address.                         ###
### Use "::1" or "127.0.0.1" to limit access to localhost only.            ###
### Default: disabled.                                                     ###
#http_vhost ::
#http_vhost 0.0.0.0

##############################################################################
###                            - http admin -                              ###
### Defines admin login for the build-in webserver.                        ###
### Default: disabled.                                                     ###
#http_admin superuser

##############################################################################
###                            - http allow -                              ###
### Defines ip networks, which are allowed to access the server.           ###
### Multiple ip networks can be specified                                  ###
### Default: all.                                                          ###
#http_allow 127.0.0.1
#http_allow 192.168.1.0/24

##############################################################################
###                            - http deny -                               ###
### Defines ip networks, that should not access the server.                ###
### Multiple ip networks can be specified                                  ###
### Default: none.                                                         ###
#http_deny 172.16.0.0/16

##############################################################################
###                            - http dir -                                ###
### Defines directory for extra files handled out by the webserver.        ###
### For example: robots.txt favicon.ico                                    ###
### Default: disabled.                                                     ###
#http_dir htdocs

##############################################################################
###                        - http admin dir -                              ###
### Defines directory for protected files handled out by the webserver     ###
### for the admin user.                                                    ###
### Default: disabled.                                                     ###
#http_admin_dir htadmin

##############################################################################
###                            - http date -                               ###
### Define output from of dates on the webpage.                            ###
### Default: %Y-%m-%d %H:%M                                                ###
#http_date %Y-%m-%d %H:%M

##############################################################################
###                            - http search -                             ###
### Enables search form in HTML page.                                      ###
### Default: disabled.                                                     ###
#http_search

##############################################################################
###                            - http index -                              ###
### Defines the page to show when no filename is given in the URL.         ###
### Default: xdcclistfile                                                  ###
### For Weblist set: http_index /?                                         ###
### For your own static page in htdocs set: http_index /index.html         ###
#http_index /?

##############################################################################
###                          - http forbidden -                            ###
### Defines the URL page to show when access is forbidden.                 ###
### The given URL must resolve in a file in http_dir.                      ###
### Default: Send only the HTTP error.                                     ###
#http_forbidden /forbidden.html

##############################################################################
###                            - http geoip -                              ###
### Enables geoip country check for HTTP requests.                         ###
### Default: disabled.                                                     ###
#http_geoip

##############################################################################
###                           - weblist info -                             ###
### Show additional information in the HTML page.                          ###
#weblist_info uptime "Uptime"
#weblist_info running "Total Uptime"
#weblist_info minspeed "Min speed"
#weblist_info maxspeed "Max speed"
#weblist_info cap "Max bandwidth"
#weblist_info record "Record bandwidth"
#weblist_info send "Record download"
#weblist_info daily "Traffic today"
#weblist_info weekly "Traffic this week"
#weblist_info monthly "Traffic this month"

##############################################################################
###                            - mime type -                               ###
### Define additional mime types for the HTML pages.                       ###
#mime_type torrent application/x-bittorrent

##############################################################################
###                           - telnet port -                              ###
### Port for the build-in Telnet server.                                   ###
### To login you must add adminhost or hadminhost with "telnet!*@telnet"   ###
### Default: 0 = disabled.                                                 ###
    print "telnet_port %s" % telnet_port

##############################################################################
###                           - telnet vhost -                             ###
### List of up to 2 local IP addresses for the Telnet server to run on.    ###
### Use "::" or "0.0.0.0" to allow any IP address.                         ###
### Use "::1" or "127.0.0.1" to limit access to localhost only.            ###
### Default: disabled.                                                     ###
#telnet_vhost ::1
    print "telnet_vhost 127.0.0.1"

##############################################################################
###                           - telnet allow -                             ###
### Defines ip networks, which are allowed to access the bot via telent.   ###
### Multiple ip networks can be specified                                  ###
### Default: all.                                                          ###
    print "telnet_allow 127.0.0.1"
#telnet_allow 192.168.1.0/24

##############################################################################
###                           - telnet deny -                              ###
### Defines ip networks, that should not access the bot via telnet.        ###
### Multiple ip networks can be specified                                  ###
### Default: none.                                                         ###
#telnet_deny 172.16.0.0/16

##############################################################################
##                                   IRC                                    ##
##############################################################################

##############################################################################
###                         - network name -                               ###
### Start a new set of servers/channels for a different irc network.       ###
### The bot supports identifying via an self signed SSL certificate.       ###
### See: http://www.oftc.net/oftc/NickServ/CertFP                          ###
### The bot looks for the file "<networkname>.pem" which must hold cert    ###
### and key. If this file is not found it looks for "<networkname>.crt"    ###
### and and "<networkname>.key".                                           ###
### The found certificate is passed to the server on connect.              ###
#network irc.efnet.net

##############################################################################
###                          - connection method -                         ###
### How should iroffer connect to the irc server.  Choices are:            ###
###  direct                      - connect directly to the irc server      ###
###  ssl                         - connect to the irc server via SSL.      ###
###                                Make sure to connect to ssl compatible  ###
###                                port of your irc server.                ###
###  bnc <ip> <port> <password> <vhost>                                    ###
###                              - connect to the irc server through a bnc ###
###                                relay at <ip>:<port> using <password>   ###
###                                <vhost> is optional                     ###
###  wingate <ip> <port>         - connect to the irc server through a     ###
###                                wingate relay at <ip>:<port>            ###
###  custom <ip> <port>          - connect to the irc server through a     ###
###                                custom set of commands, see proxyinfo   ###
###                                below for more information              ###
### most people will want to use the direct                                ###
    print "connectionmethod direct"

##############################################################################
###                       - custom connection info -                       ###
### if you use connectionmethod of custom you can place any number of      ###
### custom lines for use with your proxy/gateway/redirector. Place "$s"    ###
### and "$p" where the server and port should be placed in your text       ###
#proxyinfo connect $s:$p
#proxyinfo blah blah

##############################################################################
###                       - server connect timeout -                       ###
### Set the starting timeout in seconds on connect to the IRC-server.      ###
### This setting can only be set per network.                              ###
### Default: 5                                                             ###
#server_connect_timeout 10

##############################################################################
###                         - onjoin information -                         ###
### you can use server_join_raw to send raw IRC commands to the server     ###
### when connected (sent after NICK, USER, before MODE )                   ###
###                                                                        ###
### you can use server_connected_raw to send raw IRC commands to the       ###
### server when connected (sent after MODE, before JOIN )                  ###
###                                                                        ###
### you can use channel_join_raw to send raw IRC commands to the           ###
### server when you join a channel (multiple instances can be configured   ###
### if needed)                                                             ###
###                                                                        ###
### multiple instances of all 3 can be configured if needed                ###
#server_join_raw
#server_connected_raw
#channel_join_raw

##############################################################################
###                            - virtual hosts -                           ###
### If the computer you want to run iroffer on has multiple local IP       ###
### addresses, you can run iroffer on any of those IP addresses.           ###
### To automatically choose a local IP address leave undefined.            ###
### This setting can be global or per network.                             ###
### NOTE:  You must use the IP address in x.x.x.x format not a DNS name.   ###
### To restrict to IPv4 use local_vhost 0.0.0.0                            ###
### To restrict to IPv6 use local_vhost ::                                 ###
#local_vhost 123.456.789.123

##############################################################################
###                      - manual dcc ip translation -                     ###
### if you are behind a NAT (Network Address Translation) device which     ###
### _does_ _not_ intercept and translate dcc commands but _does_ do port   ###
### forwarding place the ip address of the NAT below if unsure, leave      ###
### commented                                                              ###
### NOTE:  You must use the IP address in x.x.x.x format not a DNS name.   ###
#usenatip 1.2.3.4

##############################################################################
###                      - automatic dcc ip translation -                  ###
### Get my own IP from the irc server and use this as value for usenatip.  ###
### Set usenatip to a default value (0.0.0.0) when using this option.      ###
#getipfromserver

##############################################################################
###                      - automatic dcc ip translation -                  ###
### Get my own IP from the upnp router and use this as value for usenatip. ###
### Set usenatip to a default value (0.0.0.0) when using this option.      ###
#getipfromupnp

##############################################################################
###                         - get ip from network -                        ###
### Get my own IP for the current Network from a different network.        ###
### You need this when the given network does not return your IP.          ###
#getip_network 1

##############################################################################
###                             - noannounce -                             ###
### Disable all announces for the current network.                         ###
#noannounce

##############################################################################
###                             - plaintext -                              ###
### Disable colors when announcing on this network.                        ###
#plaintext

##############################################################################
###                              - offline -                               ###
### Disable connecting to this network.                                    ###
#offline

##############################################################################
###                             - nickserv -                               ###
### If you would like to register with nickserv add settings here.         ###
### This setting can be global or per network.                             ###
    if nickserv_pass:
        print "nickserv_pass %s" % nickserv_pass

##############################################################################
###                             - auth name -                              ###
### If you would like to register with the AUTH command you need to define ###
### the name if the service you have to use here.                          ###
### This setting can only be set per network.                              ###
#auth_name Q@CServe.quakenet.org

##############################################################################
###                            - login name -                              ###
### If you would like to register with the LOGIN command you need to       ###
### define the name if the service you have to use here.                   ###
### This setting can only be set per network.                              ###
#login_name X@channels.undernet.org

##############################################################################
###                         - server information -                         ###
### List server/ports in the form "server irc.domain.com 6667". Port is    ###
### optional (default 6667).  Server password should be listed 3rd if      ###
### needed (port must be specified if using a password).                   ###
### Multiple servers can be specified                                      ###
#server irc.efnet.net
#server irc.efnet.net 6667
#server irc.efnet.net 6667 server-password
    for (server, port) in server_list:
      print "server %s %s" % (server, port)

##############################################################################
###                         - channels (up to 50) -                        ###
### channel format:                                                        ###
### "channel <channel> [-plist <time>] [-plistoffset <time>]               ###
###    [-pformat <full|minimal|summary>] [-pgroup <group>] [-key <key>]    ###
###    [-delay <time>] [-noannounce] [-joinmsg "text"] [-headline "text"]  ###
###    [-fish <key>] [-listmsg "text"] [-rgroup "group1 group2"]           ###
###    [-notrigger] [-plaintext] [-waitjoin <time>]                        ###
### plist:       <time> is number of minutes between plists. Using same or ###
###              multiples of the same number plist time is recommended.   ###
### plistoffset: <time> is number of minutes to offset list.               ###
### pformat:     "full" is normal and default if pformat is not used.      ###
###              "minimal" is similar to full but removes some lines.      ###
###              "summary" displays only a 2 line summary.                 ###
### pgroup:      Send normal list of <group> to channel.                   ###
### key:         For +k channels, the key specified is used when joining.  ###
### delay:       Delay output to channel by <time> seconds between lines.  ###
### noannounce:  No extra announces on this channel.                       ###
### joinmsg:     After join, post <text> to the channel.                   ###
### headline:    <text> after this keyword is used as a channel specific   ###
###              headline.                                                 ###
### fish:        For encrypted channels, the <key> specified is used when  ###
###              posting into that channel and parsing triggers in it.     ###
### listmsg:     <text> is used as a channel specific                      ###
###              respondtochannellistmsg.                                  ###
### rgroup:      Users in this channel can only access packs in groups     ###
###              group1 or group2, or packs in main pool.                  ###
### notrigger:   No triggers are active in this channel.                   ###
### plaintext:   Disable colors when announcing for this channel.          ###
### waitjoin:    Wait given seconds after connect before joining this      ###
###              channel.                                                  ###
#channel #chan01
#channel #chan02 -plist 14
#channel #chan03 -plist 28 -pformat minimal
#channel #chan04 -plist 14 -pformat summary -key thekey
#channel #chan04 -plist 14 -pformat summary -headline "moving soon"
#channel #chan04 -plist 14 -pformat summary -delay 60 -noannounce
#channel #chan04 -plist 14 -pformat full -pgroup XXX
#channel #chan04 -plist 14 -pformat full -joinmsg "!voiceme"
#channel #chan04 -plist 14 -pformat full -fish secret
    for chan in chan_list:
      print "channel %s" % chan

# 1st Network
#network rizon4
#{
#local_vhost 0.0.0.0
#server irc.rizon.net
#channel #dinoex -noannounce
#}

# 2nd Network
#network otakubox
#{
#server irc.otakubox.at 6667
#channel #dinoex -noannounce
#}

# 3st Network
#network rizon6
#{
#local_vhost ::
#user_nick XDCC|MyBot|IPv6
#server irc.rizon.net
#channel #dinoex -noannounce
#}

##############################################################################
###                           - wait after join -                          ###
### When joining a channel, skip announces for given seconds.              ###
### This will avoid banning your bot for join+spam.                        ###
### Default: 200 seconds.                                                  ###
#waitafterjoin 200

##############################################################################
###                           - no auto rejoin -                           ###
### Do not rejoin channel when bots is kicked.                             ###
#noautorejoin

##############################################################################
###                          - reconnect delay -                           ###
### Do not reconnect when connections is dropped for given seconds.        ###
    print "reconnect_delay 15"

##############################################################################
###                          - user information -                          ###
### user_nick global setting is required, can be changed per network       ###
    print "user_nick %s" % nick
    print "user_realname %s" % mybot

##############################################################################
###                             - user mode -                              ###
### user_modes global setting is required, can be changed per network      ###
### B Marks you as being a Bot                                             ###
### i Invisible (not shown in /who)                                        ###
### Modes are diffrent on the IRC networks you use, please read the docs   ###
### for your networks before setting then.                                 ###
    print "user_modes +iB"

##############################################################################
###                             - owner nick -                             ###
### Nick to notify if bot has trouble. Answer to XDCC OWNER command.       ###
#owner_nick OwnerNick mailto:user@example.com

##############################################################################
###                           - watch this user -                          ###
### No new "xdcc send" are accepted, when this user is not online.         ###
### Old queue entries are still send.                                      ###
#enable_nick master

##############################################################################
###                      - incoming TCP connections -                      ###
### If you are behind a firewall that you control and want to have iroffer ###
### use a specified range for TCP ports for incoming connections set       ###
### tcprangestart to the first port used (ports will be used from that     ###
### number upwards as needed (usually 1 per transfer attempt).             ###
### If undefined, incoming TCP ports are automatically chosen by the OS.   ###
### You can limit the maximum port number used, by setting tcprangelimit.  ###
#tcprangestart 4000
#tcprangelimit 65535

##############################################################################
###                           - TCP buffer size -                          ###
### Set the Networkbuffer for TCP connection to the given value in kByte.  ###
### Default: 0 = the operating system default.                             ###
### On CYGWIN the default is 372                                           ###
#tcp_buffer_size 372

##############################################################################
###                            - TCP no delay -                            ###
### Disable the Nagle buffering algorithm in TCP.                          ###
### The operating system will not optimze the size of each TCP packet.     ###
### Default: no, on CYGWIN Default: yes                                    ###
#tcp_nodelay no
#tcp_nodelay yes

##############################################################################
###                       - override unix loginname -                      ###
### Override your unix loginname. Will only work if identd isn't running.  ###
#loginname fakelogin

##############################################################################
###                          -  passive dcc -                              ###
### Force all downloads over passive dcc.                                  ###
### NOTE: all users must have working NAT on their end with this option.   ###
### Default: normal dcc                                                    ###
#passive_dcc

##############################################################################
###                          -  mirc dcc64 -                               ###
### All transfers greater 4GB will use mIRC style 64bit DCC.               ###
### NOTE: This works only with mIRC version 6.33 and upper.                ###
### NOTE: XChat, Irssi will work only in 32bit DCC mode.                   ###
### Default: 32bit DCC                                                     ###
#mirc_dcc64

##############################################################################
###                          -  UPnP router -                              ###
### activate UPnP support.                                                 ###
#upnp_router

##############################################################################
###                      - excluded from auto-ignore -                     ###
### These hostmasks (one per line) will never be ignored.                  ###
#autoignore_exclude nickserv!nickserv@services.domain.com
#autoignore_exclude chanserv!chanserv@services.domain.com
#autoignore_exclude *!*@services.otakubox.de
#autoignore_exclude *!*@services.otakubox.at
#autoignore_exclude *!SERVICES@EUIRC.NET

##############################################################################
###                          - auto-ignore rate -                          ###
### How strict should the auto-ignore be? autoignore_rate is the maximum   ###
### number of requests per second from a user.                             ###
### auto-ignore.  The default is 8 request.                                ###
#autoignore_rate 8

##############################################################################
###                        - auto-ignore threshold -                       ###
### How long should the auto-ignore last? autoignore_threshold is the      ###
### average number of seconds between requests that will re-trigger the    ###
### auto-ignore.  The default is 10 seconds.                               ###
#autoignore_threshold 10

##############################################################################
###                        - flood protection rate -                       ###
### How strict should the bot activate its global flooding protection.     ###
### Value is the maximum number successful executed commands in the last   ###
### 10 seconds.                                                            ###
### Default: 6                                                             ###
#flood_protection_rate 6


##############################################################################
##                                   xdcc                                   ##
##############################################################################

##############################################################################
###                         - maximum xdcc slots -                         ###
    print "slotsmax 20"

##############################################################################
###                         - Queue Information -                          ###
### Main Queue Size, set to 0 for no queue                                 ###
    print "queuesize 10"

##############################################################################
###                      - max transfers per person -                      ###
### maximum transfers per person at a time                                 ###
    print "maxtransfersperperson 1"

##############################################################################
###                        - ignore duplicate ip -                         ###
### Detect faked hostmasks and abort multiple transfers to the same host   ###
### and ignore the user for the give time in hours.                        ###
### Default: 0 == no check.                                                ###
#ignore_duplicate_ip 24

##############################################################################
###                     - max queued items per person -                    ###
### maximum number of times a user can be in a queue simultaneously        ###
    print "maxqueueditemsperperson 2"

##############################################################################
###                          - idle queue size -                           ###
### Idle queue size, set to 0 for no queue                                 ###
### This queue is required to support XDCC BACTH.                          ###
    print "idlequeuesize 100"

##############################################################################
###                 - max idle queued items per person -                   ###
### maximum number of times a user can be in the idle queue simultaneously ###
    print "maxidlequeuedperperson 20"

##############################################################################
###                        - balanced_queue -                              ###
### When a user is done using a slot, the next file retrieved from the     ###
### queue would NOT be a file queued by the same user. This helps to       ###
### distribute the bandwidth better in bots with few slots.                ###
### Default: first in, first out                                           ###
    print "balanced_queue"

##############################################################################
###                         - requeue_sends -                              ###
### When the bot shutdowns, sends are aborted. With this option set, sends ###
### are saved with the queued items, so transfers might resume on restart. ###
    print "requeue_sends"

##############################################################################
###                        - reminder send retry -                         ###
### Defines how often the bot retries to start the XDDC SEND to the user.  ###
### The default is 2 retries.                                              ###
#reminder_send_retry 2

##############################################################################
###                          - send batch -                                ###
### Permit XDCC BATCH. The packs are Queued up in the bot is possible.     ###
### Default: disabled                                                      ###
    print "send_batch"

##############################################################################
###                            - holdqueue -                               ###
### don't send from queue, let current transfers run out, so the bot       ###
### can shutdown cleanly without stopping transfers                        ###
#holdqueue

##############################################################################
###                 - add/chfile command helper directory -                ###
### optional directory where iroffer will look after trying normal         ###
### relative/absolute paths when using the add or chfile admin command.    ###
### Add/chfile will first try to open the file using just the argument you ###
### provide to the command, and if that fails it will try again with       ###
### filedir added to the front of the argument.                            ###
### multiple directories can be configured.                                ###
#filedir /home/me/files
    for filedir in filedir_list:
      print "filedir %s" % filedir

##############################################################################
###                 - no duplicate files -                                 ###
### When configured, add, adddir and addnew refuses to add a files that    ###
### already have been added.                                               ###
    print "noduplicatefiles"

##############################################################################
###                   - no duplicate filenames -                           ###
### When configured, add, adddir and addnew refuses to add a files with a  ###
### name that already have been added.                                     ###
#no_duplicate_filenames

##############################################################################
###                     - include subdirs -                                ###
### When configured, addir, addnew and removedir will scan into sub-       ###
### directories and process the files found.                               ###
    print "include_subdirs"

##############################################################################
###                     - subdirs delayed -                                ###
### When configured, addir, addnew, and autoadd will scan subdirs later.   ###
### This keeps the bot responsive if you have a huge directory tree.       ###
### Default: off, subdirectories are scanned immediatly.                   ###
#subdirs_delayed

##############################################################################
###                     - remove lost files -                              ###
### if a files is no longer accessible on the server, remove the pack.     ###
### use with care, if started in wrong dir it may delete all packs.        ###
#removelostfiles

##############################################################################
###                        - monitor files -                               ###
### Check only given number of files per second for removal or update.     ###
### Default: 20                                                            ###
#monitor_files 20

##############################################################################
###                           - groups in caps -                           ###
### if set, all groups names changed will be folded to uppercase.          ###
#groupsincaps

##############################################################################
###                        - auto default group -                          ###
### When adding a new file, search for matching filenames and add the new  ###
### file to the same group.                                                ###
    print "auto_default_group"

##############################################################################
###                          - auto path group -                           ###
### When adding a new file, search for matching directories and add the    ###
### new file to the same group.                                            ###
    print "auto_path_group"

##############################################################################
###                        - auto crc check -                              ###
### When adding a new file, verify the crc32 in the given filename.        ###
    print "auto_crc_check"

##############################################################################
###                   - crc exclude pattern -                              ###
### When configured, auto crc check will ignore files matching this        ###
### patterns.                                                              ###
    print "autocrc_exclude *.torrent"
    print "autocrc_exclude *.xdelta"

##############################################################################
###                 - adddir exclude pattern -                             ###
### When configured, addir, adnew and autoadd will skip all files or dirs  ###
### that match this patterns.                                              ###
    print "adddir_exclude *.txt"
    print "adddir_exclude *.md5"

##############################################################################
###                  - adddir match pattern -                              ###
### When configured, addir, adnew and autoadd will skip all files that do  ###
### not match this patterns.                                               ###
#adddir_match *.avi
#adddir_match *.mkv
#adddir_match *.mp4

##############################################################################
###                   - adddir min size -                                  ###
### When configured, addir, adnew and autoadd will skip all files that are ###
### smaller then the gives size in kB.                                     ###
### Default: no check                                                      ###
#adddir_min_size 10

##############################################################################
###                    - auto add announce -                               ###
### When configured, each add will be announced on all channels with <msg> ###
### patterns.                                                              ###
#autoaddann added

##############################################################################
###                 - auto add announce short -                            ###
### When configured, each add will be announced on all channels with pack  ###
### Number and Filename.                                                   ###
#autoaddann_short

##############################################################################
###                - auto add announce match -                             ###
### When configured, addir, adnew and autoadd will only announce files     ###
### that do match this patterns.                                           ###
#autoaddann_mask *.avi
#autoaddann_mask *.mkv

##############################################################################
###                       - announce seperator -                           ###
### printed between pack number and name on announce.                      ###
### Default: space                                                         ###
#announce_seperator " "
    print 'announce_seperator " - "'

##############################################################################
###                       - announce size -                                ###
### print size of pack on announce.                                        ###
### Default: no                                                            ###
#announce_size

##############################################################################
###                      - auto add time -                                 ###
### Time in seconds when the bot checks for new files in autoadd_dir.      ###
### Default: 0 = disabled.                                                 ###
#autoadd_time 300

##############################################################################
###                      - auto add delay -                                ###
### Time in seconds that files must been unchanged to be added.            ###
### Default: 0 = disabled.                                                 ###
#autoadd_delay 300

##############################################################################
###                       - auto add dir -                                 ###
### Directory for files that will be added without further interaction     ###
### either by "autoadd_time" or by the "AUTOADD" command.                  ###
### You can list multiple directories here.                                ###
#autoadd_dir /home/me/new
#autoadd_dir /home/other/new

##############################################################################
###                      - auto add group -                                ###
### Set group for files to be added in autoadd_dir. Default "MAIN"         ###
#autoadd_group NEWSTUFF

##############################################################################
###                    - autoadd_group match -                             ###
### Define groups for files to be added in autoadd_dir based on matching   ###
### the given pattern with the full path of the file.                      ###
#autoadd_group_match NEWVIDEO *.avi
#autoadd_group_match NEWMUSIC *.mp3

##############################################################################
###                      - auto add color -                                ###
### Set color for files to be added in autoadd_dir.                        ###
### Default no color.                                                      ###
### Format: <color>,<background>,<style>                                   ###
### values for color, background:                                          ###
###     0 no color                                                         ###
###     1 black                                                            ###
###     2 blue (navy)                                                      ###
###     3 green                                                            ###
###     4 red                                                              ###
###     5 brown (maroon)                                                   ###
###     6 purple                                                           ###
###     7 orange (olive)                                                   ###
###     8 yellow                                                           ###
###     9 light green (lime)                                               ###
###    10 teal (a green/blue cyan)                                         ###
###    11 light cyan (cyan) (aqua)                                         ###
###    12 light blue (royal)                                               ###
###    13 pink (light purple) (fuchsia)                                    ###
###    14 grey                                                             ###
###    15 light grey (silver)                                              ###
###    16 white                                                            ###
###                                                                        ###
###  values for style:                                                     ###
###     0 = none                                                           ###
###     1 = bold                                                           ###
###     2 = underline                                                      ###
###     4 = italic                                                         ###
###     8 = inverse                                                        ###
###                                                                        ###
#autoadd_color 0,0,1

##############################################################################
###                   - announce suffix color -                            ###
### Set color for the instructions suffix in the announce message.         ###
### This will print the text "/MSG <botname> XDCC GET <nr>" in color.      ###
### Default no color.                                                      ###
#announce_suffix_color 0,0,1

##############################################################################
###                      - auto add sort -                                 ###
### If defined, all added packs will be inserted in the giving order.      ###
### The existing packs must already be sorted in the same way.             ###
### You can define multiple arguments:                                     ###
### NAME = sorted by full pathname            -NAME = backwards sort       ###
### DESC = sorted by description              -DESC = backwards sort       ###
### GROUP = sorted by group                   -GROUP = backwards sort      ###
### PATH = sorted by directory                -PATH = backwards sort       ###
### SIZE = sorted by size in bytes            -SIZE = backwards sort       ###
### TIME = sorted by file modification time   -TIME = backwards sort       ###
### ADDED = sorted by file add time           -ADDED = backwards sort      ###
#autoadd_sort GROUP NAME

##############################################################################
###                     - no natural sort -                                ###
### If configurend, all text is sorted by plain ASCII.                     ###
### Default: use natural sort order.                                       ###
#no_natural_sort

##############################################################################
###                  - restrict xdcc list and xdcc send -                  ###
### if set, xdcc list and/or xdcc send|info will be restricted to users    ###
### who are on a known channel. If a user is not on one of the known       ###
### channels they will not be able to list and/or get packs                ###
### restrictprivlist disables all private xdcc list requests completely.   ###
### use restrictprivlistmsg to change the message that restrictprivlist    ###
### sends                                                                  ###
### restrictsend, restrictlist can be global or per network.               ###
    print "restrictlist"
    if restrictprivlistmsg:
      print "restrictprivlist"
      print "restrictprivlistmsg %s" % restrictprivlistmsg
    print "restrictsend"

##############################################################################
###                      - restrictsend warning -                          ###
### If set, it will try to warn the user when he/she leaves the channel.   ###
    print "restrictsend_warning"

##############################################################################
###                      - restrictsend timeout -                          ###
### Timeout in seconds to cancel transfer after user left channel.         ###
    print "restrictsend_timeout 300"

##############################################################################
###                       - restrictsend delay -                           ###
### Time in seconds to wait after connect till restrictsend is enforced.   ###
#restrictsend_delay 300

##############################################################################
###                      - restrictprivlistmain -                          ###
### If set, "xdcc list" without an option will be rejected.                ###
### This allows to list a single group only.                               ###
#restrictprivlistmain

##############################################################################
###                      - restrictprivlistfull -                          ###
### If set, "xdcc list all" will be rejected.                              ###
#restrictprivlistfull

##############################################################################
###                       - remove_dead_users -                            ###
### If the bot can't notify a nick:                                        ###
### If set to 1, further queued messages are dropped.                      ###
### If set to 2, all this nicks queued packs are removed.                  ###
### Default: 0, no action.                                                 ###
    print "remove_dead_users 2"

##############################################################################
###                         - need voice -                                 ###
### Restrict list/send to only voiced/opped users.                         ###
### restrictlist and restrictsend must be set yes.                         ###
### This setting can be global or per network.                             ###
#need_voice

##############################################################################
###                         - need level -                                 ###
### Restrict list/send to only voiced/opped users.                         ###
### restrictlist and restrictsend must be set yes.                         ###
### This setting can be global or per network.                             ###
### 0 = all users                                                          ###
### 1 = user with voice,hop,op only                                        ###
### 2 = user with hop,op only                                              ###
### 3 = user with op only                                                  ###
#need_level 1

##############################################################################
###                      - channel xdcc commands -                         ###
### if set, iroffer will respond to xdcc requests sent to a channel in     ###
### addition to xdcc requests sent to iroffer directly.                    ###
### This setting can be global or per network.                             ###
#respondtochannelxdcc

##############################################################################
###                      - channel !list command -                         ###
### if set, iroffer will respond to !list requests sent to a channel       ###
### This setting can be global or per network.                             ###
#respondtochannellist

##############################################################################
###                      - channel !list text -                            ###
### text that is put int each response to !list in a channel.              ###
#respondtochannellistmsg packlist at http://www.examle.com/

##############################################################################
###                      - slow slow_privmsg -                             ###
### Restrict PRIVMSG to n lines per sec in this network to avoid flooding. ###
### This setting is only per network.                                      ###
### Default: 1                                                             ###
#slow_privmsg 1

##############################################################################
###                      - server send max -                               ###
### Restrict the size of the buffer the bot sends to the irc-server.       ###
### Otherwise the bot will be banned cause of excess flooding.             ###
### This setting is only per network.                                      ###
### Default: 600                                                           ###
#server_send_max 600

##############################################################################
###                      - server send rate -                              ###
### Limit the median number of characters per second the bot sends         ###
### to the IRC server.                                                     ###
### Otherwise the bot will be banned cause of excess flooding.             ###
### This setting is only per network.                                      ###
### Default: 25                                                            ###
#server_send_rate 25 

##############################################################################
###                          - privmsg fish -                              ###
### If set, decode encrypted messages with this global fish key.           ###
#privmsg_fish secret

##############################################################################
###                           - fish only -                                ###
### If set, ignores not encrypted triggers in channels with a fish key.    ###
#fish_only

##############################################################################
###                         - privmsg encrypt -                            ###
### If set, all notice and privmsg will be encrypted.                      ###
#privmsg_encrypt

##############################################################################
###                       - fish exclude nick -                            ###
### Messages to this nicks won't be encryted.                              ###
#fish_exclude_nick nickserv

##############################################################################
###                      - channel @find command -                         ###
### iroffer will respond to "@find pattern" requests sent to a channel     ###
### with a pattern that contains at least <n> non wild cards chars         ###
### wild cards are:                                                        ###
###  * = 0 or more characters,  ? = 1 character,  # = any positive integer ###
### Default: 0 = no response at all                                        ###
#atfind 3

##############################################################################
###                         - no find trigger -                            ###
### Iroffer will respond to "!find" too if atfind is defined.              ###
### This flag will make the bot ignore "!find".                            ###
### Default: response to "!find"                                           ###
#no_find_trigger

##############################################################################
###                           - new trigger -                              ###
### iroffer will respond to "!new" requests sent to a channel.             ###
### It will respond with latest <n> packs added.                           ###
### Default: 0 = no response at all                                        ###
#new_trigger 3

##############################################################################
###                             - max find -                               ###
### Limit matches to @find and XDCC SEARCH commands.                       ###
### Default: 0 = no limit.                                                 ###
#max_find 100

##############################################################################
###                   - bypass queue for small files -                     ###
### If someone requests a small file, bypass queue and max sends.  If the  ###
### offered file is under this size (in KB), send immediately.             ###
    print "smallfilebypass 1024"

##############################################################################
###                      - spaces in filenames -                           ###
### Allow spaces in filenames via DCC                                      ###
### Default: spaces are converted to '_'                                   ###
#spaces_in_filenames

##############################################################################
###                      - authorized download hosts -                     ###
### Specify who can download from this bot.  Use *!*@* to allow anyone.    ###
### Multiple hostmasks can be specified                                    ###
### wild cards are:                                                        ###
###  * = 0 or more characters,  ? = 1 character,  # = any positive integer ###
    if downloadhost_list:
        for downloadhost in downloadhost_list:
          print "downloadhost %s" % downloadhost
    else:
        print "downloadhost *!*@*"
#downloadhost *!~me@*.domain.com
#downloadhost *!me@192.168.10.#

##############################################################################
###                       - blacklist download hosts -                     ###
### Specify who can not download from this bot.                            ###
### Multiple hostmasks can be specified                                    ###
### wild cards are:                                                        ###
###  * = 0 or more characters,  ? = 1 character,  # = any positive integer ###
#nodownloadhost *!~me@*.domain.com

##############################################################################
###                      - unlimited download hosts -                      ###
### Specify Nicks and Hostnames which are not limited in bandwidth.        ###
#unlimitedhost XDCC|*!*@*

##############################################################################
###                            - xdcc allow -                              ###
### Defines ip masks, which are allowed to download from the server.       ###
### Multiple ip masks can be specified                                     ###
### Default: all.                                                          ###
#xdcc_allow 127.0.0.1
#xdcc_allow 192.168.1.0/24

##############################################################################
###                            - xdcc deny -                               ###
### Defines ip masks, that should not download from the server.            ###
### Multiple ip masks can be specified                                     ###
### Default: none.                                                         ###
#xdcc_deny 172.16.0.0/16

##############################################################################
###                      - geoip country check -                           ###
### Allow downloads only for users in the given countries.                 ###
### this sets default access to deny and disables nogeoipcountry.          ###
#geoipcountry de
#geoipcountry ch
#geoipcountry at

##############################################################################
###                      - geoip country check -                           ###
### Disallow downloads only for users in the given countries.              ###
### this sets default access to allow and disables geoipcountry.           ###
#nogeoipcountry jp

##############################################################################
###                      - geoip exclude nick -                            ###
### Allow downloads for this nicks, even if geoip entry differs.           ###
#geoipexcludenick aoluser

##############################################################################
###                      - geoip exclude group -                           ###
### Allow downloads for packs in this group, even if geoip entry differs.  ###
#geoipexcludegroup FREE

##############################################################################
###                        - geoip database -                              ###
### Use a custom path to the database file for IPv4.                       ###
### If you don't have a database you can download it from:                 ###
### http://dev.maxmind.com/geoip/geolite                                   ###
#geoipdatabase /usr/local/share/GeoIP/GeoIP.dat
#geoipdatabase GeoIP.dat

##############################################################################
###                       - geoip6 database -                              ###
### Set the path to the database file for IPv6.                            ###
### If you don't have a database you can download it from:                 ###
### http://www.maxmind.com/app/geolitecountry                              ###
### Default: no lookups for IPv6.                                          ###
#geoip6database GeoIPv6.dat


##############################################################################
##                               Network Usage                              ##
##############################################################################

##############################################################################
###                      - Allow with low bandwidth -                      ###
### If packs are queued, and the bandwidth usage is below this amount, a   ###
### queued person will be sent their pack. (K/sec)                         ###
### WARNING! do not set this amount to an unreasonably high number!        ###
    print "lowbdwth 15"

##############################################################################
###                         - transfer min speed -                         ###
### Per-transfer min speed in KB/sec used unless 'chmins' set per pack.    ###
    print "transferminspeed 10"

##############################################################################
###                         - transfer max speed -                         ###
### Per-transfer max speed in KB/sec used unless 'chmaxs' set per pack.    ###
    print "transfermaxspeed 4096"

##############################################################################
###                        - bandwidth limiting -                          ###
### Is your sysadmin complaining about you using up too much bandwidth?    ###
### You can set a maximum KB/sec that will be sent to the network.         ###
### Please set the maximum bandwidth, so the bot can calculate the traffic ###
### and share it under the users.                                          ###
### You can define two different limits depending on time of day,          ###
### overallmaxspeed is the general limit, overallmaxspeeddayspeed is the   ###
### limit during the hours defined by overallmaxspeeddaytime (0 ... 23)    ###
### (no looping) and during days of week ( MTWRFSU )                       ###
    print "overallmaxspeed 8192"
#overallmaxspeeddayspeed 100
#overallmaxspeeddaytime 9 17
#overallmaxspeeddaydays MTWRF

##############################################################################
###                    - daily/weekly/monthly limits -                     ###
### If you want to limit total sent during a day/week/month, define        ###
### transferlimits and set one or more of the limits.  Setting to 0        ###
### disables that limit, non-zero limits total transfered in that period   ###
### to that number of MB. If you define more than one value, then all      ###
### limits apply. Days begin at midnight, Weeks begin Sunday morning.      ###
###                                                                        ###
### transferlimits <daily MB> <weekly MB> <monthly MB>                     ###
###                                                                        ###
### EXAMPLE: 'transferlimits 200' would limit to 200MB per day.            ###
###                                                                        ###
### EXAMPLE: 'transferlimits 0 0 5000' would limit to 5000MB per month.    ###
###                                                                        ###
### EXAMPLE: 'transferlimits 200 1200 5000' would limit to:                ###
###           200MB per day, 1200MB per week and 5000MB per month.         ###
#transferlimits 200 1200 5000

##############################################################################
###                           - start of month -                           ###
### day of month when to reset the monthly traffic limit, default 1        ###
### this value is only checked when the old month is over.                 ###
#start_of_month 1

##############################################################################
###                       - ignore upload bandwidth -                      ###
### don't count uploads traffic into transferlimits.                       ###
### Fast uploads will stop any downloads without this option.              ###
    print "ignoreuploadbandwidth"

##############################################################################
###                         - extend status line -                         ###
### print out upload and download bandwidth in status line.                ###
    print "extend_status_line"

##############################################################################
###                        - status time dcc chat -                        ###
### Defines the time in seconds for a status line in dcc chat.             ###
### Default: 120                                                           ###
#status_time_dcc_chat 120

##############################################################################
###                          - no status chat -                            ###
### If defined, iroffer will suppress status line in chat.                 ###
#no_status_chat

##############################################################################
###                           - no status log -                            ###
### If defined, iroffer will suppress status line in logfile.              ###
#no_status_log

##############################################################################
###                           - no auto rehsh -                            ###
### If defined, iroffer will not automaticlly REHASH when a configfile was ###
### was changed. Default: Do a REHASH.                                     ###
#no_auto_rehash

##############################################################################
##                                   Other                                  ##
##############################################################################

##############################################################################
###                          - autosend feature -                          ###
### Set if you want iroffer to automatically send a pack when someone says ###
### a certain word publicly in a channel.                                  ###
### Only the first matching trigger will start a send.                     ###
### autosendpack <pack#> <trigger> <message ...>                           ###
### the message is now optional                                            ###
###               == MOST USERS WILL NOT NEED THIS FEATURE ==              ###
###             == GET PERMISSION FROM YOUR CHANNEL OPS FIRST ==           ###
#autosendpack 1 !rules Sending you the rules.
#autosendpack 2 !faq Sending you the FAQ.
    for (num, trigger, msg) in autosend_list:
      print "autosendpack %s %s %s" % (num, trigger, msg)

##############################################################################
###                             - headline -                               ###
### Put a headline at the top of all xdcc lists                            ###
#headline New Stuff Just Added!!
    print "headline %s" % headline

##############################################################################
###                           - credit line -                              ###
### Put a credit at the end of your xdcc list                              ###
#creditline Brought to you by me

##############################################################################
###                     - download completed msg -                         ###
### Put a credit at the end of each transfer.                              ###
#download_completed_msg Please visit http://exmaple.com/

##############################################################################
###                             - hide_list_info -                         ###
### Don't print line with "/msg nick xdcc info #x"                         ###
#hide_list_info

##############################################################################
###                             - hide_list_stop -                         ###
### Don't print line with "/msg nick xdcc stop"                            ###
#hide_list_stop

##############################################################################
###                             - show list all -                          ###
### print line with "/msg nick xdcc list all".                             ###
#show_list_all

##############################################################################
###                            - disablexdccinfo -                         ###
### disable all XDCC INFO requests                                         ###
#disablexdccinfo

##############################################################################
###                            - hidelockedpacks -                         ###
### Don't show locked packs to users with XDCC INFO and XDCC SEND          ###
#hidelockedpacks

##############################################################################
###                            - show date added -                         ###
### Show date the pack was added with XDCC LIST.                           ###
#show_date_added

##############################################################################
###                        - show group of pack -                          ###
### Export your xdcc list with group for each pack.                        ###
### Default output is just the packs                                       ###
#show_group_of_pack

##############################################################################
###                         - index bot notify -                           ###
### if you want iroffer to periodically msg some nick for indexing or some ###
### other purpose use periodicmsg in the form:                             ###
### "periodicmsg <nick> <num minutes> <message ...>                        ###
### This setting is only per network. Multiple lines per net allowed.      ###
#periodicmsg nick 10 index me

##############################################################################
###                        - remote admin info -                           ###
### Remote commands can only be issued by a nick with a matching hostmask  ###
### and knows the adminpass. Remote commands are issued by dcc chat or by  ###
### /msg nickDCC admin 'adminpass' 'command' adminhost's are full          ###
### hostmasks: nick!user@host don't forget a "~" if you don't use identd   ###
### wild cards are:                                                        ###
###  * = 0 or more characters,  ? = 1 character,  # = any positive integer ###
### For security, your adminpass must be stored in the config file         ###
### encrypted.  To generate an encrypted password run iroffer with the     ###
### "-c" flag and follow the instructions.                                 ###
#adminpass add_your_encrypted_password_here
#adminhost *!~me@*.domain.com
#adminhost *!me@192.168.10.#
#adminhost telnet!*@telnet
    print "adminpass %s" % adminpass
    for domain in adminhost:
      print "adminhost %s" % domain.strip()

##############################################################################
###                       - remote admin level -                           ###
### Limit remote admin commands to level.                                  ###
### 1 = info and stats only                                                ###
### 2 = lock and unlock                                                    ###
### 3 = add and change                                                     ###
### 4 = remove packs                                                       ###
### 5 = full, may rename or removes files on disk                          ###
### Default: 5                                                             ###
    print "adminlevel 5"

##############################################################################
###                     - remote half admin info -                         ###
### Remote commands can only be issued by a nick with a matching hostmask  ###
### and knows the hadminpass. Remote commands are issued by dcc chat or by ###
### /msg nickDCC admin 'hadminpass' 'command'                              ###
### This account can not modify packs besides locking or unlocking them.   ###
### For security, your hadminpass must be stored in the config file        ###
### encrypted. <hadminhost> should not overlap with the <adminhost>.       ###
#hadminpass add_your_encrypted_password_here
#hadminhost *!~me@*.domain.com
#hadminhost *!me@192.168.10.#
#hadminhost telnet!*@telnet
    print "hadminpass %s" % hadminpass
    for domain in hadminhost:
      print "hadminhost %s" % domain.strip()

##############################################################################
###                     - remote half admin level -                        ###
### Limit remote half admin commands to level.                             ###
### Values see adminlevel                                                  ###
### Default: 2                                                             ###
    print "hadminlevel 4"

##############################################################################
###                        - remote group admin -                          ###
### Remote commands can only be issued by a nick with a matching hostmask  ###
### and knows the coresponding password. Access is limit to the groups     ###
### listed in the same line and by the given level.                        ###
### group_admin <level> <hostmask> <encrypted_password> <grouplist>        ###
### After the grouplist you can define an uploaddir for this admin.        ###
### The hostmask will be automatically added as uploadhost.                ###
### The hostmask should not overlap with <adminhost> or <hadminhost>       ###
#group_admin 3 *!~me@*.domain.com encrypted_password GROUP1,GROUP2

##############################################################################
###                       -  passive dcc xchat -                           ###
### Allow all admins to use passive DCC chat on the bot.                   ###
### Default: off.                                                          ###
### Admins must use "/MSG bot ADMIN password CHATME" instead.              ###
    print "passive_dcc_chat"

##############################################################################
###                          - upload directory -                          ###
### If you want iroffer to accept DCC transfers (upload) define one or     ###
### more uploadhosts and define an uploaddir where files should be saved.  ###
### uploadmaxsize if the maximum size in MB of any individual transfer,    ###
### files over that size will be rejected (0 for no limit).                ###
### wild cards are:                                                        ###
###  * = 0 or more characters,  ? = 1 character,  # = any positive integer ###
### WARNING!!  specify a directory used exclusively for uploads. This will ###
### WARNING!!  prevent users from creating/appending important files       ###
#uploadhost *!~me@*.domain.com
#uploadhost *!me@192.168.10.#
#uploaddir /home/me/upload
#uploadmaxsize 10
    for dir in uploaddir_list:
      print "uploaddir %s" % dir
    for host in uploadhost_list:
      print "uploadhost %s" % host

##############################################################################
###                          - upload min space -                          ###
### Check free space on disk and do not start uploads when disk gets full. ###
### Specifies the minimum size in MB available before upload.              ###
#uploadminspace 10

##############################################################################
###                             - disk quota -                             ###
### Check used space on disk for files and do not add more packs.          ###
### Specifies the maximum size in MB used in all packs.                    ###
#disk_quota 1000

##############################################################################
###                             - max uploads -                            ###
### Do not allow more than given number of concurrent uploads.             ###
### Default: not limited.                                                  ###
#max_uploads 3

##############################################################################
###                             - max upspeed -                            ###
### You can set a maximum KB/sec that will be uploaded over the network.   ###
### Default: no limit.                                                     ###
#max_upspeed 1000

##############################################################################
###                          - hide OS information -                       ###
### If you do not want iroffer to show OS information in version and quit  ###
### messages enable this option                                            ###
    print "hideos"

##############################################################################
###                        - log notices/messages -                        ###
### If defined, iroffer will log notices and/or messages to the msglog     ###
#lognotices
#logmessages

##############################################################################
###                      - logfile notices/messages -                      ###
### If defined, iroffer will log notices and/or messages to the given      ###
### logfile.                                                               ###
#logfile_notices notice.log
#logfile_messages message.log

##############################################################################
###                            - logfile httpd -                           ###
### If defined, iroffer will log http request and errors in this logfile.  ###
#logfile_httpd httpd_error.log

##############################################################################
###                          - log exclude host -                          ###
### Exclude given list of hostmasks from filling up your logfiles          ###
### or polluting your saved messages.                                      ###
#log_exclude_host SpamScanner!scanner@euirc.net
#log_exclude_host Defender!Defender@security.otakubox.de

#############################################################################
###                          - log exclude text -                          ###
### Exclude given list of patterns from filling up your logfiles           ###
### or polluting your saved messages.                                      ###
### Wild cards are:                                                        ###
###  * = 0 or more characters,  ? = 1 character,  [0-9] = any digit        ###
#log_exclude_text LAG
#log_exclude_text TIME

##############################################################################
###                           - timestamp console -                        ###
### If defined, iroffer will place timestamps on all console output        ###
    print "timestampconsole"

##############################################################################
###                             - quiet mode -                             ###
### If defined, iroffer will suppress most informational messages to users ###
### No transfer completed mesage                                           ###
### No DCC send remind message                                             ###
### No XDCC QUEUE notifications                                            ###
#quietmode

##############################################################################
###                       - periodic notify time -                         ###
### How often should iroffer notify users of queue/bandwidth status        ###
### (in minutes).  If not defined default is 5 minutes. Setting to 0       ###
### disables notification entirely.                                        ###
#notifytime 5

##############################################################################
###                         - punish slow users -                          ###
### If a user is disconnected due to failing to meet a minspeed            ###
### requirement, punish them by disconnecting all transfers/queues and     ###
### ignoring them for n minutes                                            ###
#punishslowusers 10

##############################################################################
###                        - no minspeed on free -                         ###
### Don't enforce minspeed when bot still has free slots.                  ###
    print "no_minspeed_on_free"

##############################################################################
###                      - disable md5sum of files -                       ###
### By default, iroffer will calculate md5sums all offered files.  If you  ###
### want to disable this feature define 'nomd5sum' below.                  ###
### nomd5sum implies nocrc32, so disabling all checksums                   ###
#nomd5sum

##############################################################################
###                 - md5sum exclude pattern -                             ###
### When configured, MD5 and CRC32 will be not computed for files matching ###
### this patterns.                                                         ###
#md5sum_exclude *.txt

##############################################################################
###                      - disable crc32 of files -                        ###
### By default, iroffer will calculate crc32 checksums for all offered     ###
### files.  If you want to disable this feature define 'nocrc32' below.    ###
#nocrc32

##############################################################################
###                           - verbose crc32 -                            ###
### By default, after adding iroffer will only report bad checksums.       ###
### If set, it will print out the computed checksum in every case.         ###
#verbose_crc32

##############################################################################
###                        - direct file access -                          ###
### Enable admin commands to manipulate files on disk.                     ###
### This is required if you want to download files with FETCH.             ###
#direct_file_access

##############################################################################
###                        - direct config access -                        ###
### Enable admin commands to manipulate configuration.                     ###
#direct_config_access

##############################################################################
###                           - trashcan dir -                             ###
### Instead of deleting files, they are moved to this directory.           ###
### Default: delete files on disk.                                         ###
#trashcan_dir /home/me/trashcan

##############################################################################
###                      - fileremove max packs -                          ###
### Max number of packs on this bot, if more are added, the oldest ones    ###
### are removed from disk.                                                 ###
### Default: 0 = disabled.                                                 ###
#fileremove_max_packs 10

##############################################################################
###                           - ruby script -                              ###
### Run a ruby script on each line the bot gets from the irc server.       ###
#ruby_script "ruby-helper.rb"

##############################################################################
###                           - dump all -                                 ###
### If set shows all config vars on DUMP.                                  ###
### Default is to show only non default entries.                           ###
#dump_all

##############################################################################
###                             - debug -                                  ###
### Show more information on the Console.                                  ###
### Default: 0 == none                                                     ###
### 1 = general debug messages                                             ###
### 11 = channel members                                                   ###
### 12 = dcc chat                                                          ###
### 13 = queued irc                                                        ###
### 14 = crypted irc                                                       ###
### 15 = raw irc                                                           ###
### 21 = ignoring directory                                                ###
### 22 = ignoring exlcuded file                                            ###
### 23 = ignoring matched file                                             ###
### 24 = ignoring added file                                               ###
### 31 = md5 read bytes                                                    ###
### 41 = http not found                                                    ###
### 42 = http send size                                                    ###
### 47 = http send bytes                                                   ###
### 48 = http recv data                                                    ###
### 51 = upload recv bytes                                                 ###
### 52 = transfer send bytes                                               ###
### 53 = transfer read junk                                                ###
### 54 = transfer mmap status                                              ###
### 55 = transfer acknowleged bytes                                        ###
### 81 = kqueue                                                            ###
### 82 = select                                                            ###
#debug 1

##############################################################################
##                                    End                                   ##
##############################################################################
