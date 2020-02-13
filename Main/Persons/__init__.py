#coding:utf-8
'''
Created on 2020年2月12日

@author: sherl
'''

import os
import importlib

print ('Persons imported',os.getcwd(),__file__)

abspath=os.path.abspath(__file__)

def get_modules(package=os.path.dirname(abspath)):
    """
    : 获取包名下所有非__init__的模块名
    """
    modules = []
    files = os.listdir(package)

    for file in files:
        if file.startswith('person'):
            name, ext = os.path.splitext(file)
            modules.append(name)

    return modules

modules_list=get_modules()

class_list=[   getattr( importlib.import_module('.'+x, 'Persons'), x  )    for x in modules_list]
#print (class_list)
