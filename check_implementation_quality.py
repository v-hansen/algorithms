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

def is_placeholder_or_empty(file_path, file_size):
    """Verifica se um arquivo é um placeholder ou está vazio"""
    if file_size < 50:  # Arquivos muito pequenos são suspeitos
        return True
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().strip()
            
        # Verifica se é muito pequeno ou contém apenas comentários básicos
        if len(content) < 50:
            return True
            
        # Verifica padrões de placeholder
        placeholder_patterns = [
            "// TODO", "# TODO", "/* TODO", 
            "// Implementation needed", "# Implementation needed",
            "// Placeholder", "# Placeholder",
            "console.log('TODO')", "print('TODO')",
            "println!(\"TODO\")", "System.out.println(\"TODO\")"
        ]
        
        for pattern in placeholder_patterns:
            if pattern in content:
                return True
                
        return False
        
    except Exception:
        return True

def check_implementation_quality():
    base_dir = '/Users/vitorh/Documents/GIthub/algorithms'
    issues = {}
    
    for algorithm in ALGORITHMS:
        algorithm_dir = os.path.join(base_dir, algorithm)
        
        if not os.path.exists(algorithm_dir):
            continue
            
        algorithm_issues = []
        
        for lang, ext in LANGUAGES.items():
            pattern = os.path.join(algorithm_dir, f"*{ext}")
            files = glob.glob(pattern)
            
            if files:
                file_path = files[0]  # Pega o primeiro arquivo encontrado
                file_size = os.path.getsize(file_path)
                
                if is_placeholder_or_empty(file_path, file_size):
                    algorithm_issues.append({
                        'lang': lang,
                        'file': os.path.basename(file_path),
                        'size': file_size,
                        'issue': 'placeholder_or_empty'
                    })
        
        if algorithm_issues:
            issues[algorithm] = algorithm_issues
    
    # Relatório
    if issues:
        print("🔍 ARQUIVOS COM POSSÍVEIS PROBLEMAS:")
        print("=" * 60)
        
        total_issues = 0
        for algorithm, algorithm_issues in issues.items():
            print(f"\n📁 {algorithm}:")
            for issue in algorithm_issues:
                print(f"   ⚠️  {issue['lang']} - {issue['file']} ({issue['size']} bytes)")
                total_issues += 1
        
        print(f"\n📊 RESUMO:")
        print(f"Algoritmos com problemas: {len(issues)}")
        print(f"Total de arquivos problemáticos: {total_issues}")
    else:
        print("✅ Todas as implementações parecem estar completas!")

if __name__ == "__main__":
    check_implementation_quality()
