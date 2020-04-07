

import {T, R, S, V} from "./myjs/util/Commonly.js";

T.getTypeDoById("history-container").addEventListener(
    'click', function (e) {
        console.log(e);
        console.log(e.target.value)
    }, true
);