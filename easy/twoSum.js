// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//     Example:
// Given nums = [2, 7, 11, 15], target = 9,

//     Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

var twoSum = function (nums, target) {
    //     loop over each index
    // for each index, loop over the list again and add element from list a and elemetn from list b
    //stop once you have your answer
    //since we assume each input has one solution, we can't put empty array in there

    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            sum = nums[i] + nums[j]
            if (sum === target) {
                return [i, j]
            }

        }

    }


};