#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet

from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def treeTopo():
    c1 = RemoteController('c1', ip = '127.0.0.1', port=6653)
    topo = TCPTopo()
    net = Mininet(topo = topo, host = CPULimitedHost, link = TCLink, controller=RemoteController)
    #net.addController(c1)
    net.start()
    #CLI(net)
    #dumpNodeConnections(net.hosts)
    net.pingAll()
    net.stop()

class TCPTopo(Topo):
    def build(self):
 	h1 = self.addHost('h1', mac = "00:00:00:00:00:01")
	h2 = self.addHost('h2', mac = "00:00:00:00:00:02")
	h3 = self.addHost('h3', mac = "00:00:00:00:00:03")
	h4 = self.addHost('h4', mac = "00:00:00:00:00:04")
	h5 = self.addHost('h5', mac = "00:00:00:00:00:05")
	h6 = self.addHost('h6', mac = "00:00:00:00:00:06")
	h7 = self.addHost('h7', mac = "00:00:00:00:00:07")
	h8 = self.addHost('h8', mac = "00:00:00:00:00:08")
	s1 = self.addSwitch('s1')
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')
	s5 = self.addSwitch('s5')
	s6 = self.addSwitch('s6')
	s7 = self.addSwitch('s7')
	self.addLink(h1, s3)
	self.addLink(h2, s3)
	self.addLink(h3, s4)
	self.addLink(h4, s4)
	self.addLink(h5, s6)
	self.addLink(h6, s6)
	self.addLink(h7, s7)
	self.addLink(h8, s7)
	self.addLink(s3, s2)
	self.addLink(s4, s2)
	self.addLink(s6, s5)
	self.addLink(s7, s5)
	self.addLink(s2, s1)
	self.addLink(s5, s1)
	return

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
