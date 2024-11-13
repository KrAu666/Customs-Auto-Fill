import json
import re
import time
import execjs
from get_dict_item import get_dict_items

def get_course_list(session, CourseID):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://172.22.17.14:850',
        'Pragma': 'no-cache',
        'Referer': 'http://172.22.17.14:850/Mooc953Student/PracticeList?paras=121|97|110|90|104|101|110|103|61|50|52|49|50|56|55|38|108|111|103|105|110|84|121|112|101|61|49|55|38|117|115|101|114|84|121|112|101|61|49|38|99|108|97|115|115|78|111|61|51|56|53|38|117|115|101|114|82|105|103|104|116|115|61|48|38|65|49|49|49|54|61|48|38|65|49|49|49|55|61|48|38|67|111|117|114|115|101|76|97|110|103|117|97|103|101|61|99|110|38|99|111|117|114|115|101|67|97|116|101|103|111|114|121|61|49|55|38|99|111|117|114|115|101|73|100|61|49|49|55|49|50|38|65|49|48|49|49|49|61|49|38|76|97|110|103|117|97|103|101|83|101|108|101|99|116|61|49|38|116|121|112|101|61|49|38|115|116|97|116|117|115|61|48|38|99|116|121|112|101|61|48|38|65|49|49|48|56|61|57|53|51|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|49|48|61|49|50|38|115|116|117|100|101|110|116|73|100|61|50|52|49|50|56|55|38|109|101|110|117|73|110|100|101|120|61|50',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'courseId': CourseID,
        'contrltype': 'treelist',
        'language': '1',
    }

    response = session.post(
        'http://172.22.17.14:850/MoocOther/GetCourseCatalogList?paras=121|97|110|90|104|101|110|103|61|50|52|49|50|56|55|38|108|111|103|105|110|84|121|112|101|61|49|55|38|117|115|101|114|84|121|112|101|61|49|38|99|108|97|115|115|78|111|61|51|56|53|38|117|115|101|114|82|105|103|104|116|115|61|48|38|65|49|49|49|54|61|48|38|65|49|49|49|55|61|48|38|67|111|117|114|115|101|76|97|110|103|117|97|103|101|61|99|110|38|99|111|117|114|115|101|67|97|116|101|103|111|114|121|61|49|55|38|99|111|117|114|115|101|73|100|61|49|49|55|49|50|38|65|49|48|49|49|49|61|49|38|76|97|110|103|117|97|103|101|83|101|108|101|99|116|61|49|38|116|121|112|101|61|49|38|115|116|97|116|117|115|61|48|38|99|116|121|112|101|61|48|38|65|49|49|48|56|61|57|53|51|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|49|48|61|49|50|38|115|116|117|100|101|110|116|73|100|61|50|52|49|50|56|55|38|109|101|110|117|73|110|100|101|120|61|50',
        headers=headers,
        data=data,
        verify=False,
    )
    data = json.loads(response.text)
    tree_first = data['jsonStr']
    tree_first = json.loads(tree_first)

    return tree_first, session


# 主要修复的是 JSON 中嵌套的 HTML 字符串中的引号，确保它们被正确地转义
def fix_missing_commas(text):
    # Step 1: 修复对象键值对和数组元素之间的缺少逗号
    # 查找键值对之间或数组元素之间换行且没有逗号的情况，并在换行之前插入逗号
    text = re.sub(r'(?<=[}\]"\d])\s*[\r\n]+\s*(?=[{\["\d])', r',\n', text)
    # Step 2: 修复可能存在的嵌套情况
    # 如果对象或数组中存在嵌套，使用正则表达式确保嵌套结构的键值对之间也有逗号
    text = re.sub(r'(?<=["\d])\s*[\r\n]+\s*(?=["\w])', r',\n', text)
    # Step 3: 去除多余的逗号
    # 删除 '}' 或 ']' 之前可能存在的多余逗号，以确保不会产生错误的 JSON 结构
    text = re.sub(r',\s*(?=[}\]])', '', text)
    # Step 4: 去除逗号之后多余的空白符或换行符
    # 确保逗号后面是合法的换行或者空格，不会有多余的内容
    text = re.sub(r',\s*\n+', r',\n', text)
    # Step 5: 删除从 "A3828": 到 "A3812": 的部分
    # 删除从 "A3828": 开始到其值结束并包含 "A3812" 的部分
    text = re.sub(r'"A3828":\s*".*?"A3812":\s*[\d]+,?', '', text, flags=re.DOTALL)
    # 使用正则表达式删除从 "A3839t" 开始到 "A3825": 0, 的整个键值对
    text = re.sub(r'"A3839t":\s*".*?"A3825": 0,', '"A3825": 0,', text, flags=re.DOTALL)
    return text


def get_detailed_message(session, CourseID):
    tree_first, session = get_course_list(session, CourseID)
    number = 0
    list_number = execjs.compile(open('./get_course.js', 'r', encoding='utf-8').read()).call('get_list_number', tree_first)
    course_munber = get_dict_items(list_number, number)
    course_munber = int(course_munber)
    number += 1
    url = execjs.compile(open('./get_course.js','r', encoding='utf-8').read()).call('PracticeInto', course_munber - 1, tree_first)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'http://172.22.17.14:850/Mooc953Student/PracticeList?paras=121|97|110|90|104|101|110|103|61|50|52|49|50|56|55|38|108|111|103|105|110|84|121|112|101|61|49|55|38|117|115|101|114|84|121|112|101|61|49|38|99|108|97|115|115|78|111|61|51|56|53|38|117|115|101|114|82|105|103|104|116|115|61|48|38|65|49|49|49|54|61|48|38|65|49|49|49|55|61|48|38|67|111|117|114|115|101|76|97|110|103|117|97|103|101|61|99|110|38|99|111|117|114|115|101|67|97|116|101|103|111|114|121|61|49|55|38|99|111|117|114|115|101|73|100|61|49|49|55|49|50|38|65|49|48|49|49|49|61|49|38|76|97|110|103|117|97|103|101|83|101|108|101|99|116|61|49|38|116|121|112|101|61|49|38|115|116|97|116|117|115|61|48|38|99|116|121|112|101|61|48|38|65|49|49|48|56|61|57|53|51|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|49|48|61|49|50|38|115|116|117|100|101|110|116|73|100|61|50|52|49|50|56|55|38|109|101|110|117|73|110|100|101|120|61|50',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }

    data = {
        'courseId': CourseID,
        'pId': '3',
        'contrltype': 'treelist',
        'language': '1',
    }
    response = session.get(
        url,
        data=data,
        headers=headers,
        verify=False,
    )
    data = json.loads(response.text)
    jsonStr = data['jsonStr']
    jsonStr = jsonStr.encode().decode('unicode_escape')
    decoded_bytes = bytes(jsonStr, 'latin1')
    jsonStr = decoded_bytes.decode('utf-8')
    jsonStr = fix_missing_commas(jsonStr)
    jsonStr = json.loads(jsonStr)
    return session, url, jsonStr, number
