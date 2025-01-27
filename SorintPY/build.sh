#!/bin/bash

# Environement Variables
VERSION=1.5
FILE_PATH="RPM/sorint-$VERSION"
REMOTE_HOST=192.168.122.122
REMOTE_USER="user"
REMOTE_USER_PASS="user"

# Make Sure Packages Directory Exist
mkdir -p $FILE_PATH

# Create The RPM Build Directory
rm -rf /home/$USER/rpmbuild
rpmdev-setuptree

# Copy the Spec File to the RPM
cp $FILE_PATH/$VERSION-sorint.spec /home/$USER/rpmbuild/SPECS/sorint.spec

# delete old tar file
rm $FILE_PATH/sorint-$VERSION.tar.gz 2> /dev/null

# Creating Remote SSH ENV
echo "REMOTE_USER=$REMOTE_USER" > /tmp/sshenv
echo "VERSION=$VERSION" >> /tmp/sshenv
echo "REMOTE_USER_PASS=$REMOTE_USER_PASS" >> /tmp/sshenv
rsync /tmp/sshenv $REMOTE_USER@$REMOTE_HOST:~/.ssh/environment

# Delete Old Files From Remote Host
ssh -T $REMOTE_USER@$REMOTE_HOST << 'EOF' | grep -v 'Activate the web console with: systemctl enable --now cockpit.socket'
rm -rf /home/$USER/sorint* 2> /dev/null
echo $REMOTE_USER_PASS | sudo -S rpm -e sorint 2> /dev/null
echo "##################################################\nSorint File and Package has beed deleted\n##################################################\n"
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
if echo $REMOTE_USER_PASS | sudo -S rpm -i /home/$USER/sorint*; then echo "#######  PACKAGE INSTALLED SUCCESSFULLY  #######"; fi
echo $REMOTE_USER_PASS | sudo -S rpm -qi sorint | head -n 5 2> /dev/null
echo "######### END OF SORINT PACKAGE CHECK ##########"
EOF


ssh -T $REMOTE_USER@$REMOTE_HOST << 'EOF' | grep -v 'Activate the web console with: systemctl enable --now cockpit.socket'
echo "###########  BEGIN SORINT COMMAND LOG  ###########"
echo "\n\n------  Course 101 start  -------"
sorint start course101
echo "\n\n------  Course 101 grade  -------"
sorint grade course101
echo "\n\n------  Course 102 Start  -------"
sorint start course102
echo "\n\n------  Course 102 grade  -------"
yes 'N' |sorint grade course102
echo "\n\n------  Course 103 start  -------"
sorint start course103
echo "\n\n------  Course 103 grade  -------"
sorint grade course103
echo $REMOTE_USER_PASS | sudo -S dnf remove httpd -y | tail -n 2 2> /dev/null
echo "\n\n------  Course 104 start  -------"
sorint start course104
echo "\n\n------  Course 104 grade  -------"
sorint grade course104
echo "######### END OF SORINT COMMAND LOG ##########"
EOF