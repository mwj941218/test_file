import os,re
import sys
import unittest
import time,datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from HTMLTestRunner import HTMLTestRunner
import pymysql
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# sys.path.append('E:/webdriver/Page/test_mathfun.py')
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
print(ABSPATH)


class detectionTest(unittest.TestCase):
    global member_id
    #member_id = 351873967
    member_id = 8289882
    global url
    # = 'https://testweixin.drcuiyutao.com/yxy-edu-web/mymaster?_channel=wx&appId=wx51baca73da72c79f&openId=&city=&country=&headImgUrl=h&nickName=&sex=1&unionId=&accountId=391656288142090240&memberId=351873967&childId=391672105486450688&yxyWhiteList=1&yxyToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTU3MTM3NjI2MjY2OH0.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiIzOTE2NTYyODgxNDIwOTAyNDAiLCJsb2dpblR5cGUiOiJ3ZWl4aW4iLCJsb2dnZXIiOiJvcmcuc2xmNGouaW1wbC5Mb2c0akxvZ2dlckFkYXB0ZXIoY29tLnl4eS5mcmFtZXdvcmsubW9kZWwuand0Lkp3dFBheWxvYWQpIiwiYXBwQ29kZSI6IllVWFkiLCJkZXZpY2VubyI6Im51bGwiLCJleHAiOjE1NzEzOTc4NjIsImlhdCI6MTU3MTM3NjI2MiwianRpIjoiMCIsIm1lbWJlcklkIjoiMzUxODczOTY3In0.HYS4Uu42ezvQxi2YTqaGSKxzV4gFabQfRH9gDdbCIm4'
    # url ='https://testweixin.drcuiyutao.com/yxy-edu-web/detection?_channel=wx&appId=wx51baca73da72c79f&openId=&city=&country=&headImgUrl=h&nickName=&sex=1&unionId=&accountId=258906953042010112&memberId=8289882&childId=376658718054612992&yxyWhiteList=1&yxyToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTU3MTk5MjE1MjU3M30.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiIyNTg5MDY5NTMwNDIwMTAxMTIiLCJsb2dpblR5cGUiOiJ1c2VyIiwibG9nZ2VyIjoib3JnLnNsZjRqLmltcGwuTG9nNGpMb2dnZXJBZGFwdGVyKGNvbS55eHkuZnJhbWV3b3JrLm1vZGVsLmp3dC5Kd3RQYXlsb2FkKSIsImFwcENvZGUiOiJZVVhZIiwiZGV2aWNlbm8iOiJFQzo4Qzo5QTo1Mzo2MjpFMCIsImV4cCI6MTU3MjAxMzc1MiwiaWF0IjoxNTcxOTkyMTUyLCJqdGkiOiIwIiwibWVtYmVySWQiOiI4Mjg5ODgyIn0.Nh_XLV3-be0hZxw5Nc3yl_zjFpwNLNj4LBjD4x0xPkQ'
    url='https://testweixin.drcuiyutao.com/yxy-edu-web/evaluation?_channel=wx&appId=wx51baca73da72c79f&openId=&city=&country=&headImgUrl=h&nickName=&sex=1&unionId=&accountId=258906953042010112&memberId=8289882&childId=376658718054612992&yxyWhiteList=1&yxyToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImlzc3VlciI6bnVsbCwiaWF0VGltZSI6MTU3MTk5MjE1MjU3M30.eyJpbXBsaWNpdExvZ2luIjoiZmFsc2UiLCJhY2NvdW50SWQiOiIyNTg5MDY5NTMwNDIwMTAxMTIiLCJsb2dpblR5cGUiOiJ1c2VyIiwibG9nZ2VyIjoib3JnLnNsZjRqLmltcGwuTG9nNGpMb2dnZXJBZGFwdGVyKGNvbS55eHkuZnJhbWV3b3JrLm1vZGVsLmp3dC5Kd3RQYXlsb2FkKSIsImFwcENvZGUiOiJZVVhZIiwiZGV2aWNlbm8iOiJFQzo4Qzo5QTo1Mzo2MjpFMCIsImV4cCI6MTU3MjAxMzc1MiwiaWF0IjoxNTcxOTkyMTUyLCJqdGkiOiIwIiwibWVtYmVySWQiOiI4Mjg5ODgyIn0.Nh_XLV3-be0hZxw5Nc3yl_zjFpwNLNj4LBjD4x0xPkQ&courseId=402075498824351744&courseType=1&tabType=2'
    global conn
    conn = pymysql.connect(host="rm-2zef5uf5348qgu4e2.mysql.rds.aliyuncs.com", port=3306,
                           user="maxiaoliang", passwd="5V4G25GbqrQj", db="yxy_usercenter", charset="utf8")
    global cur
    cur = conn.cursor()

    @classmethod
    def setUpClass(self):
        print('执行setUp.。。。。。。。。。。。。。。。。。。。')
        # self.driver = webdriver.Chrome()
        #加请求头UA信息，模式微信端访问
        options = webdriver.ChromeOptions()
        WIDTH = 400
        HEIGHT = 600
        PIXEL_RATIO = 3.0
        #User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN
        user_agent = ('Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.4(0x17000428) NetType/WIFI Language/zh_CN')
        # options.add_argument('user-agent=%s' % user_agent)

        # mobile_emulation = {"deviceName": "iPhone 6"}
        # options.add_experimental_option("mobileEmulation", mobile_emulation)

        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": user_agent}
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options)
        import time
        time.sleep(1)
        # self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(5)

        # pass

    def test_case1(self):
        """打开测评页"""
        print('执行case1.。。。。。。。。。。。。。。。。。。。')
        sql = 'SELECT name FROM yxy_edu.student WHERE id = (SELECT child_id FROM yxy_edu.member_current_child WHERE member_id = %s)' % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("当前宝宝:" + str(rows[0]))
        name = str(rows[0])
        img1='https://public.qn.ivybaby.me/edu/image/20190806144844/file-c5f44ca8-a869-457e-823b-f80aa0d2cd13.png'
        img2='https://public.qn.ivybaby.me/edu/image/20190806144915/file-7e57a657-c56a-4551-8fac-50a818f47a09.png'
        img3=' https://public.qn.ivybaby.me/edu/image/20190826132422/file-48eadf0d-900b-4410-a782-77650618dbb4.png'
        img4='https://public.qn.ivybaby.me/edu/image/20190806145007/file-2c750a0b-4fc5-44bd-aa0a-a646256cd62c.png'
        img5='https://public.qn.ivybaby.me/edu/image/20190806145032/file-c2f75b4a-e43e-42bd-b668-f2fe04b78bd6.png'
        img6='https://public.qn.ivybaby.me/edu/image/20190806145043/file-9ff7325a-96ac-4dfb-908f-7ec5d573c465.png'

        img_list = [img1,img2,img3,img4,img5,img6]
        # name = "宝5"
        assert "0-6岁成长发育测评" in self.driver.title
        assert name  in self.driver.page_source
        assert '立即测评' in self.driver.page_source
        assert '绝不错过宝宝启蒙关键期' in self.driver.page_source
        for img in img_list:
            print('检查图片：'+img)
            assert img in self.driver.page_source

    def test_case2(self):
        """立即测评"""
        print('执行case2.。。。。。。。。。。。。。。。。。。。')
        #点击立即测评按钮 //*[@id="app"]/div/div[1]/div[4]/div[1]
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[4]/div[1]').click()
        # self.driver.find_element_by_link_text('立即测评').click()
        import time
        time.sleep(3)
        #点击开始测评按钮 //*[@id="app"]/div/footer/a
        self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/a').click()
        time.sleep(3)
        #点击能//*[@id="app"]/div/div[1]/div[2]/div/button[1]
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
        # time.sleep(1)
        a = 1
        while True:
            print('循环次数：'+str(a))
            result = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]').is_displayed()
            # result = EC.alert_is_present()(self.driver)
            print(result)
            if result:
                print('y')
                print('点击弹框')
                #/html/body/div[5]/div/div[2]/div[3]/a
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[3]/a').click()
                time.sleep(2)

            else:
                print("alert 未弹出！")
                # quizQuestion = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click
                try:
                    quizQuestion = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]')
                except Exception as e:
                    print('页面中不存在能、不能、不确定按钮')
                    quizQuestion = False
                print('判断是否有能按钮：'+str(quizQuestion))
                #判断是否为答题页
                if quizQuestion:
                    print('有能按钮')
                    self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/button[1]').click()
                    print('点能按钮后等1秒')
                    time.sleep(1)
                else:
                    print('没有能按钮，跳出循环')
                    break
            a = a + 1
        time.sleep(5)
        #判断是否进入添加体重页面
        try:
            print('判断是否进入体重页面')
            # flag = self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/a')
            # assert '恭喜您答完所有题' in self.driver.page_source
            #输入体重
            self.driver.find_element_by_xpath('//*[@id="app"]/div/main/table/tr[1]/th/input').send_keys('3.5')
            #选择是否早产 //*[@id="app"]/div/main/table/tr[3]/td/label[1]/input
            self.driver.find_element_by_xpath('//*[@id="app"]/div/main/table/tr[3]/td/label[1]/input').click()
            #选择是否顺产 //*[@id="app"]/div/main/table/tr[4]/td/label[1]/input
            self.driver.find_element_by_xpath('//*[@id="app"]/div/main/table/tr[4]/td/label[1]/input').click()
            #选择宝宝数量 //*[@id="app"]/div/main/table/tr[5]/td/label[1]/input
            self.driver.find_element_by_xpath('//*[@id="app"]/div/main/table/tr[5]/td/label[1]/input').click()
            # time.sleep(3)
            #点击下一步 //*[@id="app"]/div/footer/button
            self.driver.find_element_by_xpath('//*[@id="app"]/div/footer/button').click()
            time.sleep(3)

        except Exception as e:
            print('未进入添加体重页面，直接生成报告')
        today = datetime.date.today()
        print(today)
        # print('今日日期：' + str(today))
        # 日期转字符串
        today_str = datetime.datetime.strftime(today, "%Y-%m-%d")
        print("--1---:" + datetime.datetime.strftime(today, "%Y-%m-%d"))
        sql = 'SELECT NAME,CASE WHEN sex =0 THEN "女" ELSE  "男" END,birthday,CASE WHEN birth_gestational_week IS NULL OR birth_gestational_week="" THEN "未知" ELSE birth_gestational_week END,id FROM yxy_edu.student WHERE id = (SELECT child_id FROM yxy_edu.member_current_child WHERE member_id = %s)' % member_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        name = rows[0]
        sex = rows[1]
        birthday = time.strftime("%m-%d", time.localtime(rows[2] / 1000))
        birth_gestational_week = rows[3]
        child_id = '%d' % rows[4]
        print('宝宝名+性别+生日+出生孕周+宝宝id：' + name + ' ' + sex + ' ' + birthday + ' ' + birth_gestational_week+' '+child_id)

        #查询宝宝的体重
        sql_quiz ='SELECT CASE WHEN premature_delivery =0 THEN "足月" ELSE "早产" END,CASE WHEN eutocia = 0 THEN "顺产" ELSE "剖腹产" END,weight FROM yxy_quiz.quiz_child_info WHERE child_id =%s' % child_id
        print(sql_quiz)
        cur.execute(sql_quiz)
        rows = cur.fetchone()
        premature_delivery = rows[0]
        eutocia = rows[1]
        # weight = str(rows[2])
        weight = "%.2g" % rows[2]
        premature_delivery_eutocia = premature_delivery+eutocia

        print('出生方式+出生体重：'+premature_delivery_eutocia+' '+weight)

        assert name in self.driver.page_source and sex in self.driver.page_source \
               and birthday in self.driver.page_source and birth_gestational_week in self.driver.page_source \
               and weight in self.driver.page_source and premature_delivery_eutocia in self.driver.page_source
        assert '进入学习首页，查看完整方案' in self.driver.page_source



    def test_case3(self):
        """快捷入口"""
        print('执行case2.。。。。。。。。。。。。。。。。。。。')

        sql = 'SELECT NAME,icon FROM yxy_edu.quick_entry WHERE is_del =0 AND STATUS = 0 ORDER BY show_order'
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        name = str(rows[0])
        icon =str(rows[1])
        print("快捷入口+图片:" + name +' '+icon)
        assert name and icon in self.driver.page_source

        import time
        # time.sleep(3)

    def test_case4(self):
        """儿童成长游戏课"""
        print('执行case3.。。。。。。。。。。。。。。。。。。。')

        # sql = 'SELECT skip_url FROM yxy_edu.operational_location_content WHERE operational_location_id =342255158307229696 AND STATUS = 0 AND is_del =0 ORDER BY show_order'
        sql ='SELECT ol.title,olc.skip_url,olc.image FROM yxy_edu.operational_location ol LEFT JOIN yxy_edu.operational_location_content olc ON ol.id = olc.operational_location_id WHERE  ol.type = 2 AND olc.status =0'
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("标题:" + str(rows[0]))
        print("跳转链接:" + str(rows[1]))
        print("图片:" + str(rows[2]))
        title = str(rows[0])
        skip_url = str(rows[1])
        image = str(rows[2])
        #skip_url ='https://testweixin.drcuiyutao.com/yxy-edu-web/courseIntroduction?courseId=1'

        #虚拟销量
        sql_virtual_sale_count ='SELECT SUM(virtual_sale_count) FROM yxy_edu.product WHERE course_id = 1'
        cur.execute(sql_virtual_sale_count)
        rows = cur.fetchone()
        virtual_sale_count = rows[0]
        #真实销量
        sql_sale_num ='SELECT SUM(sale_num) FROM yxy_platform_goods.goods_sale WHERE ware_id IN (SELECT id FROM yxy_edu.product WHERE course_id = 1);'
        cur.execute(sql_sale_num)
        rows = cur.fetchone()
        sale_num = rows[0]
        print(virtual_sale_count)
        print(sale_num)
        #总量
        saleSum = virtual_sale_count + sale_num
        print('购买总数：'+str(saleSum))
        assert str(saleSum) in self.driver.page_source
        assert image in self.driver.page_source
        # self.driver.back()
        # print('返回')
        import time
        # time.sleep(3)

    def test_case5(self):
        """成长学院"""
        print('执行case4.。。。。。。。。。。。。。。。。。。。')
        import time
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        #// *[ @ id = "app"] / div / div[1] / div / div[5] / div / div / div[2]
        # element=self.driver.find_element_by_xpath('// *[ @ id = "app"] / div / div[1] / div / div[5] / div / div / div[2]')
        # self.driver.execute_script("arguments[0].scrollIntoView(false);",element)
        # self.driver.execute_script("window.scrollTo(5000,document.body.scrollHeight)")
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # import time
        time.sleep(1)
        sql = 'SELECT  title,sub_title FROM yxy_edu.operational_location WHERE TYPE =3'
        cur.execute(sql)
        rows = cur.fetchone()
        title = str(rows[0])
        sub_title = str(rows[1]).split('&')[0]
        # skip_url = str(rows[2])
        print('标题+子标题：'+title+' '+sub_title+ ' ')
        assert title  in self.driver.page_source
        assert sub_title  in self.driver.page_source

        sql_title = 'SELECT NAME,cover FROM yxy_platform_course.course WHERE course_category = 6 AND STATUS =0 ORDER BY create_at DESC '#LIMIT 2
        print('执行sql：'+sql_title)
        cur.execute(sql_title)
        rows = cur.fetchone()
        name1 = str(rows[0])
        cover1 = str(rows[1])
        print('第一个标题+第一个封面图：'+name1+' '+cover1)
        rows = cur.fetchone()
        name2 = str(rows[0])
        cover2 = str(rows[1])
        print('第二个标题+第二个封面图：' + name2+' '+cover2)
        # print('前两个成长学院课程标题：'+name1+' '+name2)
        assert name1 and cover1 in self.driver.page_source
        assert name2 and cover2 in self.driver.page_source

        print('点击成长学院列表检查列表标题')
        # //*[@id="app"]/div/div[1]/div/div[6]/div/div/div[1]/div/span
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[6]/div/div/div[1]/div/span').click()
        time.sleep(3)
        assert '成长学院' in self.driver.page_source
        rows = cur.fetchall()
        for sku in rows:
            assert sku[0] in self.driver.page_source

        time.sleep(1)
        self.driver.back()
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        time.sleep(1)


        print('点击一个成长学院进入详情')
        #//*[@id="app"]/div/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[1]
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[1]').click()
        time.sleep(3)
        #===========================================================================================
        sql_frist_product = 'SELECT NAME,cover_image FROM yxy_edu.product WHERE id = (SELECT product_id FROM yxy_edu.course_default_product WHERE course_id = (SELECT id FROM yxy_platform_course.course WHERE course_category = 6 AND STATUS =0 ORDER BY create_at DESC LIMIT 1))'
        print('执行sql：' + sql_frist_product)
        cur.execute(sql_frist_product)
        rows = cur.fetchone()
        name = str(rows[0])
        cover_image = str(rows[1])
        print('详情页的课程标题+封面图：'+name+' '+cover_image)
        assert name and cover_image  in self.driver.page_source

        sql_course_lesson ='SELECT title,icon FROM yxy_platform_course.course_lesson WHERE course_id = (SELECT id FROM yxy_platform_course.course WHERE course_category = 6 AND STATUS =0 ORDER BY create_at DESC LIMIT 1)'
        print('执行sql：' + sql_course_lesson)
        cur.execute(sql_course_lesson)
        rows = cur.fetchone()
        title = str(rows[0])
        icon = str(rows[1])
        print('详情页单节课标题+图标：' + title + ' ' + icon)

        try:
            assert title in self.driver.page_source and icon  in self.driver.page_source
        except Exception as e:
            print('检查详情页单节课错误'+ str(e))
            raise

        time.sleep(3)
        print('12323241241111111111111111111111111111111111111111111111111111111111111')
        self.driver.back()
        time.sleep(3)

    def test_case6(self):
        """小育专栏"""
        print('执行case5.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(3)
        #页面下拉
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)

        sql = 'SELECT title,cover_img,author,create_at,content FROM yxy_edu.topic_article WHERE is_del = 0 AND  STATUS =0 AND TYPE =1 ORDER BY update_at DESC'
        cur.execute(sql)
        rows = cur.fetchone()
        title = str(rows[0])
        cover_img = str(rows[1])
        print('第一条小育专栏的标题+图片'+title+' '+cover_img)
        author = rows[2]

        #获取创建时间日期
        import time
        # create_at = time.localtime(rows[3] / 1000)
        otherStyleTime = time.strftime("%Y-%m-%d", time.localtime(rows[3] / 1000))
        create_at = otherStyleTime.split('-')[0] + '年' + otherStyleTime.split('-')[1] + '月' + otherStyleTime.split('-')[
            2] + '日'
        # content = rows[4]
        content = re.search(r'[\u4e00-\u9fa5]{4,10}', rows[4])[0]

        assert title and cover_img in self.driver.page_source
        #//*[@id="app"]/div/div[1]/div/div[10]/div/div/div[2]/div[1]
        #进入小育专栏详情
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[10]/div/div/div[2]/div[1]').click()

        time.sleep(3)
        assert title and author and create_at and content in self.driver.page_source

        self.driver.back()
        print('返回')

    def test_case7(self):
        """快捷入口点击第一个入口"""
        print('执行case7.。。。。。。。。。。。。。。。。。。。')
        #//*[@id="app"]/div/div[1]/div/div[3]/div/div/ul/li[1]
        import time
        time.sleep(2)
        #页面滑动至顶部
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        time.sleep(2)

        # self.driver.find_element_by_link_text('游戏课程').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div/div/ul/li[1]').click()
        time.sleep(5)
        product_id ='77e3f436f6384d7781f8ea0baa9f9e9b'
        #商品基本信息
        sql ='SELECT NAME,cover_image,content,promotion_info,virtual_sale_count,remark,tag_id FROM yxy_edu.product WHERE id = "%s"'  % product_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        product_name = rows[0]
        product_cover_image = rows[1]
        product_content =rows[2]
        product_content = re.search(r'file-.{8}-.{4}-.{4}-.{4}-.{12}\.png', product_content)[0]
        product_promotion_info = rows[3]
        product_virtual_sale_count = str(rows[4])
        product_remark = rows[5]
        product_tag_id = str(rows[6])

        print('商品名+商品图片+内容+促销文案+虚拟销量+简介+标签:' + product_name+' '+ product_cover_image+' '+ product_content+' '+ product_promotion_info+' '+ product_virtual_sale_count+' '+ product_remark+' '+product_tag_id)
        print('商品图片:'+product_cover_image)
        print('内容:' + product_content)
        print('促销文案:' + product_promotion_info)
        print('虚拟销量:' + product_virtual_sale_count)
        print('简介:' + product_remark)
        print('标签:' + product_tag_id)

        assert "儿童成长游戏课" in self.driver.title
        assert product_name and product_remark and product_cover_image  in self.driver.page_source
        assert product_promotion_info in self.driver.page_source
        #标签
        sql ='SELECT NAME FROM yxy_edu.tag WHERE id = "%s"' % product_tag_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        tag_name = rows[0]
        print('标签：'+tag_name)
        assert tag_name in self.driver.page_source
        #商品销量=虚拟销量+实际销量
        sql ='SELECT SUM(sale_num) FROM yxy_platform_goods.goods_sale WHERE ware_id = "%s"' %product_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        sale_num = rows[0]
        sum_sale = int(sale_num)+int(product_virtual_sale_count)
        print('销量：' + str(sum_sale))
        assert str(sum_sale) in self.driver.page_source


        #检查商品价格区间
        sql='SELECT MAX(price),MIN(price) FROM yxy_edu.product_sku WHERE product_id ="%s" AND STATUS = 0 AND is_del =0;' %product_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        max_price = str(rows[0])
        min_price = str(rows[1])
        price = min_price+'-'+max_price
        print('价格区间：'+min_price+'-'+max_price)
        assert price in self.driver.page_source
        #页面下滑检查内容中的图片
        js = "var q=document.documentElement.scrollTop=2000"
        self.driver.execute_script(js)
        time.sleep(5)
        assert product_content  in self.driver.page_source

        # self.driver.back()
        print('返回')
    def test_case8(self):
        """商品售卖页-打卡记录"""
        print('执行case8.。。。。。。。。。。。。。。。。。。。')
        import time

        #//*[@id="main"]/div/div[4]/div[2]/div[3]
        # self.driver.find_element_by_class_name("tab-item").click()
        # import time
        # time.sleep(10)

        # sql = 'SELECT address FROM yxy_usercenter.member_address WHERE member_id = %s and is_del =0' % member_id
        sql='SELECT content,create_at,create_name FROM yxy_comment.user_comment WHERE model_code ="YEDU" AND top_hat =1 AND topic_author =1 ORDER BY create_at DESC '

        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        print("打卡内容:" + rows[0])
        content = rows[0]
        #获取打卡时间并转化成日期
        createTime = rows[1]
        create_at = time.localtime(createTime/1000)
        print(create_at)
        otherStyleTime = time.strftime("%Y-%m-%d", create_at)
        print(otherStyleTime)
        create_at = otherStyleTime.split('-')[0]+'年'+ otherStyleTime.split('-')[1]+'月'+ otherStyleTime.split('-')[2]+'日'
        print('打卡时间：'+create_at)
        create_name = rows[2]
        print('打卡人姓名：'+create_name)

        assert content in self.driver.page_source
        assert create_at in self.driver.page_source
        assert create_name in self.driver.page_source


        # self.driver.back()
        print('返回')
    def test_case9(self):
        """游戏售卖页-点击购买-0元单-激活课程"""
        print('执行case9.。。。。。。。。。。。。。。。。。。。')
        #//*[@id="main"]/div/div[5]/div/button
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[5]/div/button').click()
        import time
        time.sleep(3)

        # 商品基本信息
        product_id = '77e3f436f6384d7781f8ea0baa9f9e9b'
        sql = 'SELECT cover_image FROM yxy_edu.product WHERE id = "%s"' % product_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        cover_image = rows[0]
        assert cover_image in self.driver.page_source
        # 检查商品价格区间
        sql = 'SELECT MAX(price),MIN(price) FROM yxy_edu.product_sku WHERE product_id ="%s" AND STATUS = 0 AND is_del =0;' % product_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        max_price = str(rows[0])
        min_price = str(rows[1])
        price = min_price + '-' + max_price
        print('价格区间：' + min_price + '-' + max_price)
        assert price in self.driver.page_source
        #检查sku
        sql = 'SELECT name FROM yxy_edu.product_sku WHERE product_id ="%s" AND STATUS = 0 AND is_del =0 ORDER BY price;' % product_id
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        for sku in rows:
            assert sku[0] in self.driver.page_source

        #//*[@id="main"]/div/div[6]/div[2]/div[2]/div/div[2]/span[1] 选择规格
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[6]/div[2]/div[2]/div/div[2]/span[1]').click()
        time.sleep(1)
        #//*[@id="main"]/div/div[6]/div[2]/div[3]/button 点击下一步
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div[6]/div[2]/div[3]/button').click()
        time.sleep(10)
        assert '恭喜您支付成功' in self.driver.page_source

        #//*[@id="app"]/div/div[1]/div 点击下一步
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div').click()
        time.sleep(10)
        assert '为哪位宝宝定制' in self.driver.page_source
        #选择宝宝 //*[@id="app"]/div/div[1]/div[6]/div/div/ul/li[1]/div[3]
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[6]/div/div/ul/li[1]/div[3]').click()
        time.sleep(3)
        assert '确认绑定课时' in self.driver.page_source
        #点击确定按钮 /html/body/div[5]/div/div[2]/div[2]/a[2]
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/a[2]').click()
        time.sleep(3)

        # 进入宝宝确认页点击下一步 //*[@id="app"]/div/div[1]/div[6]/div/div[2]/div[3]
        assert '宝宝昵称' in self.driver.page_source
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[6]/div/div[2]/div[3]').click()
        time.sleep(3)

        assert '专属课程' in self.driver.page_source

        time.sleep(3)
        #进入学习页需要点击发现tab //*[@id="app"]/div/div[1]/div[5]/div/a[1]
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[5]/div/a[1]').click()
        time.sleep(5)
        print('返回')
    def test_case10(self):
        """检查图文运营位"""
        print('执行case10.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(2)
        # 页面滑动至顶部
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        time.sleep(2)

        #检查主标题
        sql ='SELECT title FROM yxy_edu.operational_location WHERE id IN (SELECT operational_location_id FROM yxy_edu.view_operational_location WHERE view_code ="XYSDSD343GHGH") AND TYPE=4 AND STATUS = 0 LIMIT 1'
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        title = rows[0]
        assert title in self.driver.page_source
        #检查子内容
        sql = 'SELECT image,skip_url,title,sub_title,remark FROM yxy_edu.operational_location_content WHERE operational_location_id = (SELECT id FROM yxy_edu.operational_location WHERE id IN (SELECT operational_location_id FROM yxy_edu.view_operational_location WHERE view_code ="XYSDSD343GHGH") AND TYPE =4 AND STATUS = 0 LIMIT 1) AND STATUS =0'
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        image = rows[0]
        skip_url = rows[1]
        title = rows[2]
        sub_title =rows[3]
        remark = rows[4]
        print('image+skip_url+title+sub_title:'+image+' '+skip_url+' '+title+' '+sub_title)
        assert image  in self.driver.page_source and title in self.driver.page_source and sub_title in self.driver.page_source and remark in self.driver.page_source
        # assert  skip_url  in self.driver.page_source

    def test_case11(self):
        """检查图片运营位"""
        print('执行case11.。。。。。。。。。。。。。。。。。。。')

        import time
        time.sleep(2)
        # 页面滑动至中间
        js = "var q=document.documentElement.scrollTop=1000"
        self.driver.execute_script(js)
        time.sleep(2)

        sql = 'SELECT image,skip_url FROM yxy_edu.operational_location_content WHERE operational_location_id = (SELECT id FROM yxy_edu.operational_location WHERE id IN (SELECT operational_location_id FROM yxy_edu.view_operational_location WHERE view_code ="XYSDSD343GHGH") AND TYPE =5 AND STATUS = 0 LIMIT 1) AND STATUS =0 AND channel ="1,2,3"'
        print(sql)
        cur.execute(sql)
        rows = cur.fetchone()
        image = rows[0]
        skip_url = rows[1]
        print('图片的地址和跳转链接：'+image +' '+skip_url)

        assert image  in self.driver.page_source


    @classmethod
    def tearDownClass(self):
        print('执行tearDown.。。。。。。。。。。。。。。。。。。。')
        self.driver.quit()
        # self.driver.refresh()  # 将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        # pass


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()     # 构造测试集
    suite.addTest(detectionTest("test_case1"))  # 加入测试用例
    suite.addTest(detectionTest("test_case2"))
    # suite.addTest(detectionTest("test_case3"))
    # suite.addTest(detectionTest("test_case4"))
    # suite.addTest(detectionTest("test_case5"))
    # suite.addTest(detectionTest("test_case6"))
    # suite.addTest(detectionTest("test_case7"))
    # suite.addTest(detectionTest("test_case8"))
    # suite.addTest(detectionTest("test_case9"))
    # suite.addTest(detectionTest("test_case10"))
    # suite.addTest(detectionTest("test_case11"))
    # suite.addTest(detectionTest("test_quit"))
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
