Last login: Tue Oct 16 10:03:49 on ttys001
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ ssh -l dtripathi sf-dev2.lab.nbttech.com
dtripathi@sf-dev2.lab.nbttech.com's password: 
Permission denied, please try again.
dtripathi@sf-dev2.lab.nbttech.com's password: 
Permission denied, please try again.
dtripathi@sf-dev2.lab.nbttech.com's password: 
Permission denied (publickey,password).
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ ssh -l dtripathi sf-dev2.lab.nbttech.com
dtripathi@sf-dev2.lab.nbttech.com's password: 
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

286 packages can be updated.
0 updates are security updates.

New release '18.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


***********************************
* SteelFusion Development Machine *
***********************************

DO NOT INSTALL SOFTWARE OR MAKE CONFIGURATION CHANGES TO THIS SYSTEM.

Instead, make changes to the Salt recipies.  Recipes can be found here:
    git@gitlab.lab.nbttech.com:eng-lab/salt.git  roles/rockmachine/steelfusion/

Once your changes are committed, wait a minute for them to propagate, and then:
    $ sudo salt-minion

Nothing on this system is backed up.  /work is available for use as scratch
space -- please place your build trees, etc. there.

*** NOTE: For maximum parallel goodness, please use "pmake".  You do not
*** need to specify a -j option.  pmake will ensure system resources are
*** used (and shared) effectively.

Last login: Tue Oct 16 11:55:07 2018 from 10.34.24.125
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ 
dtripathi@sf-dev2:~$ cd /work/dtripathi/
dtripathi@sf-dev2:/work/dtripathi$ 
dtripathi@sf-dev2:/work/dtripathi$ 
dtripathi@sf-dev2:/work/dtripathi$ ls -lrt
total 120
drwxr-xr-x  5 dtripathi users 4096 Feb 18  2016 commitlog
drwxr-xr-x  2 dtripathi users 4096 Mar 16  2016 dpnfs
drwxr-xr-x  4 dtripathi users 4096 Jun 23  2016 steelfsmgmt
drwxr-xr-x 32 dtripathi users 4096 Jul 27  2016 vmab
drwxr-xr-x  4 dtripathi users 4096 Aug 30  2016 steelfsvmab
drwxr-xr-x  3 dtripathi users 4096 Sep 26  2016 fscode
drwxr-xr-x  4 dtripathi users 4096 Jan  5  2017 blockarch
drwxr-xr-x  3 dtripathi users 4096 Jan  9  2017 bs2arch
drwxr-xr-x  3 dtripathi users 4096 Jan 24  2017 gdbpython
drwxr-xr-x  3 dtripathi users 4096 Jan 31  2017 bstrunk
drwxr-xr-x  2 dtripathi users 4096 Feb 15  2017 bs2files
drwxr-xr-x 36 dtripathi users 4096 Feb 16  2017 steelfs
-rw-r--r--  1 dtripathi users  534 Feb 17  2017 COMMIT_MSG
drwxr-xr-x  3 dtripathi users 4096 Mar  7  2017 pvbs
drwxr-xr-x  3 dtripathi users 4096 Mar 11  2017 pocbs
drwxr-xr-x  4 dtripathi users 4096 Jul 18  2017 alpha
drwxr-xr-x  3 dtripathi users 4096 Sep  5  2017 trunk
drwxr-xr-x  3 dtripathi users 4096 Sep 29  2017 newha
drwxr-xr-x  2 dtripathi users 4096 Sep 29  2017 temppy
drwxr-xr-x  3 dtripathi users 4096 Nov  6  2017 example
drwxr-xr-x  3 dtripathi users 4096 Feb 13  2018 oldpoc
drwxr-xr-x  3 dtripathi users 4096 Feb 26  2018 bspoc
drwxr-xr-x  3 dtripathi users 4096 Mar  2  2018 bsint
drwxr-xr-x  3 dtripathi users 4096 Mar  9  2018 bssvm
drwxr-xr-x  3 dtripathi users 4096 Mar 12  2018 intsvm
drwxr-xr-x  3 dtripathi users 4096 Mar 26  2018 testing
drwxr-xr-x  3 dtripathi users 4096 Apr 10  2018 poc
drwxr-xr-x  3 dtripathi users 4096 May 14 08:54 tests
drwxr-xr-x  2 dtripathi users 4096 Oct 16 11:32 statsparser
drwxr-xr-x  3 dtripathi users 4096 Oct 16 12:16 temp
dtripathi@sf-dev2:/work/dtripathi$ vi COMMIT_MSG 
dtripathi@sf-dev2:/work/dtripathi$ 
dtripathi@sf-dev2:/work/dtripathi$ 
dtripathi@sf-dev2:/work/dtripathi$ 
dtripathi@sf-dev2:/work/dtripathi$ rm COMMIT_MSG 
dtripathi@sf-dev2:/work/dtripathi$ cd statsparser/
dtripathi@sf-dev2:/work/dtripathi/statsparser$ ls
plot.py
dtripathi@sf-dev2:/work/dtripathi/statsparser$ vi ./plot.py 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ ./plot.py 
Traceback (most recent call last):
  File "./plot.py", line 5, in <module>
    import sdrstats
ImportError: No module named sdrstats
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ lx 
-bash: lx: command not found
dtripathi@sf-dev2:/work/dtripathi/statsparser$ ls
plot.py
dtripathi@sf-dev2:/work/dtripathi/statsparser$  
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ 
dtripathi@sf-dev2:/work/dtripathi/statsparser$ cd ../
dtripathi@sf-dev2:/work/dtripathi$ find . -name sdrstats.py
dtripathi@sf-dev2:/work/dtripathi$ logout
Connection to sf-dev2.lab.nbttech.com closed.
C02RX1E4G8WL-MAC:~ DTRIPATHI$ ssh -l dtripathi sf-dev3.lab.nbttech.com
dtripathi@sf-dev3.lab.nbttech.com's password: 
Welcome to Ubuntu 16.04.3 LTS (GNU/Linux 4.4.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

***********************************
* SteelFusion Development Machine *
***********************************

DO NOT INSTALL SOFTWARE OR MAKE CONFIGURATION CHANGES TO THIS SYSTEM.

Instead, make changes to the Salt recipies.  Recipes can be found here:
    git@gitlab.lab.nbttech.com:eng-lab/salt.git  roles/rockmachine/steelfusion/

Once your changes are committed, wait a minute for them to propagate, and then:
    $ sudo salt-minion

Nothing on this system is backed up.  /work is available for use as scratch
space -- please place your build trees, etc. there.

*** NOTE: For maximum parallel goodness, please use "pmake".  You do not
*** need to specify a -j option.  pmake will ensure system resources are
*** used (and shared) effectively.

Last login: Tue Oct 16 12:20:32 2018 from 10.34.24.125
dtripathi@sf-dev3:~$ 
dtripathi@sf-dev3:~$ 
dtripathi@sf-dev3:~$ cd /work/dtripathi/
dtripathi@sf-dev3:/work/dtripathi$ ls -lrt
total 32
drwxr-xr-x 3 dtripathi users 4096 Aug 12  2017 hapoc
drwxr-xr-x 3 dtripathi users 4096 Oct 16  2017 edgedr
drwxr-xr-x 3 dtripathi users 4096 Dec 12  2017 temp
drwxr-xr-x 3 dtripathi users 4096 Jan  8  2018 reppoc
drwxr-xr-x 3 dtripathi users 4096 Apr  2  2018 bspoctest
drwxr-xr-x 4 dtripathi users 4096 Jun 18 07:22 myha
drwxr-xr-x 6 dtripathi users 4096 Aug 12 14:27 myalgo
drwxr-xr-x 2 dtripathi users 4096 Aug 14 16:38 talpha
dtripathi@sf-dev3:/work/dtripathi$ find . -name sdrstats.py
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ 
dtripathi@sf-dev3:/work/dtripathi$ cd hapoc/
dtripathi@sf-dev3:/work/dtripathi/hapoc$ ls -lrt
total 4
drwxr-xr-x 40 dtripathi users 4096 Oct 16  2017 va
dtripathi@sf-dev3:/work/dtripathi/hapoc$ cd ../
dtripathi@sf-dev3:/work/dtripathi$ ls -lrt
total 32
drwxr-xr-x 3 dtripathi users 4096 Aug 12  2017 hapoc
drwxr-xr-x 3 dtripathi users 4096 Oct 16  2017 edgedr
drwxr-xr-x 3 dtripathi users 4096 Dec 12  2017 temp
drwxr-xr-x 3 dtripathi users 4096 Jan  8  2018 reppoc
drwxr-xr-x 3 dtripathi users 4096 Apr  2  2018 bspoctest
drwxr-xr-x 4 dtripathi users 4096 Jun 18 07:22 myha
drwxr-xr-x 6 dtripathi users 4096 Aug 12 14:27 myalgo
drwxr-xr-x 2 dtripathi users 4096 Aug 14 16:38 talpha
dtripathi@sf-dev3:/work/dtripathi$ cd talpha/
dtripathi@sf-dev3:/work/dtripathi/talpha$ ls -lrt
total 0
dtripathi@sf-dev3:/work/dtripathi/talpha$  
dtripathi@sf-dev3:/work/dtripathi/talpha$ cd ../
dtripathi@sf-dev3:/work/dtripathi$ logout
Connection to sf-dev3.lab.nbttech.com closed.
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ pwd
/Users/DTRIPATHI
C02RX1E4G8WL-MAC:~ DTRIPATHI$ ls
AndroidStudioProjects	Movies			myproj
Applications		Music			mystats
Calibre Library		Pictures		octave-workspace
Desktop			Public			self
Documents		VirtualBox VMs		work
Downloads		eclipse
Library			myalgo
C02RX1E4G8WL-MAC:~ DTRIPATHI$ find . -name plot.py
./mystats/plot.py

./work/sfusion/alpha/va/scripts/trace-graphs/plot.py
./work/sfusion/bs15/va/scripts/trace-graphs/plot.py
./work/sfusion/demo1/va/scripts/trace-graphs/plot.py
./work/sfusion/ha/va/scripts/trace-graphs/plot.py
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ find . -name plot.py
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ 
C02RX1E4G8WL-MAC:~ DTRIPATHI$ cd mystats/
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ls -lrt
total 2000
-rw-r--r--  1 DTRIPATHI  staff  796328 Aug 28  2016 sdr.stats
-rw-r--r--  1 DTRIPATHI  staff     544 Aug 28  2016 csvview.py
-rw-r--r--  1 DTRIPATHI  staff     188 Aug 28  2016 walktest.py
-rw-r--r--  1 DTRIPATHI  staff    2672 Aug 28  2016 topstats.py
-rw-r--r--  1 DTRIPATHI  staff     295 Aug 28  2016 test.py
-rw-r--r--  1 DTRIPATHI  staff    2137 Aug 28  2016 sdrstats.py
-rwxr-xr-x  1 DTRIPATHI  staff    4952 Aug 28  2016 plot.py
-rw-r--r--  1 DTRIPATHI  staff    1852 Aug 28  2016 messages.py
-rw-r--r--  1 DTRIPATHI  staff    1004 Aug 28  2016 gnuplot.py
-rw-r--r--  1 DTRIPATHI  staff    2207 Aug 28  2016 exhibit.py
-rw-r--r--  1 DTRIPATHI  staff     276 Aug 28  2016 dygraph.py
-rw-r--r--  1 DTRIPATHI  staff   67192 Aug 28  2016 edge.stats
-rw-r--r--  1 DTRIPATHI  staff    2967 Sep 16  2016 topstats.pyc
-rw-r--r--  1 DTRIPATHI  staff    3707 Sep 16  2016 sdrstats.pyc
-rw-r--r--  1 DTRIPATHI  staff    2229 Sep 16  2016 messages.pyc
-rw-r--r--  1 DTRIPATHI  staff    1359 Sep 16  2016 gnuplot.pyc
-rw-r--r--  1 DTRIPATHI  staff    1978 Sep 16  2016 exhibit.pyc
-rw-r--r--  1 DTRIPATHI  staff     602 Sep 16  2016 dygraph.pyc
-rw-r--r--  1 DTRIPATHI  staff   40179 Sep 16  2016 x
-rw-r--r--  1 DTRIPATHI  staff    3949 Sep 16  2016 stats.py
-rw-r--r--  1 DTRIPATHI  staff    6061 Sep 16  2016 stats.pyc
-rw-r--r--  1 DTRIPATHI  staff   22347 Sep 17  2016 ed.stats
-rwxr-xr-x  1 DTRIPATHI  staff    2518 Sep 19  2016 sfstats.py
-rwxr-xr-x  1 DTRIPATHI  staff     660 Sep 22  2016 pp.py
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ./plot.py 
usage: ./plot.py [files to parse] [directories to search]
parses stats files and serves and interative website to display them
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ./plot.py ./sdr.stats 
Parsing sdr stats ./sdr.stats
Running rules on ./sdr.stats
Traceback (most recent call last):
  File "./plot.py", line 136, in <module>
    r = parse(arg, arg, rules)
  File "./plot.py", line 115, in parse
    parse_sdr_stats(name, file, rules)
  File "./plot.py", line 88, in parse_sdr_stats
    subprocess.Popen(args).wait()
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 710, in __init__
    errread, errwrite)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 1335, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ./plot.py 
usage: ./plot.py [files to parse] [directories to search]
parses stats files and serves and interative website to display them
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ./sdrst
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ pwd
/Users/DTRIPATHI/mystats
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ls -lrt
total 2000
-rw-r--r--  1 DTRIPATHI  staff  796328 Aug 28  2016 sdr.stats
-rw-r--r--  1 DTRIPATHI  staff     544 Aug 28  2016 csvview.py
-rw-r--r--  1 DTRIPATHI  staff     188 Aug 28  2016 walktest.py
-rw-r--r--  1 DTRIPATHI  staff    2672 Aug 28  2016 topstats.py
-rw-r--r--  1 DTRIPATHI  staff     295 Aug 28  2016 test.py
-rw-r--r--  1 DTRIPATHI  staff    2137 Aug 28  2016 sdrstats.py
-rwxr-xr-x  1 DTRIPATHI  staff    4952 Aug 28  2016 plot.py
-rw-r--r--  1 DTRIPATHI  staff    1852 Aug 28  2016 messages.py
-rw-r--r--  1 DTRIPATHI  staff    1004 Aug 28  2016 gnuplot.py
-rw-r--r--  1 DTRIPATHI  staff    2207 Aug 28  2016 exhibit.py
-rw-r--r--  1 DTRIPATHI  staff     276 Aug 28  2016 dygraph.py
-rw-r--r--  1 DTRIPATHI  staff   67192 Aug 28  2016 edge.stats
-rw-r--r--  1 DTRIPATHI  staff    2967 Sep 16  2016 topstats.pyc
-rw-r--r--  1 DTRIPATHI  staff    3707 Sep 16  2016 sdrstats.pyc
-rw-r--r--  1 DTRIPATHI  staff    2229 Sep 16  2016 messages.pyc
-rw-r--r--  1 DTRIPATHI  staff    1359 Sep 16  2016 gnuplot.pyc
-rw-r--r--  1 DTRIPATHI  staff    1978 Sep 16  2016 exhibit.pyc
-rw-r--r--  1 DTRIPATHI  staff     602 Sep 16  2016 dygraph.pyc
-rw-r--r--  1 DTRIPATHI  staff   40179 Sep 16  2016 x
-rw-r--r--  1 DTRIPATHI  staff    3949 Sep 16  2016 stats.py
-rw-r--r--  1 DTRIPATHI  staff    6061 Sep 16  2016 stats.pyc
-rw-r--r--  1 DTRIPATHI  staff   22347 Sep 17  2016 ed.stats
-rwxr-xr-x  1 DTRIPATHI  staff    2518 Sep 19  2016 sfstats.py
-rwxr-xr-x  1 DTRIPATHI  staff     660 Sep 22  2016 pp.py
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi sfstats.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ./sfstats.py 
Traceback (most recent call last):
  File "./sfstats.py", line 98, in <module>
    with open(sys.argv[1]) as f:
IndexError: list index out of range
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ./sfstats.py ./edge.stats 
GraniteEdge stats at ---- ----Tue 2016-07-26 00:20:45 GMT
2016-07-26 00:20:45
      Dumping RdiskEdge Stats
      Dumping BlockStore Stats
/blockstore/10/dc_last_write_time 1469479904
/blockstore/10/dc_last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
10/dc_last_write_time
1469479904
HERE 
NAME:10
dc_last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/10/last_write_time 1469479904
/blockstore/10/last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
10/last_write_time
1469479904
HERE 
NAME:10
last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/10/nr_blk_commits 91706813
/blockstore/10/nr_blk_commits
91706813
In BEFORE
HERE 
NAME:blockstore
10/nr_blk_commits
91706813
HERE 
NAME:10
nr_blk_commits
91706813
HERE 
Out BEFORE
/blockstore/10/nr_blk_writes 91706813
/blockstore/10/nr_blk_writes
91706813
In BEFORE
HERE 
NAME:blockstore
10/nr_blk_writes
91706813
HERE 
NAME:10
nr_blk_writes
91706813
HERE 
Out BEFORE
/blockstore/11/dc_last_write_time 1469479904
/blockstore/11/dc_last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
11/dc_last_write_time
1469479904
HERE 
NAME:11
dc_last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/11/last_write_time 1469479904
/blockstore/11/last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
11/last_write_time
1469479904
HERE 
NAME:11
last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/11/nr_blk_commits 99990631
/blockstore/11/nr_blk_commits
99990631
In BEFORE
HERE 
NAME:blockstore
11/nr_blk_commits
99990631
HERE 
NAME:11
nr_blk_commits
99990631
HERE 
Out BEFORE
/blockstore/11/nr_blk_writes 99990631
/blockstore/11/nr_blk_writes
99990631
In BEFORE
HERE 
NAME:blockstore
11/nr_blk_writes
99990631
HERE 
NAME:11
nr_blk_writes
99990631
HERE 
Out BEFORE
/blockstore/12/dc_last_write_time 1469479905
/blockstore/12/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
12/dc_last_write_time
1469479905
HERE 
NAME:12
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/12/last_write_time 1469479905
/blockstore/12/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
12/last_write_time
1469479905
HERE 
NAME:12
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/12/nr_blk_commits 2894843
/blockstore/12/nr_blk_commits
2894843
In BEFORE
HERE 
NAME:blockstore
12/nr_blk_commits
2894843
HERE 
NAME:12
nr_blk_commits
2894843
HERE 
Out BEFORE
/blockstore/12/nr_blk_writes 2894843
/blockstore/12/nr_blk_writes
2894843
In BEFORE
HERE 
NAME:blockstore
12/nr_blk_writes
2894843
HERE 
NAME:12
nr_blk_writes
2894843
HERE 
Out BEFORE
/blockstore/13/dc_last_write_time 1469479905
/blockstore/13/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
13/dc_last_write_time
1469479905
HERE 
NAME:13
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/13/last_write_time 1469479905
/blockstore/13/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
13/last_write_time
1469479905
HERE 
NAME:13
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/13/nr_blk_commits 4727607438
/blockstore/13/nr_blk_commits
4727607438
In BEFORE
HERE 
NAME:blockstore
13/nr_blk_commits
4727607438
HERE 
NAME:13
nr_blk_commits
4727607438
HERE 
Out BEFORE
/blockstore/13/nr_blk_writes 4727607438
/blockstore/13/nr_blk_writes
4727607438
In BEFORE
HERE 
NAME:blockstore
13/nr_blk_writes
4727607438
HERE 
NAME:13
nr_blk_writes
4727607438
HERE 
Out BEFORE
/blockstore/14/dc_last_write_time 1469479905
/blockstore/14/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
14/dc_last_write_time
1469479905
HERE 
NAME:14
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/14/last_write_time 1469479905
/blockstore/14/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
14/last_write_time
1469479905
HERE 
NAME:14
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/14/nr_blk_commits 1835272490
/blockstore/14/nr_blk_commits
1835272490
In BEFORE
HERE 
NAME:blockstore
14/nr_blk_commits
1835272490
HERE 
NAME:14
nr_blk_commits
1835272490
HERE 
Out BEFORE
/blockstore/14/nr_blk_writes 1835272490
/blockstore/14/nr_blk_writes
1835272490
In BEFORE
HERE 
NAME:blockstore
14/nr_blk_writes
1835272490
HERE 
NAME:14
nr_blk_writes
1835272490
HERE 
Out BEFORE
/blockstore/16/dc_last_write_time 1469479905
/blockstore/16/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
16/dc_last_write_time
1469479905
HERE 
NAME:16
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/16/last_write_time 1469479905
/blockstore/16/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
16/last_write_time
1469479905
HERE 
NAME:16
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/16/nr_blk_commits 12455455463
/blockstore/16/nr_blk_commits
12455455463
In BEFORE
HERE 
NAME:blockstore
16/nr_blk_commits
12455455463
HERE 
NAME:16
nr_blk_commits
12455455463
HERE 
Out BEFORE
/blockstore/16/nr_blk_writes 12455455463
/blockstore/16/nr_blk_writes
12455455463
In BEFORE
HERE 
NAME:blockstore
16/nr_blk_writes
12455455463
HERE 
NAME:16
nr_blk_writes
12455455463
HERE 
Out BEFORE
/blockstore/8/dc_last_write_time 1469479902
/blockstore/8/dc_last_write_time
1469479902
In BEFORE
HERE 
NAME:blockstore
8/dc_last_write_time
1469479902
HERE 
NAME:8
dc_last_write_time
1469479902
HERE 
Out BEFORE
/blockstore/8/last_write_time 1469479902
/blockstore/8/last_write_time
1469479902
In BEFORE
HERE 
NAME:blockstore
8/last_write_time
1469479902
HERE 
NAME:8
last_write_time
1469479902
HERE 
Out BEFORE
/blockstore/8/nr_blk_commits 61845671
/blockstore/8/nr_blk_commits
61845671
In BEFORE
HERE 
NAME:blockstore
8/nr_blk_commits
61845671
HERE 
NAME:8
nr_blk_commits
61845671
HERE 
Out BEFORE
/blockstore/8/nr_blk_writes 61845671
/blockstore/8/nr_blk_writes
61845671
In BEFORE
HERE 
NAME:blockstore
8/nr_blk_writes
61845671
HERE 
NAME:8
nr_blk_writes
61845671
HERE 
Out BEFORE
/blockstore/9/dc_last_write_time 1469479905
/blockstore/9/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
9/dc_last_write_time
1469479905
HERE 
NAME:9
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/9/last_write_time 1469479905
/blockstore/9/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
9/last_write_time
1469479905
HERE 
NAME:9
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/9/nr_blk_commits 80280964
/blockstore/9/nr_blk_commits
80280964
In BEFORE
HERE 
NAME:blockstore
9/nr_blk_commits
80280964
HERE 
NAME:9
nr_blk_commits
80280964
HERE 
Out BEFORE
/blockstore/9/nr_blk_writes 80280964
/blockstore/9/nr_blk_writes
80280964
In BEFORE
HERE 
NAME:blockstore
9/nr_blk_writes
80280964
HERE 
NAME:9
nr_blk_writes
80280964
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/slab_count 976
/blockstore/bufferpool/41407808/slab_count
976
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/slab_count
976
HERE 
NAME:bufferpool
41407808/slab_count
976
HERE 
NAME:41407808
slab_count
976
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/slab_size 8704
/blockstore/bufferpool/41407808/slab_size
8704
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/slab_size
8704
HERE 
NAME:bufferpool
41407808/slab_size
8704
HERE 
NAME:41407808
slab_size
8704
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/unable_to_allocate 0
/blockstore/bufferpool/41407808/unable_to_allocate
0
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/unable_to_allocate
0
HERE 
NAME:bufferpool
41407808/unable_to_allocate
0
HERE 
NAME:41407808
unable_to_allocate
0
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/unused 8495104
/blockstore/bufferpool/41407808/unused
8495104
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/unused
8495104
HERE 
NAME:bufferpool
41407808/unused
8495104
HERE 
NAME:41407808
unused
8495104
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms time taken for commit
/blockstore/commit_processor/commit_time_ms time taken for
commit
  max: 0 milliseconds

/blockstore/commit_processor/commit_time_ms/aggregate 0
/blockstore/commit_processor/commit_time_ms/aggregate
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/aggregate
0
HERE 
NAME:commit_processor
commit_time_ms/aggregate
0
HERE 
NAME:commit_time_ms
aggregate
0
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms/average NaN
/blockstore/commit_processor/commit_time_ms/average
NaN
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/average
nan
HERE 
NAME:commit_processor
commit_time_ms/average
nan
HERE 
NAME:commit_time_ms
average
nan
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms/nupdates 0
/blockstore/commit_processor/commit_time_ms/nupdates
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/nupdates
0
HERE 
NAME:commit_processor
commit_time_ms/nupdates
0
HERE 
NAME:commit_time_ms
nupdates
0
HERE 
Out BEFORE
/blockstore/commit_processor/dirty_data_present 1
/blockstore/commit_processor/dirty_data_present
1
In BEFORE
HERE 
NAME:blockstore
commit_processor/dirty_data_present
1
HERE 
NAME:commit_processor
dirty_data_present
1
HERE 
Out BEFORE
/blockstore/commit_processor/next_commit [LSN::INVALID]
/blockstore/commit_processor/next_commit
[LSN::INVALID]
/blockstore/commit_processor/nr_blk_commits 19356165132
/blockstore/commit_processor/nr_blk_commits
19356165132
In BEFORE
HERE 
NAME:blockstore
commit_processor/nr_blk_commits
19356165132
HERE 
NAME:commit_processor
nr_blk_commits
19356165132
HERE 
Out BEFORE
/blockstore/commit_processor/nr_blk_commits_in_mem 0
/blockstore/commit_processor/nr_blk_commits_in_mem
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/nr_blk_commits_in_mem
0
HERE 
NAME:commit_processor
nr_blk_commits_in_mem
0
HERE 
Out BEFORE
/blockstore/commit_processor/page_reads_cache 0
/blockstore/commit_processor/page_reads_cache
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/page_reads_cache
0
HERE 
NAME:commit_processor
page_reads_cache
0
HERE 
Out BEFORE
/blockstore/commit_processor/page_reads_disk 0
/blockstore/commit_processor/page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/page_reads_disk
0
HERE 
NAME:commit_processor
page_reads_disk
0
HERE 
Out BEFORE
/blockstore/commit_processor/pause_count 0
/blockstore/commit_processor/pause_count
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/pause_count
0
HERE 
NAME:commit_processor
pause_count
0
HERE 
Out BEFORE
/blockstore/commit_processor/paused_msecs 0
/blockstore/commit_processor/paused_msecs
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/paused_msecs
0
HERE 
NAME:commit_processor
paused_msecs
0
HERE 
Out BEFORE
/blockstore/commit_processor/pending_commits 0
/blockstore/commit_processor/pending_commits
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/pending_commits
0
HERE 
NAME:commit_processor
pending_commits
0
HERE 
Out BEFORE
/blockstore/commit_processor/running_msecs 0
/blockstore/commit_processor/running_msecs
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/running_msecs
0
HERE 
NAME:commit_processor
running_msecs
0
HERE 
Out BEFORE
/blockstore/commit_processor/state INIT
/blockstore/commit_processor/state
INIT
/blockstore/disk_helper/ha_peer_write_time ha peer op write time
/blockstore/disk_helper/ha_peer_write_time ha peer op write
time
  max: 0 ms

/blockstore/disk_helper/ha_peer_write_time/aggregate 0
/blockstore/disk_helper/ha_peer_write_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/aggregate
0
HERE 
NAME:disk_helper
ha_peer_write_time/aggregate
0
HERE 
NAME:ha_peer_write_time
aggregate
0
HERE 
Out BEFORE
/blockstore/disk_helper/ha_peer_write_time/average NaN
/blockstore/disk_helper/ha_peer_write_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/average
nan
HERE 
NAME:disk_helper
ha_peer_write_time/average
nan
HERE 
NAME:ha_peer_write_time
average
nan
HERE 
Out BEFORE
/blockstore/disk_helper/ha_peer_write_time/nupdates 0
/blockstore/disk_helper/ha_peer_write_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/nupdates
0
HERE 
NAME:disk_helper
ha_peer_write_time/nupdates
0
HERE 
NAME:ha_peer_write_time
nupdates
0
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time local op write time
/blockstore/disk_helper/local_write_time local op write
time
  max: 0 ms

/blockstore/disk_helper/local_write_time/aggregate 0
/blockstore/disk_helper/local_write_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/aggregate
0
HERE 
NAME:disk_helper
local_write_time/aggregate
0
HERE 
NAME:local_write_time
aggregate
0
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time/average NaN
/blockstore/disk_helper/local_write_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/average
nan
HERE 
NAME:disk_helper
local_write_time/average
nan
HERE 
NAME:local_write_time
average
nan
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time/nupdates 0
/blockstore/disk_helper/local_write_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/nupdates
0
HERE 
NAME:disk_helper
local_write_time/nupdates
0
HERE 
NAME:local_write_time
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/dirty_skips 0
/blockstore/fifo/dirty_skips
0
In BEFORE
HERE 
NAME:blockstore
fifo/dirty_skips
0
HERE 
NAME:fifo
dirty_skips
0
HERE 
Out BEFORE
/blockstore/fifo/error_status 0
/blockstore/fifo/error_status
0
In BEFORE
HERE 
NAME:blockstore
fifo/error_status
0
HERE 
NAME:fifo
error_status
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_mode_allocations 0
/blockstore/fifo/fifo_mode_allocations
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_mode_allocations
0
HERE 
NAME:fifo
fifo_mode_allocations
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips /blockstore/fifo/fifo_page_skips
/blockstore/fifo/fifo_page_skips
/blockstore/fifo/fifo_page_skips
  max: 0 pages

/blockstore/fifo/fifo_page_skips/aggregate 0
/blockstore/fifo/fifo_page_skips/aggregate
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/aggregate
0
HERE 
NAME:fifo
fifo_page_skips/aggregate
0
HERE 
NAME:fifo_page_skips
aggregate
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips/average NaN
/blockstore/fifo/fifo_page_skips/average
NaN
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/average
nan
HERE 
NAME:fifo
fifo_page_skips/average
nan
HERE 
NAME:fifo_page_skips
average
nan
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips/nupdates 0
/blockstore/fifo/fifo_page_skips/nupdates
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/nupdates
0
HERE 
NAME:fifo
fifo_page_skips/nupdates
0
HERE 
NAME:fifo_page_skips
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/last_commit [LSN::INVALID]
/blockstore/fifo/last_commit
[LSN::INVALID]
/blockstore/fifo/last_commit_on_disk [LSN::INVALID]
/blockstore/fifo/last_commit_on_disk
[LSN::INVALID]
/blockstore/fifo/last_sync [LSN::INVALID]
/blockstore/fifo/last_sync
[LSN::INVALID]
/blockstore/fifo/last_write [LSN::INVALID]
/blockstore/fifo/last_write
[LSN::INVALID]
/blockstore/fifo/last_write_on_disk [LSN::INVALID]
/blockstore/fifo/last_write_on_disk
[LSN::INVALID]
/blockstore/fifo/next_write [LSN::INVALID]
/blockstore/fifo/next_write
[LSN::INVALID]
/blockstore/fifo/nr_evictions 0
/blockstore/fifo/nr_evictions
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_evictions
0
HERE 
NAME:fifo
nr_evictions
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages 410203586
/blockstore/fifo/nr_pages
410203586
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages
410203586
HERE 
NAME:fifo
nr_pages
410203586
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_evictable 0
/blockstore/fifo/nr_pages_evictable
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_evictable
0
HERE 
NAME:fifo
nr_pages_evictable
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_evictable_unused 0
/blockstore/fifo/nr_pages_evictable_unused
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_evictable_unused
0
HERE 
NAME:fifo
nr_pages_evictable_unused
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_inuse 0
/blockstore/fifo/nr_pages_inuse
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_inuse
0
HERE 
NAME:fifo
nr_pages_inuse
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_pinnable 0
/blockstore/fifo/nr_pages_pinnable
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_pinnable
0
HERE 
NAME:fifo
nr_pages_pinnable
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_pinned 0
/blockstore/fifo/nr_pages_pinned
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_pinned
0
HERE 
NAME:fifo
nr_pages_pinned
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_unused 410203586
/blockstore/fifo/nr_pages_unused
410203586
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_unused
410203586
HERE 
NAME:fifo
nr_pages_unused
410203586
HERE 
Out BEFORE
/blockstore/fifo/nr_pinned_pages_used 0
/blockstore/fifo/nr_pinned_pages_used
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pinned_pages_used
0
HERE 
NAME:fifo
nr_pinned_pages_used
0
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used # blocks used in page
/blockstore/fifo/page_blocks_used # blocks used in
page
  max: 0 blocks

