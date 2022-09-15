def notas(*n, sit=False):
    r= {}
    r['TOTAL']= len(n)
    r['MAIOR']= max(n)
    r['MENOR']= min(n)
    r['MÉDIA']= sum(n)/len(n)
    if (sit==True):
        if r['MÉDIA']>=7:
            r['SITUAÇÃO']= 'BOA'
        if r['MÉDIA']>=5:
            r['SITUAÇÃO']= 'RAZOAVEL'
        if r['MÉDIA']<5:
            r['SITUAÇÃO']= 'RUIM'       
    return r


resp= notas(5.5, 2.5, 8.5, sit=False)
print(resp)