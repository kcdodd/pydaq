#!/bin/bash

#http://maztories.blogspot.com/2013/03/ni-usb-6008-card-can-be-installed-in.html

BASE=$PWD

MNT="/media/tmpniisomntpt"

NIKAL_FILE="NIKAL175"
NIKAL_VERSION="17.5.1"

if [ -d "$NIKAL_FILE" ]; then
  rm -r "$NIKAL_FILE"
fi

if [ ! -f "${NIKAL_FILE}.iso" ]; then
  url="http://download.ni.com/support/softlib/kal/$NIKAL_VERSION/$NIKAL_FILE.iso"
  echo "Downloading '$url'"
  wget "$url"
fi


if [ ! -d "$MNT" ]; then
  mkdir "$MNT"
fi

mount -o loop "${NIKAL_FILE}.iso" "$MNT"

if [[ $(findmnt -M "$MNT") ]]; then
  echo "Copying contents to '$NIKAL_FILE'"
  cp -R "$MNT" "$NIKAL_FILE"
  umount "$MNT"
else
  echo "Failed to mount '${NIKAL_FILE}.iso'."
  exit 1
fi

rm -r "$MNT"


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

cd "$NIKAL_FILE"
tarfile=$(find . -regex "^./nikal\-.+\.tar\.gz$")

tar -zxf "$tarfile"

cd rpms
alien -k --scripts ni-kal-*.noarch.rpm
dpkg -i ni-kal_*.deb

cd /usr/local/natinst/nikal/bin

#./nikalKernelInstaller -i

. ni-kalInstallerUtility.sh

#nikaliPostInstall

ni_kalPostInstall

./updateNIDrivers

#echo "Reboot computer to finish installation"
