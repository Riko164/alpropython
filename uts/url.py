def extract_url(string):
    isi = string.split("/")
    print(isi[0].replace(':',''))
    print(isi[2])
    print(isi[len(isi)-1])



extract_url('https://www.torrenting.com/download/manage.php')
