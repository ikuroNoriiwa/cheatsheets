# Passwd File 

# Example passwd
```
test:x:1001:1001:,,,:/home/test:/bin/bash
# {{1}}:{{2}}:{{3}}:{{4}}:{{5}}:{{6}}:{{7}}
```
1. username : used to log user, should be between 1 and 32 char
2. password : X indicates an encrypted passwd 
3. user ID (UID) : UID 
4. Group ID (GID) : primary group ID (checkout /etc/group)
5. User ID infos (GECOS) : comments field, allow to add extra informations such as full name, phone number, ... 
6. Home directory : absolute path for home dir 
7. command/shell : command or shell (/bin/bash, /bin/nologin, ...)
   