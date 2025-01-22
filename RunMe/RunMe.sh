#!/bin/bash

# Update the package manager
sudo dnf update -y

# Upgrade the system
sudo dnf upgrade -y

# Install the packages
sudo dnf install vim-enhanced firewalld net-tools openssh-server git curl wget python3 python3-pip nano openssh-clients tree rsync -y

# install needed python Models
pip install psutil
pip install termcolor

# Remove unnecessary files and packages
sudo dnf autoremove -y
sudo dnf clean all

# Remove SSH host keys
sudo rm -rf /etc/ssh/ssh_host_*

# Disable SELinux
sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config

# Clear logs and machine-specific data
sudo rm -rf /var/log/*

echo "Packages installed successfully!"
echo "SELinux has been disabled."
echo "Keys Has been removed."
