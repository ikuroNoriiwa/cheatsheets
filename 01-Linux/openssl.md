# Openssl 

## Check p12 cert informations 
openssl pkcs12 -info -in <p12CERTFILE>.p12 -nodes

## export p12 private key to pem file 
openssl pkcs12 -in <p12CERTFILE>.p12 -clcerts -nodes -nocerts | openssl rsa -outform PEM > <private_key>.pem