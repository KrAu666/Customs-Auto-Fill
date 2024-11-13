import json
import re
import time

from get_unicode import new_unicode

def auto_answer(data, url_datas, session):
    # &A3816=None删除
    # 使用正则表达式删除 &A3816= 后的内容
    data_url = re.sub(r"&A3816=[^&]*", "", url_datas)
    # 使用正则表达式提取数据并直接赋值给变量
    # 将字符串中的反斜杠替换为双反斜杠
    data = data.replace('\\', '')

    # 使用正则表达式提取数据
    docAnswerId_match = re.search(r'"A4013_DT":\s*(\d+)', data)
    A3802_match = re.search(r'"A3802":\s*(\d+)', data)
    DocName_match = re.search(r'"A4024":\s*"([^"]*)"', data)
    DocType_match = re.search(r'"A4009":\s*"([^"]*)"', data)
    docId_match = re.search(r'"A4013":\s*(\d+)', data)

    # 将匹配结果赋值给变量，如果没有匹配则为 None
    docAnswerId = int(docAnswerId_match.group(1)) if docAnswerId_match else None
    A3802 = int(A3802_match.group(1)) if A3802_match else None
    DocName = DocName_match.group(1) if DocName_match else None
    DocType = DocType_match.group(1) if DocType_match else None
    docId = int(docId_match.group(1)) if docId_match else None

    # 匹配内容
    data_url = data_url + f'&DocId={docId}&DocType={DocType}&DocStyle=0&DocName={DocName}&docAnswerId={docAnswerId}&A3802={A3802}&IsMain=1'
    data_url = new_unicode(data_url)
    data_url = f'http://172.22.17.14:850/Document/MakeDocument?paras={data_url}'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://172.22.17.14:850',
        'Pragma': 'no-cache',
        'Referer': 'http://172.22.17.14:850/Document/M05?show=0&paras=121|97|110|90|104|101|110|103|61|50|52|49|50|56|55|38|108|111|103|105|110|84|121|112|101|61|49|55|38|117|115|101|114|84|121|112|101|61|49|38|99|108|97|115|115|78|111|61|51|56|53|38|117|115|101|114|82|105|103|104|116|115|61|48|38|65|49|49|49|54|61|48|38|65|49|49|49|55|61|48|38|67|111|117|114|115|101|76|97|110|103|117|97|103|101|61|99|110|38|99|111|117|114|115|101|67|97|116|101|103|111|114|121|61|49|55|38|99|111|117|114|115|101|73|100|61|49|49|55|49|50|38|65|49|48|49|49|49|61|49|38|76|97|110|103|117|97|103|101|83|101|108|101|99|116|61|49|38|116|121|112|101|61|49|38|115|116|97|116|117|115|61|48|38|99|116|121|112|101|61|48|38|65|49|49|48|56|61|57|53|51|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|49|48|61|49|50|38|115|116|117|100|101|110|116|73|100|61|50|52|49|50|56|55|38|109|101|110|117|73|110|100|101|120|61|50|38|116|114|101|101|95|105|100|61|51|38|116|114|101|101|95|110|97|109|101|61|19968|33324|20986|21475|36135|29289|38|112|97|103|101|73|100|61|49|54|53|38|68|111|99|73|100|61|49|51|57|54|55|55|50|53|38|68|111|99|84|121|112|101|61|77|48|53|38|68|111|99|83|116|121|108|101|61|48|38|68|111|99|78|97|109|101|61|20986|21475|36135|29289|25253|20851|21333|38|100|111|99|65|110|115|119|101|114|73|100|61|49|50|56|51|55|49|56|50|38|65|51|56|48|50|61|49|54|53|38|73|115|77|97|105|110|61|49',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'docId': docId,
        'userRole': '0',
        'language': '1',
    }

    response = session.post(
        data_url,
        headers=headers,
        data=data,
        verify=False,
    )
    data = json.loads(response.text)
    Msg = data['result']['Msg']
    print(Msg)
