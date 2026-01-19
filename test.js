var plusOne = function (digits) {
    for (let i = digits.length - 1; i >= 0; i--) {
        digits[i]++;              // add 1
        digits[i] %= 10;          // keep last digit
        if (digits[i] !== 0) {    // no carry → done
            return digits;
        }
    }
    // all were 9 → we have carry 1 at the front
    return [1, ...digits];
}

var subsets = function(nums) {
    let result = [];

    let backtrack = (path, start) => {
        result.push([...path]);
        for(let i = start; i < nums.length; i++){
            path.push(nums[i]);
            backtrack(path, i + 1);
            path.pop();
        }
    }
    backtrack([],0);

    return result;
};


var combinationSum = function(candidates, target) {
    let result = [];

    let backtrack = (remainSum , path , start) => {

        if(remainSum == target){
            result.push([...path])
        }

        if(remainSum >= target) return;

        for(let i = start; i < candidates.length; i++){
            path.push(candidates[i]);
            backtrack(remainSum + candidates[i], path, i);
            path.pop();
        }
    }
    backtrack(0 , [], 0)
};


var merge = function(arr) {
    let result = [];
    let n = arr.length;
    let i = 0;
    while(i > 0 && arr[i-1][1] < arr[i][0]){
        result.push(arr[i]);
        i++;
    }
    while(arr[i][1] >= arr[i+1][0]){
        let max = Math.max(arr[i][1], arr[i+1][1]);
        arr[i+1][1] = max;
        i++;
    }
    result.push(arr[i]);
    
    

    while(i < n){
        result.push(arr[i]);
        i++;
    }

    return result;
};

var eraseOverlapIntervals = function(intervals) {

    let result = [];
    intervals.sort((a,b) => a[1] - b[1]);
    let count = 0;
    let k = -Infinity;
    for(let i = 0; i < intervals.length; i++){
        let a = intervals[i][0];
        if(a < k){
            // we not got this interval 
            count++;
        }else{
            k = intervals[i][1];
        }
        
    }
    return count;
    
};


console.log(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]));