/blockstore/fifo/page_blocks_used/aggregate 0
/blockstore/fifo/page_blocks_used/aggregate
0
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/aggregate
0
HERE 
NAME:fifo
page_blocks_used/aggregate
0
HERE 
NAME:page_blocks_used
aggregate
0
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used/average NaN
/blockstore/fifo/page_blocks_used/average
NaN
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/average
nan
HERE 
NAME:fifo
page_blocks_used/average
nan
HERE 
NAME:page_blocks_used
average
nan
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used/nupdates 0
/blockstore/fifo/page_blocks_used/nupdates
0
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/nupdates
0
HERE 
NAME:fifo
page_blocks_used/nupdates
0
HERE 
NAME:page_blocks_used
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/stable_write_limit [LSN::INVALID]
/blockstore/fifo/stable_write_limit
[LSN::INVALID]
/blockstore/last_rebuild/cancelled_pages 0
/blockstore/last_rebuild/cancelled_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/cancelled_pages
0
HERE 
NAME:last_rebuild
cancelled_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/completed_pages 0
/blockstore/last_rebuild/completed_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/completed_pages
0
HERE 
NAME:last_rebuild
completed_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/fifo_completed_pages 0
/blockstore/last_rebuild/fifo_completed_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/fifo_completed_pages
0
HERE 
NAME:last_rebuild
fifo_completed_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/is_full_rebuild 0
/blockstore/last_rebuild/is_full_rebuild
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/is_full_rebuild
0
HERE 
NAME:last_rebuild
is_full_rebuild
0
HERE 
Out BEFORE
/blockstore/last_rebuild/r2l_time 0us
/blockstore/last_rebuild/r2l_time
0us
/blockstore/last_rebuild/start_time 
/blockstore/last_rebuild/start_time

/blockstore/last_rebuild/total_pages 4294967295
/blockstore/last_rebuild/total_pages
4294967295
In BEFORE
HERE 
NAME:blockstore
last_rebuild/total_pages
4294967295
HERE 
NAME:last_rebuild
total_pages
4294967295
HERE 
Out BEFORE
/blockstore/last_rebuild/total_time 0us
/blockstore/last_rebuild/total_time
0us
/blockstore/page_cache/nr_page_lookups 0
/blockstore/page_cache/nr_page_lookups
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups
0
HERE 
NAME:page_cache
nr_page_lookups
0
HERE 
Out BEFORE
/blockstore/page_cache/nr_page_lookups_absent 0
/blockstore/page_cache/nr_page_lookups_absent
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups_absent
0
HERE 
NAME:page_cache
nr_page_lookups_absent
0
HERE 
Out BEFORE
/blockstore/page_cache/nr_page_lookups_on_disk 0
/blockstore/page_cache/nr_page_lookups_on_disk
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups_on_disk
0
HERE 
NAME:page_cache
nr_page_lookups_on_disk
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal page alloc time - normal
/blockstore/page_cache/page_alloc_time_normal page alloc time -
normal
  max: 0 ms

/blockstore/page_cache/page_alloc_time_normal/aggregate 0
/blockstore/page_cache/page_alloc_time_normal/aggregate
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/aggregate
0
HERE 
NAME:page_cache
page_alloc_time_normal/aggregate
0
HERE 
NAME:page_alloc_time_normal
aggregate
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal/average NaN
/blockstore/page_cache/page_alloc_time_normal/average
NaN
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/average
nan
HERE 
NAME:page_cache
page_alloc_time_normal/average
nan
HERE 
NAME:page_alloc_time_normal
average
nan
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal/nupdates 0
/blockstore/page_cache/page_alloc_time_normal/nupdates
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/nupdates
0
HERE 
NAME:page_cache
page_alloc_time_normal/nupdates
0
HERE 
NAME:page_alloc_time_normal
nupdates
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued page alloc time - queued requests
/blockstore/page_cache/page_alloc_time_queued page alloc time - queued
requests
  max: 0 ms

/blockstore/page_cache/page_alloc_time_queued/aggregate 0
/blockstore/page_cache/page_alloc_time_queued/aggregate
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/aggregate
0
HERE 
NAME:page_cache
page_alloc_time_queued/aggregate
0
HERE 
NAME:page_alloc_time_queued
aggregate
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued/average NaN
/blockstore/page_cache/page_alloc_time_queued/average
NaN
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/average
nan
HERE 
NAME:page_cache
page_alloc_time_queued/average
nan
HERE 
NAME:page_alloc_time_queued
average
nan
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued/nupdates 0
/blockstore/page_cache/page_alloc_time_queued/nupdates
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/nupdates
0
HERE 
NAME:page_cache
page_alloc_time_queued/nupdates
0
HERE 
NAME:page_alloc_time_queued
nupdates
0
HERE 
Out BEFORE
/blockstore/page_cache/pages 617000
/blockstore/page_cache/pages
617000
In BEFORE
HERE 
NAME:blockstore
page_cache/pages
617000
HERE 
NAME:page_cache
pages
617000
HERE 
Out BEFORE
/blockstore/page_cache/pages_on_freelist 477
/blockstore/page_cache/pages_on_freelist
477
In BEFORE
HERE 
NAME:blockstore
page_cache/pages_on_freelist
477
HERE 
NAME:page_cache
pages_on_freelist
477
HERE 
Out BEFORE
/blockstore/page_cache/store_pages_in_mem 0
/blockstore/page_cache/store_pages_in_mem
0
In BEFORE
HERE 
NAME:blockstore
page_cache/store_pages_in_mem
0
HERE 
NAME:page_cache
store_pages_in_mem
0
HERE 
Out BEFORE
/blockstore/page_cache/stores_dropped 0
/blockstore/page_cache/stores_dropped
0
In BEFORE
HERE 
NAME:blockstore
page_cache/stores_dropped
0
HERE 
NAME:page_cache
stores_dropped
0
HERE 
Out BEFORE
/blockstore/phash/ha_unsynced_pages 0
/blockstore/phash/ha_unsynced_pages
0
In BEFORE
HERE 
NAME:blockstore
phash/ha_unsynced_pages
0
HERE 
NAME:phash
ha_unsynced_pages
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr 0
/blockstore/read/nr_blk_reads_usr
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr
0
HERE 
NAME:read
nr_blk_reads_usr
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr_other_hits 0
/blockstore/read/nr_blk_reads_usr_other_hits
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr_other_hits
0
HERE 
NAME:read
nr_blk_reads_usr_other_hits
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr_store_hits 0
/blockstore/read/nr_blk_reads_usr_store_hits
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr_store_hits
0
HERE 
NAME:read
nr_blk_reads_usr_store_hits
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user 0
/blockstore/read/nr_page_lookups_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user
0
HERE 
NAME:read
nr_page_lookups_user
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user_absent 0
/blockstore/read/nr_page_lookups_user_absent
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user_absent
0
HERE 
NAME:read
nr_page_lookups_user_absent
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user_on_disk 0
/blockstore/read/nr_page_lookups_user_on_disk
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user_on_disk
0
HERE 
NAME:read
nr_page_lookups_user_on_disk
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_disk 0
/blockstore/read/nr_page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_disk
0
HERE 
NAME:read
nr_page_reads_disk
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_disk_user 0
/blockstore/read/nr_page_reads_disk_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_disk_user
0
HERE 
NAME:read
nr_page_reads_disk_user
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_rdc_user 0
/blockstore/read/nr_page_reads_rdc_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_rdc_user
0
HERE 
NAME:read
nr_page_reads_rdc_user
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk no.of total disk reads (RDC + WBC) per user readOp
/blockstore/read/op_page_reads_disk no.of total disk reads (RDC + WBC) per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_disk/aggregate 0
/blockstore/read/op_page_reads_disk/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/aggregate
0
HERE 
NAME:read
op_page_reads_disk/aggregate
0
HERE 
NAME:op_page_reads_disk
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk/average NaN
/blockstore/read/op_page_reads_disk/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/average
nan
HERE 
NAME:read
op_page_reads_disk/average
nan
HERE 
NAME:op_page_reads_disk
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk/nupdates 0
/blockstore/read/op_page_reads_disk/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/nupdates
0
HERE 
NAME:read
op_page_reads_disk/nupdates
0
HERE 
NAME:op_page_reads_disk
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits no.of Read Cache hits per user readOp
/blockstore/read/op_page_reads_rdc_hits no.of Read Cache hits per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_rdc_hits/aggregate 0
/blockstore/read/op_page_reads_rdc_hits/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/aggregate
0
HERE 
NAME:read
op_page_reads_rdc_hits/aggregate
0
HERE 
NAME:op_page_reads_rdc_hits
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits/average NaN
/blockstore/read/op_page_reads_rdc_hits/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/average
nan
HERE 
NAME:read
op_page_reads_rdc_hits/average
nan
HERE 
NAME:op_page_reads_rdc_hits
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits/nupdates 0
/blockstore/read/op_page_reads_rdc_hits/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/nupdates
0
HERE 
NAME:read
op_page_reads_rdc_hits/nupdates
0
HERE 
NAME:op_page_reads_rdc_hits
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses no.of Read Cache misses per user readOp
/blockstore/read/op_page_reads_rdc_misses no.of Read Cache misses per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_rdc_misses/aggregate 0
/blockstore/read/op_page_reads_rdc_misses/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/aggregate
0
HERE 
NAME:read
op_page_reads_rdc_misses/aggregate
0
HERE 
NAME:op_page_reads_rdc_misses
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses/average NaN
/blockstore/read/op_page_reads_rdc_misses/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/average
nan
HERE 
NAME:read
op_page_reads_rdc_misses/average
nan
HERE 
NAME:op_page_reads_rdc_misses
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses/nupdates 0
/blockstore/read/op_page_reads_rdc_misses/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/nupdates
0
HERE 
NAME:read
op_page_reads_rdc_misses/nupdates
0
HERE 
NAME:op_page_reads_rdc_misses
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_total_time reads: total time taken
/blockstore/read/op_total_time reads: total time
taken
  max: 0 ms

/blockstore/read/op_total_time/aggregate 0
/blockstore/read/op_total_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/aggregate
0
HERE 
NAME:read
op_total_time/aggregate
0
HERE 
NAME:op_total_time
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_total_time/average NaN
/blockstore/read/op_total_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/average
nan
HERE 
NAME:read
op_total_time/average
nan
HERE 
NAME:op_total_time
average
nan
HERE 
Out BEFORE
/blockstore/read/op_total_time/nupdates 0
/blockstore/read/op_total_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/nupdates
0
HERE 
NAME:read
op_total_time/nupdates
0
HERE 
NAME:op_total_time
nupdates
0
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size Size of user read request not completely satisfied by Read Cache
/blockstore/read/rdc_misses_op_size Size of user read request not completely satisfied by Read
Cache
  max: 0 blocks

/blockstore/read/rdc_misses_op_size/aggregate 0
/blockstore/read/rdc_misses_op_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/aggregate
0
HERE 
NAME:read
rdc_misses_op_size/aggregate
0
HERE 
NAME:rdc_misses_op_size
aggregate
0
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size/average NaN
/blockstore/read/rdc_misses_op_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/average
nan
HERE 
NAME:read
rdc_misses_op_size/average
nan
HERE 
NAME:rdc_misses_op_size
average
nan
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size/nupdates 0
/blockstore/read/rdc_misses_op_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/nupdates
0
HERE 
NAME:read
rdc_misses_op_size/nupdates
0
HERE 
NAME:rdc_misses_op_size
nupdates
0
HERE 
Out BEFORE
/blockstore/read/reads_queued 0
/blockstore/read/reads_queued
0
In BEFORE
HERE 
NAME:blockstore
read/reads_queued
0
HERE 
NAME:read
reads_queued
0
HERE 
Out BEFORE
/blockstore/read_cache/last_flush_lsn [LSN::INVALID]
/blockstore/read_cache/last_flush_lsn
[LSN::INVALID]
/blockstore/read_cache/nr_readcache_hits 0
/blockstore/read_cache/nr_readcache_hits
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_hits
0
HERE 
NAME:read_cache
nr_readcache_hits
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_hits_user 0
/blockstore/read_cache/nr_readcache_hits_user
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_hits_user
0
HERE 
NAME:read_cache
nr_readcache_hits_user
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_misses 0
/blockstore/read_cache/nr_readcache_misses
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_misses
0
HERE 
NAME:read_cache
nr_readcache_misses
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_misses_user 0
/blockstore/read_cache/nr_readcache_misses_user
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_misses_user
0
HERE 
NAME:read_cache
nr_readcache_misses_user
0
HERE 
Out BEFORE
/blockstore/readahead/nr_hits 0
/blockstore/readahead/nr_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_hits
0
HERE 
NAME:readahead
nr_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_pages 0
/blockstore/readahead/nr_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_pages
0
HERE 
NAME:readahead
nr_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_fifo_seq_hits 0
/blockstore/readahead/nr_read_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_fifo_seq_hits
0
HERE 
NAME:readahead
nr_read_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_fifo_seq_pages 0
/blockstore/readahead/nr_read_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_fifo_seq_pages
0
HERE 
NAME:readahead
nr_read_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_fifo_seq_hits 0
/blockstore/readahead/nr_read_lba_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_fifo_seq_hits
0
HERE 
NAME:readahead
nr_read_lba_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_fifo_seq_pages 0
/blockstore/readahead/nr_read_lba_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_fifo_seq_pages
0
HERE 
NAME:readahead
nr_read_lba_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_seq_hits 0
/blockstore/readahead/nr_read_lba_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_seq_hits
0
HERE 
NAME:readahead
nr_read_lba_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_seq_pages 0
/blockstore/readahead/nr_read_lba_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_seq_pages
0
HERE 
NAME:readahead
nr_read_lba_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_fifo_seq_hits 0
/blockstore/readahead/nr_write_merge_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_fifo_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_fifo_seq_pages 0
/blockstore/readahead/nr_write_merge_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_fifo_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_fifo_seq_hits 0
/blockstore/readahead/nr_write_merge_lba_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_fifo_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_lba_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_fifo_seq_pages 0
/blockstore/readahead/nr_write_merge_lba_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_fifo_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_lba_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_seq_hits 0
/blockstore/readahead/nr_write_merge_lba_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_lba_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_seq_pages 0
/blockstore/readahead/nr_write_merge_lba_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_lba_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_ read-ahead:(read, fifo seq) page hit postion
/blockstore/readahead/read_fifo_seq_hit_page_ read-ahead:(read, fifo seq) page hit
postion
  max: 0 pages

/blockstore/readahead/read_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/read_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:read_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_/average NaN
/blockstore/readahead/read_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_fifo_seq_hit_page_/average
nan
HERE 
NAME:read_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/read_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:read_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_ read-ahead:(read, lba& fifo seq)  page hit postion
/blockstore/readahead/read_lba_fifo_seq_hit_page_ read-ahead:(read, lba& fifo seq)  page hit
postion
  max: 0 pages

/blockstore/readahead/read_lba_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/read_lba_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:read_lba_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_/average NaN
/blockstore/readahead/read_lba_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:read_lba_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/read_lba_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:read_lba_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_ read-ahead:(read, lba seq) page hit postion
/blockstore/readahead/read_lba_seq_hit_page_ read-ahead:(read, lba seq) page hit
postion
  max: 0 pages

/blockstore/readahead/read_lba_seq_hit_page_/aggregate 0
/blockstore/readahead/read_lba_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_lba_seq_hit_page_/aggregate
0
HERE 
NAME:read_lba_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_/average NaN
/blockstore/readahead/read_lba_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_lba_seq_hit_page_/average
nan
HERE 
NAME:read_lba_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_/nupdates 0
/blockstore/readahead/read_lba_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_lba_seq_hit_page_/nupdates
0
HERE 
NAME:read_lba_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_ read-ahead:(write_merge, fifo seq) page hit postion
/blockstore/readahead/write_merge_fifo_seq_hit_page_ read-ahead:(write_merge, fifo seq) page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/average
nan
HERE 
NAME:write_merge_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_ read-ahead:(write_merge,lba& fifo seq)  page hit postion
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_ read-ahead:(write_merge,lba& fifo seq)  page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_ read-ahead:(write_merge, lba seq) page hit postion
/blockstore/readahead/write_merge_lba_seq_hit_page_ read-ahead:(write_merge, lba seq) page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_lba_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_lba_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_lba_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_lba_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/average
nan
HERE 
NAME:write_merge_lba_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_lba_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_lba_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op Number of pages in a batchIO of write op
/blockstore/wbcache/batch_size_write_op Number of pages in a batchIO of write
op
170173955 : 1
  max: 1 pages
      Aggregate : 170173955 pages. Avg size : 1
/blockstore/wbcache/batch_size_write_op/aggregate 170173955
/blockstore/wbcache/batch_size_write_op/aggregate
170173955
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/aggregate
170173955
HERE 
NAME:wbcache
batch_size_write_op/aggregate
170173955
HERE 
NAME:batch_size_write_op
aggregate
170173955
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op/average 1
/blockstore/wbcache/batch_size_write_op/average
1
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/average
1
HERE 
NAME:wbcache
batch_size_write_op/average
1
HERE 
NAME:batch_size_write_op
average
1
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op/nupdates 170173955
/blockstore/wbcache/batch_size_write_op/nupdates
170173955
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/nupdates
170173955
HERE 
NAME:wbcache
batch_size_write_op/nupdates
170173955
HERE 
NAME:batch_size_write_op
nupdates
170173955
HERE 
Out BEFORE
/blockstore/wbcache/last_hdd_write [149:546467]
/blockstore/wbcache/last_hdd_write
[149:546467]
/blockstore/wbcache/last_persistent_hdd_write [149:469365]
/blockstore/wbcache/last_persistent_hdd_write
[149:469365]
/blockstore/wbcache/last_persistent_hdd_write_on_disk [149:377865]
/blockstore/wbcache/last_persistent_hdd_write_on_disk
[149:377865]
/blockstore/wbcache/last_ssd_write [149:560922]
/blockstore/wbcache/last_ssd_write
[149:560922]
/blockstore/wbcache/last_ssd_write_on_disk [149:457819]
/blockstore/wbcache/last_ssd_write_on_disk
[149:457819]
/blockstore/wbcache/nr_disk_fixes 0
/blockstore/wbcache/nr_disk_fixes
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes
0
HERE 
NAME:wbcache
nr_disk_fixes
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_fixes_fail 0
/blockstore/wbcache/nr_disk_fixes_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes_fail
0
HERE 
NAME:wbcache
nr_disk_fixes_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_fixes_success 0
/blockstore/wbcache/nr_disk_fixes_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes_success
0
HERE 
NAME:wbcache
nr_disk_fixes_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs 0
/blockstore/wbcache/nr_disk_scrubs
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs
0
HERE 
NAME:wbcache
nr_disk_scrubs
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs_fail 0
/blockstore/wbcache/nr_disk_scrubs_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs_fail
0
HERE 
NAME:wbcache
nr_disk_scrubs_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs_success 0
/blockstore/wbcache/nr_disk_scrubs_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs_success
0
HERE 
NAME:wbcache
nr_disk_scrubs_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_read_retries_ssd 0
/blockstore/wbcache/nr_page_read_retries_ssd
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_read_retries_ssd
0
HERE 
NAME:wbcache
nr_page_read_retries_ssd
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_reads 6
/blockstore/wbcache/nr_page_reads
6
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_reads
6
HERE 
NAME:wbcache
nr_page_reads
6
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_reads_ssd 4
/blockstore/wbcache/nr_page_reads_ssd
4
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_reads_ssd
4
HERE 
NAME:wbcache
nr_page_reads_ssd
4
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_writes 170173955
/blockstore/wbcache/nr_page_writes
170173955
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_writes
170173955
HERE 
NAME:wbcache
nr_page_writes
170173955
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes 0
/blockstore/wbcache/nr_ssd_fixes
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes
0
HERE 
NAME:wbcache
nr_ssd_fixes
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes_fail 0
/blockstore/wbcache/nr_ssd_fixes_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes_fail
0
HERE 
NAME:wbcache
nr_ssd_fixes_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes_success 0
/blockstore/wbcache/nr_ssd_fixes_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes_success
0
HERE 
NAME:wbcache
nr_ssd_fixes_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs 0
/blockstore/wbcache/nr_ssd_scrubs
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs
0
HERE 
NAME:wbcache
nr_ssd_scrubs
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs_fail 0
/blockstore/wbcache/nr_ssd_scrubs_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs_fail
0
HERE 
NAME:wbcache
nr_ssd_scrubs_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs_success 0
/blockstore/wbcache/nr_ssd_scrubs_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs_success
0
HERE 
NAME:wbcache
nr_ssd_scrubs_success
0
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd write op ssd time
/blockstore/wbcache/op_write_time_ssd write op ssd
time
1077180 : 0
 299863 : 1
 235901 : 2
 427542 : 3-4
 811818 : 5-8
1898987 : 9-16
4252142 : 17-32
24617200 : 33-64
135336580 : 65-128
1154621 : 129-256
  60235 : 257-512
    341 : 513-1K
     24 : 1K-2K
     12 : 2K-4K
    356 : 4K-8K
  max: 5038 ms
      Aggregate : 12470127569 ms. Avg size : 73.2792
/blockstore/wbcache/op_write_time_ssd/aggregate 12470127569
/blockstore/wbcache/op_write_time_ssd/aggregate
12470127569
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/aggregate
12470127569
HERE 
NAME:wbcache
op_write_time_ssd/aggregate
12470127569
HERE 
NAME:op_write_time_ssd
aggregate
12470127569
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd/average 73.2792
/blockstore/wbcache/op_write_time_ssd/average
73.2792
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/average
73.2792
HERE 
NAME:wbcache
op_write_time_ssd/average
73.2792
HERE 
NAME:op_write_time_ssd
average
73.2792
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd/nupdates 170172802
/blockstore/wbcache/op_write_time_ssd/nupdates
170172802
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/nupdates
170172802
HERE 
NAME:wbcache
op_write_time_ssd/nupdates
170172802
HERE 
NAME:op_write_time_ssd
nupdates
170172802
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total write op total time
/blockstore/wbcache/op_write_time_total write op total
time
1010562 : 0
 309587 : 1
 229056 : 2
 414651 : 3-4
 782982 : 5-8
1563763 : 9-16
3861972 : 17-32
23333624 : 33-64
136973156 : 65-128
1454898 : 129-256
 232476 : 257-512
   5539 : 513-1K
    168 : 1K-2K
     12 : 2K-4K
    356 : 4K-8K
  max: 5249 ms
      Aggregate : 12653031089 ms. Avg size : 74.354
/blockstore/wbcache/op_write_time_total/aggregate 12653031089
/blockstore/wbcache/op_write_time_total/aggregate
12653031089
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/aggregate
12653031089
HERE 
NAME:wbcache
op_write_time_total/aggregate
12653031089
HERE 
NAME:op_write_time_total
aggregate
12653031089
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total/average 74.354
/blockstore/wbcache/op_write_time_total/average
74.354
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/average
74.354
HERE 
NAME:wbcache
op_write_time_total/average
74.354
HERE 
NAME:op_write_time_total
average
74.354
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total/nupdates 170172802
/blockstore/wbcache/op_write_time_total/nupdates
170172802
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/nupdates
170172802
HERE 
NAME:wbcache
op_write_time_total/nupdates
170172802
HERE 
NAME:op_write_time_total
nupdates
170172802
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk read op hdd time
/blockstore/wbcache/page_read_time_disk read op hdd
time
      2 : 17-32
  max: 22 ms
      Aggregate : 41 ms. Avg size : 20.5
/blockstore/wbcache/page_read_time_disk/aggregate 41
/blockstore/wbcache/page_read_time_disk/aggregate
41
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/aggregate
41
HERE 
NAME:wbcache
page_read_time_disk/aggregate
41
HERE 
NAME:page_read_time_disk
aggregate
41
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk/average 20.5
/blockstore/wbcache/page_read_time_disk/average
20.5
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/average
20.5
HERE 
NAME:wbcache
page_read_time_disk/average
20.5
HERE 
NAME:page_read_time_disk
average
20.5
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk/nupdates 2
/blockstore/wbcache/page_read_time_disk/nupdates
2
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/nupdates
2
HERE 
NAME:wbcache
page_read_time_disk/nupdates
2
HERE 
NAME:page_read_time_disk
nupdates
2
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd read op ssd time
/blockstore/wbcache/page_read_time_ssd read op ssd
time
      2 : 0
      1 : 5-8
      1 : 9-16
  max: 14 ms
      Aggregate : 21 ms. Avg size : 5.25
/blockstore/wbcache/page_read_time_ssd/aggregate 21
/blockstore/wbcache/page_read_time_ssd/aggregate
21
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/aggregate
21
HERE 
NAME:wbcache
page_read_time_ssd/aggregate
21
HERE 
NAME:page_read_time_ssd
aggregate
21
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd/average 5.25
/blockstore/wbcache/page_read_time_ssd/average
5.25
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/average
5.25
HERE 
NAME:wbcache
page_read_time_ssd/average
5.25
HERE 
NAME:page_read_time_ssd
average
5.25
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd/nupdates 4
/blockstore/wbcache/page_read_time_ssd/nupdates
4
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/nupdates
4
HERE 
NAME:wbcache
page_read_time_ssd/nupdates
4
HERE 
NAME:page_read_time_ssd
nupdates
4
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total read op total time
/blockstore/wbcache/page_read_time_total read op total
time
      2 : 0
      1 : 9-16
      3 : 17-32
  max: 25 ms
      Aggregate : 83 ms. Avg size : 13.8333
/blockstore/wbcache/page_read_time_total/aggregate 83
/blockstore/wbcache/page_read_time_total/aggregate
83
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/aggregate
83
HERE 
NAME:wbcache
page_read_time_total/aggregate
83
HERE 
NAME:page_read_time_total
aggregate
83
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total/average 13.8333
/blockstore/wbcache/page_read_time_total/average
13.8333
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/average
13.8333
HERE 
NAME:wbcache
page_read_time_total/average
13.8333
HERE 
NAME:page_read_time_total
average
13.8333
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total/nupdates 6
/blockstore/wbcache/page_read_time_total/nupdates
6
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/nupdates
6
HERE 
NAME:wbcache
page_read_time_total/nupdates
6
HERE 
NAME:page_read_time_total
nupdates
6
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_slice 3
/blockstore/wbcache/pages_per_slice
3
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_slice
3
HERE 
NAME:wbcache
pages_per_slice
3
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op count of pages per write op
/blockstore/wbcache/pages_per_write_op count of pages per write
op
170173955 : 1
  max: 1 pages
      Aggregate : 170173955 pages. Avg size : 1
/blockstore/wbcache/pages_per_write_op/aggregate 170173955
/blockstore/wbcache/pages_per_write_op/aggregate
170173955
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/aggregate
170173955
HERE 
NAME:wbcache
pages_per_write_op/aggregate
170173955
HERE 
NAME:pages_per_write_op
aggregate
170173955
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op/average 1
/blockstore/wbcache/pages_per_write_op/average
1
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/average
1
HERE 
NAME:wbcache
pages_per_write_op/average
1
HERE 
NAME:pages_per_write_op
average
1
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op/nupdates 170173955
/blockstore/wbcache/pages_per_write_op/nupdates
170173955
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/nupdates
170173955
HERE 
NAME:wbcache
pages_per_write_op/nupdates
170173955
HERE 
NAME:pages_per_write_op
nupdates
170173955
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_dirty_offsets_length 387
/blockstore/wbcache/processor/avg_dirty_offsets_length
387
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_dirty_offsets_length
387
HERE 
NAME:wbcache
processor/avg_dirty_offsets_length
387
HERE 
NAME:processor
avg_dirty_offsets_length
387
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_sync_time 0
/blockstore/wbcache/processor/avg_sync_time
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_sync_time
0
HERE 
NAME:wbcache
processor/avg_sync_time
0
HERE 
NAME:processor
avg_sync_time
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_trim_length 0
/blockstore/wbcache/processor/avg_trim_length
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_trim_length
0
HERE 
NAME:wbcache
processor/avg_trim_length
0
HERE 
NAME:processor
avg_trim_length
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/buffer_id 41407808
/blockstore/wbcache/processor/buffer_id
41407808
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/buffer_id
41407808
HERE 
NAME:wbcache
processor/buffer_id
41407808
HERE 
NAME:processor
buffer_id
41407808
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time How long it took to write a page to hdd
/blockstore/wbcache/processor/hdd_write_time How long it took to write a page to
hdd
   7383 : 0
1349087 : 1
17378490 : 2
102196728 : 3-4
10661241 : 5-8
11232175 : 9-16
12660715 : 17-32
9982710 : 33-64
3665337 : 65-128
 752605 : 129-256
 281415 : 257-512
   4608 : 513-1K
  max: 805 ms
      Aggregate : 1862801063 ms. Avg size : 10.9465
