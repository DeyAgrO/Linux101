#!/bin/bash

# Create The RPM Build Directory
rm -rf /home/$USER/rpmbuild
rpmdev-setuptree

# Copy the Spec File to the RPM
cp sorint.spec /home/$USER/rpmbuild/SPECS

# delete old tar file
rm sorint-1.4.tar.gz

# Create tar archive
tar --create --file sorint-1.4.tar.gz sorint-1.4

# Copy the Spec File to the RPM
cp sorint-1.4.tar.gz /home/$USER/rpmbuild/SOURCES

# Build the rpm
rpmbuild -ba --define='_buildhost FC41' ~/rpmbuild/SPECS/sorint.spec


# copy the RPM to the remote
rsync ~/rpmbuild/RPMS/noarch/sorint-1.4-el9.noarch.rpm user@192.168.122.122:/home/user/
