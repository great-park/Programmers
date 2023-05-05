import java.util.*;

class Solution {
    int depth = 0;
    int[] visit;
    ArrayList<Integer>[] adj;
    
    public int solution(int n, int[][] edge) {
        int answer = 0;
        visit = new int[n+1];
        adj = new ArrayList[n+1];
        for(int i=1; i<=n; i++) adj[i] = new ArrayList<>();
        
        for(int i=0; i<edge.length; i++) {
            adj[edge[i][0]].add(edge[i][1]);
            adj[edge[i][1]].add(edge[i][0]);
        }
        
        bfs(1,1);
        
        for(int i=2; i<=n; i++){
            System.out.println(visit[i]);
            if(depth == visit[i]) answer++;
        }
        
        return answer;
    }
    
    public void bfs(int start, int cnt) {
        Queue<Integer> q = new LinkedList();
        q.offer(start);
        q.offer(cnt);
        
        while(!q.isEmpty()) {
            int cur_node = q.poll();
            int cur_cnt = q.poll();
            
            if(depth < cur_cnt) depth = cur_cnt;
            for(int i=0; i<adj[cur_node].size(); i++) {
                int next_node = adj[cur_node].get(i);
                
                if(visit[next_node] == 0) {
                    visit[next_node] = cur_cnt + 1;
                    q.offer(next_node);
                    q.offer(cur_cnt+1);
                }
            }
        }
    }
}