#Iroffer dinoex init script and utils

This repository contain both an init script and a configuration generation 
script for [iroffer dinoex](https://github.com/dinoex/iroffer-dinoex)

The init script also work (for basic functionalities start, stop,…) 
with the old mainline [iroffer](http://iroffer.org/)


## Init scritp

 Running ```make install``` will install the initscript and create a tree view under ```/etc/iroffer/``` corresponding to configuration generated : 

 * ```.``` the current dir, containing config generation script (optional but quite handy then manager severals bots)
 * ```config/``` contening generated (or static) bots config and initscript config file ```iroffer.default``` for enabling or disabling chrooting
 * ```list/``` for bots files listing
 * ```log/``` for bots logs
 * ```pid/``` for bots pids files
 * ```state/``` for bots state files
 * ```telnet/``` (optional) for bots telnet port files

Most of this files need to be under the same tree view in order to be readable/writable 
by iroffer then chrooted


Chroot can be enable or disabled by editing the file ```/etc/iroffer/config/iroffer.default```.
If chroot is enabled, beware of changing any path of bots config file.

If several chroot are needed, just add several init script with different names and a tree 
view ```/etc/init_script_name``` for each init script 
(and a ```/etc/init_script_name/config/init_script_name.default``` for chroot config).


### Fonctionnalities

You can call ```/etc/init.d/iroffer command Botname``` to do command on botname only
or just call ```/etc/init.d/iroffer command``` to do command on all bots.

The list of possible command is : 
 * start
 * stop
 * restart
 * reload
 * status
 * reconnect (force bot to change server, handy during netsplits)
 * genconf (call the generation script if used)
 * telnet (can only be called with a bot name as parameter : open a telnet admin console)

## Generation script

It's a quite simple python script writed from the sample config file of iroffer.
Functionalities are hadded then I need them.

The file ```sample.py``` give an example of bot config generation script.

I will try to keep the script update with the last corresponding config file 
of the [iroffer dinoex](https://github.com/dinoex/iroffer-dinoex) repository.

It's very handing because it's allow to share a part of the configuration 
(for example, the adminhost list) between severals bots. So only one file need to be 
edited and the conf regenerated.
