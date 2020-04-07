

import {T, R, S, V} from "./myjs/util/Commonly.js";


console.log(T.getTypeInById("currentpage").getAttribute("value"));


T.getTypeDoById("history-container").addEventListener(
    'click', function (e) {
        console.log(e);
        console.log(e.target.value)
    }, true
);