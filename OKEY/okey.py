from colorama import Style,Fore,init
from random import randint
import json
from time import sleep
import os

init()
green = Style.BRIGHT+Fore.GREEN
magenta = Style.BRIGHT+Fore.MAGENTA
default = Style.RESET_ALL
blue = Style.BRIGHT+Fore.BLUE
red = Style.BRIGHT+Fore.RED
yellow = Style.BRIGHT+Fore.YELLOW

clear = lambda:os.system('clear')
log= [f'\t\t{yellow}RAUND 1{default}']
raund = 1
while True:
    welcome = input('New Game? Y/N  ').lower()
    if welcome =='y':
        group1= input('Enter group 1 name: ')
        group2= input('Enter group 2 name: ')
        scor_group1 = 0
        scor_group2= 0
        try:
            with open('okey_data/group1.json','w') as f:
                json.dump(group1,f)
        except:
            os.mkdir('okey_data')
            with open('okey_data/group1.json','w') as f:
                json.dump(group1,f)
        with open('okey_data/group2.json','w') as f:
            json.dump(group2,f)
        with open('okey_data/scor_group1.json','w') as f:
            json.dump(scor_group1,f)
        with open('okey_data/scor_group2.json','w') as f:
            json.dump(scor_group2,f)
        templog = []
        with open('okey_data/logs','w') as f:
            json.dump(templog,f)
        break
    if welcome=='n':
        try:
            with open('okey_data/group1.json') as f:
                group1 = json.load(f)
            with open('okey_data/group2.json') as f:
                group2 = json.load(f)
            with open('okey_data/scor_group1.json') as f:
                scor_group1 = json.load(f)
            with open('okey_data/scor_group2.json') as f:
                scor_group2 = json.load(f)
            with open('okey_data/logs') as f:
                log = json.load(f)
            print(f"Veriler yüklendi.\nGrup1 = {group1} Skor:{scor_group1}\nGrup2 = {group2} Skor:{scor_group2}")
            input()
            break
        except Exception as eee:
            input(eee)
group1 = group1.title()
group2 = group2.title()

