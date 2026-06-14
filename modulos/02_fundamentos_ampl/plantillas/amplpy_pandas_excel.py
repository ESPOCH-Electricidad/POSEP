from pathlib import Path
import pandas as pd

excel_path = Path('../excel/pintura_ampl.xlsx')
products = pd.read_excel(excel_path, sheet_name='products')
params = pd.read_excel(excel_path, sheet_name='parameters')

with open('pintura_generado.dat', 'w', encoding='utf-8') as f:
    f.write('set P := ' + ' '.join(products['PRODUCT'].astype(str)) + ';

')
    for col in ['price', 'rate', 'market']:
        f.write(f'param {col} :=
')
        for _, row in products.iterrows():
            f.write(f"{row['PRODUCT']} {row[col]}
")
        f.write(';

')
    hours = params.loc[params['parameter'] == 'Hours', 'value'].iloc[0]
    f.write(f'param Hours := {hours};
')
