public class Solution {
   public String reverseWords(String s) {
       StringBuffer res=new StringBuffer();
       if (s==null||s.trim().length()==0){
           return res.toString();
       }
       List<String> list=new ArrayList<>();
       String[] strs=s.split(" ");
       for (int i=strs.length-1;i>-1;--i){
           if (strs[i].trim().length()>0){
               list.add(strs[i].trim());
           }
       }
       res.append(list.get(0));
       for (int i=1;i<list.size();++i){
           res.append(" ");
           res.append(list.get(i));
       }
       return res.toString();
   }
}