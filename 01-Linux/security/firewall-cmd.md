# firewall-cmd 

## Open port on Centos Based server 
```
firewall-cmd --zone=public --add-port=8200/tcp --permanent 
firewall-cmd --reload
```
Open port 8200 on zone public (Low level of trust). The `--permanent` indicate the firewall rule will be applied on every reboot of firewalld service 

## List Firewall zones 
```
firewall-cmd --get-zones 
```

