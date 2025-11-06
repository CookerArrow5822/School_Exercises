#!/usr/bin/env python3

def ip2int(address):
	o1, o2, o3, o4 = [int(o) for o in address.split('.')]
	return (o1 << 24) + (o2 << 16) + (o3 << 8) + o4

def int2ip(number):
	o4 = number & 255
	o3 = (number >> 8) & 255
	o2 = (number >> 16) & 255
	o1 = number >> 24
	return '.'.join([str(o) for o in [o1, o2, o3, o4]])

class IPv4Network(object):

	def __init__(self, address, subnet_mask):
		self.address = ip2int(address)
		self.subnet_mask = ip2int(subnet_mask)

	def on_network(self, address):
		return self.address & self.subnet_mask == ip2int(
			address) & self.subnet_mask

	def __str__(self):
		ips = []
		caddr = self.address & self.subnet_mask
		faddr = caddr | ((1 << 32) - 1 - self.subnet_mask)
		while caddr <= faddr:
			ips.append(int2ip(caddr))
			caddr += 1
		return '\n'.join(ips)