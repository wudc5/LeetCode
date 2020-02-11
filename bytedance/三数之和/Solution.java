class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result=new ArrayList<List<Integer>>();
        int i,j,k,reserve;
        for(i = 0; i<nums.length-2; i++){
            reserve = -nums[i];
            j = i+1;
            k = nums.length-1;
            while(j<k){
                if(nums[j] + nums[k] == reserve){
                    List<Integer> tmp=new ArrayList<Integer>();
                    tmp.add(nums[i]);
                    tmp.add(nums[j]);
                    tmp.add(nums[k]);
                    result.add(tmp);
                    j++;
                    while(j<k && nums[j-1] == nums[j]){
                        j++;
                    }
                    k--;
                }else if(nums[j] + nums[k] < reserve){
                    j++;
                    while(j<k && nums[j-1] == nums[j]){
                        j++;
                    }
                }else{
                    k--;
                    while(j<k-1 && nums[k] == nums[k+1]){
                        k--;
                    }
                }
            }
            while(i+1<nums.length-2 && nums[i]==nums[i+1]){
                i++;
            }
        }
        return result;
    }
}