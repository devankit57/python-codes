def bin2dec(bin):
   
    dec=0
    for i in bin:
        dec=dec*2+int(i)

    print(dec)

bin2dec(101011)

