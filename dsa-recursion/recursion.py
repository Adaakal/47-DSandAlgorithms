#product: calculate the product of an array of numbers. */

def product(nums): return nums[0] * product(nums[1:]) if nums else 1;

#longest: return the length of the longest word in an array of words. */

def longest(words): return len(words[0]) if len(words[0]) > longest(words[1:]) else longes(words[1:]) if words else 0;
# */

/** everyOther: return a string with every other letter. */

function everyOther(str) {

}

/** isPalindrome: checks whether a string is a palindrome or not. */

function isPalindrome(str) {

}

/** findIndex: return the index of val in arr (or -1 if val is not present). */

function findIndex(arr, val) {

}

/** revString: return a copy of a string, but in reverse. */

function revString(str) {

}

/** gatherStrings: given an object, return an array of all of the string values. */

function gatherStrings(obj) {

}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */

function binarySearch(arr, val) {

}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};
