/**
 *
 */

import {T, R, S, V} from "./myjs/util/Commonly.js";
import {hex_md5} from "./myjs/T01/Md5.js";

const COM = {
    ACCOUNT: "in-account",
    SMSCODE: "in-smscode",
    PASSWORD: "in-password",
    REPASSWORD: "in-password-re",
    ERROR: "out-tips",
    SMS: "do-smscode",
    REGISTER: "do-register",
    LOGIN: "do-login",
    FORGET: "do-forget",
};
const ERRORTIPS = {
    NOERROR: "",
    ACCOUNT: "提示: 请输入正确的手机号。",
    PASSWORD: "提示: 密码不一致",
    BLANKACCOUNT: "提示: 手机号不得为空。",
    BLANKSMSCODE: "提示: 验证码不得为空。",
    BLANKPASSWORD: "提示: 密码不得为空。",
    BLANKREPASSWORD: "提示: 再次确认密码为空",
    PASSWORDNOTSAME: "提示: 2次输入密码不一致",
    REGISTER: "提示: 出现错误，请重试。"
};


// 账号输入栏，失去焦点后，验证是否为空，是否符合账号规则
var blurAccount = function () {
    validateAccount();
};
var validateAccount = function () {
    let str_account = T.getTypeInValueById(COM.ACCOUNT);
    let isaccount = V.checkPhone(str_account);
    if (T.showError(str_account, "", COM.ERROR, ERRORTIPS.BLANKACCOUNT, ERRORTIPS.NOERROR)) {
        return false;
    } else if (!isaccount) {
        T.showError(isaccount, false, COM.ERROR, ERRORTIPS.ACCOUNT, ERRORTIPS.NOERROR);
        return false;
    } else {
        return true;
    }
};

// 短信验证输入栏，失去焦点后，验证是否为空
var blurSmscode = function () {
    validateSmscode();
};
var validateSmscode = function () {
    let str_smscode = T.getTypeInValueById(COM.SMSCODE);
    if (!T.showError(str_smscode, "", COM.ERROR, ERRORTIPS.BLANKSMSCODE, ERRORTIPS.NOERROR)) {
        return false;
    }
    return true;
};

// 密码输入栏，失去焦点后，验证是否为空
var blurPassword = function () {
    validatePassword();
};
var validatePassword = function () {
    let str_password = T.getTypeInValueById(COM.PASSWORD);
    if (!T.showError(str_password, "", COM.ERROR, ERRORTIPS.BLANKPASSWORD, ERRORTIPS.NOERROR)) {
        return false;
    }
    return true;
};


// 确认密码输入栏，失去焦点后，验证是否为空
var blurRePassword = function () {
    validateRePassword();
};
var validateRePassword = function () {
    let str_repassword = T.getTypeInValueById(COM.REPASSWORD);
    let str_password = T.getTypeInValueById(COM.PASSWORD);
    let password_state = (str_password == str_repassword);
    if (!T.showError(str_repassword, "", COM.ERROR, ERRORTIPS.BLANKREPASSWORD, ERRORTIPS.NOERROR)) {
        return false;
    } else if (!password_state) {
        T.showError(password_state, false, COM.ERROR, ERRORTIPS.PASSWORDNOTSAME, ERRORTIPS.NOERROR);
        return false;
    }
    return true;
};

var clickSms = function () {
    let accountState = validateAccount();
    // console.log("ClickSms_outter");
    // console.log(accountState);
    let str_account = T.getTypeInValueById(COM.ACCOUNT);
    if (accountState) {
        // console.log("ClickSms_inner");
        let csrf_token = S.getCsrf();
        R.ajax({
            method: 'POST',
            url: './sms.do',
            data: {
                "account": str_account,
                "csrfmiddlewaretoken": csrf_token,
            },
            success: function (response) {
                // console.log(response);
            }
        });
        let btn_sms = T.getTypeDoById(COM.SMS);
        let res = btn_sms.getAttribute("timer");
        if (res === null || res == 0) {
            res = 10;
            btn_sms.setAttribute("timer", res);
            clickSmsChange();
        } else {

        }
    }

};

var clickSmsChange = function () {
    let state = setInterval(function refresh() {
        let btn_sms = T.getTypeDoById(COM.SMS);
        let res = btn_sms.getAttribute("timer");
        // console.log(res);
        if (res == 0) {
            btn_sms.setAttribute("timer", res);
            // console.log("state: " + state)
            T.getTypeDoById(COM.SMS).removeAttribute("disabled")
            T.getTypeDoById(COM.SMS).innerText = "发送验证码";
            clearInterval(state);
        } else {
            res--;
            btn_sms.setAttribute("timer", res);
            T.getTypeDoById(COM.SMS).setAttribute("disabled", true);
            T.getTypeDoById(COM.SMS).innerText = res.toString() + "s 后可重发"
        }
    }, 1000);
};

var clickForget = function () {
    T.setTypeOutValue(COM.ERROR, "");
    console.log(1);
    if (validateAccount() && validateSmscode() && validatePassword() && validateRePassword()) {

    } else {
        console.log(2);
        let str_account = T.getTypeInValueById(COM.ACCOUNT);
        let str_code = T.getTypeInValueById(COM.SMSCODE);
        let str_password = T.getTypeInValueById(COM.PASSWORD);

        let csrf_token = S.getCsrf();
        let real_password = hex_md5(str_password);
        R.ajax({
            method: 'POST',
            url: './forget.do',
            data: {
                "account": str_account,
                "code": str_code,
                "password": real_password,
                "csrfmiddlewaretoken": csrf_token,
            },
            success: function (response) {
                console.log(response);
                if (response == "True") {
                    T.setTypeOutValue(COM.ERROR, "提示: 修改成功，请返回登录");
                } else {
                    T.setTypeOutValue(COM.ERROR, "提示: 修改失败,请重试");
                }
            }
        });
    }
};

var clickLogin = function () {
    window.location.href = "./";
};

T.getTypeInById(COM.ACCOUNT).onblur = blurAccount;
T.getTypeInById(COM.SMSCODE).onblur = blurSmscode;
T.getTypeInById(COM.PASSWORD).onblur = blurPassword;
T.getTypeInById(COM.REPASSWORD).onblur = blurRePassword;

T.getTypeDoById(COM.SMS).onclick = clickSms;
T.getTypeDoById(COM.FORGET).onclick = clickForget;
T.getTypeDoById(COM.LOGIN).onclick = clickLogin;
