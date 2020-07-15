import random

import allure
import requests
from config.conf import API_URL
from tools.api import request_tool

@allure.feature("用户管理")
@allure.story("充值提现模块")
@allure.title("扣款接口-账户余额不足") #修改用例标题
def test_chang_post_chongzhi(pub_data,db):
    res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL ;")
    pub_data["account_name"]=random.choice(res)[0]
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${account_name}",
  "changeMoney": 500000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_zyl_sql(db):
    # 执行查询sql语句
    with allure.step("第一步、执行SQL语句"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS=0 AND account_name IS NOT NULL;")
    # 从查询结果中随机获取一条，取第一个数据
    with allure.step("第二步、从查询结果中随机获取一条，取第一个数据"):
        account_name = random.choice(res)[0]
    data = {
        "accountName":account_name,
        "changeMoney":1000
    }
    # 使用requests框架发送http请求
    r = requests.post(API_URL + "/acc/charge",json=data)
    with allure.step("第五步、获取请求内容"):
        allure.attach(r.request.method, "请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url, "请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers), "请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body, "请求正文",allure.attachment_type.TEXT)
    with allure.step("第六步、获取响应内容"):
        allure.attach(str(r.status_code), "响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers), "响应头",allure.attachment_type.TEXT)
        allure.attach(r.text, "响应正文",allure.attachment_type.TEXT)
    with allure.step("第七步、断言"):
        allure.attach(r.text, "实际结果",allure.attachment_type.TEXT)
        allure.attach("账户余额不足", "预期结果",allure.attachment_type.TEXT)
        assert "账户余额不足" in r.text