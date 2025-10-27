#!/usr/bin/env python3
import os
import glob

LANGUAGES = {
    'c': '.c', 'cpp': '.cpp', 'cs': '.cs', 'clj': '.clj',
    'go': '.go', 'java': '.java', 'js': '.js', 'kt': '.kt',
    'php': '.php', 'py': '.py', 'rb': '.rb', 'rs': '.rs', 'ts': '.ts'
}

ALGORITHMS = [
    'binary-search', 'linear-search', 'two_pointers',
    'bubble-sort', 'merge-sort', 'quick-sort', 'heap-sort',
    'linear-regression', 'logistic-regression', 'decision-trees', 
    'random-forest', 'support-vector-machines', 'k-means-clustering',
    'k-nearest-neighbors', 'gradient-boosting',
    'depth-first-search', 'breadth-first-search', 'dijkstra-algorithm',
    'topological-sort', 'hash-table', 'binary-search-tree', 'linked-list',
    'trie', 'dynamic-programming', 'knapsack-problem', 'edit-distance',
    'longest-common-subsequence', 'coin-change', 'kmp-algorithm',
    'palindrome', 'fibonacci', 'euclidean-algorithm', 'sieve-of-eratosthenes',
    'matrix-multiplication'
]

def analyze_file(file_path):
    """Analisa um arquivo e determina seu status"""
    try:
        size = os.path.getsize(file_path)
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().strip()
        
        # Verifica se é placeholder
        placeholder_indicators = [
            'println("', 'console.log("', 'print("', 'printf("',
            'System.out.println("', 'puts "', 'echo "', 'fmt.Println("'
        ]
        
        is_placeholder = any(indicator in content for indicator in placeholder_indicators)
        
        if size < 100 and is_placeholder:
            return "PLACEHOLDER"
        elif size < 100:
            return "MUITO_PEQUENO"
        elif size > 500:
            return "IMPLEMENTADO"
        else:
            return "PARCIAL"
            
    except Exception:
        return "ERRO"

def generate_final_report():
    base_dir = '/Users/vitorh/Documents/GIthub/algorithms'
    
    print("📊 RELATÓRIO FINAL DE IMPLEMENTAÇÕES")
    print("=" * 80)
    
    total_expected = len(ALGORITHMS) * len(LANGUAGES)
    implemented = 0
    placeholders = 0
    partial = 0
    missing = 0
    
    problematic_algorithms = []
    
    for algorithm in ALGORITHMS:
        algorithm_dir = os.path.join(base_dir, algorithm)
        
        if not os.path.exists(algorithm_dir):
            print(f"❌ {algorithm} - Diretório não encontrado")
            missing += len(LANGUAGES)
            continue
        
        algo_status = {"implemented": 0, "placeholder": 0, "partial": 0, "missing": 0}
        
        for lang, ext in LANGUAGES.items():
            pattern = os.path.join(algorithm_dir, f"*{ext}")
            files = glob.glob(pattern)
            
            if files:
                status = analyze_file(files[0])
                if status == "IMPLEMENTADO":
                    algo_status["implemented"] += 1
                    implemented += 1
                elif status == "PLACEHOLDER":
                    algo_status["placeholder"] += 1
                    placeholders += 1
                else:
                    algo_status["partial"] += 1
                    partial += 1
            else:
                algo_status["missing"] += 1
                missing += 1
        
        # Status do algoritmo
        total_files = sum(algo_status.values())
        if algo_status["implemented"] == len(LANGUAGES):
            status_icon = "✅"
        elif algo_status["implemented"] > len(LANGUAGES) // 2:
            status_icon = "🟡"
            problematic_algorithms.append(algorithm)
        else:
            status_icon = "❌"
            problematic_algorithms.append(algorithm)
        
        print(f"{status_icon} {algorithm:<25} - Impl: {algo_status['implemented']:2d} | "
              f"Placeholder: {algo_status['placeholder']:2d} | "
              f"Parcial: {algo_status['partial']:2d} | "
              f"Faltando: {algo_status['missing']:2d}")
    
    print("\n" + "=" * 80)
    print("📈 ESTATÍSTICAS GERAIS:")
    print(f"Total esperado: {total_expected} implementações")
    print(f"Implementadas: {implemented} ({implemented/total_expected*100:.1f}%)")
    print(f"Placeholders: {placeholders} ({placeholders/total_expected*100:.1f}%)")
    print(f"Parciais: {partial} ({partial/total_expected*100:.1f}%)")
    print(f"Faltando: {missing} ({missing/total_expected*100:.1f}%)")
    
    completion_rate = implemented / total_expected * 100
    print(f"\n🎯 TAXA DE COMPLETUDE REAL: {completion_rate:.1f}%")
    
    if problematic_algorithms:
        print(f"\n⚠️  ALGORITMOS QUE PRECISAM DE ATENÇÃO ({len(problematic_algorithms)}):")
        for algo in problematic_algorithms:
            print(f"   • {algo}")

if __name__ == "__main__":
    generate_final_report()