/blockstore/wbcache/processor/hdd_write_time/aggregate 1862801063
/blockstore/wbcache/processor/hdd_write_time/aggregate
1862801063
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/aggregate
1862801063
HERE 
NAME:wbcache
processor/hdd_write_time/aggregate
1862801063
HERE 
NAME:processor
hdd_write_time/aggregate
1862801063
HERE 
NAME:hdd_write_time
aggregate
1862801063
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time/average 10.9465
/blockstore/wbcache/processor/hdd_write_time/average
10.9465
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/average
10.9465
HERE 
NAME:wbcache
processor/hdd_write_time/average
10.9465
HERE 
NAME:processor
hdd_write_time/average
10.9465
HERE 
NAME:hdd_write_time
average
10.9465
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time/nupdates 170172494
/blockstore/wbcache/processor/hdd_write_time/nupdates
170172494
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/nupdates
170172494
HERE 
NAME:wbcache
processor/hdd_write_time/nupdates
170172494
HERE 
NAME:processor
hdd_write_time/nupdates
170172494
HERE 
NAME:hdd_write_time
nupdates
170172494
HERE 
Out BEFORE
/blockstore/wbcache/processor/max_dirty_offsets_length 12226
/blockstore/wbcache/processor/max_dirty_offsets_length
12226
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/max_dirty_offsets_length
12226
HERE 
NAME:wbcache
processor/max_dirty_offsets_length
12226
HERE 
NAME:processor
max_dirty_offsets_length
12226
HERE 
Out BEFORE
/blockstore/wbcache/processor/nr_pages_read 170172699
/blockstore/wbcache/processor/nr_pages_read
170172699
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/nr_pages_read
170172699
HERE 
NAME:wbcache
processor/nr_pages_read
170172699
HERE 
NAME:processor
nr_pages_read
170172699
HERE 
Out BEFORE
/blockstore/wbcache/processor/nr_pages_read_in_mem 169371491
/blockstore/wbcache/processor/nr_pages_read_in_mem
169371491
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/nr_pages_read_in_mem
169371491
HERE 
NAME:wbcache
processor/nr_pages_read_in_mem
169371491
HERE 
NAME:processor
nr_pages_read_in_mem
169371491
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time How long it took to free up pages
/blockstore/wbcache/processor/page_free_time How long it took to free up
pages
      8 : 3-4
     40 : 5-8
    108 : 9-16
    166 : 17-32
    348 : 33-64
    599 : 65-128
    860 : 129-256
    910 : 257-512
    955 : 513-1K
   1087 : 1K-2K
    491 : 2K-4K
      7 : 4K-8K
  max: 4543 ms
      Aggregate : 4110310 ms. Avg size : 736.747
/blockstore/wbcache/processor/page_free_time/aggregate 4110310
/blockstore/wbcache/processor/page_free_time/aggregate
4110310
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/aggregate
4110310
HERE 
NAME:wbcache
processor/page_free_time/aggregate
4110310
HERE 
NAME:processor
page_free_time/aggregate
4110310
HERE 
NAME:page_free_time
aggregate
4110310
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time/average 736.747
/blockstore/wbcache/processor/page_free_time/average
736.747
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/average
736.747
HERE 
NAME:wbcache
processor/page_free_time/average
736.747
HERE 
NAME:processor
page_free_time/average
736.747
HERE 
NAME:page_free_time
average
736.747
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time/nupdates 5579
/blockstore/wbcache/processor/page_free_time/nupdates
5579
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/nupdates
5579
HERE 
NAME:wbcache
processor/page_free_time/nupdates
5579
HERE 
NAME:processor
page_free_time/nupdates
5579
HERE 
NAME:page_free_time
nupdates
5579
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_reads 0
/blockstore/wbcache/processor/pending_reads
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_reads
0
HERE 
NAME:wbcache
processor/pending_reads
0
HERE 
NAME:processor
pending_reads
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes # write io requests pending at disk, updated after issuing a write request to disk
 188676 : 1
 182172 : 2
 397148 : 3-4
 961457 : 5-8
2772369 : 9-16
13503201 : 17-32
69791766 : 33-64
26306187 : 65-128
18739139 : 129-256
18121215 : 257-512
19209369 : 513-1K
  max: 976 requests
      Aggregate : 31002918341 requests. Avg size : 182.185
/blockstore/wbcache/processor/pending_writes 205
/blockstore/wbcache/processor/pending_writes/aggregate 31002918341
/blockstore/wbcache/processor/pending_writes/aggregate
31002918341
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/aggregate
31002918341
HERE 
NAME:wbcache
processor/pending_writes/aggregate
31002918341
HERE 
NAME:processor
pending_writes/aggregate
31002918341
HERE 
NAME:pending_writes
aggregate
31002918341
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes/average 182.185
/blockstore/wbcache/processor/pending_writes/average
182.185
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/average
182.185
HERE 
NAME:wbcache
processor/pending_writes/average
182.185
HERE 
NAME:processor
pending_writes/average
182.185
HERE 
NAME:pending_writes
average
182.185
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes/nupdates 170172699
/blockstore/wbcache/processor/pending_writes/nupdates
170172699
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/nupdates
170172699
HERE 
NAME:wbcache
processor/pending_writes/nupdates
170172699
HERE 
NAME:processor
pending_writes/nupdates
170172699
HERE 
NAME:pending_writes
nupdates
170172699
HERE 
Out BEFORE
/blockstore/wbcache/processor/read_iops 13512
/blockstore/wbcache/processor/read_iops
13512
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/read_iops
13512
HERE 
NAME:wbcache
processor/read_iops
13512
HERE 
NAME:processor
read_iops
13512
HERE 
Out BEFORE
/blockstore/wbcache/processor/read_throughput 117610224
/blockstore/wbcache/processor/read_throughput
117610224
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/read_throughput
117610224
HERE 
NAME:wbcache
processor/read_throughput
117610224
HERE 
NAME:processor
read_throughput
117610224
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time How long it took to read a page from ssd
/blockstore/wbcache/processor/ssd_read_time How long it took to read a page from
ssd
   1960 : 0
   3803 : 1
   2822 : 2
   9859 : 3-4
  24026 : 5-8
  55418 : 9-16
 258201 : 17-32
 113261 : 33-64
 197854 : 65-128
 134004 : 129-256
  max: 208 ms
      Aggregate : 52904739 ms. Avg size : 66.0312
/blockstore/wbcache/processor/ssd_read_time/aggregate 52904739
/blockstore/wbcache/processor/ssd_read_time/aggregate
52904739
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/aggregate
52904739
HERE 
NAME:wbcache
processor/ssd_read_time/aggregate
52904739
HERE 
NAME:processor
ssd_read_time/aggregate
52904739
HERE 
NAME:ssd_read_time
aggregate
52904739
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time/average 66.0312
/blockstore/wbcache/processor/ssd_read_time/average
66.0312
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/average
66.0312
HERE 
NAME:wbcache
processor/ssd_read_time/average
66.0312
HERE 
NAME:processor
ssd_read_time/average
66.0312
HERE 
NAME:ssd_read_time
average
66.0312
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time/nupdates 801208
/blockstore/wbcache/processor/ssd_read_time/nupdates
801208
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/nupdates
801208
HERE 
NAME:wbcache
processor/ssd_read_time/nupdates
801208
HERE 
NAME:processor
ssd_read_time/nupdates
801208
HERE 
NAME:ssd_read_time
nupdates
801208
HERE 
Out BEFORE
/blockstore/wbcache/processor/write_iops 13512
/blockstore/wbcache/processor/write_iops
13512
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/write_iops
13512
HERE 
NAME:wbcache
processor/write_iops
13512
HERE 
NAME:processor
write_iops
13512
HERE 
Out BEFORE
/blockstore/wbcache/processor/write_throughput 117610083
/blockstore/wbcache/processor/write_throughput
117610083
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/write_throughput
117610083
HERE 
NAME:wbcache
processor/write_throughput
117610083
HERE 
NAME:processor
write_throughput
117610083
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time read op queued time
/blockstore/wbcache/read_queued_time read op queued
time
      3 : 0
      1 : 3-4
      1 : 5-8
      1 : 9-16
  max: 9 ms
      Aggregate : 20 ms. Avg size : 3.33333
/blockstore/wbcache/read_queued_time/aggregate 20
/blockstore/wbcache/read_queued_time/aggregate
20
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/aggregate
20
HERE 
NAME:wbcache
read_queued_time/aggregate
20
HERE 
NAME:read_queued_time
aggregate
20
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time/average 3.33333
/blockstore/wbcache/read_queued_time/average
3.33333
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/average
3.33333
HERE 
NAME:wbcache
read_queued_time/average
3.33333
HERE 
NAME:read_queued_time
average
3.33333
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time/nupdates 6
/blockstore/wbcache/read_queued_time/nupdates
6
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/nupdates
6
HERE 
NAME:wbcache
read_queued_time/nupdates
6
HERE 
NAME:read_queued_time
nupdates
6
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful total unsuccessful page read time
/blockstore/wbcache/total_page_read_time_unsuccessful total unsuccessful page read
time
  max: 0 ms

/blockstore/wbcache/total_page_read_time_unsuccessful/aggregate 0
/blockstore/wbcache/total_page_read_time_unsuccessful/aggregate
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/aggregate
0
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/aggregate
0
HERE 
NAME:total_page_read_time_unsuccessful
aggregate
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful/average NaN
/blockstore/wbcache/total_page_read_time_unsuccessful/average
NaN
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/average
nan
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/average
nan
HERE 
NAME:total_page_read_time_unsuccessful
average
nan
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful/nupdates 0
/blockstore/wbcache/total_page_read_time_unsuccessful/nupdates
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/nupdates
0
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/nupdates
0
HERE 
NAME:total_page_read_time_unsuccessful
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful total unsuccessful page write time
/blockstore/wbcache/total_page_write_time_unsuccessful total unsuccessful page write
time
  max: 0 ms

/blockstore/wbcache/total_page_write_time_unsuccessful/aggregate 0
/blockstore/wbcache/total_page_write_time_unsuccessful/aggregate
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/aggregate
0
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/aggregate
0
HERE 
NAME:total_page_write_time_unsuccessful
aggregate
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful/average NaN
/blockstore/wbcache/total_page_write_time_unsuccessful/average
NaN
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/average
nan
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/average
nan
HERE 
NAME:total_page_write_time_unsuccessful
average
nan
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful/nupdates 0
/blockstore/wbcache/total_page_write_time_unsuccessful/nupdates
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/nupdates
0
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/nupdates
0
HERE 
NAME:total_page_write_time_unsuccessful
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/wbc_version 5
/blockstore/wbcache/wbc_version
5
In BEFORE
HERE 
NAME:blockstore
wbcache/wbc_version
5
HERE 
NAME:wbcache
wbc_version
5
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time write op queued time
/blockstore/wbcache/write_queued_time write op queued
time
170173954 : 0
      1 : 1
  max: 1 ms
      Aggregate : 1 ms. Avg size : 5.87634e-09
/blockstore/wbcache/write_queued_time/aggregate 1
/blockstore/wbcache/write_queued_time/aggregate
1
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/aggregate
1
HERE 
NAME:wbcache
write_queued_time/aggregate
1
HERE 
NAME:write_queued_time
aggregate
1
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time/average 5.87634e-09
/blockstore/wbcache/write_queued_time/average
5.87634e-09
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/average
5.87634e-09
HERE 
NAME:wbcache
write_queued_time/average
5.87634e-09
HERE 
NAME:write_queued_time
average
5.87634e-09
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time/nupdates 170173955
/blockstore/wbcache/write_queued_time/nupdates
170173955
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/nupdates
170173955
HERE 
NAME:wbcache
write_queued_time/nupdates
170173955
HERE 
NAME:write_queued_time
nupdates
170173955
HERE 
Out BEFORE
/blockstore/workload/pending_pages # user io pages pending when a user read/write req is received
/blockstore/workload/pending_pages # user io pages pending when a user read/write req is
received
  max: 0 pages

/blockstore/workload/pending_pages/aggregate 0
/blockstore/workload/pending_pages/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/aggregate
0
HERE 
NAME:workload
pending_pages/aggregate
0
HERE 
NAME:pending_pages
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/pending_pages/average NaN
/blockstore/workload/pending_pages/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/average
nan
HERE 
NAME:workload
pending_pages/average
nan
HERE 
NAME:pending_pages
average
nan
HERE 
Out BEFORE
/blockstore/workload/pending_pages/nupdates 0
/blockstore/workload/pending_pages/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/nupdates
0
HERE 
NAME:workload
pending_pages/nupdates
0
HERE 
NAME:pending_pages
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/pending_requests # user io requests pending when a user read/write req is received
/blockstore/workload/pending_requests # user io requests pending when a user read/write req is
received
  max: 0 requests

/blockstore/workload/pending_requests/aggregate 0
/blockstore/workload/pending_requests/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/aggregate
0
HERE 
NAME:workload
pending_requests/aggregate
0
HERE 
NAME:pending_requests
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/pending_requests/average NaN
/blockstore/workload/pending_requests/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/average
nan
HERE 
NAME:workload
pending_requests/average
nan
HERE 
NAME:pending_requests
average
nan
HERE 
Out BEFORE
/blockstore/workload/pending_requests/nupdates 0
/blockstore/workload/pending_requests/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/nupdates
0
HERE 
NAME:workload
pending_requests/nupdates
0
HERE 
NAME:pending_requests
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/readop_size size of user read request
/blockstore/workload/readop_size size of user read
request
  max: 0 blocks

/blockstore/workload/readop_size/aggregate 0
/blockstore/workload/readop_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/aggregate
0
HERE 
NAME:workload
readop_size/aggregate
0
HERE 
NAME:readop_size
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/readop_size/average NaN
/blockstore/workload/readop_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/average
nan
HERE 
NAME:workload
readop_size/average
nan
HERE 
NAME:readop_size
average
nan
HERE 
Out BEFORE
/blockstore/workload/readop_size/nupdates 0
/blockstore/workload/readop_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/nupdates
0
HERE 
NAME:workload
readop_size/nupdates
0
HERE 
NAME:readop_size
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/writeop_size write request size
/blockstore/workload/writeop_size write request
size
  max: 0 blocks

/blockstore/workload/writeop_size/aggregate 0
/blockstore/workload/writeop_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/aggregate
0
HERE 
NAME:workload
writeop_size/aggregate
0
HERE 
NAME:writeop_size
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/writeop_size/average NaN
/blockstore/workload/writeop_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/average
nan
HERE 
NAME:workload
writeop_size/average
nan
HERE 
NAME:writeop_size
average
nan
HERE 
Out BEFORE
/blockstore/workload/writeop_size/nupdates 0
/blockstore/workload/writeop_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/nupdates
0
HERE 
NAME:workload
writeop_size/nupdates
0
HERE 
NAME:writeop_size
nupdates
0
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs Superseded offset count blocked by the pending superseding page write
/blockstore/write/dirty_superseded_offs Superseded offset count blocked by the pending superseding page
write
  max: 0 offsets

/blockstore/write/dirty_superseded_offs/aggregate 0
/blockstore/write/dirty_superseded_offs/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/aggregate
0
HERE 
NAME:write
dirty_superseded_offs/aggregate
0
HERE 
NAME:dirty_superseded_offs
aggregate
0
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs/average NaN
/blockstore/write/dirty_superseded_offs/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/average
nan
HERE 
NAME:write
dirty_superseded_offs/average
nan
HERE 
NAME:dirty_superseded_offs
average
nan
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs/nupdates 0
/blockstore/write/dirty_superseded_offs/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/nupdates
0
HERE 
NAME:write
dirty_superseded_offs/nupdates
0
HERE 
NAME:dirty_superseded_offs
nupdates
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes 19356165132
/blockstore/write/nr_blk_writes
19356165132
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes
19356165132
HERE 
NAME:write
nr_blk_writes
19356165132
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_and_stores 0
/blockstore/write/nr_blk_writes_and_stores
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_and_stores
0
HERE 
NAME:write
nr_blk_writes_and_stores
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_in_mem 0
/blockstore/write/nr_blk_writes_in_mem
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_in_mem
0
HERE 
NAME:write
nr_blk_writes_in_mem
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_inherited 0
/blockstore/write/nr_blk_writes_inherited
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_inherited
0
HERE 
NAME:write
nr_blk_writes_inherited
0
HERE 
Out BEFORE
/blockstore/write/nr_page_reads_disk_store 0
/blockstore/write/nr_page_reads_disk_store
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_reads_disk_store
0
HERE 
NAME:write
nr_page_reads_disk_store
0
HERE 
Out BEFORE
/blockstore/write/nr_page_reads_rdc_store 0
/blockstore/write/nr_page_reads_rdc_store
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_reads_rdc_store
0
HERE 
NAME:write
nr_page_reads_rdc_store
0
HERE 
Out BEFORE
/blockstore/write/nr_page_stores 0
/blockstore/write/nr_page_stores
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_stores
0
HERE 
NAME:write
nr_page_stores
0
HERE 
Out BEFORE
/blockstore/write/nr_page_stores_denied_ 0
/blockstore/write/nr_page_stores_denied_
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_stores_denied_
0
HERE 
NAME:write
nr_page_stores_denied_
0
HERE 
Out BEFORE
/blockstore/write/nr_page_writes 0
/blockstore/write/nr_page_writes
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_writes
0
HERE 
NAME:write
nr_page_writes
0
HERE 
Out BEFORE
/blockstore/write/nr_page_writes_pending 0
/blockstore/write/nr_page_writes_pending
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_writes_pending
0
HERE 
NAME:write
nr_page_writes_pending
0
HERE 
Out BEFORE
/blockstore/write/nr_pages_partial 0
/blockstore/write/nr_pages_partial
0
In BEFORE
HERE 
NAME:blockstore
write/nr_pages_partial
0
HERE 
NAME:write
nr_pages_partial
0
HERE 
Out BEFORE
/blockstore/write/nr_pages_superseded 0
/blockstore/write/nr_pages_superseded
0
In BEFORE
HERE 
NAME:blockstore
write/nr_pages_superseded
0
HERE 
NAME:write
nr_pages_superseded
0
HERE 
Out BEFORE
/blockstore/write/op_page_alloc writes: time taken for page alloc
/blockstore/write/op_page_alloc writes: time taken for page
alloc
  max: 0 ms

/blockstore/write/op_page_alloc/aggregate 0
/blockstore/write/op_page_alloc/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/aggregate
0
HERE 
NAME:write
op_page_alloc/aggregate
0
HERE 
NAME:op_page_alloc
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_page_alloc/average NaN
/blockstore/write/op_page_alloc/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/average
nan
HERE 
NAME:write
op_page_alloc/average
nan
HERE 
NAME:op_page_alloc
average
nan
HERE 
Out BEFORE
/blockstore/write/op_page_alloc/nupdates 0
/blockstore/write/op_page_alloc/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/nupdates
0
HERE 
NAME:write
op_page_alloc/nupdates
0
HERE 
NAME:op_page_alloc
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_queued_time writes: time waiting in queue for turn
/blockstore/write/op_queued_time writes: time waiting in queue for
turn
  max: 0 ms

/blockstore/write/op_queued_time/aggregate 0
/blockstore/write/op_queued_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/aggregate
0
HERE 
NAME:write
op_queued_time/aggregate
0
HERE 
NAME:op_queued_time
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_queued_time/average NaN
/blockstore/write/op_queued_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/average
nan
HERE 
NAME:write
op_queued_time/average
nan
HERE 
NAME:op_queued_time
average
nan
HERE 
Out BEFORE
/blockstore/write/op_queued_time/nupdates 0
/blockstore/write/op_queued_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/nupdates
0
HERE 
NAME:write
op_queued_time/nupdates
0
HERE 
NAME:op_queued_time
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge writes: time taken for read and merge
/blockstore/write/op_read_n_merge writes: time taken for read and
merge
  max: 0 ms

/blockstore/write/op_read_n_merge/aggregate 0
/blockstore/write/op_read_n_merge/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/aggregate
0
HERE 
NAME:write
op_read_n_merge/aggregate
0
HERE 
NAME:op_read_n_merge
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge/average NaN
/blockstore/write/op_read_n_merge/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/average
nan
HERE 
NAME:write
op_read_n_merge/average
nan
HERE 
NAME:op_read_n_merge
average
nan
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge/nupdates 0
/blockstore/write/op_read_n_merge/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/nupdates
0
HERE 
NAME:write
op_read_n_merge/nupdates
0
HERE 
NAME:op_read_n_merge
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_total_time writes: total time taken
/blockstore/write/op_total_time writes: total time
taken
  max: 0 ms

/blockstore/write/op_total_time/aggregate 0
/blockstore/write/op_total_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/aggregate
0
HERE 
NAME:write
op_total_time/aggregate
0
HERE 
NAME:op_total_time
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_total_time/average NaN
/blockstore/write/op_total_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/average
nan
HERE 
NAME:write
op_total_time/average
nan
HERE 
NAME:op_total_time
average
nan
HERE 
Out BEFORE
/blockstore/write/op_total_time/nupdates 0
/blockstore/write/op_total_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/nupdates
0
HERE 
NAME:write
op_total_time/nupdates
0
HERE 
NAME:op_total_time
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes aligned small or multi-page write
/blockstore/write/rmw/aligned_writes aligned small or multi-page
write
  max: 0 blocks

/blockstore/write/rmw/aligned_writes/aggregate 0
/blockstore/write/rmw/aligned_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/aggregate
0
HERE 
NAME:write
rmw/aligned_writes/aggregate
0
HERE 
NAME:rmw
aligned_writes/aggregate
0
HERE 
NAME:aligned_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes/average NaN
/blockstore/write/rmw/aligned_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/average
nan
HERE 
NAME:write
rmw/aligned_writes/average
nan
HERE 
NAME:rmw
aligned_writes/average
nan
HERE 
NAME:aligned_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes/nupdates 0
/blockstore/write/rmw/aligned_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/nupdates
0
HERE 
NAME:write
rmw/aligned_writes/nupdates
0
HERE 
NAME:rmw
aligned_writes/nupdates
0
HERE 
NAME:aligned_writes
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece Time gap between old write and new  big write (>=16 sectors)
/blockstore/write/rmw/big_write_time_differece Time gap between old write and new  big write (>=16
sectors)
  max: 0 sec

/blockstore/write/rmw/big_write_time_differece/aggregate 0
/blockstore/write/rmw/big_write_time_differece/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/aggregate
0
HERE 
NAME:write
rmw/big_write_time_differece/aggregate
0
HERE 
NAME:rmw
big_write_time_differece/aggregate
0
HERE 
NAME:big_write_time_differece
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece/average NaN
/blockstore/write/rmw/big_write_time_differece/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/average
nan
HERE 
NAME:write
rmw/big_write_time_differece/average
nan
HERE 
NAME:rmw
big_write_time_differece/average
nan
HERE 
NAME:big_write_time_differece
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece/nupdates 0
/blockstore/write/rmw/big_write_time_differece/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/nupdates
0
HERE 
NAME:write
rmw/big_write_time_differece/nupdates
0
HERE 
NAME:rmw
big_write_time_differece/nupdates
0
HERE 
NAME:big_write_time_differece
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/nr_page_reads_disk 0
/blockstore/write/rmw/nr_page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/nr_page_reads_disk
0
HERE 
NAME:write
rmw/nr_page_reads_disk
0
HERE 
NAME:rmw
nr_page_reads_disk
0
HERE 
Out BEFORE
/blockstore/write/rmw/nr_page_reads_rdc 0
/blockstore/write/rmw/nr_page_reads_rdc
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/nr_page_reads_rdc
0
HERE 
NAME:write
rmw/nr_page_reads_rdc
0
HERE 
NAME:rmw
nr_page_reads_rdc
0
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece Time gap between old write and new  short write(<16 sectors)
/blockstore/write/rmw/small_write_time_differece Time gap between old write and new  short write(<16
sectors)
  max: 0 sec

/blockstore/write/rmw/small_write_time_differece/aggregate 0
/blockstore/write/rmw/small_write_time_differece/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/aggregate
0
HERE 
NAME:write
rmw/small_write_time_differece/aggregate
0
HERE 
NAME:rmw
small_write_time_differece/aggregate
0
HERE 
NAME:small_write_time_differece
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece/average NaN
/blockstore/write/rmw/small_write_time_differece/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/average
nan
HERE 
NAME:write
rmw/small_write_time_differece/average
nan
HERE 
NAME:rmw
small_write_time_differece/average
nan
HERE 
NAME:small_write_time_differece
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece/nupdates 0
/blockstore/write/rmw/small_write_time_differece/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/nupdates
0
HERE 
NAME:write
rmw/small_write_time_differece/nupdates
0
HERE 
NAME:rmw
small_write_time_differece/nupdates
0
HERE 
NAME:small_write_time_differece
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes small write at the end of the page or  unaligned multi page write
/blockstore/write/rmw/unaligned_other_writes small write at the end of the page or  unaligned multi page
write
  max: 0 blocks

/blockstore/write/rmw/unaligned_other_writes/aggregate 0
/blockstore/write/rmw/unaligned_other_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/aggregate
0
HERE 
NAME:write
rmw/unaligned_other_writes/aggregate
0
HERE 
NAME:rmw
unaligned_other_writes/aggregate
0
HERE 
NAME:unaligned_other_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes/average NaN
/blockstore/write/rmw/unaligned_other_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/average
nan
HERE 
NAME:write
rmw/unaligned_other_writes/average
nan
HERE 
NAME:rmw
unaligned_other_writes/average
nan
HERE 
NAME:unaligned_other_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes/nupdates 0
/blockstore/write/rmw/unaligned_other_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/nupdates
0
HERE 
NAME:write
rmw/unaligned_other_writes/nupdates
0
HERE 
NAME:rmw
unaligned_other_writes/nupdates
0
HERE 
NAME:unaligned_other_writes
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset starting offset of (other) unaligned wrtes
/blockstore/write/rmw/unaligned_other_writes_starting_offset starting offset of (other) unaligned
wrtes
  max: 0 block

/blockstore/write/rmw/unaligned_other_writes_starting_offset/aggregate 0
/blockstore/write/rmw/unaligned_other_writes_starting_offset/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:unaligned_other_writes_starting_offset
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset/average NaN
/blockstore/write/rmw/unaligned_other_writes_starting_offset/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:unaligned_other_writes_starting_offset
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset/nupdates 0
/blockstore/write/rmw/unaligned_other_writes_starting_offset/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:unaligned_other_writes_starting_offset
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes small write in the middle of the page
/blockstore/write/rmw/unaligned_within_page_writes small write in the middle of the
page
  max: 0 blocks

/blockstore/write/rmw/unaligned_within_page_writes/aggregate 0
/blockstore/write/rmw/unaligned_within_page_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/aggregate
0
HERE 
NAME:write
rmw/unaligned_within_page_writes/aggregate
0
HERE 
NAME:rmw
unaligned_within_page_writes/aggregate
0
HERE 
NAME:unaligned_within_page_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes/average NaN
/blockstore/write/rmw/unaligned_within_page_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/average
nan
HERE 
NAME:write
rmw/unaligned_within_page_writes/average
nan
HERE 
NAME:rmw
unaligned_within_page_writes/average
nan
HERE 
NAME:unaligned_within_page_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes/nupdates 0
/blockstore/write/rmw/unaligned_within_page_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/nupdates
0
HERE 
NAME:write
rmw/unaligned_within_page_writes/nupdates
0
HERE 
NAME:rmw
unaligned_within_page_writes/nupdates
0
HERE 
NAME:unaligned_within_page_writes
nupdates
0
HERE 
Out BEFORE
      Dumping iSCSI Stats
      Dumping MGMT Stats
/mgmt/actionqueue/queue_size 0
/mgmt/actionqueue/queue_size
0
In BEFORE
HERE 
NAME:mgmt
actionqueue/queue_size
0
HERE 
NAME:actionqueue
queue_size
0
HERE 
Out BEFORE
/mgmt/actionstore/queue_size 120
/mgmt/actionstore/queue_size
120
In BEFORE
HERE 
NAME:mgmt
actionstore/queue_size
120
HERE 
NAME:actionstore
queue_size
120
HERE 
Out BEFORE
    Finished dumping external listener.
GraniteEdge stats at ---- ----Tue 2016-07-26 00:50:45 GMT
2016-07-26 00:50:45
      Dumping RdiskEdge Stats
      Dumping BlockStore Stats
/blockstore/10/dc_last_write_time 1469479904
/blockstore/10/dc_last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
10/dc_last_write_time
1469479904
HERE 
NAME:10
dc_last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/10/last_write_time 1469479904
/blockstore/10/last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
10/last_write_time
1469479904
HERE 
NAME:10
last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/10/nr_blk_commits 91706813
/blockstore/10/nr_blk_commits
91706813
In BEFORE
HERE 
NAME:blockstore
10/nr_blk_commits
91706813
HERE 
NAME:10
nr_blk_commits
91706813
HERE 
Out BEFORE
/blockstore/10/nr_blk_writes 91706813
/blockstore/10/nr_blk_writes
91706813
In BEFORE
HERE 
NAME:blockstore
10/nr_blk_writes
91706813
HERE 
NAME:10
nr_blk_writes
91706813
HERE 
Out BEFORE
/blockstore/11/dc_last_write_time 1469479904
/blockstore/11/dc_last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
11/dc_last_write_time
1469479904
HERE 
NAME:11
dc_last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/11/last_write_time 1469479904
/blockstore/11/last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
11/last_write_time
1469479904
HERE 
NAME:11
last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/11/nr_blk_commits 99990631
/blockstore/11/nr_blk_commits
99990631
In BEFORE
HERE 
NAME:blockstore
11/nr_blk_commits
99990631
HERE 
NAME:11
nr_blk_commits
99990631
HERE 
Out BEFORE
/blockstore/11/nr_blk_writes 99990631
/blockstore/11/nr_blk_writes
99990631
In BEFORE
HERE 
NAME:blockstore
11/nr_blk_writes
99990631
HERE 
NAME:11
nr_blk_writes
99990631
HERE 
Out BEFORE
/blockstore/12/dc_last_write_time 1469479905
/blockstore/12/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
12/dc_last_write_time
1469479905
HERE 
NAME:12
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/12/last_write_time 1469479905
/blockstore/12/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
12/last_write_time
1469479905
HERE 
NAME:12
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/12/nr_blk_commits 2894843
/blockstore/12/nr_blk_commits
2894843
In BEFORE
HERE 
NAME:blockstore
12/nr_blk_commits
2894843
HERE 
NAME:12
nr_blk_commits
2894843
HERE 
Out BEFORE
/blockstore/12/nr_blk_writes 2894843
/blockstore/12/nr_blk_writes
2894843
In BEFORE
HERE 
NAME:blockstore
12/nr_blk_writes
2894843
HERE 
NAME:12
nr_blk_writes
2894843
HERE 
Out BEFORE
/blockstore/13/dc_last_write_time 1469479905
/blockstore/13/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
13/dc_last_write_time
1469479905
HERE 
NAME:13
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/13/last_write_time 1469479905
/blockstore/13/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
13/last_write_time
1469479905
HERE 
NAME:13
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/13/nr_blk_commits 4727607438
/blockstore/13/nr_blk_commits
4727607438
In BEFORE
HERE 
NAME:blockstore
13/nr_blk_commits
4727607438
HERE 
NAME:13
nr_blk_commits
4727607438
HERE 
Out BEFORE
/blockstore/13/nr_blk_writes 4727607438
/blockstore/13/nr_blk_writes
4727607438
In BEFORE
HERE 
NAME:blockstore
13/nr_blk_writes
4727607438
HERE 
NAME:13
nr_blk_writes
4727607438
HERE 
Out BEFORE
/blockstore/14/dc_last_write_time 1469479905
/blockstore/14/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
14/dc_last_write_time
1469479905
HERE 
NAME:14
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/14/last_write_time 1469479905
/blockstore/14/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
14/last_write_time
1469479905
HERE 
NAME:14
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/14/nr_blk_commits 1835272490
/blockstore/14/nr_blk_commits
1835272490
In BEFORE
HERE 
NAME:blockstore
14/nr_blk_commits
1835272490
HERE 
NAME:14
nr_blk_commits
1835272490
HERE 
Out BEFORE
/blockstore/14/nr_blk_writes 1835272490
/blockstore/14/nr_blk_writes
1835272490
In BEFORE
HERE 
NAME:blockstore
14/nr_blk_writes
1835272490
HERE 
NAME:14
nr_blk_writes
1835272490
HERE 
Out BEFORE
/blockstore/16/dc_last_write_time 1469479905
/blockstore/16/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
16/dc_last_write_time
1469479905
HERE 
NAME:16
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/16/last_write_time 1469479905
/blockstore/16/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
16/last_write_time
1469479905
HERE 
NAME:16
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/16/nr_blk_commits 12455455463
/blockstore/16/nr_blk_commits
12455455463
In BEFORE
HERE 
NAME:blockstore
16/nr_blk_commits
12455455463
HERE 
NAME:16
nr_blk_commits
12455455463
HERE 
Out BEFORE
/blockstore/16/nr_blk_writes 12455455463
/blockstore/16/nr_blk_writes
12455455463
In BEFORE
HERE 
NAME:blockstore
16/nr_blk_writes
12455455463
HERE 
NAME:16
nr_blk_writes
12455455463
HERE 
Out BEFORE
/blockstore/8/dc_last_write_time 1469479902
/blockstore/8/dc_last_write_time
1469479902
In BEFORE
HERE 
NAME:blockstore
8/dc_last_write_time
1469479902
HERE 
NAME:8
dc_last_write_time
1469479902
HERE 
Out BEFORE
/blockstore/8/last_write_time 1469479902
/blockstore/8/last_write_time
1469479902
In BEFORE
HERE 
NAME:blockstore
8/last_write_time
1469479902
HERE 
NAME:8
last_write_time
1469479902
HERE 
Out BEFORE
/blockstore/8/nr_blk_commits 61845671
/blockstore/8/nr_blk_commits
61845671
In BEFORE
HERE 
NAME:blockstore
8/nr_blk_commits
61845671
HERE 
NAME:8
nr_blk_commits
61845671
HERE 
Out BEFORE
/blockstore/8/nr_blk_writes 61845671
/blockstore/8/nr_blk_writes
61845671
In BEFORE
HERE 
NAME:blockstore
8/nr_blk_writes
61845671
HERE 
NAME:8
nr_blk_writes
61845671
HERE 
Out BEFORE
/blockstore/9/dc_last_write_time 1469479905
/blockstore/9/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
9/dc_last_write_time
1469479905
HERE 
NAME:9
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/9/last_write_time 1469479905
/blockstore/9/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
9/last_write_time
1469479905
HERE 
NAME:9
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/9/nr_blk_commits 80280964
/blockstore/9/nr_blk_commits
80280964
In BEFORE
HERE 
NAME:blockstore
9/nr_blk_commits
80280964
HERE 
NAME:9
nr_blk_commits
80280964
HERE 
Out BEFORE
/blockstore/9/nr_blk_writes 80280964
/blockstore/9/nr_blk_writes
80280964
In BEFORE
HERE 
NAME:blockstore
9/nr_blk_writes
80280964
HERE 
NAME:9
nr_blk_writes
80280964
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/slab_count 976
/blockstore/bufferpool/41407808/slab_count
976
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/slab_count
976
HERE 
NAME:bufferpool
41407808/slab_count
976
HERE 
NAME:41407808
slab_count
976
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/slab_size 8704
/blockstore/bufferpool/41407808/slab_size
8704
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/slab_size
8704
HERE 
NAME:bufferpool
41407808/slab_size
8704
HERE 
NAME:41407808
slab_size
8704
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/unable_to_allocate 0
/blockstore/bufferpool/41407808/unable_to_allocate
0
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/unable_to_allocate
0
HERE 
NAME:bufferpool
41407808/unable_to_allocate
0
HERE 
NAME:41407808
unable_to_allocate
0
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/unused 8495104
/blockstore/bufferpool/41407808/unused
8495104
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/unused
8495104
HERE 
NAME:bufferpool
41407808/unused
8495104
HERE 
NAME:41407808
unused
8495104
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms time taken for commit
/blockstore/commit_processor/commit_time_ms time taken for
commit
  max: 0 milliseconds

