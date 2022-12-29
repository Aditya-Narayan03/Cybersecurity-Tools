#!/bin/sh

read -p "Enter the target IP: " IPADDR
read -p "Enter the no. of ping to send: " PINGNUM
ping -c $PINGNUM $IPADDR 
