#!/usr/bin/env python3
import os
import glob

# Linguagens esperadas
LANGUAGES = {
    'c': '.c',
    'cpp': '.cpp', 
    'cs': '.cs',
    'clj': '.clj',
    'go': '.go',
    'java': '.java',
    'js': '.js',
    'kt': '.kt',
    'php': '.php',
    'py': '.py',
    'rb': '.rb',
    'rs': '.rs',
    'ts': '.ts'
}

# Algoritmos esperados baseados no README
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

def check_algorithm_completeness():
    base_dir = '/Users/vitorh/Documents/GIthub/algorithms'
    missing_implementations = {}
    
    for algorithm in ALGORITHMS:
        algorithm_dir = os.path.join(base_dir, algorithm)
        
        if not os.path.exists(algorithm_dir):
            print(f"❌ Diretório não encontrado: {algorithm}")
            continue
            
        missing_langs = []
        
        for lang, ext in LANGUAGES.items():
            # Procurar por arquivos com a extensão
            pattern = os.path.join(algorithm_dir, f"*{ext}")
            files = glob.glob(pattern)
            
            if not files:
                missing_langs.append(lang)
        
        if missing_langs:
            missing_implementations[algorithm] = missing_langs
        else:
            print(f"✅ {algorithm} - Completo")
    
    # Relatório de implementações faltantes
    if missing_implementations:
        print("\n🔍 IMPLEMENTAÇÕES FALTANTES:")
        print("=" * 50)
        
        total_missing = 0
        for algorithm, missing_langs in missing_implementations.items():
            print(f"\n📁 {algorithm}:")
            for lang in missing_langs:
                print(f"   ❌ {lang} ({LANGUAGES[lang]})")
                total_missing += 1
        
        print(f"\n📊 RESUMO:")
        print(f"Total de algoritmos: {len(ALGORITHMS)}")
        print(f"Algoritmos completos: {len(ALGORITHMS) - len(missing_implementations)}")
        print(f"Algoritmos incompletos: {len(missing_implementations)}")
        print(f"Total de implementações faltantes: {total_missing}")
        print(f"Total esperado: {len(ALGORITHMS) * len(LANGUAGES)} implementações")
        print(f"Completude: {((len(ALGORITHMS) * len(LANGUAGES) - total_missing) / (len(ALGORITHMS) * len(LANGUAGES))) * 100:.1f}%")
    else:
        print("\n🎉 TODOS OS ALGORITMOS ESTÃO COMPLETOS!")

if __name__ == "__main__":
    check_algorithm_completeness()