/blockstore/commit_processor/commit_time_ms/aggregate 0
/blockstore/commit_processor/commit_time_ms/aggregate
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/aggregate
0
HERE 
NAME:commit_processor
commit_time_ms/aggregate
0
HERE 
NAME:commit_time_ms
aggregate
0
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms/average NaN
/blockstore/commit_processor/commit_time_ms/average
NaN
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/average
nan
HERE 
NAME:commit_processor
commit_time_ms/average
nan
HERE 
NAME:commit_time_ms
average
nan
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms/nupdates 0
/blockstore/commit_processor/commit_time_ms/nupdates
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/nupdates
0
HERE 
NAME:commit_processor
commit_time_ms/nupdates
0
HERE 
NAME:commit_time_ms
nupdates
0
HERE 
Out BEFORE
/blockstore/commit_processor/dirty_data_present 1
/blockstore/commit_processor/dirty_data_present
1
In BEFORE
HERE 
NAME:blockstore
commit_processor/dirty_data_present
1
HERE 
NAME:commit_processor
dirty_data_present
1
HERE 
Out BEFORE
/blockstore/commit_processor/next_commit [LSN::INVALID]
/blockstore/commit_processor/next_commit
[LSN::INVALID]
/blockstore/commit_processor/nr_blk_commits 19356165132
/blockstore/commit_processor/nr_blk_commits
19356165132
In BEFORE
HERE 
NAME:blockstore
commit_processor/nr_blk_commits
19356165132
HERE 
NAME:commit_processor
nr_blk_commits
19356165132
HERE 
Out BEFORE
/blockstore/commit_processor/nr_blk_commits_in_mem 0
/blockstore/commit_processor/nr_blk_commits_in_mem
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/nr_blk_commits_in_mem
0
HERE 
NAME:commit_processor
nr_blk_commits_in_mem
0
HERE 
Out BEFORE
/blockstore/commit_processor/page_reads_cache 0
/blockstore/commit_processor/page_reads_cache
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/page_reads_cache
0
HERE 
NAME:commit_processor
page_reads_cache
0
HERE 
Out BEFORE
/blockstore/commit_processor/page_reads_disk 0
/blockstore/commit_processor/page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/page_reads_disk
0
HERE 
NAME:commit_processor
page_reads_disk
0
HERE 
Out BEFORE
/blockstore/commit_processor/pause_count 0
/blockstore/commit_processor/pause_count
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/pause_count
0
HERE 
NAME:commit_processor
pause_count
0
HERE 
Out BEFORE
/blockstore/commit_processor/paused_msecs 0
/blockstore/commit_processor/paused_msecs
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/paused_msecs
0
HERE 
NAME:commit_processor
paused_msecs
0
HERE 
Out BEFORE
/blockstore/commit_processor/pending_commits 0
/blockstore/commit_processor/pending_commits
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/pending_commits
0
HERE 
NAME:commit_processor
pending_commits
0
HERE 
Out BEFORE
/blockstore/commit_processor/running_msecs 0
/blockstore/commit_processor/running_msecs
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/running_msecs
0
HERE 
NAME:commit_processor
running_msecs
0
HERE 
Out BEFORE
/blockstore/commit_processor/state INIT
/blockstore/commit_processor/state
INIT
/blockstore/disk_helper/ha_peer_write_time ha peer op write time
/blockstore/disk_helper/ha_peer_write_time ha peer op write
time
  max: 0 ms

/blockstore/disk_helper/ha_peer_write_time/aggregate 0
/blockstore/disk_helper/ha_peer_write_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/aggregate
0
HERE 
NAME:disk_helper
ha_peer_write_time/aggregate
0
HERE 
NAME:ha_peer_write_time
aggregate
0
HERE 
Out BEFORE
/blockstore/disk_helper/ha_peer_write_time/average NaN
/blockstore/disk_helper/ha_peer_write_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/average
nan
HERE 
NAME:disk_helper
ha_peer_write_time/average
nan
HERE 
NAME:ha_peer_write_time
average
nan
HERE 
Out BEFORE
/blockstore/disk_helper/ha_peer_write_time/nupdates 0
/blockstore/disk_helper/ha_peer_write_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/nupdates
0
HERE 
NAME:disk_helper
ha_peer_write_time/nupdates
0
HERE 
NAME:ha_peer_write_time
nupdates
0
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time local op write time
/blockstore/disk_helper/local_write_time local op write
time
  max: 0 ms

/blockstore/disk_helper/local_write_time/aggregate 0
/blockstore/disk_helper/local_write_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/aggregate
0
HERE 
NAME:disk_helper
local_write_time/aggregate
0
HERE 
NAME:local_write_time
aggregate
0
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time/average NaN
/blockstore/disk_helper/local_write_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/average
nan
HERE 
NAME:disk_helper
local_write_time/average
nan
HERE 
NAME:local_write_time
average
nan
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time/nupdates 0
/blockstore/disk_helper/local_write_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/nupdates
0
HERE 
NAME:disk_helper
local_write_time/nupdates
0
HERE 
NAME:local_write_time
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/dirty_skips 0
/blockstore/fifo/dirty_skips
0
In BEFORE
HERE 
NAME:blockstore
fifo/dirty_skips
0
HERE 
NAME:fifo
dirty_skips
0
HERE 
Out BEFORE
/blockstore/fifo/error_status 0
/blockstore/fifo/error_status
0
In BEFORE
HERE 
NAME:blockstore
fifo/error_status
0
HERE 
NAME:fifo
error_status
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_mode_allocations 0
/blockstore/fifo/fifo_mode_allocations
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_mode_allocations
0
HERE 
NAME:fifo
fifo_mode_allocations
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips /blockstore/fifo/fifo_page_skips
/blockstore/fifo/fifo_page_skips
/blockstore/fifo/fifo_page_skips
  max: 0 pages

/blockstore/fifo/fifo_page_skips/aggregate 0
/blockstore/fifo/fifo_page_skips/aggregate
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/aggregate
0
HERE 
NAME:fifo
fifo_page_skips/aggregate
0
HERE 
NAME:fifo_page_skips
aggregate
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips/average NaN
/blockstore/fifo/fifo_page_skips/average
NaN
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/average
nan
HERE 
NAME:fifo
fifo_page_skips/average
nan
HERE 
NAME:fifo_page_skips
average
nan
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips/nupdates 0
/blockstore/fifo/fifo_page_skips/nupdates
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/nupdates
0
HERE 
NAME:fifo
fifo_page_skips/nupdates
0
HERE 
NAME:fifo_page_skips
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/last_commit [LSN::INVALID]
/blockstore/fifo/last_commit
[LSN::INVALID]
/blockstore/fifo/last_commit_on_disk [LSN::INVALID]
/blockstore/fifo/last_commit_on_disk
[LSN::INVALID]
/blockstore/fifo/last_sync [LSN::INVALID]
/blockstore/fifo/last_sync
[LSN::INVALID]
/blockstore/fifo/last_write [LSN::INVALID]
/blockstore/fifo/last_write
[LSN::INVALID]
/blockstore/fifo/last_write_on_disk [LSN::INVALID]
/blockstore/fifo/last_write_on_disk
[LSN::INVALID]
/blockstore/fifo/next_write [LSN::INVALID]
/blockstore/fifo/next_write
[LSN::INVALID]
/blockstore/fifo/nr_evictions 0
/blockstore/fifo/nr_evictions
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_evictions
0
HERE 
NAME:fifo
nr_evictions
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages 410203586
/blockstore/fifo/nr_pages
410203586
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages
410203586
HERE 
NAME:fifo
nr_pages
410203586
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_evictable 0
/blockstore/fifo/nr_pages_evictable
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_evictable
0
HERE 
NAME:fifo
nr_pages_evictable
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_evictable_unused 0
/blockstore/fifo/nr_pages_evictable_unused
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_evictable_unused
0
HERE 
NAME:fifo
nr_pages_evictable_unused
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_inuse 0
/blockstore/fifo/nr_pages_inuse
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_inuse
0
HERE 
NAME:fifo
nr_pages_inuse
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_pinnable 0
/blockstore/fifo/nr_pages_pinnable
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_pinnable
0
HERE 
NAME:fifo
nr_pages_pinnable
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_pinned 0
/blockstore/fifo/nr_pages_pinned
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_pinned
0
HERE 
NAME:fifo
nr_pages_pinned
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_unused 410203586
/blockstore/fifo/nr_pages_unused
410203586
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_unused
410203586
HERE 
NAME:fifo
nr_pages_unused
410203586
HERE 
Out BEFORE
/blockstore/fifo/nr_pinned_pages_used 0
/blockstore/fifo/nr_pinned_pages_used
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pinned_pages_used
0
HERE 
NAME:fifo
nr_pinned_pages_used
0
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used # blocks used in page
/blockstore/fifo/page_blocks_used # blocks used in
page
  max: 0 blocks

/blockstore/fifo/page_blocks_used/aggregate 0
/blockstore/fifo/page_blocks_used/aggregate
0
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/aggregate
0
HERE 
NAME:fifo
page_blocks_used/aggregate
0
HERE 
NAME:page_blocks_used
aggregate
0
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used/average NaN
/blockstore/fifo/page_blocks_used/average
NaN
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/average
nan
HERE 
NAME:fifo
page_blocks_used/average
nan
HERE 
NAME:page_blocks_used
average
nan
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used/nupdates 0
/blockstore/fifo/page_blocks_used/nupdates
0
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/nupdates
0
HERE 
NAME:fifo
page_blocks_used/nupdates
0
HERE 
NAME:page_blocks_used
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/stable_write_limit [LSN::INVALID]
/blockstore/fifo/stable_write_limit
[LSN::INVALID]
/blockstore/last_rebuild/cancelled_pages 0
/blockstore/last_rebuild/cancelled_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/cancelled_pages
0
HERE 
NAME:last_rebuild
cancelled_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/completed_pages 0
/blockstore/last_rebuild/completed_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/completed_pages
0
HERE 
NAME:last_rebuild
completed_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/fifo_completed_pages 0
/blockstore/last_rebuild/fifo_completed_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/fifo_completed_pages
0
HERE 
NAME:last_rebuild
fifo_completed_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/is_full_rebuild 0
/blockstore/last_rebuild/is_full_rebuild
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/is_full_rebuild
0
HERE 
NAME:last_rebuild
is_full_rebuild
0
HERE 
Out BEFORE
/blockstore/last_rebuild/r2l_time 0us
/blockstore/last_rebuild/r2l_time
0us
/blockstore/last_rebuild/start_time 
/blockstore/last_rebuild/start_time

/blockstore/last_rebuild/total_pages 4294967295
/blockstore/last_rebuild/total_pages
4294967295
In BEFORE
HERE 
NAME:blockstore
last_rebuild/total_pages
4294967295
HERE 
NAME:last_rebuild
total_pages
4294967295
HERE 
Out BEFORE
/blockstore/last_rebuild/total_time 0us
/blockstore/last_rebuild/total_time
0us
/blockstore/page_cache/nr_page_lookups 0
/blockstore/page_cache/nr_page_lookups
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups
0
HERE 
NAME:page_cache
nr_page_lookups
0
HERE 
Out BEFORE
/blockstore/page_cache/nr_page_lookups_absent 0
/blockstore/page_cache/nr_page_lookups_absent
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups_absent
0
HERE 
NAME:page_cache
nr_page_lookups_absent
0
HERE 
Out BEFORE
/blockstore/page_cache/nr_page_lookups_on_disk 0
/blockstore/page_cache/nr_page_lookups_on_disk
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups_on_disk
0
HERE 
NAME:page_cache
nr_page_lookups_on_disk
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal page alloc time - normal
/blockstore/page_cache/page_alloc_time_normal page alloc time -
normal
  max: 0 ms

/blockstore/page_cache/page_alloc_time_normal/aggregate 0
/blockstore/page_cache/page_alloc_time_normal/aggregate
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/aggregate
0
HERE 
NAME:page_cache
page_alloc_time_normal/aggregate
0
HERE 
NAME:page_alloc_time_normal
aggregate
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal/average NaN
/blockstore/page_cache/page_alloc_time_normal/average
NaN
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/average
nan
HERE 
NAME:page_cache
page_alloc_time_normal/average
nan
HERE 
NAME:page_alloc_time_normal
average
nan
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal/nupdates 0
/blockstore/page_cache/page_alloc_time_normal/nupdates
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/nupdates
0
HERE 
NAME:page_cache
page_alloc_time_normal/nupdates
0
HERE 
NAME:page_alloc_time_normal
nupdates
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued page alloc time - queued requests
/blockstore/page_cache/page_alloc_time_queued page alloc time - queued
requests
  max: 0 ms

/blockstore/page_cache/page_alloc_time_queued/aggregate 0
/blockstore/page_cache/page_alloc_time_queued/aggregate
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/aggregate
0
HERE 
NAME:page_cache
page_alloc_time_queued/aggregate
0
HERE 
NAME:page_alloc_time_queued
aggregate
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued/average NaN
/blockstore/page_cache/page_alloc_time_queued/average
NaN
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/average
nan
HERE 
NAME:page_cache
page_alloc_time_queued/average
nan
HERE 
NAME:page_alloc_time_queued
average
nan
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued/nupdates 0
/blockstore/page_cache/page_alloc_time_queued/nupdates
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/nupdates
0
HERE 
NAME:page_cache
page_alloc_time_queued/nupdates
0
HERE 
NAME:page_alloc_time_queued
nupdates
0
HERE 
Out BEFORE
/blockstore/page_cache/pages 617000
/blockstore/page_cache/pages
617000
In BEFORE
HERE 
NAME:blockstore
page_cache/pages
617000
HERE 
NAME:page_cache
pages
617000
HERE 
Out BEFORE
/blockstore/page_cache/pages_on_freelist 496
/blockstore/page_cache/pages_on_freelist
496
In BEFORE
HERE 
NAME:blockstore
page_cache/pages_on_freelist
496
HERE 
NAME:page_cache
pages_on_freelist
496
HERE 
Out BEFORE
/blockstore/page_cache/store_pages_in_mem 0
/blockstore/page_cache/store_pages_in_mem
0
In BEFORE
HERE 
NAME:blockstore
page_cache/store_pages_in_mem
0
HERE 
NAME:page_cache
store_pages_in_mem
0
HERE 
Out BEFORE
/blockstore/page_cache/stores_dropped 0
/blockstore/page_cache/stores_dropped
0
In BEFORE
HERE 
NAME:blockstore
page_cache/stores_dropped
0
HERE 
NAME:page_cache
stores_dropped
0
HERE 
Out BEFORE
/blockstore/phash/ha_unsynced_pages 0
/blockstore/phash/ha_unsynced_pages
0
In BEFORE
HERE 
NAME:blockstore
phash/ha_unsynced_pages
0
HERE 
NAME:phash
ha_unsynced_pages
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr 0
/blockstore/read/nr_blk_reads_usr
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr
0
HERE 
NAME:read
nr_blk_reads_usr
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr_other_hits 0
/blockstore/read/nr_blk_reads_usr_other_hits
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr_other_hits
0
HERE 
NAME:read
nr_blk_reads_usr_other_hits
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr_store_hits 0
/blockstore/read/nr_blk_reads_usr_store_hits
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr_store_hits
0
HERE 
NAME:read
nr_blk_reads_usr_store_hits
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user 0
/blockstore/read/nr_page_lookups_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user
0
HERE 
NAME:read
nr_page_lookups_user
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user_absent 0
/blockstore/read/nr_page_lookups_user_absent
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user_absent
0
HERE 
NAME:read
nr_page_lookups_user_absent
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user_on_disk 0
/blockstore/read/nr_page_lookups_user_on_disk
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user_on_disk
0
HERE 
NAME:read
nr_page_lookups_user_on_disk
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_disk 0
/blockstore/read/nr_page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_disk
0
HERE 
NAME:read
nr_page_reads_disk
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_disk_user 0
/blockstore/read/nr_page_reads_disk_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_disk_user
0
HERE 
NAME:read
nr_page_reads_disk_user
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_rdc_user 0
/blockstore/read/nr_page_reads_rdc_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_rdc_user
0
HERE 
NAME:read
nr_page_reads_rdc_user
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk no.of total disk reads (RDC + WBC) per user readOp
/blockstore/read/op_page_reads_disk no.of total disk reads (RDC + WBC) per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_disk/aggregate 0
/blockstore/read/op_page_reads_disk/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/aggregate
0
HERE 
NAME:read
op_page_reads_disk/aggregate
0
HERE 
NAME:op_page_reads_disk
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk/average NaN
/blockstore/read/op_page_reads_disk/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/average
nan
HERE 
NAME:read
op_page_reads_disk/average
nan
HERE 
NAME:op_page_reads_disk
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk/nupdates 0
/blockstore/read/op_page_reads_disk/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/nupdates
0
HERE 
NAME:read
op_page_reads_disk/nupdates
0
HERE 
NAME:op_page_reads_disk
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits no.of Read Cache hits per user readOp
/blockstore/read/op_page_reads_rdc_hits no.of Read Cache hits per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_rdc_hits/aggregate 0
/blockstore/read/op_page_reads_rdc_hits/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/aggregate
0
HERE 
NAME:read
op_page_reads_rdc_hits/aggregate
0
HERE 
NAME:op_page_reads_rdc_hits
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits/average NaN
/blockstore/read/op_page_reads_rdc_hits/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/average
nan
HERE 
NAME:read
op_page_reads_rdc_hits/average
nan
HERE 
NAME:op_page_reads_rdc_hits
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits/nupdates 0
/blockstore/read/op_page_reads_rdc_hits/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/nupdates
0
HERE 
NAME:read
op_page_reads_rdc_hits/nupdates
0
HERE 
NAME:op_page_reads_rdc_hits
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses no.of Read Cache misses per user readOp
/blockstore/read/op_page_reads_rdc_misses no.of Read Cache misses per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_rdc_misses/aggregate 0
/blockstore/read/op_page_reads_rdc_misses/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/aggregate
0
HERE 
NAME:read
op_page_reads_rdc_misses/aggregate
0
HERE 
NAME:op_page_reads_rdc_misses
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses/average NaN
/blockstore/read/op_page_reads_rdc_misses/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/average
nan
HERE 
NAME:read
op_page_reads_rdc_misses/average
nan
HERE 
NAME:op_page_reads_rdc_misses
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses/nupdates 0
/blockstore/read/op_page_reads_rdc_misses/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/nupdates
0
HERE 
NAME:read
op_page_reads_rdc_misses/nupdates
0
HERE 
NAME:op_page_reads_rdc_misses
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_total_time reads: total time taken
/blockstore/read/op_total_time reads: total time
taken
  max: 0 ms

/blockstore/read/op_total_time/aggregate 0
/blockstore/read/op_total_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/aggregate
0
HERE 
NAME:read
op_total_time/aggregate
0
HERE 
NAME:op_total_time
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_total_time/average NaN
/blockstore/read/op_total_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/average
nan
HERE 
NAME:read
op_total_time/average
nan
HERE 
NAME:op_total_time
average
nan
HERE 
Out BEFORE
/blockstore/read/op_total_time/nupdates 0
/blockstore/read/op_total_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/nupdates
0
HERE 
NAME:read
op_total_time/nupdates
0
HERE 
NAME:op_total_time
nupdates
0
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size Size of user read request not completely satisfied by Read Cache
/blockstore/read/rdc_misses_op_size Size of user read request not completely satisfied by Read
Cache
  max: 0 blocks

/blockstore/read/rdc_misses_op_size/aggregate 0
/blockstore/read/rdc_misses_op_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/aggregate
0
HERE 
NAME:read
rdc_misses_op_size/aggregate
0
HERE 
NAME:rdc_misses_op_size
aggregate
0
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size/average NaN
/blockstore/read/rdc_misses_op_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/average
nan
HERE 
NAME:read
rdc_misses_op_size/average
nan
HERE 
NAME:rdc_misses_op_size
average
nan
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size/nupdates 0
/blockstore/read/rdc_misses_op_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/nupdates
0
HERE 
NAME:read
rdc_misses_op_size/nupdates
0
HERE 
NAME:rdc_misses_op_size
nupdates
0
HERE 
Out BEFORE
/blockstore/read/reads_queued 0
/blockstore/read/reads_queued
0
In BEFORE
HERE 
NAME:blockstore
read/reads_queued
0
HERE 
NAME:read
reads_queued
0
HERE 
Out BEFORE
/blockstore/read_cache/last_flush_lsn [LSN::INVALID]
/blockstore/read_cache/last_flush_lsn
[LSN::INVALID]
/blockstore/read_cache/nr_readcache_hits 0
/blockstore/read_cache/nr_readcache_hits
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_hits
0
HERE 
NAME:read_cache
nr_readcache_hits
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_hits_user 0
/blockstore/read_cache/nr_readcache_hits_user
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_hits_user
0
HERE 
NAME:read_cache
nr_readcache_hits_user
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_misses 0
/blockstore/read_cache/nr_readcache_misses
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_misses
0
HERE 
NAME:read_cache
nr_readcache_misses
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_misses_user 0
/blockstore/read_cache/nr_readcache_misses_user
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_misses_user
0
HERE 
NAME:read_cache
nr_readcache_misses_user
0
HERE 
Out BEFORE
/blockstore/readahead/nr_hits 0
/blockstore/readahead/nr_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_hits
0
HERE 
NAME:readahead
nr_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_pages 0
/blockstore/readahead/nr_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_pages
0
HERE 
NAME:readahead
nr_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_fifo_seq_hits 0
/blockstore/readahead/nr_read_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_fifo_seq_hits
0
HERE 
NAME:readahead
nr_read_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_fifo_seq_pages 0
/blockstore/readahead/nr_read_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_fifo_seq_pages
0
HERE 
NAME:readahead
nr_read_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_fifo_seq_hits 0
/blockstore/readahead/nr_read_lba_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_fifo_seq_hits
0
HERE 
NAME:readahead
nr_read_lba_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_fifo_seq_pages 0
/blockstore/readahead/nr_read_lba_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_fifo_seq_pages
0
HERE 
NAME:readahead
nr_read_lba_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_seq_hits 0
/blockstore/readahead/nr_read_lba_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_seq_hits
0
HERE 
NAME:readahead
nr_read_lba_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_seq_pages 0
/blockstore/readahead/nr_read_lba_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_seq_pages
0
HERE 
NAME:readahead
nr_read_lba_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_fifo_seq_hits 0
/blockstore/readahead/nr_write_merge_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_fifo_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_fifo_seq_pages 0
/blockstore/readahead/nr_write_merge_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_fifo_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_fifo_seq_hits 0
/blockstore/readahead/nr_write_merge_lba_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_fifo_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_lba_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_fifo_seq_pages 0
/blockstore/readahead/nr_write_merge_lba_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_fifo_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_lba_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_seq_hits 0
/blockstore/readahead/nr_write_merge_lba_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_lba_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_seq_pages 0
/blockstore/readahead/nr_write_merge_lba_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_lba_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_ read-ahead:(read, fifo seq) page hit postion
/blockstore/readahead/read_fifo_seq_hit_page_ read-ahead:(read, fifo seq) page hit
postion
  max: 0 pages

/blockstore/readahead/read_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/read_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:read_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_/average NaN
/blockstore/readahead/read_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_fifo_seq_hit_page_/average
nan
HERE 
NAME:read_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/read_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:read_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_ read-ahead:(read, lba& fifo seq)  page hit postion
/blockstore/readahead/read_lba_fifo_seq_hit_page_ read-ahead:(read, lba& fifo seq)  page hit
postion
  max: 0 pages

/blockstore/readahead/read_lba_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/read_lba_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:read_lba_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_/average NaN
/blockstore/readahead/read_lba_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:read_lba_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/read_lba_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:read_lba_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_ read-ahead:(read, lba seq) page hit postion
/blockstore/readahead/read_lba_seq_hit_page_ read-ahead:(read, lba seq) page hit
postion
  max: 0 pages

/blockstore/readahead/read_lba_seq_hit_page_/aggregate 0
/blockstore/readahead/read_lba_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_lba_seq_hit_page_/aggregate
0
HERE 
NAME:read_lba_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_/average NaN
/blockstore/readahead/read_lba_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_lba_seq_hit_page_/average
nan
HERE 
NAME:read_lba_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_/nupdates 0
/blockstore/readahead/read_lba_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_lba_seq_hit_page_/nupdates
0
HERE 
NAME:read_lba_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_ read-ahead:(write_merge, fifo seq) page hit postion
/blockstore/readahead/write_merge_fifo_seq_hit_page_ read-ahead:(write_merge, fifo seq) page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/average
nan
HERE 
NAME:write_merge_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_ read-ahead:(write_merge,lba& fifo seq)  page hit postion
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_ read-ahead:(write_merge,lba& fifo seq)  page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_ read-ahead:(write_merge, lba seq) page hit postion
/blockstore/readahead/write_merge_lba_seq_hit_page_ read-ahead:(write_merge, lba seq) page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_lba_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_lba_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_lba_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_lba_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/average
nan
HERE 
NAME:write_merge_lba_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_lba_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_lba_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op Number of pages in a batchIO of write op
/blockstore/wbcache/batch_size_write_op Number of pages in a batchIO of write
op
195746289 : 1
  max: 1 pages
      Aggregate : 195746289 pages. Avg size : 1
/blockstore/wbcache/batch_size_write_op/aggregate 195746290
/blockstore/wbcache/batch_size_write_op/aggregate
195746290
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/aggregate
195746290
HERE 
NAME:wbcache
batch_size_write_op/aggregate
195746290
HERE 
NAME:batch_size_write_op
aggregate
195746290
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op/average 1
/blockstore/wbcache/batch_size_write_op/average
1
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/average
1
HERE 
NAME:wbcache
batch_size_write_op/average
1
HERE 
NAME:batch_size_write_op
average
1
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op/nupdates 195746290
/blockstore/wbcache/batch_size_write_op/nupdates
195746290
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/nupdates
195746290
HERE 
NAME:wbcache
batch_size_write_op/nupdates
195746290
HERE 
NAME:batch_size_write_op
nupdates
195746290
HERE 
Out BEFORE
/blockstore/wbcache/last_hdd_write [171:892719]
/blockstore/wbcache/last_hdd_write
[171:892719]
/blockstore/wbcache/last_persistent_hdd_write [171:815617]
/blockstore/wbcache/last_persistent_hdd_write
[171:815617]
/blockstore/wbcache/last_persistent_hdd_write_on_disk [171:815617]
/blockstore/wbcache/last_persistent_hdd_write_on_disk
[171:815617]
/blockstore/wbcache/last_ssd_write [171:920509]
/blockstore/wbcache/last_ssd_write
[171:920509]
/blockstore/wbcache/last_ssd_write_on_disk [171:916143]
/blockstore/wbcache/last_ssd_write_on_disk
[171:916143]
/blockstore/wbcache/nr_disk_fixes 0
/blockstore/wbcache/nr_disk_fixes
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes
0
HERE 
NAME:wbcache
nr_disk_fixes
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_fixes_fail 0
/blockstore/wbcache/nr_disk_fixes_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes_fail
0
HERE 
NAME:wbcache
nr_disk_fixes_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_fixes_success 0
/blockstore/wbcache/nr_disk_fixes_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes_success
0
HERE 
NAME:wbcache
nr_disk_fixes_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs 0
/blockstore/wbcache/nr_disk_scrubs
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs
0
HERE 
NAME:wbcache
nr_disk_scrubs
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs_fail 0
/blockstore/wbcache/nr_disk_scrubs_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs_fail
0
HERE 
NAME:wbcache
nr_disk_scrubs_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs_success 0
/blockstore/wbcache/nr_disk_scrubs_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs_success
0
HERE 
NAME:wbcache
nr_disk_scrubs_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_read_retries_ssd 0
/blockstore/wbcache/nr_page_read_retries_ssd
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_read_retries_ssd
0
HERE 
NAME:wbcache
nr_page_read_retries_ssd
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_reads 6
/blockstore/wbcache/nr_page_reads
6
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_reads
6
HERE 
NAME:wbcache
nr_page_reads
6
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_reads_ssd 4
/blockstore/wbcache/nr_page_reads_ssd
4
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_reads_ssd
4
HERE 
NAME:wbcache
nr_page_reads_ssd
4
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_writes 195746290
/blockstore/wbcache/nr_page_writes
195746290
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_writes
195746290
HERE 
NAME:wbcache
nr_page_writes
195746290
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes 0
/blockstore/wbcache/nr_ssd_fixes
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes
0
HERE 
NAME:wbcache
nr_ssd_fixes
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes_fail 0
/blockstore/wbcache/nr_ssd_fixes_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes_fail
0
HERE 
NAME:wbcache
nr_ssd_fixes_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes_success 0
/blockstore/wbcache/nr_ssd_fixes_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes_success
0
HERE 
NAME:wbcache
nr_ssd_fixes_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs 0
/blockstore/wbcache/nr_ssd_scrubs
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs
0
HERE 
NAME:wbcache
nr_ssd_scrubs
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs_fail 0
/blockstore/wbcache/nr_ssd_scrubs_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs_fail
0
HERE 
NAME:wbcache
nr_ssd_scrubs_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs_success 0
/blockstore/wbcache/nr_ssd_scrubs_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs_success
0
HERE 
NAME:wbcache
nr_ssd_scrubs_success
0
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd write op ssd time
/blockstore/wbcache/op_write_time_ssd write op ssd
time
1207186 : 0
 339296 : 1
 265516 : 2
 480085 : 3-4
 916679 : 5-8
