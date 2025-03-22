import re
import netlist

input_lines = open("data.txt").read().splitlines()

net = netlist.netlist()

for line in input_lines:
    net.add_line(line)
