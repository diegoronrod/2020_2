from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica


p = Pessoa(22, 'Diego', 'Av. Otto', 555)
pf = Fisica(22, 'Diego', 'Av. Otto', '998877665', '111.222.333-44', 38, 56, 1.71)
pj = Juridica(22, 'Diego', 'Av. Otto', '998877665', '39.353.440/0001-68', '02.232.3355-6', 5)

print(pf.getIMC())
pj.imprimeCNPJ()
