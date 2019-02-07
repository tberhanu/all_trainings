""" QUESTION 8"""
import ipaddress


def increment_ip(address, val):

    return ipaddress.ip_address(address) + val



address = "192.168.3.225"
increment_value = 100
print(increment_ip(address, increment_value))
address = "192.168.3.255"
increment_value = 100
print(increment_ip(address, increment_value))
address = "192.100.255.255"
increment_value = 100
print(increment_ip(address, increment_value))
