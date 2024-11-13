import time

from get_unicode import new_unicode

def get_practice_message(data, session, UserId, tree_name):
    datas = f'yanZheng=241287&loginType=17&userType=1&classNo=385&userRights=0&A1116=0&A1117=0&CourseLanguage=cn&courseCategory=17&courseId={data["A3806"]}&A10111=1&LanguageSelect=1&type=1&status=0&ctype=0&A1108=953&A1109=9530&A1110=12&studentId=241287&menuIndex=2&tree_id=3&tree_name={tree_name}&pageId={data["id"]}&A3816={data["A3816t"]}'
    data_url = new_unicode(datas)
    data_url = f'http://172.22.17.14:850/Mooc954Student/GetPageContentDetail?paras={data_url}'

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-HK;q=0.5,zh-TW;q=0.4',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://172.22.17.14:850',
        'Pragma': 'no-cache',
        'Referer': 'http://172.22.17.14:850/Mooc954Student/DoExam?paras=121|97|110|90|104|101|110|103|61|50|52|49|50|56|55|38|108|111|103|105|110|84|121|112|101|61|49|55|38|117|115|101|114|84|121|112|101|61|49|38|99|108|97|115|115|78|111|61|51|56|53|38|117|115|101|114|82|105|103|104|116|115|61|48|38|65|49|49|49|54|61|48|38|65|49|49|49|55|61|48|38|67|111|117|114|115|101|76|97|110|103|117|97|103|101|61|99|110|38|99|111|117|114|115|101|67|97|116|101|103|111|114|121|61|49|55|38|99|111|117|114|115|101|73|100|61|49|49|55|49|50|38|65|49|48|49|49|49|61|49|38|76|97|110|103|117|97|103|101|83|101|108|101|99|116|61|49|38|116|121|112|101|61|49|38|115|116|97|116|117|115|61|48|38|99|116|121|112|101|61|48|38|65|49|49|48|56|61|57|53|51|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|49|48|61|49|50|38|115|116|117|100|101|110|116|73|100|61|50|52|49|50|56|55|38|109|101|110|117|73|110|100|101|120|61|50|38|116|114|101|101|95|105|100|61|51|38|116|114|101|101|95|110|97|109|101|61|19968|33324|20986|21475|36135|29289|38|112|97|103|101|73|100|61|49|54|55',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'userId': UserId,
        'A3801': data['A3801'],
        'A3802': data['A3802'],
        'A3806': data['A3806'],
        'language': '1',
    }

    response = session.post(
        data_url,
        headers=headers,
        data=data,
        verify=False,
    )

    return response.text, datas, session
