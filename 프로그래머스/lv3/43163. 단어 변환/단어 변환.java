import java.util.LinkedList;
import java.util.Queue;
class Solution {
    
    class Item{
        String str;
        int move;
        Item(String str, int move){
            this.str = str;
            this.move = move;
        }
    }
    
    boolean isDiffer(String start, String dest) {
        int differCount = 0;

        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) == dest.charAt(i)) continue;
            differCount++;
        }

        return differCount == 1; 
    }
    
    public int solution(String begin, String target, String[] words) {
        boolean[] visited = new boolean[words.length];
        Queue<Item> q = new LinkedList<>();    
        q.add(new Item(begin, 0));
        
        while(!q.isEmpty()){
            Item item = q.poll();
            if(item.str.equals(target))
                return item.move;
            
            for(int i = 0; i < words.length; i++){
                if(isDiffer(item.str, words[i]) && !visited[i]){
                    visited[i] = true;
                    q.add(new Item(words[i], item.move + 1));
                }
            }
        }
        
        return 0;
    }
}
