=======
Windows
=======

``tested on Windows 8.1 and Windows 10 1809 (both amd64)``


- **Build Requirements**:

  - `Build Tools for Visual Studio 2019 <https://visualstudio.microsoft.com/downloads>`_
  - `cmake <https://cmake.org/download>`_
  - `ninja <https://github.com/ninja-build/ninja/releases>`_
  - `git <(https://git-scm.com/download/win>`_
  - `nasm <https://www.nasm.us>`_
  - python (3.7+)
  - pip

  **Ensure that every requirement is in path and Windows can find it:**
  ::

    > where cmake
    C:\Program Files\CMake\bin\cmake.exe
    > where ninja
    C:\Windows\System32\ninja.exe
    > where git
    C:\Program Files\Git\cmd\git.exe
    C:\Program Files\Git\mingw64\bin\git.exe
    > where nasm
    C:\Program Files\NASM\nasm.exe
    > where python
    C:\Python39\python.exe
    > where pip
    C:\Python39\Scripts\pip.exe

  Your paths can be different but if you get ``INFO: Could not find files for the given pattern(s).`` that means this executable is not in path.


- **Build Steps:**
  
  **1.** Open the Native Tools Command Prompt for VS 2019

    It will open command line window but from it you will be able to compile code.


  **2.** Install cffi module from pypi:

    - ``pip install --upgrade cffi``

    This will allow to compile bindings


  **3.** Create a folder just to have everything in the same place:

    - ``mkdir C:\python-avif``
    - ``cd C:\python-avif``


  **4.** Now you can clone the repositories:

    - ``git clone https://github.com/Julian/avif.git``
    - ``git clone https://github.com/AOMediaCodec/libavif.git``

    The directory with python module will now appear as ``avif`` and the official avif implementation written in c will be called ``libavif``


  **5.** You will also need to clone and compile the AOM repository.

    It can be done using script included in ``libavif\ext`` directory:

    - ``cd libavif\ext``
    - ``aom.cmd``
    - ``cd ..``


  **6.** After that you can configure libavif with AOM support:

    - Ensure that you are in the main libavif directory (``cd`` should give ``C:\python-avif\libavif``)
    - ``cd cmake``
    - ``cmake .. -DAVIF_CODEC_AOM=ON -DAVIF_LOCAL_AOM=ON``


  **7.** Now open a new Native Tools Command Prompt for VS 2019 window as Administrator.


  **8.** Change current directory to cmake in this window too, then compile and install the project.

    - ``cd C:\python-avif\libavif\cmake``
    - ``msbuild INSTALL.vcxproj /p:Configuration=Release``


  **9.** After the installation is complete, ``C:\Program Files (x86)\libavif`` folder should be created and you will find there all necessary libavif resources. You can close the window that you opened as Administrator and continue in the first window.


  **10.** Then you can change directory to this project and change ``INCLUDE`` variable.

      - ``cd C:\python-avif\avif``
      - ``set INCLUDE=%INCLUDE%;C:\Program Files (x86)\libavif\include``

      You should also copy ``avif.lib`` file to project's directory:

      - ``xcopy "C:\Program Files (x86)\libavif\lib\avif.lib" .``


  **11.** Now you can run the ``setup.py`` script:

      - ``python setup.py build``
      - ``python setup.py install``


  **12.** In order to import the library you should copy ``avif.dll`` (that you can find in ``C:\Program Files (x86)\libavif\bin``) to the installed module directory. You can use ``pip show avif`` to know where the module is installed.

      In my case it says: ``... Location: c:\python39\lib\site-packages\avif-0.0.0-py3.9-win-amd64.egg ...``

      Then you can copy the .dll:

      - ``xcopy "C:\Program Files (x86)\libavif\bin\avif.dll" "c:\python39\lib\site-packages\avif-0.0.0-py3.9-win-amd64.egg"``


  **13.** You should now be able to import the library without any errors!

      .. code-block:: python
      
         >>> import avif
         >>>

      Now you can run `examples <README.rst#Examples>`_
