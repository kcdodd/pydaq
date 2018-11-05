
Prerequisites to installing the NI-DAQmx drivers

.. code-block::
  $ sudo apt-get install alien build-essential libelf-dev
  $ sudo apt-get build-dep --no-install-recommends linux-image-$(uname -r)
  $ sudo apt-get install linux-source linux-headers-$(uname -r)

Installation order

.. code-block::
  sudo install_nikal.sh

reboot computer

.. code-block::
  sudo install_nivisa.sh

reboot computer

.. code-block::
  sudo install_nidaqmxbase.sh

reboot computer
