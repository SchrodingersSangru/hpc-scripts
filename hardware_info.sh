#!/bin/bash

# Display system information
echo "===== System Information ====="
echo "Hostname: $(hostname)"
echo "Kernel Version: $(uname -r)"
echo "Operating System: $(cat /etc/os-release | grep "PRETTY_NAME" | cut -d "=" -f 2)"

# Display CPU information
echo -e "\n===== CPU Information ====="
echo "CPU Model: $(grep "model name" /proc/cpuinfo | head -n 1 | cut -d ":" -f 2)"
echo "CPU Cores: $(grep "cpu cores" /proc/cpuinfo | head -n 1 | cut -d ":" -f 2)"
echo "CPU Threads: $(grep "siblings" /proc/cpuinfo | head -n 1 | cut -d ":" -f 2)"
echo "CPU Architecture: $(arch)"

# Display memory information
echo -e "\n===== Memory Information ====="
echo "Total Memory: $(free -h | grep "Mem:" | awk '{print $2}')"
echo "Used Memory: $(free -h | grep "Mem:" | awk '{print $3}')"
echo "Free Memory: $(free -h | grep "Mem:" | awk '{print $4}')"

# Display disk information
echo -e "\n===== Disk Information ====="
echo "Total Disk Space: $(df -h / | tail -n 1 | awk '{print $2}')"
echo "Used Disk Space: $(df -h / | tail -n 1 | awk '{print $3}')"
echo "Available Disk Space: $(df -h / | tail -n 1 | awk '{print $4}')"

# Display network information
echo -e "\n===== Network Information ====="
echo "IP Addresses: $(hostname -I)"
echo "Network Interfaces: $(ip link show | grep "^[0-9]" | awk -F': ' '{print $2}')"

# Display hardware logs (dmesg)
echo -e "\n===== Hardware Logs (dmesg) ====="
dmesg | tail -n 10
