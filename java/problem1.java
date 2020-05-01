public class problem1 {
    public static void main(String[] args) {
        final long startTime = System.currentTimeMillis();

        int nr = 1000;
        nr--;
        int x3 = nr/3;
        int x5 = nr/5;
        int x15 = nr/15;

        long sum1 = 3*x3*(x3+1); 
        long sum2 = 5*x5*(x5+1);
        long sum3 = 15*x15*(x15+1);

        long sum = (sum1+sum2-sum3)/2;
        System.out.println(sum);

        final long endTime = System.currentTimeMillis();

        System.out.println("Total execution time: " + (endTime - startTime));
    }
}