#coding:utf-8
'''
Created on 2020年2月14日

@author: sherl
'''
import Persons



class base:
    cards_num_color=[0,0,0,0] #黑桃、梅花、红心、方片
    active=None    #能主动被出牌吗[true, false, none]
    name='base'
    
    scop=1  #手长 
    
    def __init__(self):
        pass
    
    @classmethod
    def cal_active(cls, person):
        tep=cls.active
        if tep is None:#不确定,以桃的处理为例
            if person.health<person.blood:
                tep= True
        return tep

    











if __name__ == '__main__':
    tep=base()