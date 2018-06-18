import os.path 
import subprocess
from getpass import getpass



def started_as_root():
    if subprocess.check_output('whoami').strip() == 'root':
        return True
    return False

class runing_with_root_privileges:
    def __init__(self):
        file = open('/etc/pulse/daemon.conf','r+')
        file1 = open('/etc/pulse/daemon.conf1','w+')
        lines = file.readlines()
        for line in lines:
            self.string = line
            file_content = self.string.replace( "daemonize = no" , "daemonize = yes")
            file1.write(file_content)
            #file1.write("\n")
        file1.close()
        os.system("sudo rm /etc/pulse/daemon.conf")
        os.system("mv /etc/pulse/daemon.conf1 /etc/pulse/daemon.conf")
        os.system("systemctl --user enable pulseaudio")
        os.system("systemctl --user start pulseaudio")
       
  

def main():
    #os.system("sudo apt-get install pulseaudio -y ")
    if started_as_root():
        runing_with_root_privileges()
    else:
        print( "You are just a user. Need to start new process with root privileges...")
        current_script = os.path.realpath(__file__)
        password_for_sudo = getpass()
        os.system('echo %s|sudo -S python %s' % (password_for_sudo, current_script))


if __name__ == '__main__':
    main()