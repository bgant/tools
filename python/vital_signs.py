#!/usr/bin/python
import subprocess

class Check:
    def __init__(self):
        if 'bluefin' in self.run('cat /etc/os-release'):
            self.bluefin_data()
        pass

    def run(self, command_string):
        '''Shorter way to run command'''
        return subprocess.check_output(command_string, shell=True, text=True)

    def bluefin_data(self):
        '''Gather data on Bluefin operating system'''
        # CPU
        self.cpu_cores = float(self.run('grep -c "cpu cores" /proc/cpuinfo').split()[0])
        self.cpu_load =  float(self.run('cat /proc/loadavg').split()[1])

        # MEMORY
        free_output = self.run('free | grep Mem')
        self.mem_total = int(free_output.split()[1])
        self.mem_used  = int(free_output.split()[2])

        # ROOT DISK
        df_output = self.run('df / | grep /')
        self.root_total = int(df_output.split()[1])
        self.root_used = int(df_output.split()[2])

        # INTERFACE
        iface = 'wlp1s0' # Need a way to specify interface in setup
        ifconfig_output = self.run(f'ifconfig {iface}')
        self.link_status = 'UP' if 'UP' in ifconfig_output else 'DOWN'
        self.network = self.run(f'nmcli dev show {iface} | grep GENERAL.TYPE').split()[1]
        self.ip = self.run(f'nmcli dev show {iface} | grep IP4.ADDRESS').split()[1]
        self.gateway = self.run(f'nmcli dev show {iface} | grep IP4.GATEWAY').split()[1]
        self.dns_server = self.run(f'nmcli dev show {iface} | grep IP4.DNS').split()[1]

    def manjaro_commands(self):
        '''Gather data on Manjaro operating system'''
        pass

    def save_state(self):
        pass

    def cpu(self):
        '''Return True if CPU load is OK'''
        return True if self.cpu_load <= self.cpu_cores else False

    def memory(self):
        '''Return True if Memory usage is OK'''
        return True if self.mem_used < self.mem_total else False

    def disk(self):
        '''Return True if root volume is OK'''
        return True if self.root_used < self.root_total else False

    def link(self):
        '''Return True if network link is UP'''
        return True if 'UP' in self.link_status else False