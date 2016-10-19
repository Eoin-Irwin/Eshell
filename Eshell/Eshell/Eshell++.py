import getpass, subprocess, time, ipgetter

systemCommands = {'pw': 'pwd', 'ifc': 'ifconfig eth0', 'ls': 'ls', 'ui': 'uid'}


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


def user_input(choice):
    for x, y in systemCommands.iteritems():
        if choice == x:
            return y


def main():
    subprocess.call('''''', shell=True)

    while True:
        x = raw_input(getpass.getuser() + "@Eshell++:#")
        x = user_input(x)

        subprocess.call(x, shell=True)


if __name__ == '__main__':
    main()
