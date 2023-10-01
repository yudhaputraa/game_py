import os

def print_state(sisi_kanan, sisi_kiri, perahu):
    print(f"Sisi Awal   : {sisi_kanan}")
    print(f"Sisi Akhir  : {sisi_kiri}")
    print(f"Perahu      : {perahu}")
    print("\n")

#def pindah_keperahu():
    

def main():
    sisi_kanan = {'domba': 1, 'serigala': 1, 'sayuran': 1}
    perahu = {'tumpangan': '' , 'posisi': 'kanan'}
    sisi_kiri = {'domba': 0, 'serigala': 0, 'sayuran': 0}

    while True:
        os.system('cls')
        tampil(sisi_kanan,perahu,sisi_kiri)

        if is_game_win(sisi_kiri):
            print("Anda menang!")
            break
        
        print("Menu :")
        print("1. Tepih ke Perahu")
        print("2. berangkat")
        if (not perahu['tumpangan'] == ''):
            print("3. perahu ke tepi")
        pilihan = input("Pilih Nomer Berapa? : ")

        if pilihan == '1':
            os.system('cls')
            tampil(sisi_kanan,perahu,sisi_kiri)
            item = input("Apa yang ingin Anda bawa ke perahu? : ")
            pengakutan(sisi_kanan,perahu,sisi_kiri,item)
        elif pilihan == '2':
            posisi_perahu(perahu)
            os.system('cls')
            tampil(sisi_kanan,perahu,sisi_kiri)
            if is_game_loss(sisi_kiri,sisi_kanan):
                print("Anda Kalah!")
                break
        elif pilihan == '3':
            pass

def is_game_win(sisi_kiri):
    return sisi_kiri['serigala'] == 1 and sisi_kiri['domba'] == 1 and sisi_kiri['sayuran'] == 1

def is_game_loss(sisi_kiri, sisi_kanan):
    return (
        ((sisi_kiri['serigala'] == 1 and sisi_kiri['domba'] == 1) and (not sisi_kiri['sayuran'] == 1)) or 
        ((sisi_kanan['serigala'] == 1 and sisi_kanan['domba'] == 1) and (not sisi_kanan['sayuran'] == 1))
        ) or (
            ((sisi_kiri['domba'] == 1 and sisi_kiri['sayuran'] == 1) and (not sisi_kiri['serigala'] == 1)) or 
            ((sisi_kanan['domba'] == 1 and sisi_kanan['sayuran'] == 1) and (not sisi_kanan['serigala'] == 1))
            )

