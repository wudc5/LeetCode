class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if(envelopes.length<=1)
            return envelopes.length;
        int[] temp;
        //排序：先排宽度，从小到大；对于相同的宽度，高度从大到小。
        for(int i = 0;i<envelopes.length;i++){
            for(int j = i+1;j<envelopes.length;j++){
                if(envelopes[i][0]>envelopes[j][0] || (envelopes[i][0]==envelopes[j][0] && envelopes[i][1]<envelopes[j][1])){
                    temp = envelopes[i];
                    envelopes[i] = envelopes[j];
                    envelopes[j] = temp;
                }
            }
        }
        //对于排序完之后的高度h，求最长上升子序列
        int res = 0;
        int[] dp = new int[envelopes.length];
        for(int i = 0;i<envelopes.length;i++){
            dp[i] = 1;
            for(int j = 0;j<i;j++){
                if(envelopes[i][1] > envelopes[j][1]){
                    dp[i] = Math.max(dp[i],dp[j]+1);
                }
            }
        }
        //返回dp中的最大值即可
        for(int i:dp){
            if(res<i) res=i;
        }
        return res;
    }

}
