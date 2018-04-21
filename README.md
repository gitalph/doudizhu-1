# 斗地主引擎

枚举了37种细分牌型，制作一个花色无关、顺序无关的字典，能够在O(1)时间内判断出牌是否有效，在O(1)时间内比较大小。

扑克出牌是54张牌的组合，牌型和排列顺序无关，在斗地主游戏中，牌型及大小和花色无关，两个王不算对子。

[详细文档](docs/engine.md)

## Quickstart

### Installing

`pip install doudizhu`

or

- git clone https://github.com/onestraw/doudizhu
- cd doudizhu && pip install .

### 开始一局游戏
```python
>>> import doudizhu
>>> from doudizhu import Card
>>> cards_groups = doudizhu.new_game()
>>>
>>> cards_groups
[[44, 28, 27, 43, 42, 72, 39, 38, 37, 69, 132, 131, 19, 34, 66, 65, 33], [14, 75, 139, 138, 26, 25, 137, 23, 71, 135, 134, 20, 67, 130, 17, 16, 128], [13, 140, 76, 74, 41, 24, 22, 70, 133, 21, 68, 36, 35, 18, 129, 64, 32], [73, 40, 136]]
>>> for cards_group in cards_groups:
...     Card.print_pretty_cards(cards_group)
...
  [ 2 ❤ ] , [ 2 ♠ ] , [ A ♠ ] , [ A ❤ ] , [ K ❤ ] , [ J ♦ ] , [ 10 ❤ ] , [ 9 ❤ ] , [ 8 ❤ ] , [ 8 ♦ ] , [ 7 ♣ ] , [ 6 ♣ ] , [ 6 ♠ ] , [ 5 ❤ ] , [ 5 ♦ ] , [ 4 ♦ ] , [ 4 ❤ ]
  [ CJ  ] , [ A ♦ ] , [ A ♣ ] , [ K ♣ ] , [ K ♠ ] , [ Q ♠ ] , [ Q ♣ ] , [ 10 ♠ ] , [ 10 ♦ ] , [ 10 ♣ ] , [ 9 ♣ ] , [ 7 ♠ ] , [ 6 ♦ ] , [ 5 ♣ ] , [ 4 ♠ ] , [ 3 ♠ ] , [ 3 ♣ ]
  [ BJ  ] , [ 2 ♣ ] , [ 2 ♦ ] , [ K ♦ ] , [ Q ❤ ] , [ J ♠ ] , [ 9 ♠ ] , [ 9 ♦ ] , [ 8 ♣ ] , [ 8 ♠ ] , [ 7 ♦ ] , [ 7 ❤ ] , [ 6 ❤ ] , [ 5 ♠ ] , [ 4 ♣ ] , [ 3 ♦ ] , [ 3 ❤ ]
  [ Q ♦ ] , [ J ❤ ] , [ J ♣ ]
```

### 检查牌型
```python
>>> test_chain = [Card.new(card_str) for card_str in ['3c', '4d', '5h', '6s', '7s', '8h']]
>>>
>>> test_four_two = [Card.new(card_str) for card_str in ['2c', '2d', '2h', '2s', 'BJ', 'CJ']]
>>>
>>> doudizhu.check_card_type(test_four_two)
(True, [('four_two_solo', 13)])
>>> doudizhu.check_card_type(test_chain)
(True, [('solo_chain_6', 0)])
>>> doudizhu.check_card_type(test_chain[:4])
(False, ValueError('invalid card type',))
```

### 比较大小
```python
>>> chain = [Card.new(card_str) for card_str in ['3c', '4d', '5h', '6s', '7s', '8h', '9h']]
>>> bomb = [Card.new(card_str) for card_str in ['8h', '8s', '8d', '8c']]
>>> rocket = [Card.new(card_str) for card_str in ['BJ', 'CJ']]
>>>
>>> doudizhu.cards_greater(chain, chain)
(False, 'solo_chain_7')
>>> doudizhu.cards_greater(chain[:6], chain[1:7])
(False, 'solo_chain_6')
>>>
>>> doudizhu.cards_greater(chain[1:7], chain[:6])
(True, 'solo_chain_6')
>>> doudizhu.cards_greater(bomb, chain)
(True, 'bomb')
>>> doudizhu.cards_greater(rocket, bomb)
(True, 'rocket')
```

### 牌型提示
```python
>>> import doudizhu
>>> from doudizhu import Card
>>>
>>> def CardStrListToCardIntList(cards):
...     return [Card.new(card_str) for card_str in cards]
...
>>>
>>> def PrettyPrint(cards_gt):
...     for card_type, cards_list in cards_gt.iteritems():
...         print 'card type: {}'.format(card_type)
...         for card_int in cards_list:
...             Card.print_pretty_cards(list(card_int))
...
>>>
>>> cards_candidate = CardStrListToCardIntList(['CJ', 'Ah', 'As', 'Ac', 'Kh', 'Qs', 'Jc', '10h', '10s', '10c', '10d', '9h', '7c', '7d', '5c', '5s'])
>>> cards_two = CardStrListToCardIntList(['Jh', 'Jc'])
>>> cards_chain_solo = CardStrListToCardIntList(['5h', '6h', '7s', '8c', '9d'])
>>> cards_trio_two = CardStrListToCardIntList(['6h', '6s', '6c', '3d', '3c'])
>>>
>>> PrettyPrint(doudizhu.list_greater_cards(cards_two, cards_candidate))
card type: pair
  [ A ♠ ] , [ A ❤ ]
card type: bomb
  [ 10 ♦ ] , [ 10 ♠ ] , [ 10 ♣ ] , [ 10 ❤ ]
>>>
>>> PrettyPrint(doudizhu.list_greater_cards(cards_chain_solo, cards_candidate))
card type: solo_chain_5
  [ K ❤ ] , [ Q ♠ ] , [ J ♣ ] , [ 10 ❤ ] , [ 9 ❤ ]
  [ A ❤ ] , [ K ❤ ] , [ Q ♠ ] , [ J ♣ ] , [ 10 ❤ ]
card type: bomb
  [ 10 ♦ ] , [ 10 ♠ ] , [ 10 ♣ ] , [ 10 ❤ ]
>>>
>>> PrettyPrint(doudizhu.list_greater_cards(cards_trio_two, cards_candidate))
card type: trio_pair
  [ A ♠ ] , [ A ❤ ] , [ 10 ♠ ] , [ 10 ♣ ] , [ 10 ❤ ]
  [ 10 ♠ ] , [ 10 ♣ ] , [ 10 ❤ ] , [ 5 ♠ ] , [ 5 ♣ ]
  [ 10 ♠ ] , [ 10 ♣ ] , [ 10 ❤ ] , [ 7 ♦ ] , [ 7 ♣ ]
  [ A ♠ ] , [ A ❤ ] , [ A ♣ ] , [ 10 ♠ ] , [ 10 ❤ ]
  [ A ♠ ] , [ A ❤ ] , [ A ♣ ] , [ 5 ♠ ] , [ 5 ♣ ]
  [ A ♠ ] , [ A ❤ ] , [ A ♣ ] , [ 7 ♦ ] , [ 7 ♣ ]
card type: bomb
  [ 10 ♦ ] , [ 10 ♠ ] , [ 10 ♣ ] , [ 10 ❤ ]
```
