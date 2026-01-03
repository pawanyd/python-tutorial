var nextGreaterElement = function (num1, num2) {

    let s = [];
    let ngmap = {};

    s.push(num2[num2.length - 1]);
    ngmap[num2[num2.length - 1]] = -1;
    for (let i = num2.length - 2; i >= 0; i--) {
        top = s[s.length - 1];
        console.log(top);
        debugger;
        if (num2[i] < top) {
            s.push(num2[i]);
            ngmap[num2[i]] = top;
        } else {
            while (s.length) {
                if (s[s.length - 1] < num2[i]) {
                    s.pop();
                }else{
                    ngmap[num2[i]] = s[s.length - 1];
                    break;
                }
            }
            if(s.length == 0){
                ngmap[num2[i]] = -1;
            }
        }
        s.push(num2[i]);
    }
    let res = [];
    for(let j =0; j < num1.length; j++){
        if(ngmap[num1[j]]){
            res.push(ngmap[num1[j]]);
        }
    }

    return ngmap;
};

console.log(nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]));