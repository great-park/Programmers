import java.util.*;

class Solution {
    ArrayList<String> allRoute;
    boolean[] visited;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        visited = new boolean[tickets.length];
        allRoute = new ArrayList<>();
        
        dfs("ICN", "ICN", tickets, 0);
        
        Collections.sort(allRoute);
        
        return allRoute.get(0).split(",");
    }
    
    public void dfs(String start, String route, String[][] tickets, int cnt) {
        if(cnt == tickets.length) {
            allRoute.add(route);
            // System.out.println(route);
            return;
        }
        
        for(int i=0; i<tickets.length; i++) {
            if(start.equals(tickets[i][0]) && !visited[i]) {
                visited[i] = true;
                dfs(tickets[i][1], route+","+tickets[i][1], tickets, cnt + 1);
                visited[i] = false;
            }
        }
    }
}

