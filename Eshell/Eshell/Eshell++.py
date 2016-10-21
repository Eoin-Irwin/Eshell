import getpass, time, ipgetter, os

systemCommands = {'pw': 'pwd', 'ifc': 'ifc', 'dt': 'date', 'ls': 'ls'}


def get_ip_address():
    ip = ipgetter.myip()
    print ip


def initial_login():
    print 64 * '='
    print """\nWelcome to Eshell++ 1.0.0 LTS (GNU/Linux 1.1.0-1-generic x86_64)

         * Documentation:  https://help.Eshell++.com
         * Management:     https://landscape.canonical.com
         * Support:        https://Eshell++.com/advantage

        15 packages can be updated.
        4 updates are security updates.


        Last login: """ + time.strftime("%a %b %d %H:%M:%S %Y") + ' from', get_ip_address()
    print 64 * '='


def ifc(choices):
    if len(x) > 1:
        os.system('ifconfig {0}'.format(x[1]))
    else:
        os.system('ifconfig eth0')


def ls(choices):
    if len(x) > 1:
        os.system('ls {0}'.format(x[1]))
    else:
        os.system('ls')


def date(choices):
    print time.strftime("%Y%m%d%H%M%S")


def pwd(choices):
    os.system('pwd')


def user_input(choice):
    for x, y in systemCommands.iteritems():
        if choice[0] == x:
            eval(y + '({0})'.format(choice))
            return True
        elif choice[0] == 'sudo':
            msg = getpass.getuser() + ',invalid permissions, this incident has been reported @ ' + time.strftime(
                "%a %b %d %H:%M:%S %Y")
            print msg
            os.system('logger ' + msg)
            break
    return False


initial_login()

x = ''
while x != 'exit':
    x = raw_input(getpass.getuser() + "@Eshell++:#")
    x = x.split(' ')
    x = user_input(x)
if not x:
    print('Command not found')
