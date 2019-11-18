#!/bin/bash 
#pwd

#ps -ef|grep server.py|grep -v grep |awk '{print $2}'|xargs -i kill -9 {} 

echo "Stop service ..."

#sleep 5

echo "Start service ..."

nohup /usr/bin/python3 server.py >output.txt &

echo "Started!"