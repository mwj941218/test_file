from selenium import webdriver
import time
import unittest


browser = webdriver.Chrome()
#browser.get('https://weixin.drcuiyutao.com/yxy-edu-web/myMaster?_channel=wx&appId=wx390b4e4d1ef0531b&openId=oznT70zc6X4hwBC4boYaWnWGBhYU&city=%E6%9C%9D%E9%98%B3&country=%E4%B8%AD%E5%9B%BD&headImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FDYAIOgq83eo47pe8Q0Lao3oyRTyK1BtfHw1lmT8CMkN1aRw1URRXmhX6icydiauk8INISADttC5Ks9iaII0E6mGVQ%2F132&nickName=andyma&sex=1&unionId=oowDnshkL608XHQTjUl0sIbdF5wA&accountId=361167232757432320&memberId=7736046')
browser.get('https://testweixin.drcuiyutao.com/yxy-edu-web/mymaster?evaluationTypeCode=d2c3eaf4ea9e42ae98c78d3a154b8ec5&_channel=wx&appId=wx51baca73da72c79f&openId=oVEKu5vD5LW0Z0HB7lC7SZ_QjZeA&city=朝阳&country=中国&headImgUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FDYAIOgq83eqANv6JSLyv6WXgoy4GPz1f6sJRBT7kELJEaKSbcyTBmfiaqkt4AxVh9Jr5yc8mlITNqpE5BXerGYA%2F132&nickName=andyma&sex=1&unionId=oowDnshkL608XHQTjUl0sIbdF5wA&accountId=369164504358100992&memberId=351872389&next=&titleFlag=false&childId=368433371823669248&birthday=1378656000000&month=67&ageRange=2&monthRange=30&courseId=353911173360619520&objectId=353911264490262528&tiroCourseType=&orderCode=&exchangeFrom=&productId=&o2oType=1&createTime=1564133503912&couponId=61c3de935fe64db1bd1fb614c99b3904&call_pay=1&courseType=')

time.sleep(3)
print(browser.find_elements_by_class_name('flexDiv')[0].text)
time.sleep(3)
print(browser.find_element_by_id('eduCenter').text)
browser.find_element_by_id('eduCenter').click()
time.sleep(3)
assert '小育专栏111' in browser.title
time.sleep(3)
browser.back()


# str = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/h4').text

browser.close()


# browser.find_elements_by_class_name('flexDiv')[0].click()
# print(browser.find_element_by_xpath('//*[@id="app"]/div/ul/li[1]/div[1]').text)
# print(browser.find_elements_by_class_name('mymasterBox')[1].find_elements_by_class_name('flexDiv')[1].text)
#app > div > ul > li:nth-child(2) > div:nth-child(1)
#//*[@id="app"]/div/ul/li[1]/div[1]
#//*[@id="app"]/div/ul/li[1]/div[1] //*[@id="app"]/div/ul/li[1]/div[1]

