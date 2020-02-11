class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int max = 0;
        int step = 1;
        if (nums.length == 0){
            return 0;
        }
        for(int i=0; i< nums.length - 1; i++){
            if(nums[i+1] > nums[i]){
                step++;
            }else{
                if(max < step)
                    max = step;
                step = 1;
            }
        }
        if(max< step)
            max = step;
        return max;
    }
}

