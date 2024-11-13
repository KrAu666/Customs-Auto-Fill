global.window = {}; // 模拟 window 对象
const JSEncrypt = require('jsencrypt'); // 确保你已安装并引入 jsencrypt


Login_Common = function (str) {
    var rsaStr = str;
    var rsaPublicKey = 'MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgG95YsdRJdcvMJZCopqAcC2n6kjIj28DeRxqvnEL5DmtO52icLIwwQ3ZZ/nhYzNNq0tg5vrw2PxC7ozqJ49eeoT/PO5wbQ+BMlYrHW1r/+uWXuOTMf9yYDJQ6YfXmpZbYkn+3jQtvALHADCqMz84Yi+kiGXJmtM+TOU6LmAeJ3GTAgMBAAE=';//字符串
    if (rsaPublicKey != "") {
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(rsaPublicKey);//公钥字符串
        var data = encrypt.encrypt(str);//加密字符串
        rsaStr = encodeURI(data).replace(/\+/g, '%2B');
    }
    return rsaStr;
}