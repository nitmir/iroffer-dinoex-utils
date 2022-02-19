#!/bin/bash
# Place bind.sh a the root of the chroot
DIR="$( cd "$( dirname "$0" )" && pwd )"

LIBS="
/usr/lib/x86_64-linux-gnu/libssl.so.1.1
/usr/lib/x86_64-linux-gnu/libcrypto.so.1.1
/lib/x86_64-linux-gnu/libcrypt.so.1
/lib/x86_64-linux-gnu/libc.so.6
/lib/x86_64-linux-gnu/libdl.so.2
/lib/x86_64-linux-gnu/libnss_compat.so.2
/lib/x86_64-linux-gnu/libnsl.so.1
/lib/x86_64-linux-gnu/libnss_nis.so.2
/lib/x86_64-linux-gnu/libnss_files.so.2
/lib/x86_64-linux-gnu/libresolv.so.2
/lib/x86_64-linux-gnu/libnss_dns.so.2

/etc/localtime
/etc/resolv.conf

/usr/lib/x86_64-linux-gnu/gconv/gconv-modules
/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache

/dev/random
/dev/urandom
/etc/hosts
/etc/host.conf
/etc/gai.conf
"
# Bind some libs (libnss_dns and libresolv)
mkdir -p "$DIR/lib/"
for lib in $LIBS; do
    if [ ! -s "$DIR/$lib" ] ; then
	mkdir -p $(dirname "$DIR/$lib")
	touch "$DIR/$lib"
	mount --bind $lib "$DIR/$lib"
    fi
done

# Make path to the chroot accessible from inside the chroot
mkdir -p "$DIR/`dirname \"$DIR\"`"
cd "$DIR/`dirname \"$DIR\"`" && ln -sr "$DIR" "$DIR/$DIR" &>/dev/null
