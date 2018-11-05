
NIDAQMX_FILE="nidaqmxbase-15.0.0"

if [ ! -d "$NIDAQMX_FILE" ]; then

  if [ ! -f "${NIDAQMX_FILE}.iso" ]; then
    url="http://download.ni.com/support/softlib/multifunction_daq/nidaqmxbase/15.0/linux/${NIDAQMX_FILE}.iso"
    echo "Downloading $url"
    wget "$url"
  fi

  mount -o loop "${NIDAQMX_FILE}.iso" /mnt
  cp -R /mnt "$NIDAQMX_FILE"
  umount /mnt
fi

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#alien -k --scripts *.rpm
#dpkg -i *.deb

# Now we have to uninstall NI-KAL again (yes, I know this looks like very inefficient way but it works ;) ):
#cd nikal22
#cd rpms
#dpkg -P nikali
#dpkg -i nikali_2.2.1-f0_all.deb

#cd /usr/local/natinst/nikal/bin
#. nikaliInstallerUtility.sh
#nikaliPostInstall
#./updateNIDrivers

echo "Reboot computer to finish installation"
