#!/usr/bin/python
import subprocess

class Check:
    def __init__(self):
        if 'bluefin' in self.run('cat /etc/os-release'):
            self.bluefin_commands()
        else:
            print('ERROR: Operating System Not Supported')

    def run(self, command_string):
        '''Shorter way to run subprocess command'''
        try:
            output = subprocess.check_output(command_string, stderr=subprocess.STDOUT, shell=True, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        return output

    def bluefin_commands(self):
        '''Commands on Bluefin operating system'''
        # CPU
        self.cpu_cores_command = "grep -c 'cpu cores' /proc/cpuinfo"
        self.cpu_load_command  = "cat /proc/loadavg | awk '{print $2}'"

        # MEMORY
        self.mem_total_command = "free | grep Mem | awk '{print $2}'"
        self.mem_used_command  = "free | grep Mem | awk '{print $3}'"

        # ROOT DISK
        self.root_total_command = "df / | grep / | awk '{print $2}'"
        self.root_used_command  = "df / | grep / | awk '{print $3}'"

        # INTERFACE
        self.get_connected_interface()
        self.link_status_command = f"ifconfig {self.iface}"
        nmcli_command = f'nmcli dev show {self.iface}'
        self.network_type_command = nmcli_command + " | grep GENERAL.TYPE | awk '{print $2}'"
        self.gateway_command      = nmcli_command + " | grep IP4.GATEWAY | awk '{print $2}'"
        self.ip_command           = nmcli_command + " | grep IP4.ADDRESS | awk '{print $2}'"
        self.dhcp_command         = 'ip route list default'  # search for dhcp or static

        # NETWORK
        self.ping_command = 'ping -nq -i0.5 -c3 '  # Add <server>
        self.traceroute_command = 'traceroute -Fn --max-hops=4 '  # Add <server>

        # DNS
        self.dns_server_command   = nmcli_command + " | grep IP4.DNS | awk '{print $2}'"
        self.dns_request_command  = 'nslookup cloudflare.com '  # Add <server>

        # SERVICE
        self.tcp_command = 'nc -vz '  # Add <server> <port>
        self.udp_command = 'nc -vzu ' # Add <server> <port>

    def manjaro_commands(self):
        """Commands on Manjaro operating system"""
        pass

    def save_state(self):
        '''Save variables and state for next run'''
        pass

    def cpu(self):
        '''Return True if CPU load is OK'''
        self.cpu_cores = float(self.run(self.cpu_cores_command))
        self.cpu_load  = float(self.run(self.cpu_load_command))
        return True if self.cpu_load <= self.cpu_cores else False

    def memory(self):
        '''Return True if Memory usage is OK'''
        self.mem_total = float(self.run(self.mem_total_command))*0.95  # Bad if within 95% of Max
        self.mem_used =  float(self.run(self.mem_used_command))
        return True if self.mem_used < self.mem_total else False

    def disk(self):
        '''Return True if root volume is OK'''
        self.root_total = float(self.run(self.root_total_command))*0.95  # Bad if within 95% of Max
        self.root_used  = float(self.run(self.root_used_command))
        return True if self.root_used < self.root_total else False

    def get_connected_interface(self):
        '''Get connected interface name'''
        self.iface = self.run("nmcli dev | grep -v loopback | grep ' connected' | awk '{print $1}'")
        if self.iface:
            self.iface = self.iface.rsplit()[0]
        else:
            self.iface = 'unknown'

    def link(self):
        '''Return True if network link is UP'''
        self.get_connected_interface()
        self.network_type = self.run(self.network_type_command)
        if 'Error' in self.network_type:
            self.network_type = None
        else:
            self.network_type = self.network_type.rsplit()[0]  # Remove newline

        self.link_status = 'UP' if 'UP' in self.run(self.link_status_command) else 'DOWN'
        return True if 'UP' in self.link_status else False

    def dhcp(self):
        '''Return True if using DHCP'''
        return True if 'dhcp' in self.run(self.dhcp_command) else False

    def ip(self):
        '''Return True if IP is assigned to Interface'''
        self.ip_address = self.run(self.ip_command)
        if not self.ip_address:
            return False
        if 'Error' in self.ip_address:
            self.ip_address = None
            return False
        self.ip_address = self.ip_address.rsplit()[0]  # Remove newline
        return True

    def router(self):
        '''Return True if local router/gateway responds to pings'''
        self.gateway = self.run(self.gateway_command)
        if '--' in self.gateway:
            self.gateway = None
            return False
        if 'Error' in self.gateway:
            self.gateway = None
            return False
        self.gateway = self.gateway.rsplit()[0]  # Remove newline
        ping_output = self.run(self.ping_command + self.gateway)
        return False if '100% packet loss' in ping_output else True

    def traceroute(self):
        '''Return True if ISP routers are responding to traceroute'''
        target = '8.8.8.8'
        self.traceroute_output = self.run(self.traceroute_command + target)
        return False if 'Network is unreachable' in self.traceroute_output else True

    def dns(self):
        '''Return True if ISP DNS responds to requests'''
        self.dns_server = self.run(self.dns_server_command)
        if not self.dns_server:
            return False
        if 'Error' in self.dns_server:
            self.dns_server = None
            return False
        self.dns_server = self.dns_server.rsplit()[0]  # Remove newline
        dns_request = self.run(self.dns_request_command + self.dns_server)
        return False if 'no servers could be reached' in dns_request else True

    def dns_google(self):
        '''Return True if Google DNS server responds to requests'''
        dns_google    = self.run(self.dns_request_command + '8.8.4.4')
        return False if 'no servers could be reached' in dns_google else True

    def dns_quad9(self):
        '''Return True if Quad9 DNS server responds to requests'''
        dns_quad9     = self.run(self.dns_request_command + '9.9.9.9')
        return False if 'no servers could be reached' in dns_quad9 else True

    def tcp(self, host, port):
        '''Return True if TCP connection to port is established'''
        connect = self.run(self.tcp_command + host + ' ' + port)
        return False if 'Connection refused' in connect else True

    def udp(self, host, port):
        '''Return True if UDP connection to port is established'''
        connect = self.run(self.udp_command + host + ' ' + port)
        return False if 'Connection refused' in connect else True

if __name__ == '__main__':
    check = Check()
    print('CPU:    OK') if check.cpu()        else print('CPU:    High')
    print('Memory: OK') if check.memory()     else print('Memory: No Space')
    print('Disk:   OK') if check.disk()       else print('Disk:   No Space')
    print(f'Link:   {check.link_status} ({check.network_type} {check.iface})') if check.link() else print('Link:   DOWN')
    print('DHCP:   YES') if check.dhcp()      else print('DHCP:   No')
    print(f'IP:     {check.ip_address}') if check.ip() else print('IP:    No')
    print('Router: OK') if check.router()     else print('Router: Not Responding')
    print('ISP:    OK') if check.traceroute() else print('ISP:    Not Responding')
    if check.dns():
        print('DNS:    OK')
    elif check.dns_google():
        print('DNS:    ISP Server Down but Google DNS works')
    else:
        print('DNS:    Not Responding')
