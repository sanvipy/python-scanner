# python-scanner
This project scans a given directory for user provided keys


Setting up local environment
1. Checkout https://github.com/sanvipy/python-scanner.git
2. In \python-scanner, run Vagant up
3. Vagrant ssh


Arguments

-d --rootdir, Directory to scan. Optional, Defaults to \python-scanner\data 

-k --keys, Keys to scan for in rootdir. Optional, Defaults to TODO

-i --ignoreList, Folder to exclude scan from. Optional, Defaults to .git

Usage: python scanner.py

Output: Reports generated under the folder \python-scanner\reports 

Note: 
Recommended to configure the build system to copy or checkout the target project source code to \python-scanner\data and pass the folder name as run time argument.

Sample: To Scan all folders under \python-scanner\data\sample-project looking for keys TODO and FIXME, excludng the folder .git 
python scanner.py -d data/sample-project -k TODO FIXME -i .git

Unit test 
location: python-scanner\tests\testRunr.py
Run: python testRunr.py




