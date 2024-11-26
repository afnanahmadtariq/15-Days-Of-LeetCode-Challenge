class Solution {
    public String reverse(String s){
        String reverse = "";
        for(int i=0; i<s.length(); i++){
            reverse += s.substring(s.length() - i - 1, s.length() - i);
        }
        return reverse;
    }
    public String reverseStr(String s, int k) {
        double times = s.length()/(double)(2*k);
        System.out.println(times);
        for(int i=0; i<times; i++){
            int dist = (i * 2 * k) ;
            s = s.substring(0,dist) + reverse(s.substring(dist,dist+k<s.length()? dist+k: s.length())) + s.substring(dist+k<s.length()? dist+k: s.length());
        }
    return s;
    }

}