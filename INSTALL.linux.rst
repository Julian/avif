=====
Linux
=====


  Tested on Arch Linux, Linux Mint 20, Ubuntu 20.04 and Fedora 33 (all amd64)


Build Requirements
------------------

- **libavif**:

  - cmake
  - make
  - ninja
  - gcc
  - g++
  - nasm
  - git
  - sudo

- **Python module**:

  - python (3.7+)
  - python development (python3-dev or python3-devel)
  - pip
  - patchelf
  - unzip


Arch
^^^^

.. code-block:: sh

  sudo pacman -Sy
  sudo pacman -S cmake make ninja gcc nasm git python3 python-pip patchelf unzip


Fedora
^^^^^^

.. code-block:: sh

  sudo dnf update
  sudo dnf install cmake make ninja-build gcc g++ nasm git python3-devel python3-pip patchelf unzip


Ubuntu
^^^^^^

.. code-block:: sh

  sudo apt-get update
  sudo apt-get install cmake make ninja-build gcc g++ nasm git python3-dev python3-pip patchelf unzip


Build Steps
-----------

  **Warning:**
  The build steps are tested only on amd64 (x86_64) architecture.


#. Create a folder just to have everything in the same place:

   - ``mkdir ~/python-avif``
   - ``cd ~/python-avif``


#. Now you can clone the repositories:

   - ``git clone https://github.com/Julian/avif.git``
   - ``git clone https://github.com/AOMediaCodec/libavif.git``

   The directory with python module will now appear as ``avif`` and the official avif implementation written in c will be called ``libavif``


#. You will also need to clone and compile the AOM repository.

   It can be done using script included in ``libavif/ext`` directory, but in order to use it from python you have to make some changes to the script by yourself.

   Edit the ``libavif/ext/aom.cmd`` script:

   - Add ``-DBUILD_SHARED_LIBS=1`` after ``cmake -G Ninja -DCMAKE_BUILD_TYPE=Release`` and keep rest of the line as is

   Alternatively if you don't want to leave your terminal, you can type this to update the file from command line:

   - ``sed -i 's/-DCMAKE_BUILD_TYPE=Release/& -DBUILD_SHARED_LIBS=1/' libavif/ext/aom.cmd``


#. Execute the script from the terminal:

   - ``cd libavif/ext``
   - ``sh aom.cmd``
   - ``cd ..``

   After compilation step you will probably be prompted to type root password to install aom libraries to your system.


#. After all of this you can compile libavif with AOM support:

   - Ensure that you are in the main libavif directory (``echo $PWD`` should give ``~/python-avif/libavif``)
   - ``cd cmake``
   - ``cmake .. -DAVIF_LOCAL_AOM=ON -DAVIF_CODEC_AOM=ON``
   - ``make -j`nproc```
   - ``sudo make install``

   It will install libavif to ``/usr/local/``.

   ``-j`nproc``` means that the compiler will use all CPU threads to compile. If you want to change it and use for example 2 threads, you can provide `-j2` instead.


#. On the python side install ``auditwheel`` module:

   - ``pip install --user auditwheel``

   This is optional, but if the shell is telling you that it couldn't find ``pip`` or ``python``
   (or if you have Python 2.x also installed), you should make some temporary aliases:

   - ``alias pip=pip3``
   - ``alias python=python3``


#. Build wheel for this package:

   - ``cd ~/python-avif/avif``
   - ``pip wheel .``


#. Now you shoud see ``.whl`` file created by pip.

   If it exists, you should run ``auditwheel`` on it to add ``libavif`` that you've compiled before to the wheel.

   - ``export LD_LIBRARY_PATH=/usr/local/lib``
   - ``python -m auditwheel repair --plat linux_x86_64 avif-*-linux_x86_64.whl``

   On some distributions, you may need to set ``LD_LIBRARY_PATH`` to ``/usr/local/lib64`` instead


#. The ``auditwheel`` binary should create folder named ``wheelhouse`` and put your final wheel there.

   - ``cd wheelhouse``
   - ``pip install --user avif-*-linux_x86_64.whl``


#. And that should be it!

   Now you can import module from Python to check if it imports correctly:

   .. code-block:: python

     >>> import avif

   You can also run the `examples <README.rst#Examples>`_.
