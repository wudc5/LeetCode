class Solution {
    public String simplifyPath(String path) {
        Stack<String> stk = new Stack();
        String [] fields = path.split("/");
        for (String fld: fields){
            if(fld.equals("..") && !stk.empty())
                stk.pop();
            else if(!fld.equals(".") && !fld.equals("") && !fld.equals(".."))
                stk.push(fld);
        }
        List<String> lst =  new ArrayList<String>(stk);
        String result = "/" + String.join("/", lst);
        return result;
    }
}