2159662 : 9-16
4778775 : 17-32
27312470 : 33-64
157069866 : 65-128
1154621 : 129-256
  60256 : 257-512
    341 : 513-1K
     24 : 1K-2K
     12 : 2K-4K
    356 : 4K-8K
  max: 5038 ms
      Aggregate : 14312073765 ms. Avg size : 73.1159
/blockstore/wbcache/op_write_time_ssd/aggregate 14312073765
/blockstore/wbcache/op_write_time_ssd/aggregate
14312073765
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/aggregate
14312073765
HERE 
NAME:wbcache
op_write_time_ssd/aggregate
14312073765
HERE 
NAME:op_write_time_ssd
aggregate
14312073765
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd/average 73.1159
/blockstore/wbcache/op_write_time_ssd/average
73.1159
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/average
73.1159
HERE 
NAME:wbcache
op_write_time_ssd/average
73.1159
HERE 
NAME:op_write_time_ssd
average
73.1159
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd/nupdates 195745145
/blockstore/wbcache/op_write_time_ssd/nupdates
195745145
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/nupdates
195745145
HERE 
NAME:wbcache
op_write_time_ssd/nupdates
195745145
HERE 
NAME:op_write_time_ssd
nupdates
195745145
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total write op total time
/blockstore/wbcache/op_write_time_total write op total
time
1131782 : 0
 351300 : 1
 258642 : 2
 465367 : 3-4
 885229 : 5-8
1754655 : 9-16
4319820 : 17-32
25814472 : 33-64
159067799 : 65-128
1455758 : 129-256
 234246 : 257-512
   5539 : 513-1K
    168 : 1K-2K
     12 : 2K-4K
    356 : 4K-8K
  max: 5249 ms
      Aggregate : 14513888407 ms. Avg size : 74.1469
/blockstore/wbcache/op_write_time_total/aggregate 14513888407
/blockstore/wbcache/op_write_time_total/aggregate
14513888407
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/aggregate
14513888407
HERE 
NAME:wbcache
op_write_time_total/aggregate
14513888407
HERE 
NAME:op_write_time_total
aggregate
14513888407
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total/average 74.1469
/blockstore/wbcache/op_write_time_total/average
74.1469
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/average
74.1469
HERE 
NAME:wbcache
op_write_time_total/average
74.1469
HERE 
NAME:op_write_time_total
average
74.1469
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total/nupdates 195745145
/blockstore/wbcache/op_write_time_total/nupdates
195745145
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/nupdates
195745145
HERE 
NAME:wbcache
op_write_time_total/nupdates
195745145
HERE 
NAME:op_write_time_total
nupdates
195745145
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk read op hdd time
/blockstore/wbcache/page_read_time_disk read op hdd
time
      2 : 17-32
  max: 22 ms
      Aggregate : 41 ms. Avg size : 20.5
/blockstore/wbcache/page_read_time_disk/aggregate 41
/blockstore/wbcache/page_read_time_disk/aggregate
41
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/aggregate
41
HERE 
NAME:wbcache
page_read_time_disk/aggregate
41
HERE 
NAME:page_read_time_disk
aggregate
41
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk/average 20.5
/blockstore/wbcache/page_read_time_disk/average
20.5
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/average
20.5
HERE 
NAME:wbcache
page_read_time_disk/average
20.5
HERE 
NAME:page_read_time_disk
average
20.5
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk/nupdates 2
/blockstore/wbcache/page_read_time_disk/nupdates
2
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/nupdates
2
HERE 
NAME:wbcache
page_read_time_disk/nupdates
2
HERE 
NAME:page_read_time_disk
nupdates
2
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd read op ssd time
/blockstore/wbcache/page_read_time_ssd read op ssd
time
      2 : 0
      1 : 5-8
      1 : 9-16
  max: 14 ms
      Aggregate : 21 ms. Avg size : 5.25
/blockstore/wbcache/page_read_time_ssd/aggregate 21
/blockstore/wbcache/page_read_time_ssd/aggregate
21
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/aggregate
21
HERE 
NAME:wbcache
page_read_time_ssd/aggregate
21
HERE 
NAME:page_read_time_ssd
aggregate
21
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd/average 5.25
/blockstore/wbcache/page_read_time_ssd/average
5.25
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/average
5.25
HERE 
NAME:wbcache
page_read_time_ssd/average
5.25
HERE 
NAME:page_read_time_ssd
average
5.25
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd/nupdates 4
/blockstore/wbcache/page_read_time_ssd/nupdates
4
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/nupdates
4
HERE 
NAME:wbcache
page_read_time_ssd/nupdates
4
HERE 
NAME:page_read_time_ssd
nupdates
4
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total read op total time
/blockstore/wbcache/page_read_time_total read op total
time
      2 : 0
      1 : 9-16
      3 : 17-32
  max: 25 ms
      Aggregate : 83 ms. Avg size : 13.8333
/blockstore/wbcache/page_read_time_total/aggregate 83
/blockstore/wbcache/page_read_time_total/aggregate
83
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/aggregate
83
HERE 
NAME:wbcache
page_read_time_total/aggregate
83
HERE 
NAME:page_read_time_total
aggregate
83
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total/average 13.8333
/blockstore/wbcache/page_read_time_total/average
13.8333
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/average
13.8333
HERE 
NAME:wbcache
page_read_time_total/average
13.8333
HERE 
NAME:page_read_time_total
average
13.8333
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total/nupdates 6
/blockstore/wbcache/page_read_time_total/nupdates
6
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/nupdates
6
HERE 
NAME:wbcache
page_read_time_total/nupdates
6
HERE 
NAME:page_read_time_total
nupdates
6
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_slice 3
/blockstore/wbcache/pages_per_slice
3
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_slice
3
HERE 
NAME:wbcache
pages_per_slice
3
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op count of pages per write op
/blockstore/wbcache/pages_per_write_op count of pages per write
op
195746291 : 1
  max: 1 pages
      Aggregate : 195746291 pages. Avg size : 1
/blockstore/wbcache/pages_per_write_op/aggregate 195746291
/blockstore/wbcache/pages_per_write_op/aggregate
195746291
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/aggregate
195746291
HERE 
NAME:wbcache
pages_per_write_op/aggregate
195746291
HERE 
NAME:pages_per_write_op
aggregate
195746291
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op/average 1
/blockstore/wbcache/pages_per_write_op/average
1
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/average
1
HERE 
NAME:wbcache
pages_per_write_op/average
1
HERE 
NAME:pages_per_write_op
average
1
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op/nupdates 195746291
/blockstore/wbcache/pages_per_write_op/nupdates
195746291
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/nupdates
195746291
HERE 
NAME:wbcache
pages_per_write_op/nupdates
195746291
HERE 
NAME:pages_per_write_op
nupdates
195746291
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_dirty_offsets_length 390
/blockstore/wbcache/processor/avg_dirty_offsets_length
390
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_dirty_offsets_length
390
HERE 
NAME:wbcache
processor/avg_dirty_offsets_length
390
HERE 
NAME:processor
avg_dirty_offsets_length
390
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_sync_time 0
/blockstore/wbcache/processor/avg_sync_time
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_sync_time
0
HERE 
NAME:wbcache
processor/avg_sync_time
0
HERE 
NAME:processor
avg_sync_time
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_trim_length 0
/blockstore/wbcache/processor/avg_trim_length
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_trim_length
0
HERE 
NAME:wbcache
processor/avg_trim_length
0
HERE 
NAME:processor
avg_trim_length
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/buffer_id 41407808
/blockstore/wbcache/processor/buffer_id
41407808
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/buffer_id
41407808
HERE 
NAME:wbcache
processor/buffer_id
41407808
HERE 
NAME:processor
buffer_id
41407808
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time How long it took to write a page to hdd
/blockstore/wbcache/processor/hdd_write_time How long it took to write a page to
hdd
   7849 : 0
1529737 : 1
20104217 : 2
117069890 : 3-4
12206493 : 5-8
12897813 : 9-16
14792487 : 17-32
11674005 : 33-64
4284801 : 65-128
 846232 : 129-256
 326409 : 257-512
   4958 : 513-1K
  max: 805 ms
      Aggregate : 2158091826 ms. Avg size : 11.025
/blockstore/wbcache/processor/hdd_write_time/aggregate 2158091826
/blockstore/wbcache/processor/hdd_write_time/aggregate
2158091826
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/aggregate
2158091826
HERE 
NAME:wbcache
processor/hdd_write_time/aggregate
2158091826
HERE 
NAME:processor
hdd_write_time/aggregate
2158091826
HERE 
NAME:hdd_write_time
aggregate
2158091826
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time/average 11.025
/blockstore/wbcache/processor/hdd_write_time/average
11.025
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/average
11.025
HERE 
NAME:wbcache
processor/hdd_write_time/average
11.025
HERE 
NAME:processor
hdd_write_time/average
11.025
HERE 
NAME:hdd_write_time
average
11.025
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time/nupdates 195744891
/blockstore/wbcache/processor/hdd_write_time/nupdates
195744891
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/nupdates
195744891
HERE 
NAME:wbcache
processor/hdd_write_time/nupdates
195744891
HERE 
NAME:processor
hdd_write_time/nupdates
195744891
HERE 
NAME:hdd_write_time
nupdates
195744891
HERE 
Out BEFORE
/blockstore/wbcache/processor/max_dirty_offsets_length 12226
/blockstore/wbcache/processor/max_dirty_offsets_length
12226
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/max_dirty_offsets_length
12226
HERE 
NAME:wbcache
processor/max_dirty_offsets_length
12226
HERE 
NAME:processor
max_dirty_offsets_length
12226
HERE 
Out BEFORE
/blockstore/wbcache/processor/nr_pages_read 195745052
/blockstore/wbcache/processor/nr_pages_read
195745052
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/nr_pages_read
195745052
HERE 
NAME:wbcache
processor/nr_pages_read
195745052
HERE 
NAME:processor
nr_pages_read
195745052
HERE 
Out BEFORE
/blockstore/wbcache/processor/nr_pages_read_in_mem 194943844
/blockstore/wbcache/processor/nr_pages_read_in_mem
194943844
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/nr_pages_read_in_mem
194943844
HERE 
NAME:wbcache
processor/nr_pages_read_in_mem
194943844
HERE 
NAME:processor
nr_pages_read_in_mem
194943844
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time How long it took to free up pages
/blockstore/wbcache/processor/page_free_time How long it took to free up
pages
     10 : 3-4
     48 : 5-8
    124 : 9-16
    194 : 17-32
    392 : 33-64
    664 : 65-128
    981 : 129-256
   1063 : 257-512
   1082 : 513-1K
   1275 : 1K-2K
    577 : 2K-4K
      7 : 4K-8K
  max: 4543 ms
      Aggregate : 4784531 ms. Avg size : 745.602
/blockstore/wbcache/processor/page_free_time/aggregate 4784531
/blockstore/wbcache/processor/page_free_time/aggregate
4784531
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/aggregate
4784531
HERE 
NAME:wbcache
processor/page_free_time/aggregate
4784531
HERE 
NAME:processor
page_free_time/aggregate
4784531
HERE 
NAME:page_free_time
aggregate
4784531
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time/average 745.602
/blockstore/wbcache/processor/page_free_time/average
745.602
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/average
745.602
HERE 
NAME:wbcache
processor/page_free_time/average
745.602
HERE 
NAME:processor
page_free_time/average
745.602
HERE 
NAME:page_free_time
average
745.602
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time/nupdates 6417
/blockstore/wbcache/processor/page_free_time/nupdates
6417
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/nupdates
6417
HERE 
NAME:wbcache
processor/page_free_time/nupdates
6417
HERE 
NAME:processor
page_free_time/nupdates
6417
HERE 
NAME:page_free_time
nupdates
6417
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_reads 0
/blockstore/wbcache/processor/pending_reads
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_reads
0
HERE 
NAME:wbcache
processor/pending_reads
0
HERE 
NAME:processor
pending_reads
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes # write io requests pending at disk, updated after issuing a write request to disk
 210689 : 1
 203436 : 2
 444581 : 3-4
1078548 : 5-8
3118454 : 9-16
15241033 : 17-32
79877642 : 33-64
30150623 : 65-128
21716270 : 129-256
21358793 : 257-512
22344983 : 513-1K
  max: 976 requests
      Aggregate : 36022364831 requests. Avg size : 184.027
/blockstore/wbcache/processor/pending_writes 161
/blockstore/wbcache/processor/pending_writes/aggregate 36022364831
/blockstore/wbcache/processor/pending_writes/aggregate
36022364831
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/aggregate
36022364831
HERE 
NAME:wbcache
processor/pending_writes/aggregate
36022364831
HERE 
NAME:processor
pending_writes/aggregate
36022364831
HERE 
NAME:pending_writes
aggregate
36022364831
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes/average 184.027
/blockstore/wbcache/processor/pending_writes/average
184.027
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/average
184.027
HERE 
NAME:wbcache
processor/pending_writes/average
184.027
HERE 
NAME:processor
pending_writes/average
184.027
HERE 
NAME:pending_writes
average
184.027
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes/nupdates 195745052
/blockstore/wbcache/processor/pending_writes/nupdates
195745052
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/nupdates
195745052
HERE 
NAME:wbcache
processor/pending_writes/nupdates
195745052
HERE 
NAME:processor
pending_writes/nupdates
195745052
HERE 
NAME:pending_writes
nupdates
195745052
HERE 
Out BEFORE
/blockstore/wbcache/processor/read_iops 13599
/blockstore/wbcache/processor/read_iops
13599
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/read_iops
13599
HERE 
NAME:wbcache
processor/read_iops
13599
HERE 
NAME:processor
read_iops
13599
HERE 
Out BEFORE
/blockstore/wbcache/processor/read_throughput 118366328
/blockstore/wbcache/processor/read_throughput
118366328
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/read_throughput
118366328
HERE 
NAME:wbcache
processor/read_throughput
118366328
HERE 
NAME:processor
read_throughput
118366328
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time How long it took to read a page from ssd
/blockstore/wbcache/processor/ssd_read_time How long it took to read a page from
ssd
   1960 : 0
   3803 : 1
   2822 : 2
   9859 : 3-4
  24026 : 5-8
  55418 : 9-16
 258201 : 17-32
 113261 : 33-64
 197854 : 65-128
 134004 : 129-256
  max: 208 ms
      Aggregate : 52904739 ms. Avg size : 66.0312
/blockstore/wbcache/processor/ssd_read_time/aggregate 52904739
/blockstore/wbcache/processor/ssd_read_time/aggregate
52904739
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/aggregate
52904739
HERE 
NAME:wbcache
processor/ssd_read_time/aggregate
52904739
HERE 
NAME:processor
ssd_read_time/aggregate
52904739
HERE 
NAME:ssd_read_time
aggregate
52904739
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time/average 66.0312
/blockstore/wbcache/processor/ssd_read_time/average
66.0312
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/average
66.0312
HERE 
NAME:wbcache
processor/ssd_read_time/average
66.0312
HERE 
NAME:processor
ssd_read_time/average
66.0312
HERE 
NAME:ssd_read_time
average
66.0312
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time/nupdates 801208
/blockstore/wbcache/processor/ssd_read_time/nupdates
801208
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/nupdates
801208
HERE 
NAME:wbcache
processor/ssd_read_time/nupdates
801208
HERE 
NAME:processor
ssd_read_time/nupdates
801208
HERE 
NAME:ssd_read_time
nupdates
801208
HERE 
Out BEFORE
/blockstore/wbcache/processor/write_iops 13599
/blockstore/wbcache/processor/write_iops
13599
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/write_iops
13599
HERE 
NAME:wbcache
processor/write_iops
13599
HERE 
NAME:processor
write_iops
13599
HERE 
Out BEFORE
/blockstore/wbcache/processor/write_throughput 118366231
/blockstore/wbcache/processor/write_throughput
118366231
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/write_throughput
118366231
HERE 
NAME:wbcache
processor/write_throughput
118366231
HERE 
NAME:processor
write_throughput
118366231
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time read op queued time
/blockstore/wbcache/read_queued_time read op queued
time
      3 : 0
      1 : 3-4
      1 : 5-8
      1 : 9-16
  max: 9 ms
      Aggregate : 20 ms. Avg size : 3.33333
/blockstore/wbcache/read_queued_time/aggregate 20
/blockstore/wbcache/read_queued_time/aggregate
20
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/aggregate
20
HERE 
NAME:wbcache
read_queued_time/aggregate
20
HERE 
NAME:read_queued_time
aggregate
20
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time/average 3.33333
/blockstore/wbcache/read_queued_time/average
3.33333
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/average
3.33333
HERE 
NAME:wbcache
read_queued_time/average
3.33333
HERE 
NAME:read_queued_time
average
3.33333
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time/nupdates 6
/blockstore/wbcache/read_queued_time/nupdates
6
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/nupdates
6
HERE 
NAME:wbcache
read_queued_time/nupdates
6
HERE 
NAME:read_queued_time
nupdates
6
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful total unsuccessful page read time
/blockstore/wbcache/total_page_read_time_unsuccessful total unsuccessful page read
time
  max: 0 ms

/blockstore/wbcache/total_page_read_time_unsuccessful/aggregate 0
/blockstore/wbcache/total_page_read_time_unsuccessful/aggregate
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/aggregate
0
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/aggregate
0
HERE 
NAME:total_page_read_time_unsuccessful
aggregate
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful/average NaN
/blockstore/wbcache/total_page_read_time_unsuccessful/average
NaN
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/average
nan
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/average
nan
HERE 
NAME:total_page_read_time_unsuccessful
average
nan
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful/nupdates 0
/blockstore/wbcache/total_page_read_time_unsuccessful/nupdates
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/nupdates
0
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/nupdates
0
HERE 
NAME:total_page_read_time_unsuccessful
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful total unsuccessful page write time
/blockstore/wbcache/total_page_write_time_unsuccessful total unsuccessful page write
time
  max: 0 ms

/blockstore/wbcache/total_page_write_time_unsuccessful/aggregate 0
/blockstore/wbcache/total_page_write_time_unsuccessful/aggregate
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/aggregate
0
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/aggregate
0
HERE 
NAME:total_page_write_time_unsuccessful
aggregate
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful/average NaN
/blockstore/wbcache/total_page_write_time_unsuccessful/average
NaN
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/average
nan
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/average
nan
HERE 
NAME:total_page_write_time_unsuccessful
average
nan
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful/nupdates 0
/blockstore/wbcache/total_page_write_time_unsuccessful/nupdates
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/nupdates
0
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/nupdates
0
HERE 
NAME:total_page_write_time_unsuccessful
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/wbc_version 5
/blockstore/wbcache/wbc_version
5
In BEFORE
HERE 
NAME:blockstore
wbcache/wbc_version
5
HERE 
NAME:wbcache
wbc_version
5
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time write op queued time
/blockstore/wbcache/write_queued_time write op queued
time
195746290 : 0
      2 : 1
  max: 1 ms
      Aggregate : 2 ms. Avg size : 1.02173e-08
/blockstore/wbcache/write_queued_time/aggregate 2
/blockstore/wbcache/write_queued_time/aggregate
2
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/aggregate
2
HERE 
NAME:wbcache
write_queued_time/aggregate
2
HERE 
NAME:write_queued_time
aggregate
2
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time/average 1.02173e-08
/blockstore/wbcache/write_queued_time/average
1.02173e-08
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/average
1.02173e-08
HERE 
NAME:wbcache
write_queued_time/average
1.02173e-08
HERE 
NAME:write_queued_time
average
1.02173e-08
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time/nupdates 195746292
/blockstore/wbcache/write_queued_time/nupdates
195746292
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/nupdates
195746292
HERE 
NAME:wbcache
write_queued_time/nupdates
195746292
HERE 
NAME:write_queued_time
nupdates
195746292
HERE 
Out BEFORE
/blockstore/workload/pending_pages # user io pages pending when a user read/write req is received
/blockstore/workload/pending_pages # user io pages pending when a user read/write req is
received
  max: 0 pages

/blockstore/workload/pending_pages/aggregate 0
/blockstore/workload/pending_pages/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/aggregate
0
HERE 
NAME:workload
pending_pages/aggregate
0
HERE 
NAME:pending_pages
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/pending_pages/average NaN
/blockstore/workload/pending_pages/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/average
nan
HERE 
NAME:workload
pending_pages/average
nan
HERE 
NAME:pending_pages
average
nan
HERE 
Out BEFORE
/blockstore/workload/pending_pages/nupdates 0
/blockstore/workload/pending_pages/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/nupdates
0
HERE 
NAME:workload
pending_pages/nupdates
0
HERE 
NAME:pending_pages
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/pending_requests # user io requests pending when a user read/write req is received
/blockstore/workload/pending_requests # user io requests pending when a user read/write req is
received
  max: 0 requests

/blockstore/workload/pending_requests/aggregate 0
/blockstore/workload/pending_requests/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/aggregate
0
HERE 
NAME:workload
pending_requests/aggregate
0
HERE 
NAME:pending_requests
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/pending_requests/average NaN
/blockstore/workload/pending_requests/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/average
nan
HERE 
NAME:workload
pending_requests/average
nan
HERE 
NAME:pending_requests
average
nan
HERE 
Out BEFORE
/blockstore/workload/pending_requests/nupdates 0
/blockstore/workload/pending_requests/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/nupdates
0
HERE 
NAME:workload
pending_requests/nupdates
0
HERE 
NAME:pending_requests
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/readop_size size of user read request
/blockstore/workload/readop_size size of user read
request
  max: 0 blocks

/blockstore/workload/readop_size/aggregate 0
/blockstore/workload/readop_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/aggregate
0
HERE 
NAME:workload
readop_size/aggregate
0
HERE 
NAME:readop_size
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/readop_size/average NaN
/blockstore/workload/readop_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/average
nan
HERE 
NAME:workload
readop_size/average
nan
HERE 
NAME:readop_size
average
nan
HERE 
Out BEFORE
/blockstore/workload/readop_size/nupdates 0
/blockstore/workload/readop_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/nupdates
0
HERE 
NAME:workload
readop_size/nupdates
0
HERE 
NAME:readop_size
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/writeop_size write request size
/blockstore/workload/writeop_size write request
size
  max: 0 blocks

/blockstore/workload/writeop_size/aggregate 0
/blockstore/workload/writeop_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/aggregate
0
HERE 
NAME:workload
writeop_size/aggregate
0
HERE 
NAME:writeop_size
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/writeop_size/average NaN
/blockstore/workload/writeop_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/average
nan
HERE 
NAME:workload
writeop_size/average
nan
HERE 
NAME:writeop_size
average
nan
HERE 
Out BEFORE
/blockstore/workload/writeop_size/nupdates 0
/blockstore/workload/writeop_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/nupdates
0
HERE 
NAME:workload
writeop_size/nupdates
0
HERE 
NAME:writeop_size
nupdates
0
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs Superseded offset count blocked by the pending superseding page write
/blockstore/write/dirty_superseded_offs Superseded offset count blocked by the pending superseding page
write
  max: 0 offsets

/blockstore/write/dirty_superseded_offs/aggregate 0
/blockstore/write/dirty_superseded_offs/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/aggregate
0
HERE 
NAME:write
dirty_superseded_offs/aggregate
0
HERE 
NAME:dirty_superseded_offs
aggregate
0
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs/average NaN
/blockstore/write/dirty_superseded_offs/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/average
nan
HERE 
NAME:write
dirty_superseded_offs/average
nan
HERE 
NAME:dirty_superseded_offs
average
nan
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs/nupdates 0
/blockstore/write/dirty_superseded_offs/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/nupdates
0
HERE 
NAME:write
dirty_superseded_offs/nupdates
0
HERE 
NAME:dirty_superseded_offs
nupdates
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes 19356165132
/blockstore/write/nr_blk_writes
19356165132
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes
19356165132
HERE 
NAME:write
nr_blk_writes
19356165132
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_and_stores 0
/blockstore/write/nr_blk_writes_and_stores
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_and_stores
0
HERE 
NAME:write
nr_blk_writes_and_stores
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_in_mem 0
/blockstore/write/nr_blk_writes_in_mem
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_in_mem
0
HERE 
NAME:write
nr_blk_writes_in_mem
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_inherited 0
/blockstore/write/nr_blk_writes_inherited
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_inherited
0
HERE 
NAME:write
nr_blk_writes_inherited
0
HERE 
Out BEFORE
/blockstore/write/nr_page_reads_disk_store 0
/blockstore/write/nr_page_reads_disk_store
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_reads_disk_store
0
HERE 
NAME:write
nr_page_reads_disk_store
0
HERE 
Out BEFORE
/blockstore/write/nr_page_reads_rdc_store 0
/blockstore/write/nr_page_reads_rdc_store
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_reads_rdc_store
0
HERE 
NAME:write
nr_page_reads_rdc_store
0
HERE 
Out BEFORE
/blockstore/write/nr_page_stores 0
/blockstore/write/nr_page_stores
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_stores
0
HERE 
NAME:write
nr_page_stores
0
HERE 
Out BEFORE
/blockstore/write/nr_page_stores_denied_ 0
/blockstore/write/nr_page_stores_denied_
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_stores_denied_
0
HERE 
NAME:write
nr_page_stores_denied_
0
HERE 
Out BEFORE
/blockstore/write/nr_page_writes 0
/blockstore/write/nr_page_writes
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_writes
0
HERE 
NAME:write
nr_page_writes
0
HERE 
Out BEFORE
/blockstore/write/nr_page_writes_pending 0
/blockstore/write/nr_page_writes_pending
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_writes_pending
0
HERE 
NAME:write
nr_page_writes_pending
0
HERE 
Out BEFORE
/blockstore/write/nr_pages_partial 0
/blockstore/write/nr_pages_partial
0
In BEFORE
HERE 
NAME:blockstore
write/nr_pages_partial
0
HERE 
NAME:write
nr_pages_partial
0
HERE 
Out BEFORE
/blockstore/write/nr_pages_superseded 0
/blockstore/write/nr_pages_superseded
0
In BEFORE
HERE 
NAME:blockstore
write/nr_pages_superseded
0
HERE 
NAME:write
nr_pages_superseded
0
HERE 
Out BEFORE
/blockstore/write/op_page_alloc writes: time taken for page alloc
/blockstore/write/op_page_alloc writes: time taken for page
alloc
  max: 0 ms

/blockstore/write/op_page_alloc/aggregate 0
/blockstore/write/op_page_alloc/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/aggregate
0
HERE 
NAME:write
op_page_alloc/aggregate
0
HERE 
NAME:op_page_alloc
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_page_alloc/average NaN
/blockstore/write/op_page_alloc/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/average
nan
HERE 
NAME:write
op_page_alloc/average
nan
HERE 
NAME:op_page_alloc
average
nan
HERE 
Out BEFORE
/blockstore/write/op_page_alloc/nupdates 0
/blockstore/write/op_page_alloc/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/nupdates
0
HERE 
NAME:write
op_page_alloc/nupdates
0
HERE 
NAME:op_page_alloc
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_queued_time writes: time waiting in queue for turn
/blockstore/write/op_queued_time writes: time waiting in queue for
turn
  max: 0 ms

/blockstore/write/op_queued_time/aggregate 0
/blockstore/write/op_queued_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/aggregate
0
HERE 
NAME:write
op_queued_time/aggregate
0
HERE 
NAME:op_queued_time
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_queued_time/average NaN
/blockstore/write/op_queued_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/average
nan
HERE 
NAME:write
op_queued_time/average
nan
HERE 
NAME:op_queued_time
average
nan
HERE 
Out BEFORE
/blockstore/write/op_queued_time/nupdates 0
/blockstore/write/op_queued_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/nupdates
0
HERE 
NAME:write
op_queued_time/nupdates
0
HERE 
NAME:op_queued_time
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge writes: time taken for read and merge
/blockstore/write/op_read_n_merge writes: time taken for read and
merge
  max: 0 ms

/blockstore/write/op_read_n_merge/aggregate 0
/blockstore/write/op_read_n_merge/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/aggregate
0
HERE 
NAME:write
op_read_n_merge/aggregate
0
HERE 
NAME:op_read_n_merge
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge/average NaN
/blockstore/write/op_read_n_merge/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/average
nan
HERE 
NAME:write
op_read_n_merge/average
nan
HERE 
NAME:op_read_n_merge
average
nan
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge/nupdates 0
/blockstore/write/op_read_n_merge/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/nupdates
0
HERE 
NAME:write
op_read_n_merge/nupdates
0
HERE 
NAME:op_read_n_merge
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_total_time writes: total time taken
/blockstore/write/op_total_time writes: total time
taken
  max: 0 ms

/blockstore/write/op_total_time/aggregate 0
/blockstore/write/op_total_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/aggregate
0
HERE 
NAME:write
op_total_time/aggregate
0
HERE 
NAME:op_total_time
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_total_time/average NaN
/blockstore/write/op_total_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/average
nan
HERE 
NAME:write
op_total_time/average
nan
HERE 
NAME:op_total_time
average
nan
HERE 
Out BEFORE
/blockstore/write/op_total_time/nupdates 0
/blockstore/write/op_total_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/nupdates
0
HERE 
NAME:write
op_total_time/nupdates
0
HERE 
NAME:op_total_time
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes aligned small or multi-page write
/blockstore/write/rmw/aligned_writes aligned small or multi-page
write
  max: 0 blocks

