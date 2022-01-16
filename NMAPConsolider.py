import nmap
import csv
import datetime
import os


def validate_ip(ip):

    try:

        blocos = ip.split('.')    # Verifica se contem 4 blocos de bits
        return len(blocos) == 4 and all(0 < len(bloco) < 4 and 0 <= int(bloco) < 256 for bloco in blocos)     # verifica se cada bloco esta entre 0 e 255

    except ValueError:

        return False # Retorna falso caso qualquer bloco nao seja convertivel para int

    except (AttributeError, TypeError):

        return False # retorna false se o ip nao for uma string



nnscan = nmap.PortScanner()

ip = input("Digite o endereco IP a ser escaneado: ")

while (not validate_ip(ip)):

    ip = input("Endereco digitado nao eh valido! Digite o endereco IP valido a ser escaneado: ")    


print("ip = ", ip)


nnscan.scan(ip)

scanresult = nnscan.csv()

print(scanresult)

os.makedirs(os.getcwd() + "/Results/",exist_ok=True)


with open(("Results/" + ip + str(datetime.datetime.now()) + ".csv"), 'w', newline='') as file:

    writer = csv.writer(file)

    rows2 = scanresult.splitlines()
    rows = [r.splitlines() for r in rows2]

    #print(rows)

    for row in rows:
        writer.writerow(row)
