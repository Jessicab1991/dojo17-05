def Menu():

    menu = 1
    while menu !=0:

        var = int(input("digite \n 1 para acessar o sistema\n 2 para leitura\n 3 para ler uma pessoa\n 4 para deletar\n>> "))
        
        match var:

            case 1:
                print("create")

            case 2:
                print("read")

            case 3:
                print("update")

            case 4:
                print("delete")
                        
        menu = int(input(" digite 1 para continuar \n digite 0 paea encerrar "))


Menu()