/blockstore/write/rmw/aligned_writes/aggregate 0
/blockstore/write/rmw/aligned_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/aggregate
0
HERE 
NAME:write
rmw/aligned_writes/aggregate
0
HERE 
NAME:rmw
aligned_writes/aggregate
0
HERE 
NAME:aligned_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes/average NaN
/blockstore/write/rmw/aligned_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/average
nan
HERE 
NAME:write
rmw/aligned_writes/average
nan
HERE 
NAME:rmw
aligned_writes/average
nan
HERE 
NAME:aligned_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes/nupdates 0
/blockstore/write/rmw/aligned_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/nupdates
0
HERE 
NAME:write
rmw/aligned_writes/nupdates
0
HERE 
NAME:rmw
aligned_writes/nupdates
0
HERE 
NAME:aligned_writes
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece Time gap between old write and new  big write (>=16 sectors)
/blockstore/write/rmw/big_write_time_differece Time gap between old write and new  big write (>=16
sectors)
  max: 0 sec

/blockstore/write/rmw/big_write_time_differece/aggregate 0
/blockstore/write/rmw/big_write_time_differece/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/aggregate
0
HERE 
NAME:write
rmw/big_write_time_differece/aggregate
0
HERE 
NAME:rmw
big_write_time_differece/aggregate
0
HERE 
NAME:big_write_time_differece
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece/average NaN
/blockstore/write/rmw/big_write_time_differece/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/average
nan
HERE 
NAME:write
rmw/big_write_time_differece/average
nan
HERE 
NAME:rmw
big_write_time_differece/average
nan
HERE 
NAME:big_write_time_differece
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece/nupdates 0
/blockstore/write/rmw/big_write_time_differece/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/nupdates
0
HERE 
NAME:write
rmw/big_write_time_differece/nupdates
0
HERE 
NAME:rmw
big_write_time_differece/nupdates
0
HERE 
NAME:big_write_time_differece
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/nr_page_reads_disk 0
/blockstore/write/rmw/nr_page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/nr_page_reads_disk
0
HERE 
NAME:write
rmw/nr_page_reads_disk
0
HERE 
NAME:rmw
nr_page_reads_disk
0
HERE 
Out BEFORE
/blockstore/write/rmw/nr_page_reads_rdc 0
/blockstore/write/rmw/nr_page_reads_rdc
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/nr_page_reads_rdc
0
HERE 
NAME:write
rmw/nr_page_reads_rdc
0
HERE 
NAME:rmw
nr_page_reads_rdc
0
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece Time gap between old write and new  short write(<16 sectors)
/blockstore/write/rmw/small_write_time_differece Time gap between old write and new  short write(<16
sectors)
  max: 0 sec

/blockstore/write/rmw/small_write_time_differece/aggregate 0
/blockstore/write/rmw/small_write_time_differece/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/aggregate
0
HERE 
NAME:write
rmw/small_write_time_differece/aggregate
0
HERE 
NAME:rmw
small_write_time_differece/aggregate
0
HERE 
NAME:small_write_time_differece
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece/average NaN
/blockstore/write/rmw/small_write_time_differece/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/average
nan
HERE 
NAME:write
rmw/small_write_time_differece/average
nan
HERE 
NAME:rmw
small_write_time_differece/average
nan
HERE 
NAME:small_write_time_differece
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece/nupdates 0
/blockstore/write/rmw/small_write_time_differece/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/nupdates
0
HERE 
NAME:write
rmw/small_write_time_differece/nupdates
0
HERE 
NAME:rmw
small_write_time_differece/nupdates
0
HERE 
NAME:small_write_time_differece
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes small write at the end of the page or  unaligned multi page write
/blockstore/write/rmw/unaligned_other_writes small write at the end of the page or  unaligned multi page
write
  max: 0 blocks

/blockstore/write/rmw/unaligned_other_writes/aggregate 0
/blockstore/write/rmw/unaligned_other_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/aggregate
0
HERE 
NAME:write
rmw/unaligned_other_writes/aggregate
0
HERE 
NAME:rmw
unaligned_other_writes/aggregate
0
HERE 
NAME:unaligned_other_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes/average NaN
/blockstore/write/rmw/unaligned_other_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/average
nan
HERE 
NAME:write
rmw/unaligned_other_writes/average
nan
HERE 
NAME:rmw
unaligned_other_writes/average
nan
HERE 
NAME:unaligned_other_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes/nupdates 0
/blockstore/write/rmw/unaligned_other_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/nupdates
0
HERE 
NAME:write
rmw/unaligned_other_writes/nupdates
0
HERE 
NAME:rmw
unaligned_other_writes/nupdates
0
HERE 
NAME:unaligned_other_writes
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset starting offset of (other) unaligned wrtes
/blockstore/write/rmw/unaligned_other_writes_starting_offset starting offset of (other) unaligned
wrtes
  max: 0 block

/blockstore/write/rmw/unaligned_other_writes_starting_offset/aggregate 0
/blockstore/write/rmw/unaligned_other_writes_starting_offset/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:unaligned_other_writes_starting_offset
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset/average NaN
/blockstore/write/rmw/unaligned_other_writes_starting_offset/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:unaligned_other_writes_starting_offset
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset/nupdates 0
/blockstore/write/rmw/unaligned_other_writes_starting_offset/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:unaligned_other_writes_starting_offset
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes small write in the middle of the page
/blockstore/write/rmw/unaligned_within_page_writes small write in the middle of the
page
  max: 0 blocks

/blockstore/write/rmw/unaligned_within_page_writes/aggregate 0
/blockstore/write/rmw/unaligned_within_page_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/aggregate
0
HERE 
NAME:write
rmw/unaligned_within_page_writes/aggregate
0
HERE 
NAME:rmw
unaligned_within_page_writes/aggregate
0
HERE 
NAME:unaligned_within_page_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes/average NaN
/blockstore/write/rmw/unaligned_within_page_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/average
nan
HERE 
NAME:write
rmw/unaligned_within_page_writes/average
nan
HERE 
NAME:rmw
unaligned_within_page_writes/average
nan
HERE 
NAME:unaligned_within_page_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes/nupdates 0
/blockstore/write/rmw/unaligned_within_page_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/nupdates
0
HERE 
NAME:write
rmw/unaligned_within_page_writes/nupdates
0
HERE 
NAME:rmw
unaligned_within_page_writes/nupdates
0
HERE 
NAME:unaligned_within_page_writes
nupdates
0
HERE 
Out BEFORE
      Dumping iSCSI Stats
      Dumping MGMT Stats
/mgmt/actionqueue/queue_size 0
/mgmt/actionqueue/queue_size
0
In BEFORE
HERE 
NAME:mgmt
actionqueue/queue_size
0
HERE 
NAME:actionqueue
queue_size
0
HERE 
Out BEFORE
/mgmt/actionstore/queue_size 120
/mgmt/actionstore/queue_size
120
In BEFORE
HERE 
NAME:mgmt
actionstore/queue_size
120
HERE 
NAME:actionstore
queue_size
120
HERE 
Out BEFORE
    Finished dumping external listener.
GraniteEdge stats at ---- ----Tue 2016-07-26 01:20:45 GMT
2016-07-26 01:20:45
      Dumping RdiskEdge Stats
      Dumping BlockStore Stats
/blockstore/10/dc_last_write_time 1469479904
/blockstore/10/dc_last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
10/dc_last_write_time
1469479904
HERE 
NAME:10
dc_last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/10/last_write_time 1469479904
/blockstore/10/last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
10/last_write_time
1469479904
HERE 
NAME:10
last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/10/nr_blk_commits 91706813
/blockstore/10/nr_blk_commits
91706813
In BEFORE
HERE 
NAME:blockstore
10/nr_blk_commits
91706813
HERE 
NAME:10
nr_blk_commits
91706813
HERE 
Out BEFORE
/blockstore/10/nr_blk_writes 91706813
/blockstore/10/nr_blk_writes
91706813
In BEFORE
HERE 
NAME:blockstore
10/nr_blk_writes
91706813
HERE 
NAME:10
nr_blk_writes
91706813
HERE 
Out BEFORE
/blockstore/11/dc_last_write_time 1469479904
/blockstore/11/dc_last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
11/dc_last_write_time
1469479904
HERE 
NAME:11
dc_last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/11/last_write_time 1469479904
/blockstore/11/last_write_time
1469479904
In BEFORE
HERE 
NAME:blockstore
11/last_write_time
1469479904
HERE 
NAME:11
last_write_time
1469479904
HERE 
Out BEFORE
/blockstore/11/nr_blk_commits 99990631
/blockstore/11/nr_blk_commits
99990631
In BEFORE
HERE 
NAME:blockstore
11/nr_blk_commits
99990631
HERE 
NAME:11
nr_blk_commits
99990631
HERE 
Out BEFORE
/blockstore/11/nr_blk_writes 99990631
/blockstore/11/nr_blk_writes
99990631
In BEFORE
HERE 
NAME:blockstore
11/nr_blk_writes
99990631
HERE 
NAME:11
nr_blk_writes
99990631
HERE 
Out BEFORE
/blockstore/12/dc_last_write_time 1469479905
/blockstore/12/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
12/dc_last_write_time
1469479905
HERE 
NAME:12
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/12/last_write_time 1469479905
/blockstore/12/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
12/last_write_time
1469479905
HERE 
NAME:12
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/12/nr_blk_commits 2894843
/blockstore/12/nr_blk_commits
2894843
In BEFORE
HERE 
NAME:blockstore
12/nr_blk_commits
2894843
HERE 
NAME:12
nr_blk_commits
2894843
HERE 
Out BEFORE
/blockstore/12/nr_blk_writes 2894843
/blockstore/12/nr_blk_writes
2894843
In BEFORE
HERE 
NAME:blockstore
12/nr_blk_writes
2894843
HERE 
NAME:12
nr_blk_writes
2894843
HERE 
Out BEFORE
/blockstore/13/dc_last_write_time 1469479905
/blockstore/13/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
13/dc_last_write_time
1469479905
HERE 
NAME:13
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/13/last_write_time 1469479905
/blockstore/13/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
13/last_write_time
1469479905
HERE 
NAME:13
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/13/nr_blk_commits 4727607438
/blockstore/13/nr_blk_commits
4727607438
In BEFORE
HERE 
NAME:blockstore
13/nr_blk_commits
4727607438
HERE 
NAME:13
nr_blk_commits
4727607438
HERE 
Out BEFORE
/blockstore/13/nr_blk_writes 4727607438
/blockstore/13/nr_blk_writes
4727607438
In BEFORE
HERE 
NAME:blockstore
13/nr_blk_writes
4727607438
HERE 
NAME:13
nr_blk_writes
4727607438
HERE 
Out BEFORE
/blockstore/14/dc_last_write_time 1469479905
/blockstore/14/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
14/dc_last_write_time
1469479905
HERE 
NAME:14
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/14/last_write_time 1469479905
/blockstore/14/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
14/last_write_time
1469479905
HERE 
NAME:14
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/14/nr_blk_commits 1835272490
/blockstore/14/nr_blk_commits
1835272490
In BEFORE
HERE 
NAME:blockstore
14/nr_blk_commits
1835272490
HERE 
NAME:14
nr_blk_commits
1835272490
HERE 
Out BEFORE
/blockstore/14/nr_blk_writes 1835272490
/blockstore/14/nr_blk_writes
1835272490
In BEFORE
HERE 
NAME:blockstore
14/nr_blk_writes
1835272490
HERE 
NAME:14
nr_blk_writes
1835272490
HERE 
Out BEFORE
/blockstore/16/dc_last_write_time 1469479905
/blockstore/16/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
16/dc_last_write_time
1469479905
HERE 
NAME:16
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/16/last_write_time 1469479905
/blockstore/16/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
16/last_write_time
1469479905
HERE 
NAME:16
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/16/nr_blk_commits 12455455463
/blockstore/16/nr_blk_commits
12455455463
In BEFORE
HERE 
NAME:blockstore
16/nr_blk_commits
12455455463
HERE 
NAME:16
nr_blk_commits
12455455463
HERE 
Out BEFORE
/blockstore/16/nr_blk_writes 12455455463
/blockstore/16/nr_blk_writes
12455455463
In BEFORE
HERE 
NAME:blockstore
16/nr_blk_writes
12455455463
HERE 
NAME:16
nr_blk_writes
12455455463
HERE 
Out BEFORE
/blockstore/8/dc_last_write_time 1469479902
/blockstore/8/dc_last_write_time
1469479902
In BEFORE
HERE 
NAME:blockstore
8/dc_last_write_time
1469479902
HERE 
NAME:8
dc_last_write_time
1469479902
HERE 
Out BEFORE
/blockstore/8/last_write_time 1469479902
/blockstore/8/last_write_time
1469479902
In BEFORE
HERE 
NAME:blockstore
8/last_write_time
1469479902
HERE 
NAME:8
last_write_time
1469479902
HERE 
Out BEFORE
/blockstore/8/nr_blk_commits 61845671
/blockstore/8/nr_blk_commits
61845671
In BEFORE
HERE 
NAME:blockstore
8/nr_blk_commits
61845671
HERE 
NAME:8
nr_blk_commits
61845671
HERE 
Out BEFORE
/blockstore/8/nr_blk_writes 61845671
/blockstore/8/nr_blk_writes
61845671
In BEFORE
HERE 
NAME:blockstore
8/nr_blk_writes
61845671
HERE 
NAME:8
nr_blk_writes
61845671
HERE 
Out BEFORE
/blockstore/9/dc_last_write_time 1469479905
/blockstore/9/dc_last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
9/dc_last_write_time
1469479905
HERE 
NAME:9
dc_last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/9/last_write_time 1469479905
/blockstore/9/last_write_time
1469479905
In BEFORE
HERE 
NAME:blockstore
9/last_write_time
1469479905
HERE 
NAME:9
last_write_time
1469479905
HERE 
Out BEFORE
/blockstore/9/nr_blk_commits 80280964
/blockstore/9/nr_blk_commits
80280964
In BEFORE
HERE 
NAME:blockstore
9/nr_blk_commits
80280964
HERE 
NAME:9
nr_blk_commits
80280964
HERE 
Out BEFORE
/blockstore/9/nr_blk_writes 80280964
/blockstore/9/nr_blk_writes
80280964
In BEFORE
HERE 
NAME:blockstore
9/nr_blk_writes
80280964
HERE 
NAME:9
nr_blk_writes
80280964
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/slab_count 976
/blockstore/bufferpool/41407808/slab_count
976
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/slab_count
976
HERE 
NAME:bufferpool
41407808/slab_count
976
HERE 
NAME:41407808
slab_count
976
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/slab_size 8704
/blockstore/bufferpool/41407808/slab_size
8704
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/slab_size
8704
HERE 
NAME:bufferpool
41407808/slab_size
8704
HERE 
NAME:41407808
slab_size
8704
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/unable_to_allocate 0
/blockstore/bufferpool/41407808/unable_to_allocate
0
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/unable_to_allocate
0
HERE 
NAME:bufferpool
41407808/unable_to_allocate
0
HERE 
NAME:41407808
unable_to_allocate
0
HERE 
Out BEFORE
/blockstore/bufferpool/41407808/unused 8495104
/blockstore/bufferpool/41407808/unused
8495104
In BEFORE
HERE 
NAME:blockstore
bufferpool/41407808/unused
8495104
HERE 
NAME:bufferpool
41407808/unused
8495104
HERE 
NAME:41407808
unused
8495104
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms time taken for commit
/blockstore/commit_processor/commit_time_ms time taken for
commit
  max: 0 milliseconds

/blockstore/commit_processor/commit_time_ms/aggregate 0
/blockstore/commit_processor/commit_time_ms/aggregate
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/aggregate
0
HERE 
NAME:commit_processor
commit_time_ms/aggregate
0
HERE 
NAME:commit_time_ms
aggregate
0
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms/average NaN
/blockstore/commit_processor/commit_time_ms/average
NaN
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/average
nan
HERE 
NAME:commit_processor
commit_time_ms/average
nan
HERE 
NAME:commit_time_ms
average
nan
HERE 
Out BEFORE
/blockstore/commit_processor/commit_time_ms/nupdates 0
/blockstore/commit_processor/commit_time_ms/nupdates
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/commit_time_ms/nupdates
0
HERE 
NAME:commit_processor
commit_time_ms/nupdates
0
HERE 
NAME:commit_time_ms
nupdates
0
HERE 
Out BEFORE
/blockstore/commit_processor/dirty_data_present 1
/blockstore/commit_processor/dirty_data_present
1
In BEFORE
HERE 
NAME:blockstore
commit_processor/dirty_data_present
1
HERE 
NAME:commit_processor
dirty_data_present
1
HERE 
Out BEFORE
/blockstore/commit_processor/next_commit [LSN::INVALID]
/blockstore/commit_processor/next_commit
[LSN::INVALID]
/blockstore/commit_processor/nr_blk_commits 19356165132
/blockstore/commit_processor/nr_blk_commits
19356165132
In BEFORE
HERE 
NAME:blockstore
commit_processor/nr_blk_commits
19356165132
HERE 
NAME:commit_processor
nr_blk_commits
19356165132
HERE 
Out BEFORE
/blockstore/commit_processor/nr_blk_commits_in_mem 0
/blockstore/commit_processor/nr_blk_commits_in_mem
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/nr_blk_commits_in_mem
0
HERE 
NAME:commit_processor
nr_blk_commits_in_mem
0
HERE 
Out BEFORE
/blockstore/commit_processor/page_reads_cache 0
/blockstore/commit_processor/page_reads_cache
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/page_reads_cache
0
HERE 
NAME:commit_processor
page_reads_cache
0
HERE 
Out BEFORE
/blockstore/commit_processor/page_reads_disk 0
/blockstore/commit_processor/page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/page_reads_disk
0
HERE 
NAME:commit_processor
page_reads_disk
0
HERE 
Out BEFORE
/blockstore/commit_processor/pause_count 0
/blockstore/commit_processor/pause_count
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/pause_count
0
HERE 
NAME:commit_processor
pause_count
0
HERE 
Out BEFORE
/blockstore/commit_processor/paused_msecs 0
/blockstore/commit_processor/paused_msecs
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/paused_msecs
0
HERE 
NAME:commit_processor
paused_msecs
0
HERE 
Out BEFORE
/blockstore/commit_processor/pending_commits 0
/blockstore/commit_processor/pending_commits
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/pending_commits
0
HERE 
NAME:commit_processor
pending_commits
0
HERE 
Out BEFORE
/blockstore/commit_processor/running_msecs 0
/blockstore/commit_processor/running_msecs
0
In BEFORE
HERE 
NAME:blockstore
commit_processor/running_msecs
0
HERE 
NAME:commit_processor
running_msecs
0
HERE 
Out BEFORE
/blockstore/commit_processor/state INIT
/blockstore/commit_processor/state
INIT
/blockstore/disk_helper/ha_peer_write_time ha peer op write time
/blockstore/disk_helper/ha_peer_write_time ha peer op write
time
  max: 0 ms

/blockstore/disk_helper/ha_peer_write_time/aggregate 0
/blockstore/disk_helper/ha_peer_write_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/aggregate
0
HERE 
NAME:disk_helper
ha_peer_write_time/aggregate
0
HERE 
NAME:ha_peer_write_time
aggregate
0
HERE 
Out BEFORE
/blockstore/disk_helper/ha_peer_write_time/average NaN
/blockstore/disk_helper/ha_peer_write_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/average
nan
HERE 
NAME:disk_helper
ha_peer_write_time/average
nan
HERE 
NAME:ha_peer_write_time
average
nan
HERE 
Out BEFORE
/blockstore/disk_helper/ha_peer_write_time/nupdates 0
/blockstore/disk_helper/ha_peer_write_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/ha_peer_write_time/nupdates
0
HERE 
NAME:disk_helper
ha_peer_write_time/nupdates
0
HERE 
NAME:ha_peer_write_time
nupdates
0
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time local op write time
/blockstore/disk_helper/local_write_time local op write
time
  max: 0 ms

/blockstore/disk_helper/local_write_time/aggregate 0
/blockstore/disk_helper/local_write_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/aggregate
0
HERE 
NAME:disk_helper
local_write_time/aggregate
0
HERE 
NAME:local_write_time
aggregate
0
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time/average NaN
/blockstore/disk_helper/local_write_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/average
nan
HERE 
NAME:disk_helper
local_write_time/average
nan
HERE 
NAME:local_write_time
average
nan
HERE 
Out BEFORE
/blockstore/disk_helper/local_write_time/nupdates 0
/blockstore/disk_helper/local_write_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
disk_helper/local_write_time/nupdates
0
HERE 
NAME:disk_helper
local_write_time/nupdates
0
HERE 
NAME:local_write_time
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/dirty_skips 0
/blockstore/fifo/dirty_skips
0
In BEFORE
HERE 
NAME:blockstore
fifo/dirty_skips
0
HERE 
NAME:fifo
dirty_skips
0
HERE 
Out BEFORE
/blockstore/fifo/error_status 0
/blockstore/fifo/error_status
0
In BEFORE
HERE 
NAME:blockstore
fifo/error_status
0
HERE 
NAME:fifo
error_status
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_mode_allocations 0
/blockstore/fifo/fifo_mode_allocations
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_mode_allocations
0
HERE 
NAME:fifo
fifo_mode_allocations
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips /blockstore/fifo/fifo_page_skips
/blockstore/fifo/fifo_page_skips
/blockstore/fifo/fifo_page_skips
  max: 0 pages

/blockstore/fifo/fifo_page_skips/aggregate 0
/blockstore/fifo/fifo_page_skips/aggregate
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/aggregate
0
HERE 
NAME:fifo
fifo_page_skips/aggregate
0
HERE 
NAME:fifo_page_skips
aggregate
0
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips/average NaN
/blockstore/fifo/fifo_page_skips/average
NaN
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/average
nan
HERE 
NAME:fifo
fifo_page_skips/average
nan
HERE 
NAME:fifo_page_skips
average
nan
HERE 
Out BEFORE
/blockstore/fifo/fifo_page_skips/nupdates 0
/blockstore/fifo/fifo_page_skips/nupdates
0
In BEFORE
HERE 
NAME:blockstore
fifo/fifo_page_skips/nupdates
0
HERE 
NAME:fifo
fifo_page_skips/nupdates
0
HERE 
NAME:fifo_page_skips
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/last_commit [LSN::INVALID]
/blockstore/fifo/last_commit
[LSN::INVALID]
/blockstore/fifo/last_commit_on_disk [LSN::INVALID]
/blockstore/fifo/last_commit_on_disk
[LSN::INVALID]
/blockstore/fifo/last_sync [LSN::INVALID]
/blockstore/fifo/last_sync
[LSN::INVALID]
/blockstore/fifo/last_write [LSN::INVALID]
/blockstore/fifo/last_write
[LSN::INVALID]
/blockstore/fifo/last_write_on_disk [LSN::INVALID]
/blockstore/fifo/last_write_on_disk
[LSN::INVALID]
/blockstore/fifo/next_write [LSN::INVALID]
/blockstore/fifo/next_write
[LSN::INVALID]
/blockstore/fifo/nr_evictions 0
/blockstore/fifo/nr_evictions
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_evictions
0
HERE 
NAME:fifo
nr_evictions
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages 410203586
/blockstore/fifo/nr_pages
410203586
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages
410203586
HERE 
NAME:fifo
nr_pages
410203586
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_evictable 0
/blockstore/fifo/nr_pages_evictable
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_evictable
0
HERE 
NAME:fifo
nr_pages_evictable
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_evictable_unused 0
/blockstore/fifo/nr_pages_evictable_unused
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_evictable_unused
0
HERE 
NAME:fifo
nr_pages_evictable_unused
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_inuse 0
/blockstore/fifo/nr_pages_inuse
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_inuse
0
HERE 
NAME:fifo
nr_pages_inuse
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_pinnable 0
/blockstore/fifo/nr_pages_pinnable
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_pinnable
0
HERE 
NAME:fifo
nr_pages_pinnable
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_pinned 0
/blockstore/fifo/nr_pages_pinned
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_pinned
0
HERE 
NAME:fifo
nr_pages_pinned
0
HERE 
Out BEFORE
/blockstore/fifo/nr_pages_unused 410203586
/blockstore/fifo/nr_pages_unused
410203586
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pages_unused
410203586
HERE 
NAME:fifo
nr_pages_unused
410203586
HERE 
Out BEFORE
/blockstore/fifo/nr_pinned_pages_used 0
/blockstore/fifo/nr_pinned_pages_used
0
In BEFORE
HERE 
NAME:blockstore
fifo/nr_pinned_pages_used
0
HERE 
NAME:fifo
nr_pinned_pages_used
0
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used # blocks used in page
/blockstore/fifo/page_blocks_used # blocks used in
page
  max: 0 blocks

/blockstore/fifo/page_blocks_used/aggregate 0
/blockstore/fifo/page_blocks_used/aggregate
0
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/aggregate
0
HERE 
NAME:fifo
page_blocks_used/aggregate
0
HERE 
NAME:page_blocks_used
aggregate
0
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used/average NaN
/blockstore/fifo/page_blocks_used/average
NaN
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/average
nan
HERE 
NAME:fifo
page_blocks_used/average
nan
HERE 
NAME:page_blocks_used
average
nan
HERE 
Out BEFORE
/blockstore/fifo/page_blocks_used/nupdates 0
/blockstore/fifo/page_blocks_used/nupdates
0
In BEFORE
HERE 
NAME:blockstore
fifo/page_blocks_used/nupdates
0
HERE 
NAME:fifo
page_blocks_used/nupdates
0
HERE 
NAME:page_blocks_used
nupdates
0
HERE 
Out BEFORE
/blockstore/fifo/stable_write_limit [LSN::INVALID]
/blockstore/fifo/stable_write_limit
[LSN::INVALID]
/blockstore/last_rebuild/cancelled_pages 0
/blockstore/last_rebuild/cancelled_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/cancelled_pages
0
HERE 
NAME:last_rebuild
cancelled_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/completed_pages 0
/blockstore/last_rebuild/completed_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/completed_pages
0
HERE 
NAME:last_rebuild
completed_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/fifo_completed_pages 0
/blockstore/last_rebuild/fifo_completed_pages
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/fifo_completed_pages
0
HERE 
NAME:last_rebuild
fifo_completed_pages
0
HERE 
Out BEFORE
/blockstore/last_rebuild/is_full_rebuild 0
/blockstore/last_rebuild/is_full_rebuild
0
In BEFORE
HERE 
NAME:blockstore
last_rebuild/is_full_rebuild
0
HERE 
NAME:last_rebuild
is_full_rebuild
0
HERE 
Out BEFORE
/blockstore/last_rebuild/r2l_time 0us
/blockstore/last_rebuild/r2l_time
0us
/blockstore/last_rebuild/start_time 
/blockstore/last_rebuild/start_time

/blockstore/last_rebuild/total_pages 4294967295
/blockstore/last_rebuild/total_pages
4294967295
In BEFORE
HERE 
NAME:blockstore
last_rebuild/total_pages
4294967295
HERE 
NAME:last_rebuild
total_pages
4294967295
HERE 
Out BEFORE
/blockstore/last_rebuild/total_time 0us
/blockstore/last_rebuild/total_time
0us
/blockstore/page_cache/nr_page_lookups 0
/blockstore/page_cache/nr_page_lookups
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups
0
HERE 
NAME:page_cache
nr_page_lookups
0
HERE 
Out BEFORE
/blockstore/page_cache/nr_page_lookups_absent 0
/blockstore/page_cache/nr_page_lookups_absent
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups_absent
0
HERE 
NAME:page_cache
nr_page_lookups_absent
0
HERE 
Out BEFORE
/blockstore/page_cache/nr_page_lookups_on_disk 0
/blockstore/page_cache/nr_page_lookups_on_disk
0
In BEFORE
HERE 
NAME:blockstore
page_cache/nr_page_lookups_on_disk
0
HERE 
NAME:page_cache
nr_page_lookups_on_disk
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal page alloc time - normal
/blockstore/page_cache/page_alloc_time_normal page alloc time -
normal
  max: 0 ms

/blockstore/page_cache/page_alloc_time_normal/aggregate 0
/blockstore/page_cache/page_alloc_time_normal/aggregate
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/aggregate
0
HERE 
NAME:page_cache
page_alloc_time_normal/aggregate
0
HERE 
NAME:page_alloc_time_normal
aggregate
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal/average NaN
/blockstore/page_cache/page_alloc_time_normal/average
NaN
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/average
nan
HERE 
NAME:page_cache
page_alloc_time_normal/average
nan
HERE 
NAME:page_alloc_time_normal
average
nan
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_normal/nupdates 0
/blockstore/page_cache/page_alloc_time_normal/nupdates
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_normal/nupdates
0
HERE 
NAME:page_cache
page_alloc_time_normal/nupdates
0
HERE 
NAME:page_alloc_time_normal
nupdates
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued page alloc time - queued requests
/blockstore/page_cache/page_alloc_time_queued page alloc time - queued
requests
  max: 0 ms

