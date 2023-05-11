#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

gnome-terminal -- bash -c "../pox/pox.py forwarding.l2_learning; exec bash"
sleep 5
sudo mn -c
sudo python sdn.py
