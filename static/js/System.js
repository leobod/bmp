


import {T, R, S, V} from "./myjs/util/Commonly.js";

var clickExit = function () {
    let csrf_token = S.getCsrf();
    R.ajax({
        method: 'POST',
        url: './exit.do',
        data: {
            "csrfmiddlewaretoken": csrf_token,
        },
        success: function (response) {
            console.log(response);
            if (response == "True") {
                window.location.href = "/";
            } else {
            }
        }
    });
};


T.getTypeDoById("do-exit").onclick = clickExit;
T.getTypeDoById("to-exit").onclick = clickExit;
