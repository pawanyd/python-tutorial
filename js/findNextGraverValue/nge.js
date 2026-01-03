var nextGreaterElement = function(nums1, nums2) {
    let stack=[];
    let map= new Map();
    debugger;
    for(num of nums2){
        while(stack.length>0 && num> stack[stack.length-1] ){
            map.set(stack.pop(),num)
        }
        stack.push(num)
    }

    while(stack.length>0){
        map.set(stack.pop(),-1)
    }
     let result = [];
    for (let num of nums1) {
        result.push(map.get(num));
    }
    return result;
};

console.log(nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]));