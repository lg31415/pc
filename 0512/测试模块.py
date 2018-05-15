import unittest


class DouYu(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.num1 = 1

    # 要测试的方法必须加test头
    def testTest1(self):
        print('西西')
        self.num1 += 1

    # 被测试的方法执行完毕后调用
    def tearDown(self):
        print('tearDown')
        print("self.num1-====>", self.num1)


if __name__ == '__main__':
    unittest.main()
