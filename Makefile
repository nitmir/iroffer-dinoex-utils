install:
	install -o root -g root -m 0755 iroffer.init /etc/init.d/iroffer
	install -d -o root -g root /etc/iroffer
	install -d -o iroffer -g root /etc/iroffer/config
	install -d -o iroffer -g root /etc/iroffer/log
	install -d -o iroffer -g root /etc/iroffer/pid
	install -d -o iroffer -g root /etc/iroffer/telnet
	install -d -o iroffer -g root /etc/iroffer/list
	install -d -o iroffer -g root /etc/iroffer/state
	install -o root -g root -m 0644 iroffer.py /etc/iroffer/iroffer.py
	install -o root -g root -m 0755 sample.py /etc/iroffer/sample.py
	install -o root -g root -m 0644 iroffer.default /etc/iroffer/config/iroffer.default
	echo "For a sample bot run : touch /etc/iroffer/config/sample.config && /etc/init.d/iroffer genconf"

uninstall:
	echo "Only conf and init script, nothing todo"
