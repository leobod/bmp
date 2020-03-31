/**
 * @File: T or CustomToolor
 * @Description: 用于操作自定义的DOM
 */
var CustomToolor = {
    getComById : function (str_id_name) {
        return document.getElementById(str_id_name);
    },

    getTypeInById: function (str_id_name) {
        return this.getComById(str_id_name);
    },
    getTypeInValueById: function (str_id_name) {
        return this.getTypeInById(str_id_name).value;
    },
    getTypeInCheckedById: function (str_in_name) {
        return this.getComById(str_in_name).checked;
    },

    getTypeOutById: function (str_id_name) {
        return this.getComById(str_id_name);
    },
    setTypeOutValue: function (str_id_name, str_out_value) {
        this.getTypeOutById(str_id_name).innerText = str_out_value;
    },

    getTypeDoById: function (str_id_name) {
        return this.getComById(str_id_name);
    },

    showError: function (str_in, rule, custom_component, error1, error2) {
        if (str_in === rule) {
            this.setTypeOutValue(custom_component, error1);
            return true;
        } else {
            this.setTypeOutValue(custom_component, error2);
            return false;
        }
    },
};
var T = CustomToolor;

/**
 * @File: R or CustomRequest
 * @Description: 与Http等的请求相关
 */
var CustomRequest = {
    /**
     * @Name: ajax()
     * @Parameter: opt -> dict
     * @Describe：Gets the component values associated with CSRF in Django
     * @Premise: null
     * @Case: R.ajax({ method: 'POST',
     *                 url: './login.do',
     *                 data: { "account": str_account, "password": str_password, "csrfmiddlewaretoken": csrf_token },
     *                 success: function (response) { console.log(response); }
     *                });
     */
    ajax: function (opt) {
        opt = opt || {};
        opt.method = opt.method.toUpperCase() || 'POST';
        opt.url = opt.url || '';
        opt.async = opt.async || true;
        opt.data = opt.data || null;
        opt.success = opt.success || function () {};
        var xmlHttp = null;
        if (XMLHttpRequest) {
            xmlHttp = new XMLHttpRequest();
        }
        else {
            xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
        }var params = [];
        for (var key in opt.data){
            params.push(key + '=' + opt.data[key]);
        }
        var postData = params.join('&');
        if (opt.method.toUpperCase() === 'POST') {
            xmlHttp.open(opt.method, opt.url, opt.async);
            xmlHttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded;charset=utf-8');
            xmlHttp.send(postData);
        }
        else if (opt.method.toUpperCase() === 'GET') {
            xmlHttp.open(opt.method, opt.url + '?' + postData, opt.async);
            xmlHttp.send(null);
        }
        xmlHttp.onreadystatechange = function () {
            if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
                opt.success(xmlHttp.responseText);
            }
        };
    },
};
var R = CustomRequest;

/**
 * @File: S or Security
 * @Description: 与安全相关的配置
 */
var CustomSecurity = {
    /**
     * @Name: getCsrf()
     * @Parameter: null
     * @Describe：Gets the component values associated with CSRF in Django
     * @Premise: CSRF needs to be injected into Html in advance
     */
    getCsrf: function () {
        let res = document.getElementsByName("csrfmiddlewaretoken");
        return res[0].value;
    },
};
var S = CustomSecurity;

/**
 * @File: V (Validator.js)
 * @Description: 与验证相关的模块
 */
var CustomValidator = {
    checkPhone : function(str_phone){
        const reg = /^[1][3,4,5,6,7,8,9][0-9]{9}$/;
        return reg.test(str_phone);
    },
};
var V = CustomValidator;

export {CustomToolor, CustomRequest, CustomSecurity, CustomValidator};
export {T, R, S, V};
