#!/bin/bash

### BEGIN INIT INFO
# Provides: EOT_init.sh
# Required-Start: $remote-fs $syslog
# Required-Stop: $remote-fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start EOT at boot time
# Description: Enable service provided by EOT
### END INIT INFO


## Open X-terminal , maximize window and run given command;
## First, open virtual environment for python. If your virtual environment
## has different name; change the 'cv' with yours.
## Then go to application folder. If your folder is not on the desktop;
##  you have to change the given directory with yours.
## Finally, launch 'Main.py'
xterm -maximized -e "workon cv ; cd ~/Desktop/EOT ;echo ':::::::::EOT has started . . .:::::::::'; python Main.py"

