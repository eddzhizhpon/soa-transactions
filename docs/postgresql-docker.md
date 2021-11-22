# Install postgresql with Docker

1. Install docker
   
2. Pull postgres resources
   ```bash
   $ docker pull postgres
   ```
3. Create a volume to persist the data
   ```bash
   $ docker volume create transaction-psql-data
   ```
4. Verify the directory
   ```bash
   $ docker volume inspect transaction-psql-data
   ```
5. Init a container 
   ```bash
    $ docker run -d --name transaction-psql-server -p 5432:5432 -v postgres-data:/var/lib/docker/volumes/transaction-psql-data/_data -e "POSTGRES_PASSWORD=PASS" username
   ```

6. Connect to postgresql
   ```bash
   $ psql -h 127.0.0.1 -p 5432 -U username
   ```

7. Create Database
   
   ```sql
   CREATE DATABASE database_name WITH ENCODING 'UTF8' OWNER username;
   ```

8. List Databases `\l`
9. Connect to Database `\c database_name`