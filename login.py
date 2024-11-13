import json
import execjs
import sys

def login(session, student_number, password):
    password = execjs.compile(open('./password.js','r',encoding='utf-8').read()).call('Login_Common', password)

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://172.22.17.14:850',
        'Pragma': 'no-cache',
        'Referer': 'http://172.22.17.14:850/User/LoginPage953?paras=65%7C49%7C49%7C49%7C48%7C61%7C49%7C50%7C38%7C65%7C49%7C49%7C49%7C55%7C61%7C48%7C38%7C65%7C49%7C49%7C49%7C54%7C61%7C48%7C38%7C108%7C111%7C103%7C105%7C110%7C84%7C121%7C112%7C101%7C61%7C49%7C55%7C38%7C65%7C49%7C49%7C48%7C57%7C61%7C57%7C53%7C51%7C48%7C38%7C65%7C49%7C49%7C48%7C56%7C61%7C57%7C53%7C51',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'loginType': '17',
        'uName': student_number,
        'uPass': password,
        'myLanguage': '1',
    }

    response = session.post(
        'http://172.22.17.14:850/User/Login?paras=65|49|49|49|48|61|49|50|38|65|49|49|49|55|61|48|38|65|49|49|49|54|61|48|38|108|111|103|105|110|84|121|112|101|61|49|55|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|48|56|61|57|53|51|38|121|97|110|90|104|101|110|103|61|117|110|100|101|102|105|110|101|100',
        headers=headers,
        data=data,
        verify=False,
    )
    if '登陆成功' in response.text:
        data = json.loads(response.text)
        name = data['modelUser']['UserName']
        UserId = data['modelUser']['UserId']
        CourseID = data['modelCourse']['CourseID']
        print(f'{name}: 登陆成功')
    else:
        print('登录失败，请检查密码')
        # 密码错误则终止进程
        sys.exit()
    return session, name, UserId, CourseID

