#!/bin/bash
nmap -v -n -p- {{IP}} -oA {{IP}}-all-ports