def tampil(sisi_kanan,perahu,sisi_kiri):
    if perahu['posisi'] == 'kanan':
        print("------------------------------------------------------")
        if sisi_kanan['serigala'] == 1:
            print("|-----------|                  /------\  |-----------|")
            print("|           |                 /        \ |  serigala |") 
        elif sisi_kiri['serigala'] == 1:
            print("|-----------|                  /------\  |-----------|")
            print("| serigala  |                 /        \ |           |")
        else:
            print("|-----------|                  /------\  |-----------|")
            print("|           |                 /        \ |           |") 
        if sisi_kanan['domba'] == 1:
            print("|-----------|                 | Petani | |-----------|")
            print("|           |                 |        | |   domba   |")
        elif sisi_kiri['domba'] == 1:
            print("|-----------|                 | Petani | |-----------|")
            print("|   domba   |                 |        | |           |")
        else:
            print("|-----------|                 | Petani | |-----------|")
            print("|           |                 |        | |           |")

        if sisi_kanan['sayuran'] == 1:
            if perahu['tumpangan'] == 'serigala':
                print("|-----------|                 |serigala| |-----------|")
            elif perahu['tumpangan'] == 'domba':
                print("|-----------|                 | domba  | |-----------|")
            elif perahu['tumpangan'] == 'sayuran':
                print("|-----------|                 |sayuran | |-----------|")
            else:
                print("|-----------|                 |        | |-----------|")
            print("|           |                 \        / |  sayuran  |")
            print("|-----------|                  \------/  |-----------|")
        elif sisi_kiri['sayuran'] == 1:
            print("|-----------|                 |        | |-----------|")
            print("|  sayuran  |                 \        / |           |")
            print("|-----------|                  \------/  |-----------|")
        else:
            print("|-----------|                 |        | |-----------|")
            print("|           |                 \        / |           |")
            print("|-----------|                  \------/  |-----------|")
        print("------------------------------------------------------")

    if perahu['posisi'] == 'kiri':
        print("------------------------------------------------------")
        if sisi_kanan['serigala'] == 1:
            print("|-----------|  /------\                  |-----------|")
            print("|           | /        \                 | serigala  |") 
        elif sisi_kiri['serigala'] == 1:
            print("|-----------|  /------\                  |-----------|")
            print("| serigala  | /        \                 |           |")
        else:
            print("|-----------|  /------\                  |-----------|")
            print("|           | /        \                 |           |")

        if sisi_kanan['domba'] == 1:
            print("|-----------| | Petani |                 |-----------|")
            print("|           | |        |                 |   domba   |")
        elif sisi_kiri['domba'] == 1:
            print("|-----------| | Petani |                 |-----------|")
            print("|   domba   | |        |                 |           |")
        else:
            print("|-----------| | Petani |                 |-----------|")
            print("|           | |        |                 |           |")

        if sisi_kanan['sayuran'] == 1:
            if perahu['tumpangan'] == 'serigala':
                print("|-----------| |serigala|                 |-----------|")
            elif perahu['tumpangan'] == 'domba':
                print("|-----------| | domba  |                 |-----------|")
            elif perahu['tumpangan'] == 'sayuran':
                print("|-----------| |sayuran |                 |-----------|")
            else:
                print("|-----------| |        |                 |-----------|")
            print("|           | \        /                 |  sayuran  |")
            print("|-----------|  \------/                  |-----------|")
        elif sisi_kiri['sayuran'] == 1:
            print("|-----------| |        |                 |-----------|")
            print("|  sayuran  | \        /                 |           |")
            print("|-----------|  \------/                  |-----------|")
        else:
            print("|-----------| |        |                 |-----------|")
            print("|           | \        /                 |           |")
            print("|-----------|  \------/                  |-----------|")
        print("------------------------------------------------------")

def posisi_perahu(perahu):
    if perahu['posisi'] == 'kanan':
        perahu['posisi'] = 'kiri'
        return perahu
    if perahu['posisi'] == 'kiri':
        perahu['posisi'] = 'kanan'
        return perahu
    
def pengakutan(sisi_kanan,perahu,sisi_kiri,item):
    # keys_kanan = sisi_kanan.keys()
    # keys_list_kanan = list(keys_kanan)
    # keys_kiri = sisi_kiri.keys()
    # keys_list_kiri = list(keys_kiri)

    if perahu['posisi'] == 'kanan':
        if 'domba' == item:
            perahu['tumpangan'] = 'domba'
            sisi_kanan['domba'] = 0
            return perahu,sisi_kanan
        elif 'serigala' == item:
            perahu['tumpangan'] = 'serigala'
            sisi_kanan['serigala'] = 0
            return perahu,sisi_kanan
        elif 'sayuran' == item:
            perahu['tumpangan'] = 'sayuran'
            sisi_kanan['serigala'] = 0
            return perahu,sisi_kanan
    
    if perahu['posisi'] == 'kiri':
        if 'domba' == item:
            perahu['tumpangan'] = 'domba'
            sisi_kiri['domba'] = 0
            return perahu,sisi_kiri
        elif 'serigala' == item:
            perahu['tumpangan'] = 'serigala'
            sisi_kiri['serigala'] = 0
            return perahu,sisi_kiri
        elif 'sayuran' == item:
            perahu['tumpangan'] = 'sayuran'
            sisi_kiri['serigala'] = 0
            return perahu,sisi_kiri


if __name__ == "__main__":
    main()