/blockstore/page_cache/page_alloc_time_queued/aggregate 0
/blockstore/page_cache/page_alloc_time_queued/aggregate
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/aggregate
0
HERE 
NAME:page_cache
page_alloc_time_queued/aggregate
0
HERE 
NAME:page_alloc_time_queued
aggregate
0
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued/average NaN
/blockstore/page_cache/page_alloc_time_queued/average
NaN
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/average
nan
HERE 
NAME:page_cache
page_alloc_time_queued/average
nan
HERE 
NAME:page_alloc_time_queued
average
nan
HERE 
Out BEFORE
/blockstore/page_cache/page_alloc_time_queued/nupdates 0
/blockstore/page_cache/page_alloc_time_queued/nupdates
0
In BEFORE
HERE 
NAME:blockstore
page_cache/page_alloc_time_queued/nupdates
0
HERE 
NAME:page_cache
page_alloc_time_queued/nupdates
0
HERE 
NAME:page_alloc_time_queued
nupdates
0
HERE 
Out BEFORE
/blockstore/page_cache/pages 617000
/blockstore/page_cache/pages
617000
In BEFORE
HERE 
NAME:blockstore
page_cache/pages
617000
HERE 
NAME:page_cache
pages
617000
HERE 
Out BEFORE
/blockstore/page_cache/pages_on_freelist 201
/blockstore/page_cache/pages_on_freelist
201
In BEFORE
HERE 
NAME:blockstore
page_cache/pages_on_freelist
201
HERE 
NAME:page_cache
pages_on_freelist
201
HERE 
Out BEFORE
/blockstore/page_cache/store_pages_in_mem 0
/blockstore/page_cache/store_pages_in_mem
0
In BEFORE
HERE 
NAME:blockstore
page_cache/store_pages_in_mem
0
HERE 
NAME:page_cache
store_pages_in_mem
0
HERE 
Out BEFORE
/blockstore/page_cache/stores_dropped 0
/blockstore/page_cache/stores_dropped
0
In BEFORE
HERE 
NAME:blockstore
page_cache/stores_dropped
0
HERE 
NAME:page_cache
stores_dropped
0
HERE 
Out BEFORE
/blockstore/phash/ha_unsynced_pages 0
/blockstore/phash/ha_unsynced_pages
0
In BEFORE
HERE 
NAME:blockstore
phash/ha_unsynced_pages
0
HERE 
NAME:phash
ha_unsynced_pages
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr 0
/blockstore/read/nr_blk_reads_usr
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr
0
HERE 
NAME:read
nr_blk_reads_usr
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr_other_hits 0
/blockstore/read/nr_blk_reads_usr_other_hits
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr_other_hits
0
HERE 
NAME:read
nr_blk_reads_usr_other_hits
0
HERE 
Out BEFORE
/blockstore/read/nr_blk_reads_usr_store_hits 0
/blockstore/read/nr_blk_reads_usr_store_hits
0
In BEFORE
HERE 
NAME:blockstore
read/nr_blk_reads_usr_store_hits
0
HERE 
NAME:read
nr_blk_reads_usr_store_hits
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user 0
/blockstore/read/nr_page_lookups_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user
0
HERE 
NAME:read
nr_page_lookups_user
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user_absent 0
/blockstore/read/nr_page_lookups_user_absent
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user_absent
0
HERE 
NAME:read
nr_page_lookups_user_absent
0
HERE 
Out BEFORE
/blockstore/read/nr_page_lookups_user_on_disk 0
/blockstore/read/nr_page_lookups_user_on_disk
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_lookups_user_on_disk
0
HERE 
NAME:read
nr_page_lookups_user_on_disk
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_disk 0
/blockstore/read/nr_page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_disk
0
HERE 
NAME:read
nr_page_reads_disk
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_disk_user 0
/blockstore/read/nr_page_reads_disk_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_disk_user
0
HERE 
NAME:read
nr_page_reads_disk_user
0
HERE 
Out BEFORE
/blockstore/read/nr_page_reads_rdc_user 0
/blockstore/read/nr_page_reads_rdc_user
0
In BEFORE
HERE 
NAME:blockstore
read/nr_page_reads_rdc_user
0
HERE 
NAME:read
nr_page_reads_rdc_user
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk no.of total disk reads (RDC + WBC) per user readOp
/blockstore/read/op_page_reads_disk no.of total disk reads (RDC + WBC) per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_disk/aggregate 0
/blockstore/read/op_page_reads_disk/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/aggregate
0
HERE 
NAME:read
op_page_reads_disk/aggregate
0
HERE 
NAME:op_page_reads_disk
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk/average NaN
/blockstore/read/op_page_reads_disk/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/average
nan
HERE 
NAME:read
op_page_reads_disk/average
nan
HERE 
NAME:op_page_reads_disk
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_disk/nupdates 0
/blockstore/read/op_page_reads_disk/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_disk/nupdates
0
HERE 
NAME:read
op_page_reads_disk/nupdates
0
HERE 
NAME:op_page_reads_disk
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits no.of Read Cache hits per user readOp
/blockstore/read/op_page_reads_rdc_hits no.of Read Cache hits per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_rdc_hits/aggregate 0
/blockstore/read/op_page_reads_rdc_hits/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/aggregate
0
HERE 
NAME:read
op_page_reads_rdc_hits/aggregate
0
HERE 
NAME:op_page_reads_rdc_hits
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits/average NaN
/blockstore/read/op_page_reads_rdc_hits/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/average
nan
HERE 
NAME:read
op_page_reads_rdc_hits/average
nan
HERE 
NAME:op_page_reads_rdc_hits
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_hits/nupdates 0
/blockstore/read/op_page_reads_rdc_hits/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_hits/nupdates
0
HERE 
NAME:read
op_page_reads_rdc_hits/nupdates
0
HERE 
NAME:op_page_reads_rdc_hits
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses no.of Read Cache misses per user readOp
/blockstore/read/op_page_reads_rdc_misses no.of Read Cache misses per user
readOp
  max: 0 pages

/blockstore/read/op_page_reads_rdc_misses/aggregate 0
/blockstore/read/op_page_reads_rdc_misses/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/aggregate
0
HERE 
NAME:read
op_page_reads_rdc_misses/aggregate
0
HERE 
NAME:op_page_reads_rdc_misses
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses/average NaN
/blockstore/read/op_page_reads_rdc_misses/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/average
nan
HERE 
NAME:read
op_page_reads_rdc_misses/average
nan
HERE 
NAME:op_page_reads_rdc_misses
average
nan
HERE 
Out BEFORE
/blockstore/read/op_page_reads_rdc_misses/nupdates 0
/blockstore/read/op_page_reads_rdc_misses/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_page_reads_rdc_misses/nupdates
0
HERE 
NAME:read
op_page_reads_rdc_misses/nupdates
0
HERE 
NAME:op_page_reads_rdc_misses
nupdates
0
HERE 
Out BEFORE
/blockstore/read/op_total_time reads: total time taken
/blockstore/read/op_total_time reads: total time
taken
  max: 0 ms

/blockstore/read/op_total_time/aggregate 0
/blockstore/read/op_total_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/aggregate
0
HERE 
NAME:read
op_total_time/aggregate
0
HERE 
NAME:op_total_time
aggregate
0
HERE 
Out BEFORE
/blockstore/read/op_total_time/average NaN
/blockstore/read/op_total_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/average
nan
HERE 
NAME:read
op_total_time/average
nan
HERE 
NAME:op_total_time
average
nan
HERE 
Out BEFORE
/blockstore/read/op_total_time/nupdates 0
/blockstore/read/op_total_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/op_total_time/nupdates
0
HERE 
NAME:read
op_total_time/nupdates
0
HERE 
NAME:op_total_time
nupdates
0
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size Size of user read request not completely satisfied by Read Cache
/blockstore/read/rdc_misses_op_size Size of user read request not completely satisfied by Read
Cache
  max: 0 blocks

/blockstore/read/rdc_misses_op_size/aggregate 0
/blockstore/read/rdc_misses_op_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/aggregate
0
HERE 
NAME:read
rdc_misses_op_size/aggregate
0
HERE 
NAME:rdc_misses_op_size
aggregate
0
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size/average NaN
/blockstore/read/rdc_misses_op_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/average
nan
HERE 
NAME:read
rdc_misses_op_size/average
nan
HERE 
NAME:rdc_misses_op_size
average
nan
HERE 
Out BEFORE
/blockstore/read/rdc_misses_op_size/nupdates 0
/blockstore/read/rdc_misses_op_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
read/rdc_misses_op_size/nupdates
0
HERE 
NAME:read
rdc_misses_op_size/nupdates
0
HERE 
NAME:rdc_misses_op_size
nupdates
0
HERE 
Out BEFORE
/blockstore/read/reads_queued 0
/blockstore/read/reads_queued
0
In BEFORE
HERE 
NAME:blockstore
read/reads_queued
0
HERE 
NAME:read
reads_queued
0
HERE 
Out BEFORE
/blockstore/read_cache/last_flush_lsn [LSN::INVALID]
/blockstore/read_cache/last_flush_lsn
[LSN::INVALID]
/blockstore/read_cache/nr_readcache_hits 0
/blockstore/read_cache/nr_readcache_hits
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_hits
0
HERE 
NAME:read_cache
nr_readcache_hits
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_hits_user 0
/blockstore/read_cache/nr_readcache_hits_user
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_hits_user
0
HERE 
NAME:read_cache
nr_readcache_hits_user
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_misses 0
/blockstore/read_cache/nr_readcache_misses
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_misses
0
HERE 
NAME:read_cache
nr_readcache_misses
0
HERE 
Out BEFORE
/blockstore/read_cache/nr_readcache_misses_user 0
/blockstore/read_cache/nr_readcache_misses_user
0
In BEFORE
HERE 
NAME:blockstore
read_cache/nr_readcache_misses_user
0
HERE 
NAME:read_cache
nr_readcache_misses_user
0
HERE 
Out BEFORE
/blockstore/readahead/nr_hits 0
/blockstore/readahead/nr_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_hits
0
HERE 
NAME:readahead
nr_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_pages 0
/blockstore/readahead/nr_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_pages
0
HERE 
NAME:readahead
nr_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_fifo_seq_hits 0
/blockstore/readahead/nr_read_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_fifo_seq_hits
0
HERE 
NAME:readahead
nr_read_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_fifo_seq_pages 0
/blockstore/readahead/nr_read_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_fifo_seq_pages
0
HERE 
NAME:readahead
nr_read_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_fifo_seq_hits 0
/blockstore/readahead/nr_read_lba_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_fifo_seq_hits
0
HERE 
NAME:readahead
nr_read_lba_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_fifo_seq_pages 0
/blockstore/readahead/nr_read_lba_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_fifo_seq_pages
0
HERE 
NAME:readahead
nr_read_lba_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_seq_hits 0
/blockstore/readahead/nr_read_lba_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_seq_hits
0
HERE 
NAME:readahead
nr_read_lba_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_read_lba_seq_pages 0
/blockstore/readahead/nr_read_lba_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_read_lba_seq_pages
0
HERE 
NAME:readahead
nr_read_lba_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_fifo_seq_hits 0
/blockstore/readahead/nr_write_merge_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_fifo_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_fifo_seq_pages 0
/blockstore/readahead/nr_write_merge_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_fifo_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_fifo_seq_hits 0
/blockstore/readahead/nr_write_merge_lba_fifo_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_fifo_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_lba_fifo_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_fifo_seq_pages 0
/blockstore/readahead/nr_write_merge_lba_fifo_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_fifo_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_lba_fifo_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_seq_hits 0
/blockstore/readahead/nr_write_merge_lba_seq_hits
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_seq_hits
0
HERE 
NAME:readahead
nr_write_merge_lba_seq_hits
0
HERE 
Out BEFORE
/blockstore/readahead/nr_write_merge_lba_seq_pages 0
/blockstore/readahead/nr_write_merge_lba_seq_pages
0
In BEFORE
HERE 
NAME:blockstore
readahead/nr_write_merge_lba_seq_pages
0
HERE 
NAME:readahead
nr_write_merge_lba_seq_pages
0
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_ read-ahead:(read, fifo seq) page hit postion
/blockstore/readahead/read_fifo_seq_hit_page_ read-ahead:(read, fifo seq) page hit
postion
  max: 0 pages

/blockstore/readahead/read_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/read_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:read_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_/average NaN
/blockstore/readahead/read_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_fifo_seq_hit_page_/average
nan
HERE 
NAME:read_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/read_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:read_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_ read-ahead:(read, lba& fifo seq)  page hit postion
/blockstore/readahead/read_lba_fifo_seq_hit_page_ read-ahead:(read, lba& fifo seq)  page hit
postion
  max: 0 pages

/blockstore/readahead/read_lba_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/read_lba_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:read_lba_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_/average NaN
/blockstore/readahead/read_lba_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:read_lba_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_lba_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/read_lba_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:read_lba_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_ read-ahead:(read, lba seq) page hit postion
/blockstore/readahead/read_lba_seq_hit_page_ read-ahead:(read, lba seq) page hit
postion
  max: 0 pages

/blockstore/readahead/read_lba_seq_hit_page_/aggregate 0
/blockstore/readahead/read_lba_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
read_lba_seq_hit_page_/aggregate
0
HERE 
NAME:read_lba_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_/average NaN
/blockstore/readahead/read_lba_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/average
nan
HERE 
NAME:readahead
read_lba_seq_hit_page_/average
nan
HERE 
NAME:read_lba_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/read_lba_seq_hit_page_/nupdates 0
/blockstore/readahead/read_lba_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/read_lba_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
read_lba_seq_hit_page_/nupdates
0
HERE 
NAME:read_lba_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_ read-ahead:(write_merge, fifo seq) page hit postion
/blockstore/readahead/write_merge_fifo_seq_hit_page_ read-ahead:(write_merge, fifo seq) page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/average
nan
HERE 
NAME:write_merge_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_ read-ahead:(write_merge,lba& fifo seq)  page hit postion
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_ read-ahead:(write_merge,lba& fifo seq)  page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/average
nan
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_lba_fifo_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_lba_fifo_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_lba_fifo_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_ read-ahead:(write_merge, lba seq) page hit postion
/blockstore/readahead/write_merge_lba_seq_hit_page_ read-ahead:(write_merge, lba seq) page hit
postion
  max: 0 pages

/blockstore/readahead/write_merge_lba_seq_hit_page_/aggregate 0
/blockstore/readahead/write_merge_lba_seq_hit_page_/aggregate
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/aggregate
0
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/aggregate
0
HERE 
NAME:write_merge_lba_seq_hit_page_
aggregate
0
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_/average NaN
/blockstore/readahead/write_merge_lba_seq_hit_page_/average
NaN
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/average
nan
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/average
nan
HERE 
NAME:write_merge_lba_seq_hit_page_
average
nan
HERE 
Out BEFORE
/blockstore/readahead/write_merge_lba_seq_hit_page_/nupdates 0
/blockstore/readahead/write_merge_lba_seq_hit_page_/nupdates
0
In BEFORE
HERE 
NAME:blockstore
readahead/write_merge_lba_seq_hit_page_/nupdates
0
HERE 
NAME:readahead
write_merge_lba_seq_hit_page_/nupdates
0
HERE 
NAME:write_merge_lba_seq_hit_page_
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op Number of pages in a batchIO of write op
/blockstore/wbcache/batch_size_write_op Number of pages in a batchIO of write
op
221391630 : 1
  max: 1 pages
      Aggregate : 221391630 pages. Avg size : 1
/blockstore/wbcache/batch_size_write_op/aggregate 221391630
/blockstore/wbcache/batch_size_write_op/aggregate
221391630
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/aggregate
221391630
HERE 
NAME:wbcache
batch_size_write_op/aggregate
221391630
HERE 
NAME:batch_size_write_op
aggregate
221391630
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op/average 1
/blockstore/wbcache/batch_size_write_op/average
1
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/average
1
HERE 
NAME:wbcache
batch_size_write_op/average
1
HERE 
NAME:batch_size_write_op
average
1
HERE 
Out BEFORE
/blockstore/wbcache/batch_size_write_op/nupdates 221391630
/blockstore/wbcache/batch_size_write_op/nupdates
221391630
In BEFORE
HERE 
NAME:blockstore
wbcache/batch_size_write_op/nupdates
221391630
HERE 
NAME:wbcache
batch_size_write_op/nupdates
221391630
HERE 
NAME:batch_size_write_op
nupdates
221391630
HERE 
Out BEFORE
/blockstore/wbcache/last_hdd_write [194:184437]
/blockstore/wbcache/last_hdd_write
[194:184437]
/blockstore/wbcache/last_persistent_hdd_write [194:107335]
/blockstore/wbcache/last_persistent_hdd_write
[194:107335]
/blockstore/wbcache/last_persistent_hdd_write_on_disk [194:15835]
/blockstore/wbcache/last_persistent_hdd_write_on_disk
[194:15835]
/blockstore/wbcache/last_ssd_write [194:207068]
/blockstore/wbcache/last_ssd_write
[194:207068]
/blockstore/wbcache/last_ssd_write_on_disk [194:113830]
/blockstore/wbcache/last_ssd_write_on_disk
[194:113830]
/blockstore/wbcache/nr_disk_fixes 0
/blockstore/wbcache/nr_disk_fixes
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes
0
HERE 
NAME:wbcache
nr_disk_fixes
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_fixes_fail 0
/blockstore/wbcache/nr_disk_fixes_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes_fail
0
HERE 
NAME:wbcache
nr_disk_fixes_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_fixes_success 0
/blockstore/wbcache/nr_disk_fixes_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_fixes_success
0
HERE 
NAME:wbcache
nr_disk_fixes_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs 0
/blockstore/wbcache/nr_disk_scrubs
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs
0
HERE 
NAME:wbcache
nr_disk_scrubs
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs_fail 0
/blockstore/wbcache/nr_disk_scrubs_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs_fail
0
HERE 
NAME:wbcache
nr_disk_scrubs_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_disk_scrubs_success 0
/blockstore/wbcache/nr_disk_scrubs_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_disk_scrubs_success
0
HERE 
NAME:wbcache
nr_disk_scrubs_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_read_retries_ssd 0
/blockstore/wbcache/nr_page_read_retries_ssd
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_read_retries_ssd
0
HERE 
NAME:wbcache
nr_page_read_retries_ssd
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_reads 6
/blockstore/wbcache/nr_page_reads
6
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_reads
6
HERE 
NAME:wbcache
nr_page_reads
6
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_reads_ssd 4
/blockstore/wbcache/nr_page_reads_ssd
4
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_reads_ssd
4
HERE 
NAME:wbcache
nr_page_reads_ssd
4
HERE 
Out BEFORE
/blockstore/wbcache/nr_page_writes 221391639
/blockstore/wbcache/nr_page_writes
221391639
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_page_writes
221391639
HERE 
NAME:wbcache
nr_page_writes
221391639
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes 0
/blockstore/wbcache/nr_ssd_fixes
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes
0
HERE 
NAME:wbcache
nr_ssd_fixes
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes_fail 0
/blockstore/wbcache/nr_ssd_fixes_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes_fail
0
HERE 
NAME:wbcache
nr_ssd_fixes_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_fixes_success 0
/blockstore/wbcache/nr_ssd_fixes_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_fixes_success
0
HERE 
NAME:wbcache
nr_ssd_fixes_success
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs 0
/blockstore/wbcache/nr_ssd_scrubs
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs
0
HERE 
NAME:wbcache
nr_ssd_scrubs
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs_fail 0
/blockstore/wbcache/nr_ssd_scrubs_fail
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs_fail
0
HERE 
NAME:wbcache
nr_ssd_scrubs_fail
0
HERE 
Out BEFORE
/blockstore/wbcache/nr_ssd_scrubs_success 0
/blockstore/wbcache/nr_ssd_scrubs_success
0
In BEFORE
HERE 
NAME:blockstore
wbcache/nr_ssd_scrubs_success
0
HERE 
NAME:wbcache
nr_ssd_scrubs_success
0
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd write op ssd time
/blockstore/wbcache/op_write_time_ssd write op ssd
time
1387116 : 0
 389273 : 1
 307394 : 2
 545040 : 3-4
1038167 : 5-8
2442146 : 9-16
5371514 : 17-32
31044543 : 33-64
177650393 : 65-128
1154627 : 129-256
  60256 : 257-512
    341 : 513-1K
     24 : 1K-2K
     12 : 2K-4K
    356 : 4K-8K
  max: 5038 ms
      Aggregate : 16105712706 ms. Avg size : 72.7478
/blockstore/wbcache/op_write_time_ssd/aggregate 16105712776
/blockstore/wbcache/op_write_time_ssd/aggregate
16105712776
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/aggregate
16105712776
HERE 
NAME:wbcache
op_write_time_ssd/aggregate
16105712776
HERE 
NAME:op_write_time_ssd
aggregate
16105712776
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd/average 72.7478
/blockstore/wbcache/op_write_time_ssd/average
72.7478
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/average
72.7478
HERE 
NAME:wbcache
op_write_time_ssd/average
72.7478
HERE 
NAME:op_write_time_ssd
average
72.7478
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_ssd/nupdates 221391205
/blockstore/wbcache/op_write_time_ssd/nupdates
221391205
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_ssd/nupdates
221391205
HERE 
NAME:wbcache
op_write_time_ssd/nupdates
221391205
HERE 
NAME:op_write_time_ssd
nupdates
221391205
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total write op total time
/blockstore/wbcache/op_write_time_total write op total
time
1300491 : 0
 403279 : 1
 299881 : 2
 529437 : 3-4
1003048 : 5-8
1971819 : 9-16
4839474 : 17-32
29307614 : 33-64
180038879 : 65-128
1456962 : 129-256
 234246 : 257-512
   5539 : 513-1K
    168 : 1K-2K
     12 : 2K-4K
    356 : 4K-8K
  max: 5249 ms
      Aggregate : 16326062519 ms. Avg size : 73.743
/blockstore/wbcache/op_write_time_total/aggregate 16326062519
/blockstore/wbcache/op_write_time_total/aggregate
16326062519
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/aggregate
16326062519
HERE 
NAME:wbcache
op_write_time_total/aggregate
16326062519
HERE 
NAME:op_write_time_total
aggregate
16326062519
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total/average 73.743
/blockstore/wbcache/op_write_time_total/average
73.743
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/average
73.743
HERE 
NAME:wbcache
op_write_time_total/average
73.743
HERE 
NAME:op_write_time_total
average
73.743
HERE 
Out BEFORE
/blockstore/wbcache/op_write_time_total/nupdates 221391205
/blockstore/wbcache/op_write_time_total/nupdates
221391205
In BEFORE
HERE 
NAME:blockstore
wbcache/op_write_time_total/nupdates
221391205
HERE 
NAME:wbcache
op_write_time_total/nupdates
221391205
HERE 
NAME:op_write_time_total
nupdates
221391205
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk read op hdd time
/blockstore/wbcache/page_read_time_disk read op hdd
time
      2 : 17-32
  max: 22 ms
      Aggregate : 41 ms. Avg size : 20.5
/blockstore/wbcache/page_read_time_disk/aggregate 41
/blockstore/wbcache/page_read_time_disk/aggregate
41
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/aggregate
41
HERE 
NAME:wbcache
page_read_time_disk/aggregate
41
HERE 
NAME:page_read_time_disk
aggregate
41
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk/average 20.5
/blockstore/wbcache/page_read_time_disk/average
20.5
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/average
20.5
HERE 
NAME:wbcache
page_read_time_disk/average
20.5
HERE 
NAME:page_read_time_disk
average
20.5
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_disk/nupdates 2
/blockstore/wbcache/page_read_time_disk/nupdates
2
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_disk/nupdates
2
HERE 
NAME:wbcache
page_read_time_disk/nupdates
2
HERE 
NAME:page_read_time_disk
nupdates
2
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd read op ssd time
/blockstore/wbcache/page_read_time_ssd read op ssd
time
      2 : 0
      1 : 5-8
      1 : 9-16
  max: 14 ms
      Aggregate : 21 ms. Avg size : 5.25
/blockstore/wbcache/page_read_time_ssd/aggregate 21
/blockstore/wbcache/page_read_time_ssd/aggregate
21
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/aggregate
21
HERE 
NAME:wbcache
page_read_time_ssd/aggregate
21
HERE 
NAME:page_read_time_ssd
aggregate
21
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd/average 5.25
/blockstore/wbcache/page_read_time_ssd/average
5.25
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/average
5.25
HERE 
NAME:wbcache
page_read_time_ssd/average
5.25
HERE 
NAME:page_read_time_ssd
average
5.25
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_ssd/nupdates 4
/blockstore/wbcache/page_read_time_ssd/nupdates
4
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_ssd/nupdates
4
HERE 
NAME:wbcache
page_read_time_ssd/nupdates
4
HERE 
NAME:page_read_time_ssd
nupdates
4
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total read op total time
/blockstore/wbcache/page_read_time_total read op total
time
      2 : 0
      1 : 9-16
      3 : 17-32
  max: 25 ms
      Aggregate : 83 ms. Avg size : 13.8333
/blockstore/wbcache/page_read_time_total/aggregate 83
/blockstore/wbcache/page_read_time_total/aggregate
83
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/aggregate
83
HERE 
NAME:wbcache
page_read_time_total/aggregate
83
HERE 
NAME:page_read_time_total
aggregate
83
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total/average 13.8333
/blockstore/wbcache/page_read_time_total/average
13.8333
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/average
13.8333
HERE 
NAME:wbcache
page_read_time_total/average
13.8333
HERE 
NAME:page_read_time_total
average
13.8333
HERE 
Out BEFORE
/blockstore/wbcache/page_read_time_total/nupdates 6
/blockstore/wbcache/page_read_time_total/nupdates
6
In BEFORE
HERE 
NAME:blockstore
wbcache/page_read_time_total/nupdates
6
HERE 
NAME:wbcache
page_read_time_total/nupdates
6
HERE 
NAME:page_read_time_total
nupdates
6
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_slice 3
/blockstore/wbcache/pages_per_slice
3
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_slice
3
HERE 
NAME:wbcache
pages_per_slice
3
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op count of pages per write op
/blockstore/wbcache/pages_per_write_op count of pages per write
op
221391641 : 1
  max: 1 pages
      Aggregate : 221391641 pages. Avg size : 1
/blockstore/wbcache/pages_per_write_op/aggregate 221391641
/blockstore/wbcache/pages_per_write_op/aggregate
221391641
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/aggregate
221391641
HERE 
NAME:wbcache
pages_per_write_op/aggregate
221391641
HERE 
NAME:pages_per_write_op
aggregate
221391641
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op/average 1
/blockstore/wbcache/pages_per_write_op/average
1
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/average
1
HERE 
NAME:wbcache
pages_per_write_op/average
1
HERE 
NAME:pages_per_write_op
average
1
HERE 
Out BEFORE
/blockstore/wbcache/pages_per_write_op/nupdates 221391641
/blockstore/wbcache/pages_per_write_op/nupdates
221391641
In BEFORE
HERE 
NAME:blockstore
wbcache/pages_per_write_op/nupdates
221391641
HERE 
NAME:wbcache
pages_per_write_op/nupdates
221391641
HERE 
NAME:pages_per_write_op
nupdates
221391641
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_dirty_offsets_length 400
/blockstore/wbcache/processor/avg_dirty_offsets_length
400
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_dirty_offsets_length
400
HERE 
NAME:wbcache
processor/avg_dirty_offsets_length
400
HERE 
NAME:processor
avg_dirty_offsets_length
400
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_sync_time 0
/blockstore/wbcache/processor/avg_sync_time
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_sync_time
0
HERE 
NAME:wbcache
processor/avg_sync_time
0
HERE 
NAME:processor
avg_sync_time
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/avg_trim_length 0
/blockstore/wbcache/processor/avg_trim_length
0
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/avg_trim_length
0
HERE 
NAME:wbcache
processor/avg_trim_length
0
HERE 
NAME:processor
avg_trim_length
0
HERE 
Out BEFORE
/blockstore/wbcache/processor/buffer_id 41407808
/blockstore/wbcache/processor/buffer_id
41407808
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/buffer_id
41407808
HERE 
NAME:wbcache
processor/buffer_id
41407808
HERE 
NAME:processor
buffer_id
41407808
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time How long it took to write a page to hdd
/blockstore/wbcache/processor/hdd_write_time How long it took to write a page to
hdd
   8423 : 0
1717047 : 1
22679753 : 2
131236998 : 3-4
13905266 : 5-8
14594790 : 9-16
17100064 : 17-32
13740294 : 33-64
5068788 : 65-128
 964514 : 129-256
 368991 : 257-512
   5985 : 513-1K
  max: 805 ms
      Aggregate : 2491006151 ms. Avg size : 11.2516
/blockstore/wbcache/processor/hdd_write_time/aggregate 2491006151
/blockstore/wbcache/processor/hdd_write_time/aggregate
2491006151
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/aggregate
2491006151
HERE 
NAME:wbcache
processor/hdd_write_time/aggregate
2491006151
HERE 
NAME:processor
hdd_write_time/aggregate
2491006151
HERE 
NAME:hdd_write_time
aggregate
2491006151
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time/average 11.2516
/blockstore/wbcache/processor/hdd_write_time/average
11.2516
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/average
11.2516
HERE 
NAME:wbcache
processor/hdd_write_time/average
11.2516
HERE 
NAME:processor
hdd_write_time/average
11.2516
HERE 
NAME:hdd_write_time
average
11.2516
HERE 
Out BEFORE
/blockstore/wbcache/processor/hdd_write_time/nupdates 221390913
/blockstore/wbcache/processor/hdd_write_time/nupdates
221390913
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/hdd_write_time/nupdates
221390913
HERE 
NAME:wbcache
processor/hdd_write_time/nupdates
221390913
HERE 
NAME:processor
hdd_write_time/nupdates
221390913
HERE 
NAME:hdd_write_time
nupdates
221390913
HERE 
Out BEFORE
/blockstore/wbcache/processor/max_dirty_offsets_length 12226
/blockstore/wbcache/processor/max_dirty_offsets_length
12226
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/max_dirty_offsets_length
12226
HERE 
NAME:wbcache
processor/max_dirty_offsets_length
12226
HERE 
NAME:processor
max_dirty_offsets_length
12226
HERE 
Out BEFORE
/blockstore/wbcache/processor/nr_pages_read 221391197
/blockstore/wbcache/processor/nr_pages_read
221391197
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/nr_pages_read
221391197
HERE 
NAME:wbcache
processor/nr_pages_read
221391197
HERE 
NAME:processor
nr_pages_read
221391197
HERE 
Out BEFORE
/blockstore/wbcache/processor/nr_pages_read_in_mem 220589989
/blockstore/wbcache/processor/nr_pages_read_in_mem
220589989
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/nr_pages_read_in_mem
220589989
HERE 
NAME:wbcache
processor/nr_pages_read_in_mem
220589989
HERE 
NAME:processor
nr_pages_read_in_mem
220589989
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time How long it took to free up pages
/blockstore/wbcache/processor/page_free_time How long it took to free up
pages
     12 : 3-4
     51 : 5-8
    133 : 9-16
    215 : 17-32
    443 : 33-64
    746 : 65-128
   1098 : 129-256
   1174 : 257-512
   1228 : 513-1K
   1464 : 1K-2K
    687 : 2K-4K
      7 : 4K-8K
  max: 4543 ms
      Aggregate : 5510815 ms. Avg size : 759.275
/blockstore/wbcache/processor/page_free_time/aggregate 5510815
/blockstore/wbcache/processor/page_free_time/aggregate
5510815
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/aggregate
5510815
HERE 
NAME:wbcache
processor/page_free_time/aggregate
5510815
HERE 
NAME:processor
page_free_time/aggregate
5510815
HERE 
NAME:page_free_time
aggregate
5510815
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time/average 759.275
/blockstore/wbcache/processor/page_free_time/average
759.275
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/average
759.275
HERE 
NAME:wbcache
processor/page_free_time/average
759.275
HERE 
NAME:processor
page_free_time/average
759.275
HERE 
NAME:page_free_time
average
759.275
HERE 
Out BEFORE
/blockstore/wbcache/processor/page_free_time/nupdates 7258
/blockstore/wbcache/processor/page_free_time/nupdates
7258
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/page_free_time/nupdates
7258
HERE 
NAME:wbcache
processor/page_free_time/nupdates
7258
HERE 
NAME:processor
page_free_time/nupdates
7258
HERE 
NAME:page_free_time
nupdates
7258
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_reads 8
/blockstore/wbcache/processor/pending_reads
8
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_reads
8
HERE 
NAME:wbcache
processor/pending_reads
8
HERE 
NAME:processor
pending_reads
8
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes # write io requests pending at disk, updated after issuing a write request to disk
 228898 : 1
 220774 : 2
 483494 : 3-4
1176762 : 5-8
3415223 : 9-16
16806565 : 17-32
89405907 : 33-64
33713791 : 65-128
24557996 : 129-256
25345596 : 257-512
26036190 : 513-1K
  max: 976 requests
      Aggregate : 41652743108 requests. Avg size : 188.141
/blockstore/wbcache/processor/pending_writes 283
/blockstore/wbcache/processor/pending_writes/aggregate 41652743108
/blockstore/wbcache/processor/pending_writes/aggregate
41652743108
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/aggregate
41652743108
HERE 
NAME:wbcache
processor/pending_writes/aggregate
41652743108
HERE 
NAME:processor
pending_writes/aggregate
41652743108
HERE 
NAME:pending_writes
aggregate
41652743108
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes/average 188.141
/blockstore/wbcache/processor/pending_writes/average
188.141
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/average
188.141
HERE 
NAME:wbcache
processor/pending_writes/average
188.141
HERE 
NAME:processor
pending_writes/average
188.141
HERE 
NAME:pending_writes
average
188.141
HERE 
Out BEFORE
/blockstore/wbcache/processor/pending_writes/nupdates 221391196
/blockstore/wbcache/processor/pending_writes/nupdates
221391196
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/pending_writes/nupdates
221391196
HERE 
NAME:wbcache
processor/pending_writes/nupdates
221391196
HERE 
NAME:processor
pending_writes/nupdates
221391196
HERE 
NAME:pending_writes
nupdates
221391196
HERE 
Out BEFORE
/blockstore/wbcache/processor/read_iops 13671
/blockstore/wbcache/processor/read_iops
13671
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/read_iops
13671
HERE 
NAME:wbcache
processor/read_iops
13671
HERE 
NAME:processor
read_iops
13671
HERE 
Out BEFORE
/blockstore/wbcache/processor/read_throughput 118994008
/blockstore/wbcache/processor/read_throughput
118994008
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/read_throughput
118994008
HERE 
NAME:wbcache
processor/read_throughput
118994008
HERE 
NAME:processor
read_throughput
118994008
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time How long it took to read a page from ssd
/blockstore/wbcache/processor/ssd_read_time How long it took to read a page from
ssd
   1960 : 0
   3803 : 1
   2822 : 2
   9859 : 3-4
  24026 : 5-8
  55418 : 9-16
 258201 : 17-32
 113261 : 33-64
 197854 : 65-128
 134004 : 129-256
  max: 208 ms
      Aggregate : 52904739 ms. Avg size : 66.0312
