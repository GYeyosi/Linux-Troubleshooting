import subprocess
subprocess.call(["systemctl" ,"--user", "enable", "pulseaudio"])
subprocess.call(["systemctl" ,"--user", "start", "pulseaudio"])