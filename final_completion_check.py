#!/usr/bin/env python3
import os
import glob

LANGUAGES = {
    'c': '.c', 'cpp': '.cpp', 'cs': '.cs', 'clj': '.clj',
    'go': '.go', 'java': '.java', 'js': '.js', 'kt': '.kt',
    'php': '.php', 'py': '.py', 'rb': '.rb', 'rs': '.rs', 'ts': '.ts'
}

def analyze_missing_implementations():
    """Analisa implementações faltantes ou muito pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms"
    
    missing_or_small = {}
    
    for root, dirs, files in os.walk(base_dir):
        if root == base_dir or '/.git' in root or '/visualizations' in root:
            continue
            
        algorithm = os.path.basename(root)
        missing_or_small[algorithm] = []
        
        for lang, ext in LANGUAGES.items():
            pattern = f"{root}/*{ext}"
            matching_files = glob.glob(pattern)
            
            if not matching_files:
                missing_or_small[algorithm].append(f"{lang} - MISSING")
            else:
                file_path = matching_files[0]
                size = os.path.getsize(file_path)
                if size < 100:  # Arquivos muito pequenos
                    missing_or_small[algorithm].append(f"{lang} - SMALL ({size}b)")
    
    # Filtrar apenas algoritmos com problemas
    problematic = {k: v for k, v in missing_or_small.items() if v}
    
    print("🔍 ANÁLISE DE IMPLEMENTAÇÕES FALTANTES/PEQUENAS:")
    print("=" * 60)
    
    for algorithm, issues in sorted(problematic.items()):
        print(f"\n📁 {algorithm}:")
        for issue in issues:
            print(f"   ❌ {issue}")
    
    total_issues = sum(len(issues) for issues in problematic.values())
    print(f"\n📊 RESUMO:")
    print(f"Algoritmos com problemas: {len(problematic)}")
    print(f"Total de implementações problemáticas: {total_issues}")
    
    return problematic

if __name__ == "__main__":
    analyze_missing_implementations()
