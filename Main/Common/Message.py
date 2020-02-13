'''
Created on 2020年2月13日

@author: sherl
'''
import json

#心跳、出牌、判定牌、发牌、回合开始、回合结束、游戏开始、游戏结束、发动技能、发动装备
msg_types=['heartbeat', 'playcard', 'judgement', 'getcard', 'roundstart', 'roundend', 'gamestart', 'gameend', 'skillstart', 'equipstart']



def form_msg(msg_name, start=None, end=None, third=None, forth=None, fifth=None, reply=True):
    kep={'msg_name':msg_name,
         'start':start,
         'end':end,
         'third':third,
         'forth':forth,
         'fifth':fifth,
         'reply':reply
        }
    return json.dumps(kep)

def form_heartbeat(reply=True):
    return form_msg(msg_types[0], reply=reply)












if __name__ == '__main__':
    tep=form_msg('test')
    print(tep)
    print (type(json.loads(tep)))