import getpass, time, ipgetter, os, sys, subprocess

systemCommands = {'pw': 'pwd', 'ifc': 'ifc', 'dt': 'date', 'ls': 'ls', 'cmatrix': 'enter',
                  'pacman4console': 'pacman', 'nsnake': 'nsnake', 'help': 'help_cmd', 'ud': 'ud'}


def get_ip_address():
    """
     Get the ip address of current system
     :param: None
     :return: None
    """
    ip = ipgetter.myip()
    print ip


def initial_login():
    """
     Initial login screen you are met with
     :param choices: None
     :return: None
   """
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
    """
      Ifconfig which by default displays eth0, unless a tail is supplied
      :param choices: None
      :return: None
    """
    if len(x) > 1:
        os.system('ifconfig {0}'.format(x[1]))
    else:
        os.system('ifconfig eth0')


def ls(choices):
    """
      ls command which will only display ls unless a tail like ls -l is entered
      :param choices: None
      :return: None
    """
    if len(x) > 1:
        os.system('ls {0}'.format(x[1]))
    else:
        os.system('ls')


def pwd(choices):
    """
      Print working directory
      :param choices: None
      :return: None
    """
    os.system('pwd')


def date(choices):
    """
      Print date command in the following format
      :param choices: None
      :return: None
    """
    print time.strftime("%Y%m%d%H%M%S")


def pacman(choices):
    """
      Enter the cmd to run the game
      :param choices: None
      :return: None
     """
    os.system('pacman4console')


def nsnake(choices):
    """
       Play a classic
      :param choices: None
      :return: None
     """
    os.system('nsnake')


def enter(choices):
    """
      Enter the matrix
      :param choices: None
      :return: None
     """
    os.system('cmatrix')


def help_cmd(choices):
    """
      Display all of the options available to the user
      :param choices: None
      :return: True: Evaluate statement the user entered
     """
    print 'Limited commands available to: ', getpass.getuser()
    for k, v in systemCommands.iteritems():
        print k


def user_input(choice):
    """
       evaluate the users choice and return the command, if sudo is entered print a message, exit if it is entered
       :param choice: None
       :return: True: Evaluate statement the user entered
    """
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
        elif choice[0] not in systemCommands:
            print choice, ': Command not found'
            break
        elif choice[0] == 'exit':
            sys.exit(0)
    return False


def ud(choices):
    """
    Prints userid, groupid, username, main groupname, iNode of users home directory.
    :param choices: None
    :return: None
    """
    uname = subprocess.check_output(['whoami']).strip("\r\n")
    uid = subprocess.check_output(['id', '-u', '{0}'.format(uname)]).strip("\r\n")
    gid = subprocess.check_output(['id', '-g', '{0}'.format(uname)]).strip("\r\n")
    grpmain = subprocess.check_output(['groups', '{0}'.format(uname)]).split(' ')
    grpmain = grpmain[2]
    inode = subprocess.check_output(['ls', '-id'])
    print("{0},{1},{2},{3},{4}".format(uid, gid, uname, grpmain, inode))


subprocess.call('clear', shell=True)
x = ''
initial_login()
while x != 'exit':
    x = raw_input(getpass.getuser() + "@Eshell++:#")
    x = x.split(' ')
    x = user_input(x)