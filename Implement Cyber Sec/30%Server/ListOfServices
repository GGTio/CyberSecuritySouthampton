#list of services to check

## Legend

N - normal
U - unusual
V - vulnerable
W - not sure
P - patched

##Start up
| Status | Program | Description|
|--------|---------|------------|
| N | acpid | Advanced Configuration and Power Interface event daemon |
| N | atd | atd is that which deals with commands to be executed a single time, but at a specific moment in the future. Can be hardened with /etc/at.allow and /etc/at.deny |
| W | backup-server | |
| N | dbus | simple interprocess messaging system |
| P | lwresd | daemon providing name lookup services to clients that use the BIND 9. PATCHED with |
| N | mcstrans | SELinux core policy utilities |
| N | motd | Dynamic message of the day |
| N | mysql | SQL server |
| W | openbsd-inetd | Internet Superserver |
| V | postgresql | SQL DB unused in the server |
| N | restorecond |daemon that watches for file creation and then sets the default SELinux file context |
| V | samba | Simple Samba file sharing server |
| N | smartmontools | control and monitor storage systems using S.M.A.R.T.(Self-Monitoring, Analysis and Reporting Technology System) |
| N | spamassassin | Open Source anti-spam platform giving system administrators a filter to classify email and block spam NOT VULN because version 3.3.2 |
| V | ssh | secure shell |
| V | sudo | special access command |
| V | apache2 | server |
| N | bootlogs | 	daemon to log boot messages |
| N | cron | daemon responsible for executing scheduled and recurring commands can be secured by defining a /etc/cron.allow or a /etc/cron.deny |
| N | exim4 | mail transport agent |
| W | rsync | a fast, versatile, remote (and local) file-copying tool |
| N | windbind | winbind is a component of the Samba suite of programs that solves the unified logon problem. |
| N | dovecot | Dovecot is an open-source IMAP and POP3 server for Linux/UNIX-like systems |
| N | rc.local | use by the system administrator. It is traditionally executed after all the normal system services are started |
| N | rmnologin | The rmnologin service is responsible for changing the state of your system from a non-logon-capable system (set by the bootmisc service) to a logon-capable one. This is needed to ensure no-one can log on to your system while important services are being loaded. |


##CRON daily

apache2 | cleans the cache
aptitude | backup for the packages states (/var/lib/aptitude/pkgstates)
dpkg | backup /var/lib/dpkg/status
logrotate | logs /etc/logrotate.conf
mlocate | updatedb 
samba | backup of smbpasswd file
apt | big backup
bsdmainutils | daily calendar maintenance script
exim4-base | 
man-db | clears cache
passwd | backup of the passwd, group shadow gshadow files
spamassassin | spamassassin updates

##CRON weekly

man-db

## Big hardenings

### SSH
https://www.cyberciti.biz/tips/linux-unix-bsd-openssh-server-best-practices.html
https://www.cyberciti.biz/faq/tcp-wrappers-hosts-allow-deny-tutorial/
https://en.wikipedia.org/wiki/Port_knocking
https://www.cyberciti.biz/tips/ssh-public-key-based-authentication-how-to.html
https://www.cyberciti.biz/faq/ssh-password-less-login-with-dsa-publickey-authentication/
https://www.cyberciti.biz/faq/ssh-passwordless-login-with-keychain-for-scripts/

Added (done) at the if already applied in the file from beginning

a)/root/.ssh/authorized_keys -> AAAA... (id_rsa.pub)
Not sure if the MII... (id_rsa) is usefull
b) no /host.allow or /host.deny
c) check for port 22 netstat -pln
d) SSH Protocol 2 -> /etc/ssh/sshd_config (done)
e) add these lines in /etc/ssh/sshd_config to kick inactive users:
ClientAliveInterval 300
ClientAliveCountMax 0
f) IgnoreRhosts yes in /etc/ssh/sshd_config (done)
g) HostbasedAuthentication no in /etc/ssh/sshd_config (done)
h) Firewall (not sure for our case)
i) RECOMMENDATION: use stronger passwords
j) RECOMMENDATION: Use public/private key pairs for authentication instead of passwords-> https://askubuntu.com/questions/2271/how-to-harden-an-ssh-server
k) USING a counter to bruteforce attacks (#16)
l) TCP wrappers
m) #20 not sure if deprecated

### SUDO

1) changed the line that granted sudo to all user to a comment
-> this fixes the use of sudo by all users

### Apache2

cf trello


- apache hardening