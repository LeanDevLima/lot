
import json
from typing import List, Tuple, Dict

ARQUIVO_JSON = "sequencias.json"

PERCENTUAIS_REGULAR = {"sena": 0.40, "quina": 0.13, "quadra": 0.15}
PERCENTUAIS_VIRADA  = {"sena": 0.90, "quina": 0.05, "quadra": 0.05}

PREMIO_BRUTO_SOBRE_ARRECADACAO = 0.4379  # ~43,79%

def carregar_sequencias(caminho: str) -> List[List[int]]:
    """Carrega e valida as sequências do JSON (20 x 6 números inteiros, únicos e 1..60)."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{caminho}' não encontrado.")
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON inválido em '{caminho}': {e}")

    if not isinstance(data, list):
        raise ValueError("Estrutura esperada: lista de sequências.")

    seqs: List[List[int]] = []
    for idx, seq in enumerate(data, start=1):
        if not isinstance(seq, list):
            raise ValueError(f"Sequência {idx} não é uma lista.")
        if len(seq) != 6:
            raise ValueError(f"Sequência {idx} deve ter 6 números; tem {len(seq)}.")
        try:
            seq_int = [int(x) for x in seq]
        except (TypeError, ValueError):
            raise ValueError(f"Sequência {idx} contém valor não numérico: {seq}")
        if len(set(seq_int)) != 6:
            raise ValueError(f"Sequência {idx} possui números repetidos: {seq_int}")
        for n in seq_int:
            if not (1 <= n <= 60):
                raise ValueError(f"Sequência {idx} contém número fora de 1..60: {n}")
        seqs.append(seq_int)

    if len(seqs) != 20:
        raise ValueError(f"Esperadas 20 sequências; arquivo contém {len(seqs)}.")
    return seqs

def ler_dezenas_sorteadas() -> List[int]:
    """Lê 6 dezenas do sorteio (01..60), sem repetição."""
    while True:
        linha = input("Dezenas sorteadas (6 números entre 1 e 60, separados por espaço): ").strip()
        try:
            nums = [int(x) for x in linha.split()]
        except ValueError:
            print("Use apenas números inteiros, separados por espaço.")
            continue
        if len(nums) != 6:
            print("É necessário informar exatamente 6 números.")
            continue
        if len(set(nums)) != 6:
            print("Não são permitidos números repetidos.")
            continue
        if any(n < 1 or n > 60 for n in nums):
            print("Todos os números devem estar no intervalo 1..60.")
            continue
        return nums

def calcular_acertos(sequencias: List[List[int]], dezenas: List[int]) -> Dict[int, List[Tuple[int, List[int]]]]:
    """Retorna {4: [...], 5: [...], 6: [...]}, com (indice_seq 1-base, dezenas_acertadas)."""
    resultado: Dict[int, List[Tuple[int, List[int]]]] = {4: [], 5: [], 6: []}
    s = set(dezenas)
    for i, seq in enumerate(sequencias, start=1):
        inter = sorted(s.intersection(seq))
        k = len(inter)
        if k in (4, 5, 6):
            resultado[k].append((i, inter))
    return resultado

def imprimir_resultado(resultado: Dict[int, List[Tuple[int, List[int]]]]) -> None:
    """Mostra quais sequências têm Quadra/Quina/Sena."""
    if not any(resultado.values()):
        print("Nenhuma sequência fez Quadra (4), Quina (5) ou Sena (6).")
        return

    if resultado[6]:
        print("\n🏆 Sena (6 acertos):")
        for idx, dezenas in resultado[6]:
            print(f" - Seq {idx}: {dezenas}")

    if resultado[5]:
        print("\n🥈 Quina (5 acertos):")
        for idx, dezenas in resultado[5]:
            print(f" - Seq {idx}: {dezenas}")

    if resultado[4]:
        print("\n🥉 Quadra (4 acertos):")
        for idx, dezenas in resultado[4]:
            print(f" - Seq {idx}: {dezenas}")

def main():
    print("=== Conferidor de Mega-Sena (sequencias.json) ===")
    sequencias = carregar_sequencias(ARQUIVO_JSON)
    dezenas_sorteadas = ler_dezenas_sorteadas()


    resultado = calcular_acertos(sequencias, dezenas_sorteadas)
    imprimir_resultado(resultado)

if __name__ == "__main__":
    main()
