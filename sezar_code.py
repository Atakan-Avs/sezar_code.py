print('Sezar Şifreleme / Çözme Programı')

while True:
    print('\n1. Şifreleme')
    print('2. Çözme')
    print('3. Çıkış')

    secim = input('Bir seçenek giriniz: (1-2-3) ')

    if secim == '1':
        metin = input('Şifrelenecek metni giriniz: ')
        kaydirma = int(input('Kaydırma miktarını giriniz: '))

        sifreliMetin = ""

        for karakter in metin:
            if karakter.isalpha():
                kaydirmaEgik = kaydirma % 26
                base = ord('a') if karakter.islower() else ord('A')
                sifreliKarakter = chr((ord(karakter) - base + kaydirmaEgik) % 26 + base)
                sifreliMetin += sifreliKarakter
            else:
                sifreliMetin += karakter

        print(f"Şifreli metin: {sifreliMetin}")

    elif secim == '2':
        metin = input('Çözülecek metni giriniz: ')
        kaydirma = int(input('Kaydırma miktarını giriniz: '))

        cozulmusMetin = ""

        for karakter in metin:
            if karakter.isalpha():
                kaydirmaEgik = -kaydirma % 26
                base = ord('a') if karakter.islower() else ord('A')
                cozulmusKarakter = chr((ord(karakter) - base + kaydirmaEgik) % 26 + base)
                cozulmusMetin += cozulmusKarakter
            else:
                cozulmusMetin += karakter

        print(f"Çözülmüş metin: {cozulmusMetin}")

    elif secim == '3':
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz giriş, lütfen 1, 2 veya 3 giriniz.")

        break
    
