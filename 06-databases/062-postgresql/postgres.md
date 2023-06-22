# Postgresql 

## Connect to postgres database with `psql`
```
psql --host=$HOSTNAME --port=5432 --username=$USERNAME --dbname=$DBNAME --password
```

## Backup database 
```
pg_dump --dbname=$DBNAME --host=$HOSTNAME --port=$PORT --username=$USERNAME --password > output-filename.sql
```

## Restore backup 
```
pg_restore --host=$HOSTNAME --port=$PORT --username=$USERNAME --password -f output-filename.sql
```

## list databases 
```
\l
```

## list tables 
```
\dt
```
