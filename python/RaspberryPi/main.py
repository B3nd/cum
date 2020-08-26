import time
import vk_api as v

vk = v.VkApi(token = 'd87c8cc59a0fbeed9d41531f8dd54f1f6fd50d0b200345dfd09d0a8fe0208cd7c7fb833940496c5934ef7')
'''
param = {
    'count' : 1,
    'time_offset' : 5, 
    'filter' : 'unread'
}'''

def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id' : user_id,
        'message' : msg, 
        'random_id' : random
    })

#print('\n\nStarting working...\n\n')

#num = int(input())

num = 5

'''
while 1:
    response = vk.method('messages.getConversations', param)
    if response['items']:
        item = response['items'][0]
        last_mess = item['last_message']
        random = last_mess['random_id']
        my_id = last_mess['peer_id']
        text = last_mess['text']
        
        #write_msg(my_id, text, random)
        print(str(my_id) + ' wrote ' + text)
        
        write_msg(349142579, text, random)
    time.sleep(1)
'''
def w():
    write_msg(349142579, 'cum', 0)
for i in range (num):
    w()