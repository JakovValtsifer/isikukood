while True:
    ikood=input("Sisesta isikukood: ")
    if len(ikood)!=11:
        print("Liiga pikk või lühike isikukood")
    else:
        print("isikukoodi kontrol")
        ik_list=list(ikood)
        print(ik_list[0])
        sl=int(ik_list[0])
        if sl not in [1,2,3,4,5,6]:
            print("Esineme sümbov ei ole õige")
        else:
            print("Elimene sümbol on õige")
            y=(ik_list[1]+ik_list[2])
            m=(ik_list[3]+ik_list[4])
            d=(ik_list[5]+ik_list[6])
            if (int(m)<1 or int(m)>13) and (int(d)<1 or int(d)>31):
                print("Sünnipäev ei saa luua")

            else:
                if sl==1 or sl==2:
                    yy="18"
                elif sl==3 or sl==4:
                    yy="19"
                else:
                    yy=="20"
                    spaev=d+"."+m+"."+yy+y
                    print(f"sünnipäev on {spaev}")
                    print("")
                    if sl in [1,2,3]:
                        print("mees")
                        if sl in [2,4,6]:
                            print("naine")
                    a1=int(ikood[0])*1
                    b1=int(ikood[1])*2
                    b2=int(ikood[2])*3
                    b3=int(ikood[3])*4
                    b4=int(ikood[4])*5
                    b5=int(ikood[5])*6
                    b6=int(ikood[6])*7
                    b7=int(ikood[7])*8
                    b8=int(ikood[8])*9
                    b9=int(ikood[9])*1

                    s11=b1+a1+b1+b2+b3+b4+b5+b6+b7+b8+b9
                    print(s11)
                    s=s11//11
                    print(s)
                    p=s*11
                    pl=s11-p
                    if pl==int(ikood[10]):
                        print()
                    else:
                        a1=int(ikood[0])*3
                        b1=int(ikood[1])*4
                        b2=int(ikood[2])*5
                        b3=int(ikood[3])*6
                        b4=int(ikood[4])*7
                        b5=int(ikood[5])*8
                        b6=int(ikood[6])*9
                        b7=int(ikood[7])*1
                        b8=int(ikood[8])*2
                        b9=int(ikood[9])*3
                    s11=b1+a1+b2+b3+b4+b5+b6+b7+b8+b9
                    print(s11)
                    s=s11//11
                    print(s)
                    p=s*11
                    p1=s11-p
                    print(p1)
                    hhh=int(ik_list[7]+ik_list[8]+ik_list[9])
                    if 1<=hhh<=10:
                        haigla="kuresaare Haigla"
                    elif 11<=hhh<=19:
                        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                    elif 20<=hhh<=220:
                        haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                    elif 221<=hhh<=270:
                        haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                    elif 271<=hhh<=310:
                        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
                    elif 371<=hhh<=420:
                        haigla="Narva Haigla"
                    elif 421<=hhh<=470:
                        haigla="Pärnu Haigla"
                    elif 471<=hhh<=490:
                        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
                    elif 491<=hhh<=520:
                        haigla="Järvamaa Haigla (Paide)"
                    elif 521<=hhh<=570:
                        haigla="Rakvere, Tapa haigla"
                    elif 571<=hhh<=600:
                        haigla="Valga Haigla"
                    elif 601<=hhh<=650:
                        haigla="Viljandi Haigla"
                    elif 651<=hhh<=700:
                        halga="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
                    print(haigla)
                    print(f"See on {sugu}, sünnipäev {spaev}. Ta on sündinud {haigla}")

