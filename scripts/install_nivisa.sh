NIVISA_FILE="NI-VISA-17.0.0"

if [ ! -d "$NIVISA_FILE" ]; then
  if [ ! -f "${NIVISA_FILE}.iso" ]; then
    wget "http://download.ni.com/support/softlib/visa/NI-VISA/17.0/Linux/${NIVISA_FILE}.iso"
  fi

  mount -o loop "${NIVISA_FILE}.iso" /mnt
  cp -R /mnt "$NIVISA_FILE"
  umount /mnt
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#cd nivisa/mnt
#/.INSTALL --nodeps

#When the installation is finished we have to install NI-KAL again. Now we access to the NI-KAL installation folder, uninstall and install the nikali package:
#cd nikal22/rpms
#dpkg -P nikali
#dpkg -i nikali_2.2*.deb

#cd /usr/local/natinst/nikal/bin
#. nikaliInstallerUtility.sh
#nikaliPostInstall
#./updateNIDrivers

echo "Reboot computer to finish installation"
