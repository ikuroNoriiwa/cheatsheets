# SSH 

## Open Proxy Socks on remote host
### -q quiet mode 
### -D Specifies a local "dynamic" Application-level port forwarding 
### -N Do not execute remote command 
### -C Request compression of all data (same algorithm as gzip)
### -f Request ssh to go to background 
ssh -D <PROXY_PORT> -q -C -N -f <REMOTE_HOST>