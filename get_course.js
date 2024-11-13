const {JSDOM} = require('jsdom');
const {window} = new JSDOM();
const $ = require('jquery')(window);

function UrlEncrypt(object) {
    var n = 10;
    object = object ? object : new object();
    var type = typeof object;
    if (type != "object")
        return "";
    type = typeof n;
    if (type != "number")
        return "";
    /*添加用户编号*/
    var yanZheng = object["yanZheng"];
    if (yanZheng == undefined) {
        var queryObject = GetQueryStringToObject();
        var paras = UrlDecrypt(queryObject["paras"]);
        object["yanZheng"] = paras["yanZheng"];
    }

    var queryString = "";
    var str = "";
    $.each(object, function (key, value) {
        queryString += "&" + key + "=" + value;
    });
    if (queryString.indexOf("&") != -1) {
        queryString = queryString.substr(1);
    }
    //$.each(queryString, function (i) {
    //    str += queryString.charCodeAt(i).toString(n) + "|";
    //});
    for (var i = 0; i < queryString.length; i++) {
        str += queryString.charCodeAt(i).toString(n) + "|";
    }
    str = str.substr(0, (str.length - 1));
    return str;
}

function UrlDecrypt(str) {
    var n = 10;
    str = str ? str : "";
    var type = typeof str;
    if (type != "string")
        return "";
    type = typeof n;
    if (type != "number")
        return "";

    var object = new Object();
    var queryString = "";
    var strs = str.split("|");

    $.each(strs, function (i, s) {
        queryString += String.fromCharCode(parseInt(s, n));
    });
    var queryStrings = queryString.split("&");
    $.each(queryStrings, function (i, s) {
        object[s.split("=")[0]] = unescape(s.split("=")[1]);
    });
    // console.log(object);
    return object;
}

function PracticeInto(i, tree_first) {
    console.log(i)
    console.log(tree_first)
    var obj = UrlDecrypt('121|97|110|90|104|101|110|103|61|50|52|49|50|56|55|38|108|111|103|105|110|84|121|112|101|61|49|55|38|117|115|101|114|84|121|112|101|61|49|38|99|108|97|115|115|78|111|61|51|56|53|38|117|115|101|114|82|105|103|104|116|115|61|48|38|65|49|49|49|54|61|48|38|65|49|49|49|55|61|48|38|67|111|117|114|115|101|76|97|110|103|117|97|103|101|61|99|110|38|99|111|117|114|115|101|67|97|116|101|103|111|114|121|61|49|55|38|99|111|117|114|115|101|73|100|61|49|49|55|49|50|38|65|49|48|49|49|49|61|49|38|76|97|110|103|117|97|103|101|83|101|108|101|99|116|61|49|38|116|121|112|101|61|49|38|115|116|97|116|117|115|61|48|38|99|116|121|112|101|61|48|38|65|49|49|48|56|61|57|53|51|38|65|49|49|48|57|61|57|53|51|48|38|65|49|49|49|48|61|49|50|38|115|116|117|100|101|110|116|73|100|61|50|52|49|50|56|55|38|109|101|110|117|73|110|100|101|120|61|50');
    var model = tree_first[i];
    obj["tree_id"] = model.id;
    obj["tree_name"] = model.A3809;
    var strParas = UrlEncrypt(obj); // 加密
    var url = "http://172.22.17.14:850/MoocOther/GetCourseCatalogList?paras=" + strParas;
    return url
}

function get_list_number(tree_first) {
    return tree_first.map(model => model.A3809);
}