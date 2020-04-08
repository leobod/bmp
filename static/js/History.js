

import {T, R, S, V} from "./myjs/util/Commonly.js";


console.log(T.getTypeInById("currentpage").getAttribute("value"));


T.getTypeDoById("history-container").addEventListener(
    'click', function (e) {
        console.log(e.target.value);
        let oid = e.target.value;
        let csrf_token = S.getCsrf();
        R.ajax({
            method: 'POST',
            url: './result.do',
            data: {
                "oid": oid,
                "csrfmiddlewaretoken": csrf_token
            },
            success: function (response) {
                console.log("跳转到结果页面");
            }
        });
    }, true
);