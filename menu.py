from controller import saudacao, create, relatorioHospedes



def Menu():

    menu = 1
    while menu !=0:
        saudacao()

        var = int(input("digite \n 1 para acessar o sistema\n 2 para leitura\n 3 para ler uma pessoa\n 4 para deletar\n>> "))
        
        match var:

            case 1:
                pessoa = {}
                pessoa["nome"] = input("digite seu nome")
                pessoa["sobrenome"] = input("digite seu sobrenome")
                pessoa["idade"] = int(input("digite sua idade"))
                pessoa["telefone"] = int(input("digite seu telefone"))


                create(pessoa)

            case 2:
                relatorioHospedes()

            case 3:
                print("update")

            case 4:
                print("delete")
                        
        menu = int(input(" digite 1 para continuar \n digite 0 paea encerrar "))


Menu()