# # import paramiko
# # pyshark  # tcpdump traffic

from util.logger import get_logger
logger = get_logger()
# https://docs.docker.com/engine/examples/running_ssh_service/#build-an-eg_sshd-image
# https://github.com/KimiNewt/pyshark

import socket
import ipaddress  # To manipulate ipv4/ipv6 address
# # import paramiko
# # import telentlib
# # pyshark  # tcpdump traffic
#
logger.info(socket.gethostname())
logger.info(socket.gethostbyname("google.com"))

# https://docs.python.org/3.6/library/ipaddress.html
# ip = ipaddress.ip_address("127.0.0.1")
#
# for addr in ipaddress.IPv4Network('192.0.2.0/28'):
#     logger.info(addr)


# import pyshark
#
# # pyshark.RemoteCapture(remote_host=, remote_interface=)
# capture = pyshark.LiveCapture(interface='Wi-Fi', display_filter="icmp", output_file="test.cap")
# capture.sniff(packet_count=3)
# print(capture)
# for packet in capture:
#     print("packet...")
#     if 'IP' in packet:
#         print(packet.highest_layer)
#         print("Destination",packet['ip'].dst)
#         print("Source",packet['ip'].src)

# scapy to minipulate packets
# from scapy.layers.inet import IP, ICMP
# from scapy.sendrecv import sr
# import sys
#
# from scapy.all import sniff
#
# pingr = IP(dst="216.58.197.46") / ICMP()
# sr(pingr)
# # sr(pingr)
#
# sniff(count=3, store=1, iface="Wi-Fi", filter="tcp")
import paramiko

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh_client.connect("192.168.99.100",port=2022, username="root",password="root")
# stdin, stdout, stderr = ssh_client.exec_command("ps -ef")
# for line in stdout:
#     print(line)


# import telnetlib
# telnet_client = telnetlib.Telnet(host="192.168.99.100",port=2023)
# print(telnet_client.host)
# telnet_client.write(b"ps -ef\n")
# import time
# time.sleep(2)
# telnet_client.write(b"exit\n")
# print(telnet_client.read_some().decode("ascii"))






