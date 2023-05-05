class Solution {
    public int solution(int[] numbers, int target) {
        int answer = backTrack(numbers, target, 0);
        return answer;
    }
    
    public int backTrack(int[] numbers, int target, int depth) {
        if (depth == numbers.length) {
            int sum = 0;
            for (int n : numbers) {
                sum += n;
            }
            
            return sum == target ? 1 : 0;
        }
        
        int result = 0;
        
        result += backTrack(numbers, target, depth+1);
        numbers[depth] *= -1;
        
        result += backTrack(numbers, target, depth+1);
        numbers[depth] *= -1;
        
        return result;
    }
    
}