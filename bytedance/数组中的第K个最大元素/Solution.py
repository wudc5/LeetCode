class Solution {
    public int parti(int[] nums, int low, int high){
        int i = low - 1;
        int j = low;
        while(j < high){
            if(nums[j] < nums[high])
                j++;
            else{
                i++;
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                // swap(nums[i], nums[j]);
                j++;
            }
        }
        i++;
        int tmp = nums[i];
        nums[i] = nums[high];
        nums[high] = tmp;
        // swap(nums[i], nums[high]);
        return i;
    }
    public void qsort(int[] nums, int low, int high){
        if(low < high){
            int index = parti(nums, low, high);
            qsort(nums, low, index-1);
            qsort(nums, index+1, high);
        }
    }
    public int findKthLargest(int[] nums, int k) {
        int low = 0;
        int high = nums.length-1;
        qsort(nums, low, high);
        return nums[k-1];
    }
}