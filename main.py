#pode aceitar quantos 'a' tiver, depois dois 'b' e 1. terminar ou 2. pegar um 'c' e pegar um 'b'

while(True):
    print("-------------------")
    entrada = input("Entrada: ")
    quantidade_caracteres = len(entrada)
    condicao_0 = False 
    condicao_1 = False
    condicao_2 = False
    condicao_3 = False
    ocorrencias_1 = 0

    for i in range(quantidade_caracteres):
        if(entrada[i] == 'b' and condicao_0 == True and condicao_1 == True and condicao_2 == True and ocorrencias_1 == 2): # 3
            print("3")
            if(i == (quantidade_caracteres-1)):
                print("Aceita#3")
            condicao_2 = False

        elif(entrada[i] == 'c' and condicao_0 == True and condicao_1 == True and condicao_2 == False and ocorrencias_1 == 2): # 2
            print("2")
            if(i == (quantidade_caracteres-1)):
                print("Rejeita#2")
            condicao_2 = True

        elif(entrada[i] == 'b' and condicao_0 == True and condicao_1 == False): # 1
            print("1")
            
            ocorrencias_1 += 1
            
            if ocorrencias_1 == 2:
                condicao_1 = True

            if(i == (quantidade_caracteres-1) and condicao_1 == False):
                print("Rejeita#1")
            elif(i == (quantidade_caracteres-1) and condicao_1 == True):
                print("Aceita#1")

        elif(entrada[i] == 'a'): # 0
            condicao_0 = True
            if(i == (quantidade_caracteres-1)):
                print("Rejeita#0")

        else:
            print("Rejeita#e")
            break
    