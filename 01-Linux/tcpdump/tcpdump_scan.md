# tcpdump
tcpdump needs to be launched by root user

## Basic scan all networks 
tcpdump 

## scan specific interface
tcpdump -i eth0

## scan specific host 
tcpdump host 1.1.1.1 

## scnan without resolving ip adresses 
tcpdump -n 

## scan without resolving services 
tcpdump -nn 

## basic filter 
tcpdump port not 22 

## Example 
tcpdump -i eth0 host 1.1.1.1 or host 1.1.4.4 and port not 22 and port not 443 -n 