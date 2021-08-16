class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        print('--------')
        # 変数に()をつけることでprintと同じ作用にできる
        method()
        print('--------')
