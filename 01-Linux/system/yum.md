# Yum 

## Repair yum error Thread diead in Berkeley DB library 
For the following error : 
```
error: rpmdb: BDB0113 Thread/process 5318/140564232927296 failed: BDB1507 Thread died in Berkeley DB library
error: db5 error(-30973) from dbenv->failchk: BDB0087 DB_RUNRECOVERY: Fatal error, run database recovery
error: cannot open Packages index using db5 -  (-30973)
error: cannot open Packages database in /var/lib/rpm
CRITICAL:yum.main:

Error: rpmdb open failed
```
It means that the RPM database is corrupted, it can be simply repaired removing the rpm database : 

```bash 
mkdir /var/lib/rpm/backup
cp -a /var/lib/rpm/__db* /var/lib/rpm/backup/
rm -f /var/lib/rpm/__db.[0-9][0-9]*
rpm --quiet -qa
rpm --rebuilddb
yum clean all
```