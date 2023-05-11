
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
# TODO Add your imports here 
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

#TODO Add your global variables here 
macs = ['00:00:00:00:00:08', '00:00:00:00:00:07', '00:00:00:00:00:06', '00:00:00:00:00:05', '00:00:00:00:00:04', '00:00:00:00:00:03', '00:00:00:00:00:02', '00:00:00:00:00:01',]
rules = []
firstline = True
with open(policyFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
	if firstline:
	    firstline = False
	    continue
	#print(row[1])
        rules.append(row[1])


class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        #TODO Add your logic here 
	for rule in rules:
	    for addrs in macs:

	        block = of.ofp_match()
	        block.dl_src = EthAddr(addrs)
	        block.dl_dst = EthAddr(rule)
		block.dl_src = EthAddr(rule)
		block.dl_dst = EthAddr(addrs)
	        flow_mod = of.ofp_flow_mod()
	        flow_mod.match = block
	        event.connection.send(flow_mod)


        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    #    Starting the Firewall module
    
    core.registerNew(Firewall)