/blockstore/wbcache/processor/ssd_read_time/aggregate 52904739
/blockstore/wbcache/processor/ssd_read_time/aggregate
52904739
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/aggregate
52904739
HERE 
NAME:wbcache
processor/ssd_read_time/aggregate
52904739
HERE 
NAME:processor
ssd_read_time/aggregate
52904739
HERE 
NAME:ssd_read_time
aggregate
52904739
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time/average 66.0312
/blockstore/wbcache/processor/ssd_read_time/average
66.0312
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/average
66.0312
HERE 
NAME:wbcache
processor/ssd_read_time/average
66.0312
HERE 
NAME:processor
ssd_read_time/average
66.0312
HERE 
NAME:ssd_read_time
average
66.0312
HERE 
Out BEFORE
/blockstore/wbcache/processor/ssd_read_time/nupdates 801208
/blockstore/wbcache/processor/ssd_read_time/nupdates
801208
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/ssd_read_time/nupdates
801208
HERE 
NAME:wbcache
processor/ssd_read_time/nupdates
801208
HERE 
NAME:processor
ssd_read_time/nupdates
801208
HERE 
NAME:ssd_read_time
nupdates
801208
HERE 
Out BEFORE
/blockstore/wbcache/processor/write_iops 13671
/blockstore/wbcache/processor/write_iops
13671
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/write_iops
13671
HERE 
NAME:wbcache
processor/write_iops
13671
HERE 
NAME:processor
write_iops
13671
HERE 
Out BEFORE
/blockstore/wbcache/processor/write_throughput 118993856
/blockstore/wbcache/processor/write_throughput
118993856
In BEFORE
HERE 
NAME:blockstore
wbcache/processor/write_throughput
118993856
HERE 
NAME:wbcache
processor/write_throughput
118993856
HERE 
NAME:processor
write_throughput
118993856
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time read op queued time
/blockstore/wbcache/read_queued_time read op queued
time
      3 : 0
      1 : 3-4
      1 : 5-8
      1 : 9-16
  max: 9 ms
      Aggregate : 20 ms. Avg size : 3.33333
/blockstore/wbcache/read_queued_time/aggregate 20
/blockstore/wbcache/read_queued_time/aggregate
20
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/aggregate
20
HERE 
NAME:wbcache
read_queued_time/aggregate
20
HERE 
NAME:read_queued_time
aggregate
20
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time/average 3.33333
/blockstore/wbcache/read_queued_time/average
3.33333
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/average
3.33333
HERE 
NAME:wbcache
read_queued_time/average
3.33333
HERE 
NAME:read_queued_time
average
3.33333
HERE 
Out BEFORE
/blockstore/wbcache/read_queued_time/nupdates 6
/blockstore/wbcache/read_queued_time/nupdates
6
In BEFORE
HERE 
NAME:blockstore
wbcache/read_queued_time/nupdates
6
HERE 
NAME:wbcache
read_queued_time/nupdates
6
HERE 
NAME:read_queued_time
nupdates
6
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful total unsuccessful page read time
/blockstore/wbcache/total_page_read_time_unsuccessful total unsuccessful page read
time
  max: 0 ms

/blockstore/wbcache/total_page_read_time_unsuccessful/aggregate 0
/blockstore/wbcache/total_page_read_time_unsuccessful/aggregate
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/aggregate
0
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/aggregate
0
HERE 
NAME:total_page_read_time_unsuccessful
aggregate
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful/average NaN
/blockstore/wbcache/total_page_read_time_unsuccessful/average
NaN
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/average
nan
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/average
nan
HERE 
NAME:total_page_read_time_unsuccessful
average
nan
HERE 
Out BEFORE
/blockstore/wbcache/total_page_read_time_unsuccessful/nupdates 0
/blockstore/wbcache/total_page_read_time_unsuccessful/nupdates
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_read_time_unsuccessful/nupdates
0
HERE 
NAME:wbcache
total_page_read_time_unsuccessful/nupdates
0
HERE 
NAME:total_page_read_time_unsuccessful
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful total unsuccessful page write time
/blockstore/wbcache/total_page_write_time_unsuccessful total unsuccessful page write
time
  max: 0 ms

/blockstore/wbcache/total_page_write_time_unsuccessful/aggregate 0
/blockstore/wbcache/total_page_write_time_unsuccessful/aggregate
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/aggregate
0
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/aggregate
0
HERE 
NAME:total_page_write_time_unsuccessful
aggregate
0
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful/average NaN
/blockstore/wbcache/total_page_write_time_unsuccessful/average
NaN
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/average
nan
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/average
nan
HERE 
NAME:total_page_write_time_unsuccessful
average
nan
HERE 
Out BEFORE
/blockstore/wbcache/total_page_write_time_unsuccessful/nupdates 0
/blockstore/wbcache/total_page_write_time_unsuccessful/nupdates
0
In BEFORE
HERE 
NAME:blockstore
wbcache/total_page_write_time_unsuccessful/nupdates
0
HERE 
NAME:wbcache
total_page_write_time_unsuccessful/nupdates
0
HERE 
NAME:total_page_write_time_unsuccessful
nupdates
0
HERE 
Out BEFORE
/blockstore/wbcache/wbc_version 5
/blockstore/wbcache/wbc_version
5
In BEFORE
HERE 
NAME:blockstore
wbcache/wbc_version
5
HERE 
NAME:wbcache
wbc_version
5
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time write op queued time
/blockstore/wbcache/write_queued_time write op queued
time
221391639 : 0
      2 : 1
  max: 1 ms
      Aggregate : 2 ms. Avg size : 9.03376e-09
/blockstore/wbcache/write_queued_time/aggregate 2
/blockstore/wbcache/write_queued_time/aggregate
2
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/aggregate
2
HERE 
NAME:wbcache
write_queued_time/aggregate
2
HERE 
NAME:write_queued_time
aggregate
2
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time/average 9.03376e-09
/blockstore/wbcache/write_queued_time/average
9.03376e-09
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/average
9.03376e-09
HERE 
NAME:wbcache
write_queued_time/average
9.03376e-09
HERE 
NAME:write_queued_time
average
9.03376e-09
HERE 
Out BEFORE
/blockstore/wbcache/write_queued_time/nupdates 221391641
/blockstore/wbcache/write_queued_time/nupdates
221391641
In BEFORE
HERE 
NAME:blockstore
wbcache/write_queued_time/nupdates
221391641
HERE 
NAME:wbcache
write_queued_time/nupdates
221391641
HERE 
NAME:write_queued_time
nupdates
221391641
HERE 
Out BEFORE
/blockstore/workload/pending_pages # user io pages pending when a user read/write req is received
/blockstore/workload/pending_pages # user io pages pending when a user read/write req is
received
  max: 0 pages

/blockstore/workload/pending_pages/aggregate 0
/blockstore/workload/pending_pages/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/aggregate
0
HERE 
NAME:workload
pending_pages/aggregate
0
HERE 
NAME:pending_pages
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/pending_pages/average NaN
/blockstore/workload/pending_pages/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/average
nan
HERE 
NAME:workload
pending_pages/average
nan
HERE 
NAME:pending_pages
average
nan
HERE 
Out BEFORE
/blockstore/workload/pending_pages/nupdates 0
/blockstore/workload/pending_pages/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_pages/nupdates
0
HERE 
NAME:workload
pending_pages/nupdates
0
HERE 
NAME:pending_pages
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/pending_requests # user io requests pending when a user read/write req is received
/blockstore/workload/pending_requests # user io requests pending when a user read/write req is
received
  max: 0 requests

/blockstore/workload/pending_requests/aggregate 0
/blockstore/workload/pending_requests/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/aggregate
0
HERE 
NAME:workload
pending_requests/aggregate
0
HERE 
NAME:pending_requests
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/pending_requests/average NaN
/blockstore/workload/pending_requests/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/average
nan
HERE 
NAME:workload
pending_requests/average
nan
HERE 
NAME:pending_requests
average
nan
HERE 
Out BEFORE
/blockstore/workload/pending_requests/nupdates 0
/blockstore/workload/pending_requests/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/pending_requests/nupdates
0
HERE 
NAME:workload
pending_requests/nupdates
0
HERE 
NAME:pending_requests
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/readop_size size of user read request
/blockstore/workload/readop_size size of user read
request
  max: 0 blocks

/blockstore/workload/readop_size/aggregate 0
/blockstore/workload/readop_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/aggregate
0
HERE 
NAME:workload
readop_size/aggregate
0
HERE 
NAME:readop_size
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/readop_size/average NaN
/blockstore/workload/readop_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/average
nan
HERE 
NAME:workload
readop_size/average
nan
HERE 
NAME:readop_size
average
nan
HERE 
Out BEFORE
/blockstore/workload/readop_size/nupdates 0
/blockstore/workload/readop_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/readop_size/nupdates
0
HERE 
NAME:workload
readop_size/nupdates
0
HERE 
NAME:readop_size
nupdates
0
HERE 
Out BEFORE
/blockstore/workload/writeop_size write request size
/blockstore/workload/writeop_size write request
size
  max: 0 blocks

/blockstore/workload/writeop_size/aggregate 0
/blockstore/workload/writeop_size/aggregate
0
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/aggregate
0
HERE 
NAME:workload
writeop_size/aggregate
0
HERE 
NAME:writeop_size
aggregate
0
HERE 
Out BEFORE
/blockstore/workload/writeop_size/average NaN
/blockstore/workload/writeop_size/average
NaN
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/average
nan
HERE 
NAME:workload
writeop_size/average
nan
HERE 
NAME:writeop_size
average
nan
HERE 
Out BEFORE
/blockstore/workload/writeop_size/nupdates 0
/blockstore/workload/writeop_size/nupdates
0
In BEFORE
HERE 
NAME:blockstore
workload/writeop_size/nupdates
0
HERE 
NAME:workload
writeop_size/nupdates
0
HERE 
NAME:writeop_size
nupdates
0
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs Superseded offset count blocked by the pending superseding page write
/blockstore/write/dirty_superseded_offs Superseded offset count blocked by the pending superseding page
write
  max: 0 offsets

/blockstore/write/dirty_superseded_offs/aggregate 0
/blockstore/write/dirty_superseded_offs/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/aggregate
0
HERE 
NAME:write
dirty_superseded_offs/aggregate
0
HERE 
NAME:dirty_superseded_offs
aggregate
0
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs/average NaN
/blockstore/write/dirty_superseded_offs/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/average
nan
HERE 
NAME:write
dirty_superseded_offs/average
nan
HERE 
NAME:dirty_superseded_offs
average
nan
HERE 
Out BEFORE
/blockstore/write/dirty_superseded_offs/nupdates 0
/blockstore/write/dirty_superseded_offs/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/dirty_superseded_offs/nupdates
0
HERE 
NAME:write
dirty_superseded_offs/nupdates
0
HERE 
NAME:dirty_superseded_offs
nupdates
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes 19356165132
/blockstore/write/nr_blk_writes
19356165132
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes
19356165132
HERE 
NAME:write
nr_blk_writes
19356165132
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_and_stores 0
/blockstore/write/nr_blk_writes_and_stores
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_and_stores
0
HERE 
NAME:write
nr_blk_writes_and_stores
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_in_mem 0
/blockstore/write/nr_blk_writes_in_mem
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_in_mem
0
HERE 
NAME:write
nr_blk_writes_in_mem
0
HERE 
Out BEFORE
/blockstore/write/nr_blk_writes_inherited 0
/blockstore/write/nr_blk_writes_inherited
0
In BEFORE
HERE 
NAME:blockstore
write/nr_blk_writes_inherited
0
HERE 
NAME:write
nr_blk_writes_inherited
0
HERE 
Out BEFORE
/blockstore/write/nr_page_reads_disk_store 0
/blockstore/write/nr_page_reads_disk_store
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_reads_disk_store
0
HERE 
NAME:write
nr_page_reads_disk_store
0
HERE 
Out BEFORE
/blockstore/write/nr_page_reads_rdc_store 0
/blockstore/write/nr_page_reads_rdc_store
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_reads_rdc_store
0
HERE 
NAME:write
nr_page_reads_rdc_store
0
HERE 
Out BEFORE
/blockstore/write/nr_page_stores 0
/blockstore/write/nr_page_stores
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_stores
0
HERE 
NAME:write
nr_page_stores
0
HERE 
Out BEFORE
/blockstore/write/nr_page_stores_denied_ 0
/blockstore/write/nr_page_stores_denied_
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_stores_denied_
0
HERE 
NAME:write
nr_page_stores_denied_
0
HERE 
Out BEFORE
/blockstore/write/nr_page_writes 0
/blockstore/write/nr_page_writes
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_writes
0
HERE 
NAME:write
nr_page_writes
0
HERE 
Out BEFORE
/blockstore/write/nr_page_writes_pending 0
/blockstore/write/nr_page_writes_pending
0
In BEFORE
HERE 
NAME:blockstore
write/nr_page_writes_pending
0
HERE 
NAME:write
nr_page_writes_pending
0
HERE 
Out BEFORE
/blockstore/write/nr_pages_partial 0
/blockstore/write/nr_pages_partial
0
In BEFORE
HERE 
NAME:blockstore
write/nr_pages_partial
0
HERE 
NAME:write
nr_pages_partial
0
HERE 
Out BEFORE
/blockstore/write/nr_pages_superseded 0
/blockstore/write/nr_pages_superseded
0
In BEFORE
HERE 
NAME:blockstore
write/nr_pages_superseded
0
HERE 
NAME:write
nr_pages_superseded
0
HERE 
Out BEFORE
/blockstore/write/op_page_alloc writes: time taken for page alloc
/blockstore/write/op_page_alloc writes: time taken for page
alloc
  max: 0 ms

/blockstore/write/op_page_alloc/aggregate 0
/blockstore/write/op_page_alloc/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/aggregate
0
HERE 
NAME:write
op_page_alloc/aggregate
0
HERE 
NAME:op_page_alloc
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_page_alloc/average NaN
/blockstore/write/op_page_alloc/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/average
nan
HERE 
NAME:write
op_page_alloc/average
nan
HERE 
NAME:op_page_alloc
average
nan
HERE 
Out BEFORE
/blockstore/write/op_page_alloc/nupdates 0
/blockstore/write/op_page_alloc/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_page_alloc/nupdates
0
HERE 
NAME:write
op_page_alloc/nupdates
0
HERE 
NAME:op_page_alloc
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_queued_time writes: time waiting in queue for turn
/blockstore/write/op_queued_time writes: time waiting in queue for
turn
  max: 0 ms

/blockstore/write/op_queued_time/aggregate 0
/blockstore/write/op_queued_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/aggregate
0
HERE 
NAME:write
op_queued_time/aggregate
0
HERE 
NAME:op_queued_time
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_queued_time/average NaN
/blockstore/write/op_queued_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/average
nan
HERE 
NAME:write
op_queued_time/average
nan
HERE 
NAME:op_queued_time
average
nan
HERE 
Out BEFORE
/blockstore/write/op_queued_time/nupdates 0
/blockstore/write/op_queued_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_queued_time/nupdates
0
HERE 
NAME:write
op_queued_time/nupdates
0
HERE 
NAME:op_queued_time
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge writes: time taken for read and merge
/blockstore/write/op_read_n_merge writes: time taken for read and
merge
  max: 0 ms

/blockstore/write/op_read_n_merge/aggregate 0
/blockstore/write/op_read_n_merge/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/aggregate
0
HERE 
NAME:write
op_read_n_merge/aggregate
0
HERE 
NAME:op_read_n_merge
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge/average NaN
/blockstore/write/op_read_n_merge/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/average
nan
HERE 
NAME:write
op_read_n_merge/average
nan
HERE 
NAME:op_read_n_merge
average
nan
HERE 
Out BEFORE
/blockstore/write/op_read_n_merge/nupdates 0
/blockstore/write/op_read_n_merge/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_read_n_merge/nupdates
0
HERE 
NAME:write
op_read_n_merge/nupdates
0
HERE 
NAME:op_read_n_merge
nupdates
0
HERE 
Out BEFORE
/blockstore/write/op_total_time writes: total time taken
/blockstore/write/op_total_time writes: total time
taken
  max: 0 ms

/blockstore/write/op_total_time/aggregate 0
/blockstore/write/op_total_time/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/aggregate
0
HERE 
NAME:write
op_total_time/aggregate
0
HERE 
NAME:op_total_time
aggregate
0
HERE 
Out BEFORE
/blockstore/write/op_total_time/average NaN
/blockstore/write/op_total_time/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/average
nan
HERE 
NAME:write
op_total_time/average
nan
HERE 
NAME:op_total_time
average
nan
HERE 
Out BEFORE
/blockstore/write/op_total_time/nupdates 0
/blockstore/write/op_total_time/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/op_total_time/nupdates
0
HERE 
NAME:write
op_total_time/nupdates
0
HERE 
NAME:op_total_time
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes aligned small or multi-page write
/blockstore/write/rmw/aligned_writes aligned small or multi-page
write
  max: 0 blocks

/blockstore/write/rmw/aligned_writes/aggregate 0
/blockstore/write/rmw/aligned_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/aggregate
0
HERE 
NAME:write
rmw/aligned_writes/aggregate
0
HERE 
NAME:rmw
aligned_writes/aggregate
0
HERE 
NAME:aligned_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes/average NaN
/blockstore/write/rmw/aligned_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/average
nan
HERE 
NAME:write
rmw/aligned_writes/average
nan
HERE 
NAME:rmw
aligned_writes/average
nan
HERE 
NAME:aligned_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/aligned_writes/nupdates 0
/blockstore/write/rmw/aligned_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/aligned_writes/nupdates
0
HERE 
NAME:write
rmw/aligned_writes/nupdates
0
HERE 
NAME:rmw
aligned_writes/nupdates
0
HERE 
NAME:aligned_writes
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece Time gap between old write and new  big write (>=16 sectors)
/blockstore/write/rmw/big_write_time_differece Time gap between old write and new  big write (>=16
sectors)
  max: 0 sec

/blockstore/write/rmw/big_write_time_differece/aggregate 0
/blockstore/write/rmw/big_write_time_differece/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/aggregate
0
HERE 
NAME:write
rmw/big_write_time_differece/aggregate
0
HERE 
NAME:rmw
big_write_time_differece/aggregate
0
HERE 
NAME:big_write_time_differece
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece/average NaN
/blockstore/write/rmw/big_write_time_differece/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/average
nan
HERE 
NAME:write
rmw/big_write_time_differece/average
nan
HERE 
NAME:rmw
big_write_time_differece/average
nan
HERE 
NAME:big_write_time_differece
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/big_write_time_differece/nupdates 0
/blockstore/write/rmw/big_write_time_differece/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/big_write_time_differece/nupdates
0
HERE 
NAME:write
rmw/big_write_time_differece/nupdates
0
HERE 
NAME:rmw
big_write_time_differece/nupdates
0
HERE 
NAME:big_write_time_differece
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/nr_page_reads_disk 0
/blockstore/write/rmw/nr_page_reads_disk
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/nr_page_reads_disk
0
HERE 
NAME:write
rmw/nr_page_reads_disk
0
HERE 
NAME:rmw
nr_page_reads_disk
0
HERE 
Out BEFORE
/blockstore/write/rmw/nr_page_reads_rdc 0
/blockstore/write/rmw/nr_page_reads_rdc
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/nr_page_reads_rdc
0
HERE 
NAME:write
rmw/nr_page_reads_rdc
0
HERE 
NAME:rmw
nr_page_reads_rdc
0
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece Time gap between old write and new  short write(<16 sectors)
/blockstore/write/rmw/small_write_time_differece Time gap between old write and new  short write(<16
sectors)
  max: 0 sec

/blockstore/write/rmw/small_write_time_differece/aggregate 0
/blockstore/write/rmw/small_write_time_differece/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/aggregate
0
HERE 
NAME:write
rmw/small_write_time_differece/aggregate
0
HERE 
NAME:rmw
small_write_time_differece/aggregate
0
HERE 
NAME:small_write_time_differece
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece/average NaN
/blockstore/write/rmw/small_write_time_differece/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/average
nan
HERE 
NAME:write
rmw/small_write_time_differece/average
nan
HERE 
NAME:rmw
small_write_time_differece/average
nan
HERE 
NAME:small_write_time_differece
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/small_write_time_differece/nupdates 0
/blockstore/write/rmw/small_write_time_differece/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/small_write_time_differece/nupdates
0
HERE 
NAME:write
rmw/small_write_time_differece/nupdates
0
HERE 
NAME:rmw
small_write_time_differece/nupdates
0
HERE 
NAME:small_write_time_differece
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes small write at the end of the page or  unaligned multi page write
/blockstore/write/rmw/unaligned_other_writes small write at the end of the page or  unaligned multi page
write
  max: 0 blocks

/blockstore/write/rmw/unaligned_other_writes/aggregate 0
/blockstore/write/rmw/unaligned_other_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/aggregate
0
HERE 
NAME:write
rmw/unaligned_other_writes/aggregate
0
HERE 
NAME:rmw
unaligned_other_writes/aggregate
0
HERE 
NAME:unaligned_other_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes/average NaN
/blockstore/write/rmw/unaligned_other_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/average
nan
HERE 
NAME:write
rmw/unaligned_other_writes/average
nan
HERE 
NAME:rmw
unaligned_other_writes/average
nan
HERE 
NAME:unaligned_other_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes/nupdates 0
/blockstore/write/rmw/unaligned_other_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes/nupdates
0
HERE 
NAME:write
rmw/unaligned_other_writes/nupdates
0
HERE 
NAME:rmw
unaligned_other_writes/nupdates
0
HERE 
NAME:unaligned_other_writes
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset starting offset of (other) unaligned wrtes
/blockstore/write/rmw/unaligned_other_writes_starting_offset starting offset of (other) unaligned
wrtes
  max: 0 block

/blockstore/write/rmw/unaligned_other_writes_starting_offset/aggregate 0
/blockstore/write/rmw/unaligned_other_writes_starting_offset/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/aggregate
0
HERE 
NAME:unaligned_other_writes_starting_offset
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset/average NaN
/blockstore/write/rmw/unaligned_other_writes_starting_offset/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/average
nan
HERE 
NAME:unaligned_other_writes_starting_offset
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_other_writes_starting_offset/nupdates 0
/blockstore/write/rmw/unaligned_other_writes_starting_offset/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:write
rmw/unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:rmw
unaligned_other_writes_starting_offset/nupdates
0
HERE 
NAME:unaligned_other_writes_starting_offset
nupdates
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes small write in the middle of the page
/blockstore/write/rmw/unaligned_within_page_writes small write in the middle of the
page
  max: 0 blocks

/blockstore/write/rmw/unaligned_within_page_writes/aggregate 0
/blockstore/write/rmw/unaligned_within_page_writes/aggregate
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/aggregate
0
HERE 
NAME:write
rmw/unaligned_within_page_writes/aggregate
0
HERE 
NAME:rmw
unaligned_within_page_writes/aggregate
0
HERE 
NAME:unaligned_within_page_writes
aggregate
0
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes/average NaN
/blockstore/write/rmw/unaligned_within_page_writes/average
NaN
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/average
nan
HERE 
NAME:write
rmw/unaligned_within_page_writes/average
nan
HERE 
NAME:rmw
unaligned_within_page_writes/average
nan
HERE 
NAME:unaligned_within_page_writes
average
nan
HERE 
Out BEFORE
/blockstore/write/rmw/unaligned_within_page_writes/nupdates 0
/blockstore/write/rmw/unaligned_within_page_writes/nupdates
0
In BEFORE
HERE 
NAME:blockstore
write/rmw/unaligned_within_page_writes/nupdates
0
HERE 
NAME:write
rmw/unaligned_within_page_writes/nupdates
0
HERE 
NAME:rmw
unaligned_within_page_writes/nupdates
0
HERE 
NAME:unaligned_within_page_writes
nupdates
0
HERE 
Out BEFORE
      Dumping iSCSI Stats
      Dumping MGMT Stats
/mgmt/actionqueue/queue_size 0
/mgmt/actionqueue/queue_size
0
In BEFORE
HERE 
NAME:mgmt
actionqueue/queue_size
0
HERE 
NAME:actionqueue
queue_size
0
HERE 
Out BEFORE
/mgmt/actionstore/queue_size 120
/mgmt/actionstore/queue_size
120
In BEFORE
HERE 
NAME:mgmt
actionstore/queue_size
120
HERE 
NAME:actionstore
queue_size
120
HERE 
Out BEFORE
    Finished dumping external listener.
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi ./sfstats.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi ./sfstats.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi ./sfstats.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi ./sfstats.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ clear

C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ clear



































C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ clear
































C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ ls -lrt
total 2000
-rw-r--r--  1 DTRIPATHI  staff  796328 Aug 28  2016 sdr.stats
-rw-r--r--  1 DTRIPATHI  staff     544 Aug 28  2016 csvview.py
-rw-r--r--  1 DTRIPATHI  staff     188 Aug 28  2016 walktest.py
-rw-r--r--  1 DTRIPATHI  staff    2672 Aug 28  2016 topstats.py
-rw-r--r--  1 DTRIPATHI  staff     295 Aug 28  2016 test.py
-rw-r--r--  1 DTRIPATHI  staff    2137 Aug 28  2016 sdrstats.py
-rwxr-xr-x  1 DTRIPATHI  staff    4952 Aug 28  2016 plot.py
-rw-r--r--  1 DTRIPATHI  staff    1852 Aug 28  2016 messages.py
-rw-r--r--  1 DTRIPATHI  staff    1004 Aug 28  2016 gnuplot.py
-rw-r--r--  1 DTRIPATHI  staff    2207 Aug 28  2016 exhibit.py
-rw-r--r--  1 DTRIPATHI  staff     276 Aug 28  2016 dygraph.py
-rw-r--r--  1 DTRIPATHI  staff   67192 Aug 28  2016 edge.stats
-rw-r--r--  1 DTRIPATHI  staff    2967 Sep 16  2016 topstats.pyc
-rw-r--r--  1 DTRIPATHI  staff    3707 Sep 16  2016 sdrstats.pyc
-rw-r--r--  1 DTRIPATHI  staff    2229 Sep 16  2016 messages.pyc
-rw-r--r--  1 DTRIPATHI  staff    1359 Sep 16  2016 gnuplot.pyc
-rw-r--r--  1 DTRIPATHI  staff    1978 Sep 16  2016 exhibit.pyc
-rw-r--r--  1 DTRIPATHI  staff     602 Sep 16  2016 dygraph.pyc
-rw-r--r--  1 DTRIPATHI  staff   40179 Sep 16  2016 x
-rw-r--r--  1 DTRIPATHI  staff    3949 Sep 16  2016 stats.py
-rw-r--r--  1 DTRIPATHI  staff    6061 Sep 16  2016 stats.pyc
-rw-r--r--  1 DTRIPATHI  staff   22347 Sep 17  2016 ed.stats
-rwxr-xr-x  1 DTRIPATHI  staff    2518 Sep 19  2016 sfstats.py
-rwxr-xr-x  1 DTRIPATHI  staff     660 Sep 22  2016 pp.py
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi messages.py
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi test.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi sfstats.py 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi stats.py
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ clear

C02RX1E4G8WL-MAC:mystats DTRIPATHI$ 
C02RX1E4G8WL-MAC:mystats DTRIPATHI$ vi stats.py




































































import math

def get_item(collection, path, delimiter="/"):
   name, sep, rest = path.partition(delimiter)
   if collection.name != name:
      raise ValueError()
   if rest == "":
      return collection
   else:
      return collection.get_item(rest, delimiter)

class Item:
   def __init__(self, name, parent, source=None):
      self.name = name
      self.parent = parent
      self.source_ = source

   def full_name(self, delimiter="/"):
      if self.parent is None:
         return self.name
      else:
         return self.parent.full_name(delimiter) + delimiter + self.name

   def source(self):
      if self.source_ is not None or self.parent is None:
         return self.source_
      else:
         return self.parent.source()

   def __repr__(self):
      return "Item(" + ", ".join([
         repr(self.name), repr(self.parent), repr(self.source_)]) + ")"

class Collection(Item):
   def __init__(self, name, parent=None, source=None):
      Item.__init__(self, name, parent, source)
      self.items = dict()

   def add_item(self, item):
      self.items[item.name] = item
      item.parent = self

   def add_value(self, path, date, value, delimiter="/"):
      print "HERE "
      if path[0] == delimiter:
         path = path[1:]
      name, sep, path = path.partition(delimiter)
      if path == "":
         if name not in self.items:
            self.items[name] = Stat(name, self)
         self.items[name].add_value(date, value)
      else:
         if name not in self.items:
            self.items[name] = Collection(name, self)
         print 'NAME:' + name
         print path
         print value
         self.items[name].add_value(path, date, value, delimiter)

   def all_stats(self, delimiter = "/"):
      for item in self.items.itervalues():
         if hasattr(item, "values"):
            yield (self.name, item)
         if hasattr(item, "all_stats"):
            for (path, stat) in item.all_stats(delimiter):
               yield (self.name + delimiter + path, stat)
               
      def get_item(self, path, delimiter="/"):
      name, sep, rest = path.partition(delimiter)
      if rest == "":
         return self.items[name]
      else:
         return self.items[name].get_item(rest, delimiter)


class Stat(Item):
   def __init__(self, name, parent):
      Item.__init__(self, name, parent)
      self.value_map = dict()

   def values(self):
      return self.value_map.itervalues()

   def number_values(self):
      for value in self.values():
         if not math.isnan(value):
            yield value

   def pairs(self):
      for date in sorted(self.value_map.iterkeys()):
         yield (date, self.value_map[date])

   def add_value(self, date, value):
      if date in self.value_map:
         return
         raise Exception("A value already exists for this date " + str(date)
               + " stat: " + self.full_name() +
               " exisiting: " + str(self.value_map[date]) +
               " new: " + str(value))
      self.value_map[date] = value

   def value_average(self):
      count = len([x for x in self.number_values()])
      if count == 0:
         return None
      return self.value_sum() / float(count)

   def value_maximum(self):
      try:
         return max(self.number_values())
      except ValueError:
         return None

   def value_minimum(self):
      try:
         return min(self.number_values())
      except ValueError:
         return None

   def value_sum(self):
      total = 0
      for value in self.number_values():
         total += value
      return total
   def value_count(self):
      return len(self.value_map)

   def nonzero(self):
      for number in self.number_values():
         if number != 0:
            return True
      return False
