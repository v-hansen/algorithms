#!/bin/bash
cd "$(dirname "$0")"

TESTS=(
    "BinarySearchTest"
    "BubbleSortTest"
    "QuickSortTest"
    "MergeSortTest"
    "HeapSortTest"
    "LinearSearchTest"
    "HashTableTest"
    "BSTTest"
    "LinkedListTest"
    "TrieTest"
    "DFSTest"
    "BFSTest"
    "FibonacciTest"
    "PalindromeTest"
    "EuclideanTest"
    "SieveTest"
    "MatrixMultTest"
    "KnapsackTest"
    "CoinChangeTest"
    "EditDistanceTest"
    "LCSTest"
    "KMPTest"
    "TwoPointersTest"
    "DynamicProgrammingTest"
    "TopologicalSortTest"
    "DijkstraTest"
    "DecisionTreeTest"
    "LinearRegressionTest"
    "LogisticRegressionTest"
    "RandomForestTest"
    "GradientBoostingTest"
    "KMeansTest"
    "KNNTest"
    "SVMTest"
)

PASSED=0
FAILED=0

for test in "${TESTS[@]}"; do
    echo "Running $test..."
    javac -cp ../../*/ "$test.java" 2>/dev/null
    if java -ea -cp ../../*/:. "$test" 2>/dev/null; then
        ((PASSED++))
    else
        echo "  FAILED: $test"
        ((FAILED++))
    fi
done

echo ""
echo "========================"
echo "Tests passed: $PASSED"
echo "Tests failed: $FAILED"
echo "========================"
