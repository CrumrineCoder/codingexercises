/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const filteredArray = nums.filter((num) => num <= target);
    for (let i = 0; i < filteredArray.length; i++) {
        if (filteredArray[i] + filteredArray[filteredArray.length - (i + 1)] === target) {
            return [i, filteredArray.length - (i + 1)];
        } else {
            filteredArray.pop();
            filteredArray.shift();
        }
    }
};

twoSum([2,7,11,15], 9);