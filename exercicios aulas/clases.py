class carro():

    def __init__(self,cor,motor,marca):

      self.cor=cor
      self.motor=motor 
      self.marca=marca


gtrr5 = carro(cor="preto",motor="v8",marca="nissan")

supramk4 = carro(cor="branco",motor='v8',marca='toyota')


print(gtrr5.cor,gtrr5.motor)

print(supramk4.motor)
