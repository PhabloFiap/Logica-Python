import hospital
pacientes = []
opcao=0

while opcao !=4:
    print ("1 - cadasta paciente")
    print ("2 - consulta paciente")
    print ("3 - atende paciente")
    print ("4 - sair")
    opcao = int (input("informe uma opção: "))

    if opcao ==1:
        hospital.cadastra_paciente (pacientes)

    elif opcao ==2:
        status = int(input("Informe o status: "))
        hospital.consulta_paciente(status, pacientes)
    elif opcao ==3:
        pos = hospital.recupera_paciente (pacientes)
        print("Nome: ", pacientes[pos])
        print("Pressão: ", pacientes[pos+4])
        print("Temperatura: ", pacientes[pos+5])
        novo_status = int(input("Resultado atendimento:"))
        pacientes[pos+6] = novo_status

print("Sistema finalizado!")

