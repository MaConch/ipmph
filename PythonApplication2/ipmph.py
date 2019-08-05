
import urllib2
import urllib
b=0
for i in range(10000):
    c=str(b)
    value={'Cookie':'route=1f01391fe3c023160fbdc6e1a93698f8; _qddab=3-afe8wc.jyu6mte1; teaching-exam-token=Bearer%20eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiV0VCLXd4d3gxNTA2MDQwMjEwIiwiaWF0IjoxNTY0NzU0ODc1LCJleHAiOjE1NjQ3NzI4NzV9.swSnulZK4HeVLtPFjAZLbF80Z2_fxT9KFTV_SLxKI10c0RZqvWFRDL-UF3idEKWJO5eVpUBNl7WnxrKfxkzcnQ; teaching-exam-userInfo={%22expire%22:18000%2C%22userName%22:%22wxwx1506040210%22%2C%22realName%22:%22%E9%87%91%E6%AC%A3%E6%80%A1%22%2C%22examType%22:%22Ehls00%22%2C%22mobile%22:null%2C%22examTypeInfo%22:{%22alias%22:%22Ehls00%22%2C%22name%22:%22%E6%8A%A4%E5%A3%AB%E6%89%A7%E4%B8%9A%22%2C%22newsLink%22:%22/hushi/%22%2C%22courseCatalogID%22:17%2C%22courseCatalogInnercode%22:%22000004000001%22%2C%22questionCatalogID%22:366%2C%22questionCatalogInnercode%22:%22000011000001%22%2C%22pointCatalogID%22:95231%2C%22pointCatalogInnercode%22:%22000036000001%22%2C%22defualtChecked%22:false}%2C%22examTypeName%22:%22%E6%8A%A4%E5%A3%AB%E6%89%A7%E4%B8%9A%22%2C%22branchID%22:12794%2C%22branchInnerCode%22:%2200012794%22%2C%22branchName%22:%22%E6%97%A0%E9%94%A1%E5%8D%AB%E6%A0%A12020%22%2C%22userType%22:null}; _qddamta_2852152829=3-0; teaching-exam-examType={%22alias%22:%22Ehls00%22%2C%22name%22:%22%E6%8A%A4%E5%A3%AB%E6%89%A7%E4%B8%9A%22%2C%22newsLink%22:%22/hushi/%22%2C%22courseCatalogID%22:17%2C%22courseCatalogInnercode%22:%22000004000001%22%2C%22questionCatalogID%22:366%2C%22questionCatalogInnercode%22:%22000011000001%22%2C%22pointCatalogID%22:95231%2C%22pointCatalogInnercode%22:%22000036000001%22%2C%22defualtChecked%22:true}; _qdda=3-1.1; Hm_lpvt_ec31b23a3a54fb0e85df69fc93bd5de9=1564754848; _qddaz=QD.usjv1w.ihzweg.jyu6mtc4; __root_domain_v=.ipmph.com; Hm_lvt_ec31b23a3a54fb0e85df69fc93bd5de9=1564754848'}
    data=urllib.urlencode(value)
    header={'Authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiV0VCLXd4d3gxNTA2MDQwMjEwIiwiaWF0IjoxNTY0NzU4ODE0LCJleHAiOjE1NjQ3NzY4MTR9.nKAAgFdVjkprctY03ueOgmy__-5RnQ3SoA4ks_iNbEKmcAIC4760ojyySfT3Df4q3tkG5FIFEkHBgsl0mUtLxA'}
    url='http://exam.ipmph.com/teach/priv/member/Ehls00/course/uploadvideoschedule?courseId=729&courseUnitId='+c+'&pointId=&microCourseId=&classId=290&videoId=45758&position=99999&lastTime=2019-08-02+22:18:05&videoType=hd&videoSuffix=flv&platform=pc&IP='
    request = urllib2.Request(url,data,header)
    request.get_method = lambda: 'PUT'
    response = urllib2.urlopen(request)
    b=b+1
    print(b)

