import getpass, subprocess, time, ipgetter, os

systemCommands = {'pw': 'pwd', 'ifc': 'ifconfig eth0', 'ls': 'ls', 'dt': 'date'}


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


initial_login()


def date():
    print time.strftime("%Y%m%d%H%M%S")


def pwd():
    os.system('pwd')


def user_input(choice):
    for x, y in systemCommands.iteritems():
        if choice[0] == x:
            eval(y + '()')
            return True
    return False


def main():
    x = ''
    while x != 'exit':
        x = raw_input(getpass.getuser() + "@Eshell++:#")
        x = x.split(' ')
        x = user_input(x)
    if not x:
        print('Command not found')


if __name__ == '__main__':
    pass
main()
