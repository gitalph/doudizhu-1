import unittest
from doudizhu import Doudizhu
import requests
import json

def toIndx(cards):
    # pokers = [i for i in range(52)]

    hand = []
    for card in cards:
        if card == 'BJ':
            hand.append(53)
            continue
        if card == 'CJ':
            hand.append(54)
            continue
        i = 1 + 'A234567890JQK'.index(card)
        while i in hand:
            i += 13
        hand.append(i)
    return hand

class TestDoudizhu(unittest.TestCase):
    def setUp(self):
        Doudizhu.init_doudizhu_dict()
        self.assertEqual(Doudizhu.TOTAL, 34152)

    def test_list_bots(self):
        cnt = 0
        url = 'http://192.168.1.47:8180/select_combination'
        headers = {'Content-type': 'application/json',
                'Accept': 'text/plain',
                'Content-Encoding': 'utf-8'}
        for item in Doudizhu.DATA:
            result = Doudizhu.check_card_type(item)
            if result[0]:
                d = {"hand" : toIndx(item.replace('10', '0').split('-'))}
                answer = requests.post(url, data=json.dumps(d), headers=headers)
                response = answer.json()
                if response['result'] == 'ERROR':
                    print(item, d)
                    cnt += 1           
        print(len(Doudizhu.DATA), Doudizhu.TOTAL, cnt, len(Doudizhu.DATA) - cnt)
        self.assertEqual(cnt, 0)

if __name__ == '__main__':
    unittest.main()
    
