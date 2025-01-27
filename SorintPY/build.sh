#!/bin/bash

# Environement Variables
VERSION=1.5
FILE_PATH="Builds/sorint-$VERSION"
REMOTE_HOST=192.168.122.122
REMOTE_USER="user"

# Make Sure Packages Directory Exist
mkdir -p $FILE_PATH

# Create The RPM Build Directory
rm -rf /home/$USER/rpmbuild
rpmdev-setuptree

# Copy the Spec File to the RPM
cp $FILE_PATH/$VERSION-sorint.spec /home/$USER/rpmbuild/SPECS/sorint.spec

# delete old tar file
rm $FILE_PATH/sorint-$VERSION.tar.gz

# Creating Remote SSH ENV
echo "REMOTE_USER=$REMOTE_USER" > /tmp/sshenv
echo "VERSION=$VERSION" >> /tmp/sshenv
rsync /tmp/sshenv $REMOTE_USER@$REMOTE_HOST:~/.ssh/environment

# Delete Old Files From Remote Host
ssh -T $REMOTE_USER@$REMOTE_HOST << 'EOF' | grep -v 'Activate the web console with: systemctl enable --now cockpit.socket'
rm -rf /home/$USER/sorint* 2> /dev/null
sudo rpm -e sorint 2> /dev/null
EOF

# Create tar archive
tar --create --file $FILE_PATH/sorint-$VERSION.tar.gz sorint-$VERSION

# Copy the Spec File to the RPM
cp $FILE_PATH/sorint-$VERSION.tar.gz /home/$USER/rpmbuild/SOURCES

# Build the rpm
rpmbuild -ba --define='_buildhost FC41' ~/rpmbuild/SPECS/sorint.spec > /dev/null 2> build.log

# Show Build Indo
echo "###########  BEGIN BUILD LOG  ###########"
tail -n 6 build.log
echo "########### END OF BUILD LOG ############"

# copy the RPM to the remote
rsync ~/rpmbuild/RPMS/noarch/sorint-$VERSION-el9.noarch.rpm $REMOTE_USER@$REMOTE_HOST:/home/$REMOTE_USER/


# Install new RPM on Remote Host
ssh -T $REMOTE_USER@$REMOTE_HOST << 'EOF' | grep -v 'Activate the web console with: systemctl enable --now cockpit.socket'
if sudo rpm -i /home/$USER/sorint*; then echo "#######  PACKAGE INSTALLED SUCCESSFULLY  #######"; fi
sudo rpm -qi sorint | head -n 5 2> /dev/null
echo "######### END OF SORINT PACKAGE CHECK ##########"
EOF


ssh -T $REMOTE_USER@$REMOTE_HOST << 'EOF' | grep -v 'Activate the web console with: systemctl enable --now cockpit.socket'
echo "###########  BEGIN SORINT COMMAND LOG  ###########"
echo "\n------  Course 101 Errors  -------"
sorint start course101 | grep -e Error -e module
echo "\n------  Course 102 Start Errors  -------"
sorint start course102 | grep -e Error -e module
echo "\n------  Course 103 Errors  -------"
sorint start course103 | grep -e Error -e module
sorint grade course103 | grep -e Error -e module
echo "\n------  Course 104 Errors  -------"
sudo sorint start course104 | grep -e Error -e module
sudo sorint grade course104 | grep -e Error -e module
echo "######### END OF SORINT COMMAND LOG ##########"
EOF
