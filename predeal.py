#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-

import sys
import re
import os

reload(sys)
sys.setdefaultencoding("utf-8")

ReString = '-*\d+\.?\d*[e]*-*\d*'
ComRe = re.compile(ReString)


def CollectData(FileName):
    data = []
    with open(FileName, 'r') as FileRead:
        for line in FileRead:
            try:
                nums = re.findall(ComRe, line)
                if 'value' in line:
                    continue
                if len(nums) != 3:
                    continue
                data.append('\t'.join(nums))
            except:
                pass
    return data


def getfiles(fPath):
    files = os.listdir(fPath)
    retfiles = []
    for eachfile in files:
        pwdpath = os.path.join(fPath, eachfile)
        if os.path.isfile(pwdpath):
            retfiles.append(pwdpath)
    return retfiles


def writefile(filename, data):
    with open(filename+'new', 'wb') as writefile:
        for line in data:
            print >> writefile, line
    return True

if __name__ == "__main__":
    FilePath = raw_input("Please input the path of the files:")
    files = getfiles(FilePath)
    for eachfile in files:
        try:
            data = CollectData(eachfile)
            writefile(eachfile, data)
        except:
            print eachfile
