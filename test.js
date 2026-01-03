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
};


console.log(plusOne([1,0,8,9,9]));