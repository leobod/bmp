


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

var clickSystem = function () {
    window.location.href = "./index";
};
var clickUpload = function () {
    window.location.href = "./upload";
};
var clickHistory = function () {
    window.location.href = "./history";
};
var clickResult = function () {
    window.location.href = "./result";
};

T.getTypeDoById("do-exit").onclick = clickExit;
T.getTypeDoById("to-exit").onclick = clickExit;

T.getTypeDoById("to-system").onclick = clickSystem;
T.getTypeDoById("to-upload").onclick = clickUpload;
T.getTypeDoById("to-history").onclick = clickHistory;
T.getTypeDoById("to-predict").onclick = clickResult;
