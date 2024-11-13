from tabulate import tabulate


def get_dict_items(jsonStr, number):
    if number == 1:
        tree_name = jsonStr[0]['A3809']
        times = 1
        # 过滤掉不符合条件的字典
        jsonStr = [i for i in jsonStr if "：" in i['A3809'] and "视频" not in i['A3809']]
        for i in jsonStr:
            i['check_times'] = times
            times += 1

        # 转换数据为列表格式，方便 tabulate 使用
        table_data = [[item["A3809"], item["check_times"]] for item in jsonStr]
        # 打印表格
        print(tabulate(table_data, headers=["项目", "练习编号"], tablefmt="grid"))
        # 用户输入选择
        while True:
            try:
                check_number = int(input('请选择您要选择的练习编号: '))
                if 1 <= check_number <= len(jsonStr):
                    break
                else:
                    print(f"请输入有效的练习编号（1 到 {len(jsonStr)}）")
            except ValueError:
                print("请输入一个数字编号")

        # 根据用户选择返回对应的字典
        data = next((item for item in jsonStr if item["check_times"] == check_number), None)
        return data, tree_name
    else:
        times = 1  # 初始化计数器
        # 过滤掉不符合条件的字符串
        jsonStr_with_times = []
        for i in jsonStr:
            item = {'A3809': i, 'check_times': times}
            jsonStr_with_times.append(item)
            times += 1

        # 转换数据为列表格式，方便 tabulate 使用
        table_data = [[item["A3809"], item["check_times"]] for item in jsonStr_with_times]
        # 打印表格
        print(tabulate(table_data, headers=["项目", "练习编号"], tablefmt="grid", showindex=False))
        # 用户输入选择
        while True:
            try:
                check_number = int(input('请选择您要选择的练习编号: '))
                if 1 <= check_number <= len(jsonStr_with_times):
                    break
                else:
                    print(f"请输入有效的练习编号（1 到 {len(jsonStr_with_times)}）")
            except ValueError:
                print("请输入一个数字编号")

        # 根据用户选择返回对应的字典
        data = next((item for item in jsonStr_with_times if item["check_times"] == check_number), None)
        return data['check_times']


if __name__ == '__main__':
    jsonStr = ['什么是单一窗口', '一般出口货物', '保税加工货物']
    get_dict_items(jsonStr,0)
