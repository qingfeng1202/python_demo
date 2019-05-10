class Game:

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


# 1.查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.创建游戏对象
game = Game("小明")
game.start_game()

# 确定方法类型：
# 1.实例方法 -- 方法内部需要访问 实例属性
# 2.类方法 -- 方法内部 只 需要访问 类属性
# 3.静态方法 -- 方法内部，不需要访问 实例属性 和 类属性

