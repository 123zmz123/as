__header = '''/**
 * AS - the open source Automotive Software on https://github.com/parai
 *
 * Copyright (C) 2015  AS <parai@foxmail.com>
 *
 * This source code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 as published by the
 * Free Software Foundation; See <http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt>.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * for more details.
 */
'''
import os,sys
from argen.KsmGen import *
from argen.OsGen import *
from argen.ArGen import *

__gen__ = [KsmGen,OsGen]

def SetDefaultRTOS(name):
    SetOS(name)

def XCC(gendir, modules=None):
    if(not os.path.exists(gendir)):os.mkdir(gendir)
    for g in __gen__:
        print('  %s ...'%(g.__name__))
        g(gendir)
    if(modules is not None):
        fp = open('%s/asmconfig.h'%(gendir),'w')
        fp.write('#ifndef _AS_MCONF_H_\n\n')
        for m in modules:
            fp.write('#ifndef USE_%s\n#define USE_%s\n#endif\n\n'%(m,m))
        fp.write('#endif /* _AS_MCONF_H_ */\n')
        fp.close()
            
    
if(__name__ == '__main__'):
    gendir = os.path.abspath(sys.argv[1])
    if(sys.argv[2]=='true'): # generate bsw
        ArGenMain('%s/autosar.arxml'%(gendir),gendir)
    else:
        XCC(gendir)
        print('  >> XCC %s/*.xml done.'%(gendir))
    