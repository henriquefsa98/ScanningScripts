from multiprocessing.connection import wait
import NMAPConsolider
import sys
import concurrent.futures

def main(args):

    print(args)

    IPsFileName = args[0]

    IPsList = open(IPsFileName, 'r').read().splitlines()

    #print(IPsList)

    ValidIPsList = [ip for ip in IPsList if NMAPConsolider.validate_ip(ip)==True]

    #for ip in IPsList:
    #    print(NMAPConsolider.validate_ip(ip))
    #print((IPsList[0]))

    #print(ValidIPsList)

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(ValidIPsList)) as executor:
        futures = []
        for ip in ValidIPsList:
            print("ip = " + ip)
            futures.append(executor.submit(NMAPConsolider.NMAPcsv, ip=ip))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())



if __name__ == "__main__":
    main(sys.argv[1:])