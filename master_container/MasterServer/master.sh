#!/bin/bash
sleep 5 # waiting for postgresql to start
psql -h /var/run/postgresql -tc "SELECT 1 FROM pg_database WHERE datname = 'master'" -d template1 | grep -q 1 || psql -h /var/run/postgresql -f /app/PwnAdventure3/initdb.sql -d template1
cd /app/PwnAdventure3/
./MasterServer
