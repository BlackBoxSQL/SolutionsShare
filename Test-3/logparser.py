import re
import csv
log = """
Oct 18 11:07:27 dummy_server systemd-logind[4405]: Removed session 109336.
Oct 18 11:07:27 dummy_server systemd-logind[4405]: New session 109337 of user ubuntu.
Oct 18 11:07:31 dummy_server sshd[25163]: Received disconnect from 192.168.12.45: 11: disconnected
by user
Oct 18 11:07:31 dummy_server sshd[25041]: pam_unix(sshd:session): session closed for user ubuntu
Oct 18 11:09:01 dummy_server CRON[26000]: pam_unix(cron:session): session opened for user root
by (uid=0)
Oct 18 11:09:01 dummy_server CRON[26000]: pam_unix(cron:session): session closed for user root
Oct 18 11:10:01 dummy_server CRON[26561]: pam_unix(cron:session): session opened for user root
by (uid=0)
Oct 18 11:10:05 dummy_server sshd[26500]: Accepted publickey for maateen from 192.168.12.45 port
36970 ssh2: RSA 1b:c6:57:28:06:fd:4e:45:6a:a9:27:03:98:77:8c:42
Oct 18 11:10:05 dummy_server sshd[26500]: pam_unix(sshd:session): session opened for user maateen
by (uid=0)
Oct 18 11:10:05 dummy_server systemd-logind[4405]: Removed session 109337.
Oct 18 11:10:05 dummy_server systemd-logind[4405]: New session 109338 of user maateen.
Oct 18 11:10:08 dummy_server sshd[26721]: Authentication refused: bad ownership or modes for file
/home/ubuntu/.ssh/authorized_keys
Oct 18 11:10:08 dummy_server sshd[26721]: Accepted password for ubuntu from 192.168.12.45 port
36998 ssh2
Oct 18 11:10:08 dummy_server sshd[26721]: pam_unix(sshd:session): session opened for user ubuntu
by (uid=0)
Oct 18 11:10:08 dummy_server systemd-logind[4405]: New session 109339 of user ubuntu.
Oct 18 11:10:09 dummy_server CRON[26561]: pam_unix(cron:session): session closed for user root
Oct 18 11:10:09 dummy_server sshd[26851]: Received disconnect from 192.168.12.45: 11: disconnected
by user
Oct 18 11:10:09 dummy_server sshd[26721]: pam_unix(sshd:session): session closed for user ubuntu
"""
# python3
entries = log.replace('\r', '').split('\n')
entries = [_f for _f in entries if _f]
csv = open('Test-3/log.csv', 'w')
csv.write('Datetime,Server,Process Name,Process ID,Message\n')
for lentry in entries:
    csvfields = re.findall(
        r'(^.*\s\d+:\d+:\d+)\s(.*?)\s(.*?)\[(.*?)\]:\s(.*?)$', lentry)
    csvfields = [_f for _f in csvfields if _f]
    if csvfields:
        c_date, c_server, c_pname, c_pid, c_message = csvfields[0]
        csv.write('{},{},{},{},{}\n'.format(
            c_date, c_server, c_pname, c_pid, c_message))


# # (\w+\s+\d+\s+\d+\:\d+\:\d+) -->to find Datetime
# # (\s\w+_\w+\s)--> to find Server
# #  --> to find ProcessName
# #  --> to find ProcessID
# #  --> to find Message
# import re
# import csv

# logfile = open('ssh_logs.log')
# logfileReader = csv.reader(logfile)

# # regexp = r'(?P<Dateime>([A-Z][a-z]{2}\s\d\d\s\d\d:\d\d:\d\d))\s(?P<Server>[a-z]{5}_[a-z]{6})'
# # date_time = re.findall(regexp, log)
# # print(date_time)

# import csv
# import re

# r = re.compile(r'(\w+\s+\d+\s+\d+\:\d+\:\d+)')

# with open('ssh_logs.log') as logfile, open('output2.csv', 'w') as csvfile:
#     csv.writer(csvfile).writerows(r.findall(str(logfile)))
