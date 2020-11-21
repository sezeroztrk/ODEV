readFile = open('source.c', 'r') # hedef dosya okuma işlemi
writeFile = open('target.c', 'w', encoding='utf-8') # hedef dosyaya yazma (hedef dosya yoksa target.c adında eklenir)

recess = 0 # yapılacak girintileme sayısı

for line in readFile:
    if line[0] == '{': # dosyada ki süslü parantez açık olanları alma
        newLine = int(recess) * '\t' + line # yeni satırın girintilemesi yapılıyor(1 tab boyunda)
        recess += 1 # Girinti sayısını artırma
    elif line[0] == '}': # dosyada ki süslü parantez kapalı olanları alma
        newLine = int(recess-1) * '\t' + line # yeni satırın girintilemesi yapılıyor(1 tab boyunda)
        recess -= 1 # Girinti sayısını azaltma
    else:
        newLine = int(recess) * '\t' + line # eğer açma kapama işareti yok ise satırı yerinde bırakma
    writeFile.write(newLine) # İşlmelere göre dosyaya doğru şekilde satırı yazma
