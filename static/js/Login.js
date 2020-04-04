/**
 *
 */

import {T, R, S, V} from "./myjs/util/Commonly.js";

import {hex_md5} from "./myjs/T01/Md5.js";

const COM = {
    ACCOUNT: "in-account",
    PASSWORD: "in-password",
    REMEMBER: "in-remember",
    ERROR: "out-tips",
    LOGIN: "do-login",
    REGISTER: "do-register",
    FORGET: "do-forget",
};
const ERRORTIPS = {
    NOERROR: "",
    ACCOUNT: "提示: 请输入正确的手机号。",
    PASSWORD: "提示: 密码不可以为空",
    LOGIN: "提示: 请检查你的输入，并输入正确的账号和密码。",
};

var blurAccount = function () {
    let str_acount = T.getTypeInValueById(COM.ACCOUNT);
    let isaccount = V.checkPhone(str_acount);
    T.showError(isaccount, false, COM.ERROR, ERRORTIPS.ACCOUNT, ERRORTIPS.NOERROR);
};

var clickLogin = function () {
    T.setTypeOutValue(COM.ERROR, "");
    let str_account = T.getTypeInValueById(COM.ACCOUNT);
    if (V.checkPhone(str_account)) {
        let str_password = T.getTypeInValueById(COM.PASSWORD);
        if (str_password !== "") {
            str_password = hex_md5(str_password);
            let is_remember = T.getTypeInCheckedById(COM.REMEMBER);
            let csrf_token = S.getCsrf();

            R.ajax({
                method: 'POST',
                url: './login.do',
                data: {
                    "account": str_account,
                    "password": str_password,
                    "csrfmiddlewaretoken": csrf_token
                },
                success: function (response) {
                    if (response == "True") {
                        if (is_remember) {
                            document.cookie = "bmp_account =" + str_account;
                            document.cookie = "bmp_password = " + str_password;
                        }
                        window.location.href = "/system/";
                    } else {
                        T.setTypeOutValue(COM.ERROR, "提示： 账号或密码错误，请重试");
                    }
                }
            });
        } else {
            T.setTypeOutValue(COM.ERROR, ERRORTIPS.PASSWORD);
        }
    } else {
        T.setTypeOutValue(COM.ERROR, ERRORTIPS.ACCOUNT);
    }

};
var clickRegister = function () {
    window.location.href = "./register";
};


T.getTypeInById(COM.ACCOUNT).onblur = blurAccount;
T.getTypeDoById(COM.LOGIN).onclick = clickLogin;
T.getTypeDoById(COM.REGISTER).onclick = clickRegister;
