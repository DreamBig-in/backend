### How to setup in your Ubuntu machine. :technologist:

[Testing url]()\
[Production url]()

---
> **_NOTE: All the cmds must be executed on terminal_** 

1. Postgresql Setup:
  ```python
  sudo -u postgres psql
  CREATE DATABASE dream;
  CREATE USER dream WITH PASSWORD 'dream';
  ALTER ROLE dream SET client_encoding TO 'utf8';
  ALTER ROLE dream SET default_transaction_isolation TO 'read committed';
  ALTER ROLE dream SET timezone TO 'UTC';
  GRANT ALL PRIVILEGES ON DATABASE dream TO dream;
  ```
 2. Python setup:
 ```python
 pip install -r requirements.txt
 sudo systemctl start postgresql
 ```
 
---
 


Cheers
Happy Coding