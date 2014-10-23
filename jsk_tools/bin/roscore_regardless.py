#!/usr/bin/env python


import rospy
import time
import subprocess
import signal
import os
import sys

global g_process_object

def isMasterAlive():
    """
    return True if master alive and return False if
    master is not alive
    """
    try:
        master = rospy.get_master()
        master.getSystemState()
        return True
    except:
        return False

def runProcess(cmds):
    global g_process_object
    g_process_object = subprocess.Popen(cmds)

def killChildProcesses(ppid):
    output = subprocess.check_output(['ps', '--ppid=' + str(ppid), '--no-headers'])
    for process_line in output.split('\n'):
        strip_process_line = process_line.strip()
        if strip_process_line:
            pid = strip_process_line.split(' ')[0]
            name = strip_process_line.split(' ')[-1]
            print 'killing %s' % (name)
            os.kill(int(pid), signal.SIGINT)

def killProcess():
    global g_process_object
    if g_process_object:
        g_process_object.send_signal(subprocess.signal.SIGINT)
        killChildProcesses(g_process_object.pid)
    
def main(cmds):
    
    previous_master_state = None
    while True:
        master_state = isMasterAlive()
        if not master_state and previous_master_state:
            print "kill process"    
            killProcess()
        elif master_state and not previous_master_state:
            print "restart process"
            runProcess(cmds)
        previous_master_state = master_state
        time.sleep(1.0)
            

if __name__ == '__main__':
    main(sys.argv[1:])
    
