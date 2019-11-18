#!/bin/bash
ps -ef|grep server.py|grep -v grep |awk '{print $2}'|xargs -i kill -9 {}