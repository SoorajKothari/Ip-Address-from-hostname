# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:55:09 2019

@author: Sooraj
"""
import socket

hostname = input('Enter Hostname as(www.example.com): ')
ip = socket.gethostbyname(hostname)
print('Ip Address of Hostname : ',hostname,' is : ',ip )