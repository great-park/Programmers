import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
 
 
public class Main {	
	public static void main(String[] args) {
    
		Scanner in = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();

        int N = in.nextInt();

        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=0;i<N;i++){
            arr.add(in.nextInt());
        }

        Collections.sort(arr);

        for (int i=0;i<N;i++){
            sb.append(arr.get(i)).append('\n');
        }
        System.out.println(sb);
	}
}