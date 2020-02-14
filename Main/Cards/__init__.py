#coding:utf-8
'''
Created on 2020年2月12日

@author: sherl
'''

import os
import importlib

print ('Cards imported',os.getcwd(),__file__)

abspath=os.path.abspath(__file__)
absdir=os.path.dirname(abspath)
package_name=os.path.split(absdir)[-1]

def get_modules(package=absdir):
    """
    : 获取包名下所有非__init__的模块名
    """
    modules = []
    files = os.listdir(package)

    for file in files:
        if file.startswith('card'):
            name, ext = os.path.splitext(file)
            modules.append(name)

    return modules

modules_list=get_modules()

class_list=[   getattr( importlib.import_module('.'+x, package_name), x  )    for x in modules_list]
#print (class_list)