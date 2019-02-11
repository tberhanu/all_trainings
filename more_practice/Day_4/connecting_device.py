""" QUESTION 9
Write a program that connect to a device it can be even localhost
(use pexpect package) and print all the files in the default directory
"""
import pexpect
def connecting_device():
    password = input("Enter your password: ")
    ssh = pexpect.spawn('ssh tess@192.168.0.18 ls')
    ssh.expect('Password:')
    ssh.sendline(password)
    ssh.read()
    print(str(ssh.before, encoding="utf-8"))

connecting_device()

