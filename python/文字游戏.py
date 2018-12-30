from sys import exit
from random import randint
from textwrap import dedent

class scene(object):
    def enter(self):
        print("你输了")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):  # 初始化传入一个Map类的对象
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene=self.scene_map.next_scene('finished')

        while current_scene!=last_scene:

            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            current_scene.enter()


class road(scene):
    def enter(self):
        print("""
        你进入了一个黑暗山洞。
        你的选择是 点亮火把 or 逃跑
        """)

        choice=input('>')

        if choice=='逃跑':
            return 'over'
        elif choice=='点亮火把':
            print('前方有两条路，左和右，你的选择是？')
            choice2=input('>')

            if choice2=='左':
                return 'left'
            elif choice2=='右':
                return 'right'
            else:
                print("你只有这两条路")
                choice2=input('>')

        else:
            print("你只有这两条路")
            choice = input('>')

class left(scene):
    def enter(self):
        print('你遇到了一头巨熊，它正在睡觉，路被它挡着，你准备怎么做？,beat it or fire it?')
        choice=input('>')

        if choice=='beat it':
            print('你怎么可能是熊的对手？？')
            return 'over'
        elif choice=='fire it':
            print('恭喜你，收货一顿烤熊肉！')
            return 'gate'
        else:
            print('小老弟，你没有退路了，选择吧')
            choice=input('>')

class right(scene):
    def enter(self):
        print('你遇到了传说中的美杜莎，她在向你抛媚眼，你的选择是？鱼水之欢 or 无视她')
        choice=input('>')

        if choice=='鱼水之欢':
            print('在历经艰险之后你重获力量，你可以进入下一个藏宝室了')
            return 'gate'

        elif choice=='无视她':
            print('美杜莎感到自己被羞辱了，把你变成了石头..')
            return 'over'

        else:
            print('美杜莎在看着你，快做选择吧')
            choice=input('>')

class presure(scene):
    def enter(self):
        print('你终于来到了山顶，眼前是一对金银珠宝，你是 全都要 or 两袖清风')
        choice=input('>')

        if choice == '全都要':
            print('恭喜你成为了宇宙首富')
            return 'finished'

        elif choice == '两袖清风':
            print('好吧，你白跑了一趟，最后因付不起路费 die!')
            return 'over'

        else:
            print('你还在等什么')
            choice = input('>')

class gate(scene):
    def enter(self):
        print('你碰到了一扇大门，上面有一个密码锁，请输入密码:')
        choice=input('>')

        while choice!='2666':
            print('快换一个密码试试，否则你要困死在这里了')
            choice=input('>')

        print('大门缓缓开启...')
        return 'presure'

class over(scene):
    def over(self):
        print('too yong too simple')

class finished(scene):
    def enter(self):
        print('你赢了')
        return 'finished'

class map(object):
    scene={
        'road':road(),
        'over':over(),
        'left':left(),
        'right':right(),
        'gate':gate(),
        'presure':presure(),
        'finished':finished()
    }


    def __init__(self, start_sence):  # 初始化开始的位置
        self.start_sence = start_sence


    def next_scene(self, scene_name):  # 根据字典获取位置的函数名
        val=map.scene.get(scene_name)
        return val


    def opening_scene(self):  # 通过传入的字典的键调用next_scene返回字典的值（位置的函数名）
        return self.next_scene(self.start_sence)


a_map = map('road')
a_game = Engine(a_map)
a_game.play()
