valorProduto = float(input())
condicaoPagamento = str(input("Qual a condição de pagamento :"))
condicaoLower = condicaoPagamento.lower()

if condicaoPagamento == 'á vista':
    print(f'Valor do Pro duto: R$ {valorProduto - (valorProduto * 0.1)}')

elif condicaoPagamento == '1x':
    print(f'VAlor do Produto 1x cédito: R$ {valorProduto - (valorProduto * 0.05)}')

elif condicaoPagamento == '2x':
    print(f'VAlor do Produto 2x cédito: R$ {valorProduto}')

elif condicaoPagamento == '3x':
    print(f'VAlor do Produto 3x cédito: R$ {valorProduto + (valorProduto * 0.2)}')
