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
        if (b == 0) return a;
        return gcdRecursive(b, a % b);
    }
    
    public static int lcm(int a, int b) {
        return Math.abs(a * b) / gcd(a, b);
    }
    
    public static int[] extendedGcd(int a, int b) {
        if (a == 0) {
            return new int[]{b, 0, 1};
        }
        
        int[] result = extendedGcd(b % a, a);
        int gcdVal = result[0];
        int x1 = result[1];
        int y1 = result[2];
        
        int x = y1 - (b / a) * x1;
        int y = x1;
        
        return new int[]{gcdVal, x, y};
    }
    
    public static void main(String[] args) {
        System.out.println("GCD(48, 18) = " + gcd(48, 18)); // 6
        System.out.println("LCM(48, 18) = " + lcm(48, 18)); // 144
    }
}
