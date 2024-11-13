import requests
from login import login
from GetCourseCatalogList import get_detailed_message
from get_dict_item import get_dict_items
from get_practice_message import get_practice_message
from auto_practice_answer import auto_answer
session = requests.session()

# 登陆所需要的学号
student_number = ''
# 密码
password = ''


# 登录中
session, name, UserId, CourseID = login(session, student_number, password)

# 获取课程对应的代码
# 从这一步开始自动获取答案的接口所需要的绝大部分参数就已经全部获取成功了，参数从这里面找
session, url, jsonStr, number = get_detailed_message(session, CourseID)

# 对要自动填写的练习进行一次筛选，只留下要操作的那一个
data, tree_name = get_dict_items(jsonStr, number)

# 进入所选的练习
data, url_datas, session = get_practice_message(data, session, UserId, tree_name)

# 自动填写内容
auto_answer(data, url_datas, session)

