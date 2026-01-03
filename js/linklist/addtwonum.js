function ListNode(val, next = null) {
    this.val = val;
    this.next = next;
}

function arrayToList(arr) {
    let dummy = new ListNode(0);
    let current = dummy;

    for (let num of arr) {
        current.next = new ListNode(num);
        current = current.next;
    }
    return dummy.next;
}


function listToArray(node) {
    let result = [];
    while (node) {
        result.push(node.val);
        node = node.next;
    }
    return result;
}


var addTwoNumbers = function(l1, l2) {
    let carry = 0;
    let result = [];
    while(l1 && l2 && l1.next && l2.next){
        
        let sum = l1.val + l2.val + carry;
        debugger;
        carry = (sum / 10);
        digit =  Math.floor(sum % 10);

        result.push(digit);

        l1 = l1.next;
        l2 = l2.next;

        console.log(l1);
        console.log(l2);
    }
    return result;
};

console.log(addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]));