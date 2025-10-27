public class EuclideanAlgorithm {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    public static int gcdRecursive(int a, int b) {
        return b == 0 ? a : gcdRecursive(b, a % b);
    }
    
    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
    
    public static int[] extendedGcd(int a, int b) {
        if (b == 0) {
            return new int[]{a, 1, 0};
        }
        int[] result = extendedGcd(b, a % b);
        int gcd = result[0];
        int x1 = result[1];
        int y1 = result[2];
        
        int x = y1;
        int y = x1 - (a / b) * y1;
        
        return new int[]{gcd, x, y};
    }
    
    public static void main(String[] args) {
        System.out.println("GCD: " + gcd(48, 18));
        System.out.println("GCD recursive: " + gcdRecursive(48, 18));
        System.out.println("LCM: " + lcm(48, 18));
        
        int[] result = extendedGcd(48, 18);
        System.out.printf("Extended GCD: gcd=%d, x=%d, y=%d%n", result[0], result[1], result[2]);
    }
}