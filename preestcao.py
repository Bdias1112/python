print("Informe a quantidade de parcelas: ")
num_prest = int(input())

print("Informe o valor das parcelas: ")
valor_prest = float(input())

print("Quantas parcelas foram pagas: ")
prest_pagas = int(input())

valor_total = num_prest * valor_prest
total_pago = prest_pagas * valor_prest
saldo_dev = valor_total - total_pago


print(f"\nNumero de parcelas: {num_prest}")
print(f"\nValor das parcelas: {valor_prest}")
print(f"\nValor total do consórcio: {valor_total}")
print(f"\nNúmero e parcelas pagas: {prest_pagas}")
print(f"\nValor total pago: {total_pago}")
print(f"\nSaldo devedor: {saldo_dev}")