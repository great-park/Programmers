import java.util.*;

class Solution {
    
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        int answer = 0;
        
        int[][] visited = new int[maps.length][maps[0].length];
        
        bfs(maps, visited);
        answer = visited[maps.length-1][maps[0].length-1];
        
        if(answer == 0){
            answer = -1;
        }
        
        return answer;
    }
    
    public void bfs(int[][] maps, int[][] visited){
        visited[0][0] = 1;
        Queue<int[]> q = new LinkedList<int[]>();
        q.offer(new int[]{0,0});
        
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            
            for(int i=0; i<4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (0 <= nx & nx < maps[0].length & 0 <= ny & ny < maps.length) {
                    if (visited[ny][nx] == 0 && maps[ny][nx] == 1){
                        q.offer(new int[]{nx,ny});
                        visited[ny][nx] = visited[y][x] + 1;
                    }
                }
                
            }
        }
    }
}