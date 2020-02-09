class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int num, max=0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length;j++){
               if(grid[i][j] == 1){
                   num = dfs(grid,i,j);
                   max = Math.max(max,num);
               }
            }
        }
        return max;
    }
    public int dfs(int[][] grid, int i, int j){
        if(i>=0&&i<grid.length&&j>=0&&j<grid[0].length&&grid[i][j] == 1){
            grid[i][j] = 0;
            int tmp = 1 + dfs(grid,i-1,j) + dfs(grid, i+1,j)+dfs(grid,i,j-1)+dfs(grid,i,j+1);
            return tmp;
        }else{
            return 0;
        }
    }
}