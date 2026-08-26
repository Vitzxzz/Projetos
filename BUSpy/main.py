##Sistema para conferir e atualizar a situação dos ônibus dentro da garagem.
from operator import truediv

frota = ["GL315", "GL330", "GL344"]
status = ["Disponível", "Em manutenção", "Em uso"]

while True:
    print("SISTEMA DE GARAGEM v1.0 ALFA")
    print("Bem vindo!")
    try:
        ident = int(input("\n" "Quem você é? (1) Motorista (2) Administrador (3) Cancelar\n"))
    except:
        ident = 11023012031023
    if ident == 1 :
          cod_vei = input("Digite o código do veículo\n")
          if cod_vei in frota :
              posicao = frota.index(cod_vei)
              situação = status[posicao]
              print ("\n" f"O veículo {cod_vei} está: {situação}")
              print ("\n" "Obrigado por usar nosso sistema.")
              print("\n" + "="*30 + "\n")
          else:
                print("Veículo não cadastrado.")
    elif ident == 2 :
          cod_adm = input("Digite a senha")
    elif ident == 3 :
        print ("Obrigado por usar nosso sistema.")
        break
    else:
          print ("Número inválido")
          break

