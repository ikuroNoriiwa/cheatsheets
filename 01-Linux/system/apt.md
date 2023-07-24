# Apt 

## Update specific repo 
```
sudo apt-get update -o Dir::Etc::sourcelist="sources.list.d/<PERSO_REPO>.list" \
    -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"
```

## Fix and Clean apt list problem 
```
apt clean 
rm -rf /var/lib/apit/lists/*
apt clean 
apt update 
apt upgrade 
```