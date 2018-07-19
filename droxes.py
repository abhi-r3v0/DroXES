# !/usr/bin/env python

import os
import ConfigParser
import subprocess
import threading

__author__ = 'Abhishek J M ( jmabhishek4@gmail.com, @abhi_r3v0 )'

class DroXES:

    def __init__(self):
        self.tool_list = ['xposed.apk', 'drozer.apk', 'term.apk', 'busybox.apk', 'rootcloak.apk', 'inspeckage.apk', 'SSLunpin.apk']
        self.bin_list = ['tcpdump', 'frida12.0.4']
        self.sys_list = ['android-tools-adb', 'python-pip','python3-pip', 'python-dev', 'python-twisted']
        self.py_dependencies = ['frida==12.0.4']
        self.sys_tools = ['drozer.deb']

    def welcome(self):
        print "\n   dddddddd     rrrrrrrr      ooooooo      xx       xx    eeeeeeee   ssssssss\n" \
              "   dd     dd    rr     rr    oo      oo     xx     xx     ee         ss\n" \
              "   dd      dd   rr     rr    oo      oo      xx   xx      ee         ss\n" \
              "   dd      dd   rr rrrr      00      oo       xx xx       eeeee      ssssssss\n" \
              "   dd      dd   rr    rr     oo      oo      xx   xx      ee               ss\n" \
              "   dd     dd    rr     rr    oo      oo     xx     xx     ee               ss\n" \
              "   dddddddd     rr      rr     oooooo      xx       xx    eeeeeeee   ssssssss\n"
        print "      ------------------------------------------------------------------"
        print "\n      | TOOL    :  Droid eXploitation Environment Setup                |"
        print "      | AUTHOR  :  " + __author__ + "   |"
        print "      | VERSION :  1.0                                                 |\n"
        print "      ------------------------------------------------------------------"


    def install_sys_tools(self):
        print "\n[+] Setting up the system"
        for i in self.sys_list:
            subprocess.call(['sudo', 'apt-get', '-f', 'install', i], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print "\t[+] Installed " + i

        for j in self.py_dependencies:
            subprocess.call(['sudo', '-H', 'pip', 'install', j], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print "\t[+] Installed " + j

        for k in self.sys_tools:
            subprocess.call(['sudo', 'dpkg', '-i', os.getcwd() + "/system/" + k], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print "\t[+] Installed " + k

    def install_tools(self):
        print "\n[+] Installing APK Tools"
        for i in self.tool_list:
            apkout = subprocess.check_output(['adb', 'install', '-r', os.getcwd() + "/apk/" + i], stderr=subprocess.PIPE)
            if 'Success' in apkout:
                print "\t[+] Installed " + i
            else:
                print "\t[-] Error Installing APK"

    def install_bin(self):
        print "\n[+] Installing Binary Tools"
        for i in self.bin_list:
            subprocess.Popen(['adb', 'push', os.getcwd() + '/bin/' + i, '/data/local/tmp'], stderr=subprocess.PIPE)
            print "\t[+] Installed " + i

        os.system('adb shell "chmod 755 /data/local/tmp/frida12.0.4"')
        os.system('adb shell "chmod 755 /data/local/tmp/tcpdump"')

def main():
    dx = DroXES()
    dx.welcome()
    dx.install_sys_tools()
    dx.install_tools()
    dx.install_bin()

if __name__ == '__main__':
    main()

