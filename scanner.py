
import json
import os
import argparse
import logging
from helpers.loghelper import *

logger = LogHelper.createlogger()

class scanner:
    """
    Scans all files in a directory and its subfolders for keys

    Manadatory Arguments
        rootdir - Directory to scan

    optional Arguments
        keys        -  List of key words to scan for
                       Default to TODO: and FIXME:
        ignorelist  - List of files and folders to exclude while scanning
                      Defaults to .git   

    """
    def __init__(self,rootdir,keys=['TODO:','FIXME:'],ignorelist=['.git']):
        self.rootdir = rootdir
        self.keys = keys
        self.ignorelist = ignorelist

    def build_files_set(self):
        """ 
        Returns a set containing all files with path under rootdir

        Mandatory args
        rootdir
        """  

        try:
            files_set = set()
            for(dirpath,dirnames,filenames) in os.walk(self.rootdir):
                for filename in filenames + dirnames:
                    full_path = os.path.join(dirpath, filename)
                    relative_path = os.path.relpath(full_path, self.rootdir)
                    files_set.add(relative_path)
            return files_set
        except Exception as e:
            logger.error('Error: Unable to build files set '+str(e))

    def remove_ignorelist(self,dir_files):
        ignore_set = set()
        for dir_item in dir_files:
            for ignore in self.ignorelist:
                if ignore+'\\' in dir_item:
                    ignore_set.add(dir_item)

        if ignore_set:
            logger.info('Following directories will not be scanned')
            for item in ignore_set:
                logger.info(item)
        return dir_files - ignore_set

    def scan(self):
        logger.info('Scanning for {0} in files under {1}'.format(self.keys,self.rootdir))
        dir_files = self.remove_ignorelist(self.build_files_set())
        results = []

        if os.path.isdir(self.rootdir):
            logger.info('\n-----Scanning--------------------')
            for member in dir_files:
                full_path = os.path.join(self.rootdir, member)
                if os.path.isfile(full_path):
                    with open(full_path) as file:    
                        for num, line in enumerate(file, 1):
                            for key in self.keys:    
                                if key in line:
                                    logger.info('{0}, line {1}'.format(full_path,num))
                                    logger.info((key + line.split(key)[-1]))
                                    results.append(member)
            return results
        else:
            logger.error('Not a valid folder: '+self.rootdir)

parser = argparse.ArgumentParser("Read root dir and keys to scan for")
parser.add_argument('-d','--rootdir',help="Directory path to scan",default="data")
parser.add_argument('-k','--keys',nargs='+', help="List of keys to scan for",default=['TODO:'])
parser.add_argument('-i','--ignoreList',nargs='+',help="List of folders to ignore",default=['.git'])
args = vars(parser.parse_args())

if __name__ == '__main__':
    new = scanner(args['rootdir'],args['keys'],args['ignoreList'])
    new.scan()    
