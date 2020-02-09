class Solution {
    public int[] twoSum(int[] nums, int target) {
         Map<Integer, Integer> tmpMap = new HashMap();
        int[] index = new int[2];
        for(int i = 0; i< nums.length; i++){
            int diff = target - nums[i];
            if (tmpMap.containsKey(nums[i])){
                index[0] = tmpMap.get(nums[i]);
                index[1] = i;
                break;
            }else
                tmpMap.put(diff, i);
        }
        return index;
    }
}