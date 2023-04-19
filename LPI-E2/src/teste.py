lanche = ('hamburguer', 'suco', 'pizza', 'pudim') #tupla

print(lanche[2])        #fatiamento simples
print(lanche[0:2])      #fatiamento de um ponto inicial a outro
print(lanche[1:])       #fatiamento de um ponto até o final
print(lanche[-1])       #Fatiamento do último elemento
print(lanche[-2])       #Fatiamento do antepenúltimo elemento
print(lanche[-4])       #Fatiamento do primeiro ponto de outra maneira
class PC:
    def __init__(self, nome, processador, p1, mainboard, p2, water_cooler, p3, ram, p4, ssd, p5, fonte,
                       p6, gabinete, p7, nobreak, p8, monitor, p9, placa_video, p10, mini_monitor, p11):
        self.nome = nome
        self.processador = processador
        self.p1=p1                          #preço referente ao processador
        self.mainboard = mainboard
        self.p2=p2
        self.water_cooler = water_cooler
        self.p3=p3
        self.ram = ram
        self.p4=p4
        self.ssd = ssd
        self.p5=p5
        self.fonte = fonte
        self.p6=p6
        self.gabinete = gabinete
        self.p7=p7
        self.nobreak = nobreak
        self.p8=p8
        self.monitor = monitor
        self.p9=p9
        self.placa_video = placa_video
        self.p10=p10
        self.mini_monitor = mini_monitor
        self.p11=p11

    def __str__(self):
        return f'{self.nome:_^20}' + '\n'