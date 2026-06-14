from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
corridors = pd.read_csv(root / 'datos' / 'tnep_corredores.csv')
cand = corridors[corridors['tipo'].str.lower() == 'candidato'].copy()
print('Corredores candidatos:')
print(cand[['line','from','to','fmax_mw','invcost_musd','maxnew']].to_string(index=False))
print('\nCosto total si se construyen todos los candidatos [MUSD]:', cand['invcost_musd'].sum())
