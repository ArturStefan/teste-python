from bis import anobissexto

while True:
    ano = int(input("Digite o ano desejado ou digite 0 pra sair: "))
    if ano == 0:
        print("\nAdeus")
        break
    else:
       print('{} {}\n'.format(ano,anobissexto(ano)))