#!/bin/bash
# Place bind.sh a the root of the chroot
DIR="$( cd "$( dirname "$0" )" && pwd )"

# Bind some libs (libnss_dns and libresolv)
mkdir -p "$DIR/lib/"
if [ ! -s "$DIR/lib/libnss_dns.so.2" ] ; then
	touch "$DIR/lib/libnss_dns.so.2"
	mount --bind /lib/x86_64-linux-gnu/libnss_dns.so.2 "$DIR/lib/libnss_dns.so.2"
fi
if [ ! -s "$DIR/lib/libresolv.so.2" ] ; then
	touch "$DIR/lib/libresolv.so.2"
	mount --bind /lib/x86_64-linux-gnu/libresolv.so.2 "$DIR/lib/libresolv.so.2"
fi

# Add a resolv.conf ile
mkdir -p "$DIR/etc/"
if [ ! -s "$DIR/etc/resolv.conf" ] ; then
	touch "$DIR/etc/resolv.conf"
	mount --bind /etc/resolv.conf "$DIR/etc/resolv.conf"
fi

# Make path to the chroot accessible from inside the chroot
mkdir -p "$DIR/`dirname \"$DIR\"`"
cd "$DIR/`dirname \"$DIR\"`" && ln -sr "$DIR" "$DIR/$DIR" &>/dev/null
