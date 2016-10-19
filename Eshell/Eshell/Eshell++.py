import getpass, subprocess

systemCommands = {'pw': 'pwd', 'ifc': 'ifconfig eth0', 'ls': 'ls'}


def user_input(choice):
    for x, y in systemCommands.iteritems():
        if choice == x:
            return y


def main():
    subprocess.call('', shell=True)

    while True:
        x = raw_input(getpass.getuser() + "@eshell++:#")
        x = user_input(x)

        subprocess.call(x, shell=True)


if __name__ == '__main__':
    main()
