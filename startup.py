# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:55:43 2019

@author: wong.w.14
"""

import platform
import sys
import time

#check is pip is installed 
try:
    import pip
except:
    print("pip not installed.")
    print("execute before re-run: $sudo apt install python3-pip")
    print("Logs will not be created")
    raise

#Check computer physical harware components and operating system
def hardwareCheck():
    import psutil
    print('Checking hardware')
    count = psutil.cpu_count(logical = False) #Physical core count
    freq = psutil.cpu_freq()[2] #Core base frequency clock speed
    mem = psutil.virtual_memory()[0] #System total memory
    
    failCount = 0
    
    print("Platform:\t{}".format(platform.system())) #Get Operating System
    
    if count < 8: #Restrict system with less than 8 physical core
        print("Core count:\t" + str(count) + " (LOW CORE COUNT!)")
        failCount = failCount + 1
    else:
        print("Core count:\t" + str(count))
        
    if freq < 3500: #Restrict system with base clock speed of 3.5 GHz
        print("Base clock:\t" + str(round(freq*pow(10,-3),1)) + "0 GHz (LOW CPU BOOST CLOCK!)")
        failCount = failCount + 1
    else:
        print("Base clock:\t" + str(round(freq*pow(10,-3),1)) + "0 GHz")
        
    if mem < 15000000000: #Restrict user with less than 16 GB of ram (15GB of ram is assigned as not all '16GB ram' is true 16GB, some might be 15.4GB)
        print("Memory:\t\t" + str(round(mem*pow(10,-9))) + " GB (LOW MEMORY!)")
        failCount = failCount + 1
    else:
        print("Memory:\t\t" + str(round(mem*pow(10,-9))) + " GB")
    
    userIn = 'n'
    
    if failCount != 0:
        userIn = input("PC does not hit the system requirement. Continue(Y/N)?")
    
    if (not(('y' == userIn) or ('Y' == userIn))) and (failCount != 0):
        print("\nSystem Exited. There are no critical exceptions. Ignore warnings\n")
        sys.exit()
    
    print('Check completed')
    
    return psutil.cpu_count(logical = True), str(platform.system()), str(round(freq*pow(10,-3),1)) + '0 GHz', str(round(mem*pow(10,-9)))+ " GB"

#pip package installer
def install(package):
    try:
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])
    except:
        print("pip install depreciated in {}. Please downgrade to version 9.0.3".format(pip.__version__))
        print("Logs will not be created")
        raise

#pip package upgrader
def upgrade(package):
    try:
        if hasattr(pip, 'main'):
            pip.main(['install','--upgrade', package])
        else:
            pip._internal.main(['install', '--upgrade', package])
    except:
        print("pip install depreciated in {}. Please downgrade to version 9.0.3".format(pip.__version__)) 
        print("Logs will not be created")
        raise

#pip package remover
def remove(package):
    try:
        if hasattr(pip, 'main'):
            pip.main(['uninstall', '-y', package])
        else:
            pip._internal.main(['uninstall', '-y', package])
    except:
        print("pip install depreciated in {}. Please downgrade to version 9.0.3".format(pip.__version__)) 
        print("Logs will not be created")
        raise
  
#package checker      
def packageCheck():        
    print('Checking packages and versions')
    
    missing = 0
    
    try:
        import numpy as np
        import pandas as pd
        import psutil
        import tsfresh
        import plotly
        
        print("numpy: {}".format(np.__version__))
        print("pandas: {}".format(pd.__version__))
        print("psutil: {}".format(psutil.__version__))
        print("tsfresh: {}".format(tsfresh.__version__))
        print("plotly: {}".format(plotly.__version__))
        
        if '0.23.4' not in pd.__version__:
            0/0
    except:
        print('\nKey packages not found/Wrong Versions. Cleaning...\n')
        time.sleep(1)
        missing = 1
    try:
        if missing == 1:
            piplist = sorted(["%s" % (i.key) for i in pip.get_installed_distributions()])
            
            #WARNING DO NOT EDIT THIS LINE OF CODE: SEGMENTATION FAULT MAY OCCUR
            #clean all related packages by removal
            toClear = "attrs,Click,cloudpickle,dask,decorator,distributed,future,HeapDict,ipython-genutils,joblib,jsonschema,jupyter-core,msgpack,nbformat,numpy,pandas,patsy,plotly,psutil,pyrsistent,python-dateutil,retrying,scikit-learn,scipy,sortedcontainers,statsmodels,tblib,toolz,tornado,tqdm,traitlets,tsfresh,zict"
            
            toClearlist = toClear.split(',')
            
            intClear = [x for x in piplist if x in toClearlist]
            
            for pack in intClear:
                remove(pack)
            
            #Installing packages that is important
            print('\nInstalling...\n')
            
            time.sleep(1)
            
            install('numpy')
            install('pandas==0.23.4')
            install('psutil')
            install('tsfresh')
            install('plotly')
            
            print('\nInstallation Completed')
            print('Re-run: $sudo python3 UserInterface.py')
            sys.exit()
        else:
            print("Check completed")
    except:
        print("pip install depreciated in {}. Please downgrade to version 9.0.3".format(pip.__version__)) 
        print("execute before re-run: $pip3 install --user --upgrade pip==9.0.3")
        print("Logs will not be created")
        sys.exit()
        
if __name__ == '__main__':
    packageCheck()