=======================
 git svn clone install
=======================

::

 $ gsci py/SomePackage

This does the equiv of::

 $ git clone -s $SVN/py/SomePackage
 $ cd SomePackage
 $ pip install -i $INDEX -e ./

See: $gsci --help for more info.


