# coding: utf-8
def delblankline(infile, outfile):
    infopen = open(infile, 'r',encoding="utf-8")
    outfopen = open(outfile, 'w',encoding="utf-8")
    db = infopen.read()
    outfopen.write(db.replace(' ','\n'))
    infopen.close()
    outfopen.close()

delblankline("C:\\Users\\hp\\Desktop\\1\\111.txt", "C:\\Users\\hp\\Desktop\\1\\333.txt")

