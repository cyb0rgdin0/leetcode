/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.stack = []
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.stack[this.stack.length] = x
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.splice(this.stack.length-1,1) 
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length-1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    let min = this.stack[0]
    for (let i = 1; i < this.stack.length; i++) {
        if (this.stack[i] < min) {
            min = this.stack[i];
        }
    }
    return min;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */