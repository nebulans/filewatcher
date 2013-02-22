# -*- coding: utf-8 -*-

#Copyright (c) 2013 Tim Davies
#Released under the MIT licence

import os
import settings
import time
import shutil


for d in settings.directories:
    contents = os.listdir(d)
    files = []
    dirs = []
    for i in contents:
        if "~" in i:
            continue
        p = os.path.join(d, i)
        if os.path.isdir(p):
            dirs.append(p)
        else:
            files.append(p)
    for f in files:
        bd = f+settings.extension
        if not bd in dirs:
            os.mkdir(bd)
        mtime = os.path.getmtime(f)
        ts = time.strftime("%Y-%m-%d-%H%M", time.gmtime(mtime))
        e = f.split(".")[-1]
        ss = ".".join([ts, e])
        if not ss in os.listdir(bd):
            shutil.copyfile(f, os.path.join(bd, ss))
            print "Backed up %s"%f
        else:
            print "%s unchanged"%f
        
#    root, dirs, files = os.walk(d)
#    print root
#    print dirs
#    print files