import os,re
import sys
import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
import pymysql
import logging


# sys.path.append('E:/webdriver/Page/test_mathfun.py')
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
print(ABSPATH)


class PersonalCenterTest(unittest.TestCase):
    global member_id
    #member_id = 351873967
    member_id = 8289882
    global url
    # = 'https://testweixin.drcuiyutao.com/yxy-edu-web/mymaster?_channel=wx&appId=wx51baca73da72c79f&openId=&city=&country=&headImgUrl=h&nickName=&sex=1&unionId=&accountId=391656288142090240&memberId=351873967&childId=391672105486450688&yxyWhiteList=1&yxyToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTU3MTM3NjI2MjY2OH0.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiIzOTE2NTYyODgxNDIwOTAyNDAiLCJsb2dpblR5cGUiOiJ3ZWl4aW4iLCJsb2dnZXIiOiJvcmcuc2xmNGouaW1wbC5Mb2c0akxvZ2dlckFkYXB0ZXIoY29tLnl4eS5mcmFtZXdvcmsubW9kZWwuand0Lkp3dFBheWxvYWQpIiwiYXBwQ29kZSI6IllVWFkiLCJkZXZpY2VubyI6Im51bGwiLCJleHAiOjE1NzEzOTc4NjIsImlhdCI6MTU3MTM3NjI2MiwianRpIjoiMCIsIm1lbWJlcklkIjoiMzUxODczOTY3In0.HYS4Uu42ezvQxi2YTqaGSKxzV4gFabQfRH9gDdbCIm4'
    url ='https://testweixin.drcuiyutao.com/yxy-edu-web/mymaster?_channel=wx&appId=wx51baca73da72c79f&openId=&city=&country=&headImgUrl=h&nickName=&sex=1&unionId=&accountId=258906953042010112&memberId=8289882&childId=376658718054612992&yxyWhiteList=1&yxyToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTU3MTk5MjE1MjU3M30.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiIyNTg5MDY5NTMwNDIwMTAxMTIiLCJsb2dpblR5cGUiOiJ1c2VyIiwibG9nZ2VyIjoib3JnLnNsZjRqLmltcGwuTG9nNGpMb2dnZXJBZGFwdGVyKGNvbS55eHkuZnJhbWV3b3JrLm1vZGVsLmp3dC5Kd3RQYXlsb2FkKSIsImFwcENvZGUiOiJZVVhZIiwiZGV2aWNlbm8iOiJFQzo4Qzo5QTo1Mzo2MjpFMCIsImV4cCI6MTU3MjAxMzc1MiwiaWF0IjoxNTcxOTkyMTUyLCJqdGkiOiIwIiwibWVtYmVySWQiOiI4Mjg5ODgyIn0.Nh_XLV3-be0hZxw5Nc3yl_zjFpwNLNj4LBjD4x0xPkQ'
    global conn
    conn = pymysql.connect(host="rm-2zef5uf5348qgu4e2.mysql.rds.aliyuncs.com", port=3306,
                           user="maxiaoliang", passwd="5V4G25GbqrQj", db="yxy_usercenter", charset="utf8")
    global cur
    cur = conn.cursor()

    @classmethod
    def setUpClass(self):
        print('执行setUp.。。。。。。。。。。。。。。。。。。。')
        # self.driver = webdriver.Chrome()
        # import time
        # time.sleep(1)
        # self.driver.maximize_window()
        # self.driver.get(url)
        # time.sleep(2)

        options = webdriver.ChromeOptions()
        WIDTH = 400
        HEIGHT = 600
        PIXEL_RATIO = 3.0
        # User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN
        user_agent = (
        'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN')
        # options.add_argument('user-agent=%s' % user_agent)

        # mobile_emulation = {"deviceName": "iPhone 6"}
        # options.add_experimental_option("mobileEmulation", mobile_emulation)

        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": user_agent}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        import time
        time.sleep(1)
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)


        # pass
    #顶顶顶顶
    def test_case1(self):
        """打开个人中心"""
        print('执行case1.。。。。。。。。。。。。。。。。。。。')
        sql = 'SELECT name FROM yxy_edu.student WHERE id = (SELECT child_id FROM yxy_edu.member_current_child WHERE member_id = %s)' % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("当前宝宝:" + str(rows[0]))
        name = str(rows[0])
        # name = "宝5"
        assert "个人中心" in self.driver.title
        import time
        time.sleep(3)
        assert name  in self.driver.page_source
        assert "我的宝宝" in self.driver.page_source and '我的课程' in self.driver.page_source \
               and '剩余课时' in self.driver.page_source and '我的测评' in self.driver.page_source\
               and '购买记录' in self.driver.page_source and '我的收货地址' in self.driver.page_source\
               and '我的优惠券' in self.driver.page_source and '育学园教育中心' in self.driver.page_source\
               and '服务协议' in self.driver.page_source

    def test_case2(self):
        """我的宝宝列表"""
        print('执行case2.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div[1]').click()
        time.sleep(3)
        print(self.driver.title)
        assert "选择宝宝" in self.driver.title
        assert "天" in self.driver.page_source

        time.sleep(3)
        self.driver.back()
        print('返回')

    def test_case3(self):
        """我的课程列表"""
        print('执行case3.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div[2]').click()
        time.sleep(3)
        assert "个人中心" in self.driver.title
        time.sleep(3)
        assert "我的课程" in self.driver.page_source
        assert "打卡记录" and '课程报告' and '班主任' in self.driver.page_source
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/li[1]/div[3]/span[1]').click()
        time.sleep(1)
        assert "还没有打卡记录" or '打卡于'  in self.driver.page_source
        self.driver.back()

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/li[1]/div[3]/span[2]').click()
        time.sleep(1)
        assert "周报" in self.driver.page_source

        self.driver.back()

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/ul/li[1]/div[3]/span[3]').click()
        time.sleep(1)
        assert "微信号" in self.driver.page_source
        self.driver.back()
        self.driver.back()

    def test_case4(self):
        """剩余课时"""
        print('执行case4.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div[3]').click()
        time.sleep(3)
        assert "课时明细" in self.driver.title
        time.sleep(3)
        assert "消耗" in self.driver.page_source
        assert '天' in self.driver.page_source

        try:
            assert "消耗" in self.driver.page_source
            assert '天' in self.driver.page_source
            assert '儿童成长游戏课' in self.driver.page_source
        except Exception as e:
            print('检查课时'+ str(e))
            raise


        time.sleep(3)
        self.driver.back()
        print('返回')
    def test_case5(self):
        """我的测评"""
        print('执行case5.。。。。。。。。。。。。。。。。。。。')

        sql = 'SELECT quiz_age FROM yxy_quiz.quiz_record WHERE child_id =(SELECT child_id FROM yxy_edu.member_current_child WHERE member_id = %s) ORDER BY quiz_time DESC ' % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div[4]').click()
        time.sleep(3)
        assert "我的测评" in self.driver.title
        # time.sleep(3)
        # assert "幼儿成长发育测评" in self.driver.page_source
        if rows is None:
            try:
                assert '宝宝还没有测评过呢' in self.driver.page_source
            except Exception as e:
                print('没有测评时的校验' + str(e))
                raise
        if rows is not None:
            print("当前宝宝最新测评的时间:" + str(rows[0]))
            quiz_age = str(rows[0])
            try:
                assert quiz_age in self.driver.page_source
            except Exception as e:
                print('有测评记录的校验' + str(e))
                raise

        time.sleep(1)
        self.driver.back()
        print('返回')
    def test_case6(self):
        """购买记录"""
        print('执行case6.。。。。。。。。。。。。。。。。。。。')

        sql ='SELECT order_code FROM yxy_edu.order_base WHERE yxy_edu.order_base.mid = %s AND pay_status=102 AND source_type !=6 ORDER BY create_at DESC'  % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("用户最新订单号:" + str(rows[0]))
        order_code = str(rows[0])

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div[1]').click()
        time.sleep(5)
        try:
            assert "我的购买记录" in self.driver.title
            assert "付款金额" in self.driver.page_source
            assert order_code in self.driver.page_source
        except Exception as e:
            print('购买记录的校验' + str(e))
            raise
        time.sleep(1)
        print('返回页面')
        self.driver.back()
        print('返回')
    def test_case7(self):
        """我的收货地址"""
        print('执行case7.。。。。。。。。。。。。。。。。。。。')

        sql = 'SELECT address FROM yxy_usercenter.member_address WHERE member_id = %s and is_del =0' % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("地址:" + str(rows[0]))
        address = str(rows[0])

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div[2]').click()
        time.sleep(3)
        assert "个人中心" in self.driver.title
        time.sleep(3)
        try:
            assert "我的收货地址" in self.driver.page_source
            assert address in self.driver.page_source
        except Exception as e:
            print('我的收货地址' + str(e))
            raise

        time.sleep(1)
        self.driver.back()
        print('返回')
    def test_case8(self):
        """我的优惠券"""
        print('执行case8.。。。。。。。。。。。。。。。。。。。')

        sql = 'SELECT title FROM yxy_promotion.user_coupon WHERE uid =%s AND entity_type =1 AND coupon_type =5 ORDER BY create_at DESC' % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("优惠券:" + str(rows[0]))
        title = str(rows[0])

        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div[3]').click()
        time.sleep(3)
        assert "个人中心" in self.driver.title
        time.sleep(3)
        try:
            assert "课程优惠券" in self.driver.page_source
            assert title in self.driver.page_source
        except Exception as e:
            print('优惠券的校验' + str(e))
            raise

        time.sleep(1)
        self.driver.back()
        print('返回')
    def test_case9(self):
        """育学园教育中心"""
        print('执行case9.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div[3]').click()
        self.driver.find_element_by_id('eduCenter').click()
        # self.driver.find_element_by_id('serviceAgre').click()
        time.sleep(3)
        try:
            assert "小育专栏" in self.driver.title
            assert "育学园教育" in self.driver.page_source
        except Exception as e:
            print('育学园教育中心' + str(e))
            raise
        time.sleep(1)
        self.driver.back()
        print('返回')
    def test_case10(self):
        """服务协议"""
        print('执行case10.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)


        # self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/li[2]/div[3]').click()
        # self.driver.find_element_by_id('eduCenter').click()
        self.driver.find_element_by_id('serviceAgre').click()
        # serviceAgre = self.driver.find_element_by_id('serviceAgre')
        # self.driver.execute_script("$(arguments[0]).click()", serviceAgre)
        time.sleep(3)
        try:
            assert "小育专栏" in self.driver.title
            assert "育学园教育" in self.driver.page_source
        except Exception as e:
            print('服务协议' + str(e))
            raise
        time.sleep(1)
        self.driver.back()
        print('返回')
    @classmethod
    def tearDownClass(self):
        print('执行tearDown.。。。。。。。。。。。。。。。。。。。')
        self.driver.quit()
        # self.driver.refresh()  # 将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        # pass


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()     # 构造测试集
    suite.addTest(PersonalCenterTest("test_case1"))  # 加入测试用例
    # suite.addTest(PersonalCenterTest("test_case2"))
    # suite.addTest(PersonalCenterTest("test_case3"))
    # suite.addTest(PersonalCenterTest("test_case4"))
    # suite.addTest(PersonalCenterTest("test_case5"))
    # suite.addTest(PersonalCenterTest("test_case6"))
    # suite.addTest(PersonalCenterTest("test_case7"))
    # suite.addTest(PersonalCenterTest("test_case8"))
    suite.addTest(PersonalCenterTest("test_case9"))
    suite.addTest(PersonalCenterTest("test_case10"))
    # suite.addTest(PersonalCenterTest("test_quit"))
    # unittest.main()

    # 执行测试
    # date = time.strftime("%Y%m%d")      # 定义date为日期，time为时间
    time = time.strftime("%Y%m%d_%H%M%S")
    path = "./report/ui/"
    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
        print('创建目录')
    else:
        print('已存在')
        pass
    report_path = path+time+"UIreport.html"      # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    print(report_path)
    report_title = u"测试报告"
    desc = u'功能自动化测试报告详情：'

    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    # 关闭report，脚本结束
    report.close()
