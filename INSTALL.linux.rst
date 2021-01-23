=====
Linux
=====


  tested on Arch Linux, Linux Mint 20, Ubuntu 20.04 and Fedora 33 (all amd64)


Build Requirements
------------------


- cmake
- make
- ninja
- gcc
- g++
- nasm
- git
- sudo
- python (3.7+)
- python development (python3-dev or python3-devel)
- pip


**Arch:**

::

  sudo pacman -Sy
  sudo pacman -S cmake make ninja gcc nasm git python3 python-pip


**Fedora:**

::

  sudo dnf update
  sudo dnf install cmake make ninja-build gcc g++ nasm git python3-devel python3-pip


**Ubuntu:**

::

  sudo apt-get update
  sudo apt-get install cmake make ninja-build gcc g++ nasm git python3-dev python3-pip


Build Steps
-----------

1. Install cffi module from pypi:

   - ``sudo pip3 install --upgrade cffi``

   This will allow to compile bindings


2. Create a folder just to have everything in the same place:

   - ``mkdir ~/python-avif``
   - ``cd ~/python-avif``


3. Now you can clone the repositories:

   - ``git clone https://github.com/Julian/avif.git``
   - ``git clone https://github.com/AOMediaCodec/libavif.git``

   The directory with python module will now appear as ``avif`` and the official avif implementation written in c will be called ``libavif``


4. You will also need to clone and compile the AOM repository.

   It can be done using script included in ``libavif/ext`` directory, but in order to use it from python you have to make some changes to the script by yourself.

   Edit the ``libavif/ext/aom.cmd`` script:

   - Add ``-DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=1`` after ``cmake -G Ninja -DCMAKE_BUILD_TYPE=Release`` and keep rest of the line as is
   - Add the line that says ``sudo ninja install`` below the line with ``ninja``


5. Execute the script from the terminal:

   - ``cd libavif/ext``
   - ``sh aom.cmd``
   - ``cd ..``

   After compilation step you will probably be prompted to type root password to install aom libraries to your system


6. After all of this you can compile libavif with AOM support:

   - Ensure that you are in the main libavif directory (``echo $PWD`` should give ``~/python-avif/libavif``)
   - ``cd cmake``
   - ``cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DAVIF_CODEC_AOM=ON``
   - ``make -j`nproc```
   - ``sudo make install``

   The ``-DCMAKE_INSTALL_PREFIX=/usr`` is optional, but without it you will almost certainly need to provide ``LD_LIBRARY_PATH=/usr/local/lib`` as an environment variable in order to use the library.

   ``-j`nproc``` means that the compiler will use all CPU threads to compile. If you want to change it and use for example 2 threads, you can provide `-j2` instead.


7. If build succeeded, you can finally install this module from python:

   - ``cd ~/python-avif/avif``
   - ``python setup.py build``
   - ``sudo python setup.py install``


8. And that should be it!

   Now you can import module from python to check if module imports correctly.

   .. code-block:: python

     >>> import avif
     >>>

   Now you can run `examples <README.rst#Examples>`_
