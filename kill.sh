#!/usr/bin/env bash
export PATH=/usr/bin/python:$PATH

ps aux | grep 'python main.py' | grep -v grep | grep 'restart\|start\|stop' | awk '{print $2}'| xargs kill -9