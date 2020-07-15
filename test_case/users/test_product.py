import pytest

from tools.api import request_tool
@pytest.mark.zyl
def test_dl(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=0ecb72339dd649bbbd6710089d5c8f8f; StuID=507; sidebarStatus=0'}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "pwd": "aaa123",
  "userName": "aaa123"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)



def test_addProd(pub_data):
    pub_data["productCode"]="自动生成 字符串 4 数字 xuepl"
    pub_data["productName"]="自动生成 字符串 4 数字 xuep2"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    header={"token":"${token}"}
    expect = ""  # 预期结果
    json_data='''{
  "brand": "小黑",
  "colors": [
    "宋小宝的黑"
  ],
  "price": 999,
  "productCode": "${productCode}",
  "productName": "${productName}",
  "sizes": [
    "256G"
  ],
  "type": "数码"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(headers=header,method=method,url=uri,pub_data=pub_data,expect=expect,feature=feature,story=story,title=title,json_data=json_data)
