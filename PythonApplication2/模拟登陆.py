import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
import time
import urllib2
import urllib

username="wxwx1506030419"
password="Dxn2609763070"
driver=webdriver.Chrome()
driver.get("http://sso.ipmph.com/login?ServiceID=examanswer2019&Referer=http%3A%2F%2Fexam.ipmph.com%2Fmyschool%2Findex.html%23%2Findex");
time.sleep(3)
elem_username=driver.find_element_by_id("UserName")
elem_username.send_keys(username)
elem_password=driver.find_element_by_id("Password")
elem_password.send_keys(password)
elem_login=driver.find_element_by_xpath("//p[@class='zz-color']/input[@onclick='loginform_submit()']")
elem_login.click()
time.sleep(2)
driver.get("http://exam.ipmph.com/myschool/index.html#/courseDetail?courseType=0&courseID=729&classID=290")
time.sleep(2)
all_cookies=driver.get_cookies()
cookies=driver.get_cookie("teaching-exam-token")
if 'value' in cookies.keys():
    Authorization=cookies['value']
Authorization=Authorization[3:]
value={'Cookie':'route=1f01391fe3c023160fbdc6e1a93698f8; _qddab=3-afe8wc.jyu6mte1; teaching-exam-token=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiV0VCLXd4d3gxNTA2MDQwMjEwIiwiaWF0IjoxNTY0NzU0ODc1LCJleHAiOjE1NjQ3NzI4NzV9.swSnulZK4HeVLtPFjAZLbF80Z2_fxT9KFTV_SLxKI10c0RZqvWFRDL-UF3idEKWJO5eVpUBNl7WnxrKfxkzcnQ; teaching-exam-userInfo={%22expire%22:18000%2C%22userName%22:%22wxwx1506040210%22%2C%22realName%22:%22%E9%87%91%E6%AC%A3%E6%80%A1%22%2C%22examType%22:%22Ehls00%22%2C%22mobile%22:null%2C%22examTypeInfo%22:{%22alias%22:%22Ehls00%22%2C%22name%22:%22%E6%8A%A4%E5%A3%AB%E6%89%A7%E4%B8%9A%22%2C%22newsLink%22:%22/hushi/%22%2C%22courseCatalogID%22:17%2C%22courseCatalogInnercode%22:%22000004000001%22%2C%22questionCatalogID%22:366%2C%22questionCatalogInnercode%22:%22000011000001%22%2C%22pointCatalogID%22:95231%2C%22pointCatalogInnercode%22:%22000036000001%22%2C%22defualtChecked%22:false}%2C%22examTypeName%22:%22%E6%8A%A4%E5%A3%AB%E6%89%A7%E4%B8%9A%22%2C%22branchID%22:12794%2C%22branchInnerCode%22:%2200012794%22%2C%22branchName%22:%22%E6%97%A0%E9%94%A1%E5%8D%AB%E6%A0%A12020%22%2C%22userType%22:null}; _qddamta_2852152829=3-0; teaching-exam-examType={%22alias%22:%22Ehls00%22%2C%22name%22:%22%E6%8A%A4%E5%A3%AB%E6%89%A7%E4%B8%9A%22%2C%22newsLink%22:%22/hushi/%22%2C%22courseCatalogID%22:17%2C%22courseCatalogInnercode%22:%22000004000001%22%2C%22questionCatalogID%22:366%2C%22questionCatalogInnercode%22:%22000011000001%22%2C%22pointCatalogID%22:95231%2C%22pointCatalogInnercode%22:%22000036000001%22%2C%22defualtChecked%22:true}; _qdda=3-1.1; Hm_lpvt_ec31b23a3a54fb0e85df69fc93bd5de9=1564754848; _qddaz=QD.usjv1w.ihzweg.jyu6mtc4; __root_domain_v=.ipmph.com; Hm_lvt_ec31b23a3a54fb0e85df69fc93bd5de9=1564754848'}
data=urllib.urlencode(value)
header={'Authorization':Authorization}
url='http://exam.ipmph.com/teach/priv/member/Ehls00/course/uploadvideoschedule?courseId=729&courseUnitId='+'8648'+'&pointId=&microCourseId=&classId=290&videoId=45758&position=99999&lastTime='+time.strftime("%Y-%m-%d+%H:%M:%S", time.localtime()) +'&videoType=hd&videoSuffix=flv&platform=pc&IP='
request = urllib2.Request(url,data,header)
request.get_method = lambda: 'PUT'
response = urllib2.urlopen(request)
time.sleep(1)