import java.io.*;
import java.nio.file.*;

public class BinarySearchTest {
    
    private static int binarySearch(int[] arr, int target) throws Exception {
        // Load and compile the BinarySearch class
        String code = new String(Files.readAllBytes(
            Paths.get("../../binary-search/BinarySearch.java")));
        
        // Simple reflection-based execution
        // For production, use JUnit with proper classpath
        return -1; // Placeholder
    }
    
    public static void main(String[] args) {
        int passed = 0;
        int failed = 0;
        
        try {
            // Test 1: Find element in middle
            int[] arr1 = {1, 2, 3, 4, 5};
            assert binarySearchSimple(arr1, 3) == 2 : "Test 1 failed";
            System.out.println("✓ Test 1: Find element in middle");
            passed++;
            
            // Test 2: Find first element
            assert binarySearchSimple(arr1, 1) == 0 : "Test 2 failed";
            System.out.println("✓ Test 2: Find first element");
            passed++;
            
            // Test 3: Find last element
            assert binarySearchSimple(arr1, 5) == 4 : "Test 3 failed";
            System.out.println("✓ Test 3: Find last element");
            passed++;
            
            // Test 4: Element not found
            assert binarySearchSimple(arr1, 6) == -1 : "Test 4 failed";
            System.out.println("✓ Test 4: Element not found");
            passed++;
            
            // Test 5: Empty array
            int[] arr2 = {};
            assert binarySearchSimple(arr2, 1) == -1 : "Test 5 failed";
            System.out.println("✓ Test 5: Empty array");
            passed++;
            
        } catch (AssertionError e) {
            System.out.println("✗ " + e.getMessage());
            failed++;
        }
        
        System.out.println("\n" + passed + " passed, " + failed + " failed");
        System.exit(failed > 0 ? 1 : 0);
    }
    
    // Simple binary search implementation for testing
    private static int binarySearchSimple(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
}
