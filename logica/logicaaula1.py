# 1. IMPOSTO ISS = 0.1
# 2. IMPOSTO DE RENDA = 0.2
# 3. CSLL = 0.05
# 4. FATURAMENTO = 5000
# 5. LUCRO = 1000


iss = 0.1
ir = 0.2
csll = 0.05
faturamento = 5000
lucro = 1000

imposto_faturamento = iss * faturamento
print(imposto_faturamento)
lucro_csll_ir = faturamento + csll * ir
print (lucro_csll_ir)

media = faturamento + lucro

