import pandas as pd
from fpdf import FPDF
from datetime import datetime

df = pd.read_excel('vendas.xlsx')

df['Total'] = df['Quantidade'] * df['Valor_Unitario']

resumo = df.groupby('Produto').agg(
    Quantidade_Total=('Quantidade', 'sum'),
    Faturamento=('Total', 'sum')
).reset_index()

resumo.to_excel('relatorio.xlsx', index=False)
print("Relatório Excel gerado com sucesso!")

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Relatório de Vendas', ln=True, align='C')
        self.ln(5)

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

pdf.cell(0, 10, f"Data de geração: {datetime.now().strftime('%d/%m/%Y')}", ln=True)
pdf.ln(10)

for i, row in resumo.iterrows():
    pdf.cell(60, 10, row['Produto'], 1)
    pdf.cell(40, 10, str(row['Quantidade_Total']), 1)
    pdf.cell(60, 10, f"R$ {row['Faturamento']:.2f}", 1, ln=True)

pdf.output('relatorio.pdf')
print("Relatório PDF gerado com sucesso!")
