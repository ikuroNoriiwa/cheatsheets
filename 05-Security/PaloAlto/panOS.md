# Pan OS 

### Configuration mode 
```
configure
```

### Commit modifications 
```
commit
```

### Usefull Commands 

Show important informations about the system (hostname, ip address, public ip, gateway, SN, ...)
```
show system info
```

Show real time stattistic about the session or applications 
``` 
show system statistics <session>/<application>
```

show resources of the systems 
```
show system resources 
```

show all the interfaces 
```
show interface all
```

show routing tables 
```
show routing route
```

Test route and show interface/gateway for a specified address --> traceroute
```
test routing fib-lookup virtual-router default ip <IP_ADDRESS>
```

show all the sessions or specified session
```
show session
```

Show all session to particular dest or port 
```
show session all filter destination <IP_ADDRESS> destination-port <PORT>
```

show all policies 
```
show running security-policy
```

show policy that match with a packet 
```
test security-policy-match from Trust to Untrust source 10.10.10.20 destination 9.9.9.9 protocol 53 
# test security-policy-match from <SOURCE_ZONE> to <DEST_ZONE> source <SOURCE_IP> destination <DEST_IP> protocol <PORT> 
```

Shutdown gracefully the system
```
retquest restart|shutdown system  
```

Show systems logs or traffic or threats 
```
show log system|traffic|threats
```

show log from begin/end of the logs 
```
show log traffic direction equal backward|forward 
```

Set manual ip address 
``` 
set deviceconfig system type static
set deviceconfig system ip-address <LOCAL_IP> netmask <MASK> default-gateway <GATEWAY_IP> dns-seeting servers primary <DNS_IP>
```

## Create security policy 
```
set rulebase security rules <POLICY_NAME> from <SOURCE_ZONE> to <DESTINATION_ZONE> rule-type <interzone|intrazone|universal> source <SOURCE_IP|COUNTRY_CODE_SOURCE|IP_RANGE_SOURCE|any> destination <DEST_IP|COUNTRY_CODE_DEST|IP_RANGE_DEST|any> application <APPLICATION_NAME|any> service <SERVICE_NAME|any> action <allow|deny>
```

## Create Security zone 
```
set zone <ZONE_name> network <layer3|layer2|tap>
```

## Create Service 
```
set service <SERVICE_NAME> protocol <tcp|udp> port <PORT_NUMBER>
```

## Create NAT policy 
```
set rulebase nat rules <RULE_NAME> from <SOURCE_ZONE> to <DESTINATION_ZONE> nat-type ipv4 
```

## Create address 
```
set address <ADDRESS_NAME> ip-range 192.168.1.10-192.168.1.20
```

## Create application Filter 
```
set application-filter <FILTER_NAME> risk <1-5>
```