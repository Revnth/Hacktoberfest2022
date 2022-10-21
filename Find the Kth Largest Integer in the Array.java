//Problem Link: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

//Solution:

class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        Arrays.sort(nums, (String s1, String s2) -> {
            if (s1.length() == s2.length()) {
                return s2.compareTo(s1);
            }
            return s2.length() - s1.length();
        });
        return nums[k - 1];
    }
}
