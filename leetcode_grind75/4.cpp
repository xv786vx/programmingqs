# 4. Median of Two Sorted Arrays
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> merged(nums1.size() + nums2.size());
        int leftIndex = 0, rightIndex = 0, mergeIndex = 0;
        while (leftIndex < nums1.size() && rightIndex < nums2.size()) {
            if (nums1[leftIndex] < nums2[rightIndex]) {
                merged[mergeIndex] = nums1[leftIndex];
                leftIndex++, mergeIndex++;
            } else {
                merged[mergeIndex] = nums2[rightIndex];
                rightIndex++, mergeIndex++;
            }
        }

        while (leftIndex < nums1.size()) {
            merged[mergeIndex] = nums1[leftIndex];
            leftIndex++, mergeIndex++;
        }

        while (rightIndex < nums2.size()) {
            merged[mergeIndex] = nums2[rightIndex];
            rightIndex++, mergeIndex++;
        }

        double median;
        if (merged.size() % 2 == 0) {
            median = (merged[(merged.size()/2)-1] + merged[merged.size()/2]) / 2.0;
        } else {
            median = merged[merged.size()/2]; 
        }

        return median;
    }
};