
// for example we have array in javascript 

// const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// find 5

// do not suggest anything i do it myself 


var findErrorNums = function(nums) {
    const n = nums.length;
    const freq = new Array(n + 1).fill(0); // index 1..n

    // count frequency of each number
    for (let num of nums) {
        freq[num]++;
    }

    let duplicate = -1;
    let missing = -1;

    // find number with count 2 and count 0
    for (let i = 1; i <= n; i++) {
        if (freq[i] === 2) duplicate = i;
        else if (freq[i] === 0) missing = i;
    }

    return [duplicate, missing];
};

// findErrorNums([1,2,2,4]);

console.log(findErrorNums([1,2,2,4]));

console.log(Array.sort([5,2,3,6,8,9,10]));