clear()
while True:
    print(f'\t\t{magenta}RAUND {raund}{default}') #bunu cezanın üstüne yaz.
    print(f"{green}{group1}{default}:{yellow}{scor_group1}\t{green}{group2}{default}:{yellow}{scor_group2}{default}")
    print('''
        1 > İşler taş cezası. 
        2 'sayi' > Açtırma cezası, çift için 2ç
        3 > Yerden okey verme 
        4 > Elden bitme 
        5 > Elden okeyle bitme 
        6 > Elden çift, okeyle bitme
        7 > Elde kalan ceza 
        8 > Açamama cezası oyuncu sayısı 1-2     
        9 > Raund sonu.
        10 > Bitme.
            log or admin 
                ''')

    try:
        menu_action = input(f'{blue}<command>{default}').lower()
        if menu_action=='log':
            clear()
            for a in log:
                if not 'RAUND' in a:
                    if '<Admin>' in a:
                        print(red,a,default)
                    elif 'Admin' not in a:
                        print(green,a,default)
                else:
                    print(a)
            input(f'{yellow}Devam etmek için enter.{default}')
            clear()
            continue
        elif menu_action=='admin':
            while True:
                clear()
                print(f"{yellow}{log[-1]}{default}")
                print(red,'\t\tADMIN',default)
                admin_input = input(f'{yellow}Örn: g1 200\n {default}')
                if admin_input=='q':
                    clear()
                    break
                try:
                    game_group, second = admin_input.split()
                    if game_group == 'g1' or game_group == 'g2':
                        if game_group == 'g1':
                            in_game_group = group1
                            in_game_score = scor_group1
                            other_group = scor_group2
                        elif game_group == 'g2':
                            in_game_group = group2
                            in_game_score = scor_group2
                            other_group = scor_group1
                        second = int(second)
                        in_game_score+=second
                        log.append(f"<Admin> {in_game_group} için {second} puanlık bir düzeltme yapıldı.")
                    else:
                        input(red, 'Yanlış grup', default)
                        continue
                except Exception as first_except:
                    clear()
                    input(f"{red}{first_except}{default}")
                    continue

        elif menu_action == '9':
            raund += 1
            clear()
            print(yellow,'Yeni raund.',default)
            num1,num2 = randint(1,6),randint(1,6)
            print(f'{yellow}Otomatik zar atıldı ; {green}{num1}-{num2}{default}')
            log.append(f"{yellow}\t\tRAUND {raund}{default}")
            continue
        elif menu_action=='':
            clear()
            continue
        space_count = menu_action.count(' ')
        if space_count==1:
            game_group,second = menu_action.split()
            if game_group=='g1' or game_group=='g2':
                if game_group == 'g1':
                    in_game_group = group1
                    in_game_score = scor_group1
                    other_group = scor_group2
                elif game_group == 'g2':
                    in_game_group = group2
                    in_game_score = scor_group2
                    other_group = scor_group1
            else:
                input(red,'Yanlış grup',default)
                continue
            if second=='1':
                in_game_score+=101
                log.append(f"{in_game_group} işler taş attı ve 101 puan ceza yedi.")
                clear()
                print(blue,log[-1],default)

            elif second=='3':
                log.append(f"{in_game_group} yerden okey kaptırdı ve 100 puan ceza yedi.")
                clear()
                print(blue,log[-1],default)
                in_game_score+=100

            elif second=='4':
                log.append(f"{in_game_group} elden bitti. ")
                clear()
                print(green, log[-1], default)
                in_game_score-=200
                other_group+=800
            elif second=='5':
                log.append(f"{in_game_group} elden okeyle bitti. ")
                clear()
                print(green, log[-1], default)
                in_game_score -= 400
                other_group += 1600

            elif second=='6':
                log.append(f"{in_game_group} elden okeyle çift bitti. ")
                clear()
                print(green, log[-1], default)
                in_game_score -= 800
                other_group += 3200
            elif second=='10':
                in_game_score-=100
                log.append(f"{in_game_group} normal bitti. ")
                clear()
                print(green,log[-1],default)
            else:
                clear()
                print(red,'hatalı komut.',default)
        elif space_count==2:
            game_group,second,third = menu_action.split()
            if game_group=='g1' or game_group=='g2':
                if game_group == 'g1':
                    in_game_group = group1
                    in_game_score = scor_group1
                    other_group = scor_group2
                elif game_group == 'g2':
                    in_game_group = group2
                    in_game_score = scor_group2
                    other_group = scor_group1
                try:
                    third = int(third)
                except:
                    input(red,'Üçüncü parametrem sayı olmalı.',default)
                    continue
            if second=='2':
                in_game_score+=third*10
                log.append(f"{in_game_group} '{third}' atarak açtırdı ve {third*10} ceza yedi. ")
                clear()
                print(blue, log[-1], default)
            elif second=='2ç':
                in_game_score += third * 20
                log.append(f"{in_game_group} '{third}' atarak çift açtırdı ve {third * 20} ceza yedi. ")
                clear()
                print(blue, log[-1], default)
            elif second=='7':
                in_game_score+=third
                log.append(f"{in_game_group} ikilisinde {third} puan ceza kaldı.")
                clear()
                print(blue, log[-1], default)
            elif second =='8':
                if third==1:
                    in_game_score+=200
                elif third==2:
                    in_game_score+=400
                elif third!=1 and third!=2:
                    clear()
                    print(red,'O kadar oyuncu olamaz.',default)
                    continue
                log.append(f"{in_game_group},{third} oyuncu açamadı ve {third*200} ceza yedi.")
                clear()
                print(blue, log[-1], default)
            else:
                clear()
                input(red,'Yanlış grup',default)
                continue
        #final
        if in_game_group==group1:
            scor_group1 = in_game_score
            scor_group2 = other_group
        elif in_game_group==group2:
            scor_group2= in_game_score
            scor_group1=other_group
        with open('okey_data/scor_group1.json', 'w') as f:
            json.dump(scor_group1, f)
        with open('okey_data/scor_group2.json', 'w') as f:
            json.dump(scor_group2, f)
        with open('okey_data/logs', 'w') as write_logs:
            json.dump(log, write_logs)

    except Exception as my_except:
        clear()
        input(red,my_except,default)
        continue
