"""Macunaíma — intervenções no texto de 1928 (RASCUNHO: ver FALTA.md e CONVENCOES.md).

Regra da obra: a grafia de Mário é parte da obra (si, pra/prá, guspir, mãi?, milhor, siquer, os
pronomes no começo da frase, as formas da fala). Só se corrige erro tipográfico conferido no
fac-símile; nada de «normalizar» o que é escolha do autor.
"""
EMENDAS = []      # (tipo, capítulo, leitura de 1928, correção): tipo 'erro' | 'ocr' | 'revisao'
AJUSTES = []
MANUAL = {        # grafia de 1928 -> de hoje, só ortografia de época (CONVENCOES.md)
    'á': 'à', 'ás': 'às',          # a crase de 1928 leva agudo («ás ordens»)
}
