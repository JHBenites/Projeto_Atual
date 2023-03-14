class OrbitaTerrestre:
    def __init__(self, numero_de_orbitas, mobilidade_extraveicular):
        self.numero_de_orbitas = numero_de_orbitas if 1 <= numero_de_orbitas <= 9 else -1
        self.mobilidade_extraveicular = mobilidade_extraveicular
    def __str__(self):
        return ' - Número de Órbitas: ' + str(self.numero_de_orbitas) + self.__to_str_mobilidade_extraveicular__()
    def __to_str_mobilidade_extraveicular__(self):
        if not self.mobilidade_extraveicular:
            return ''
        else:
            if self.mobilidade_extraveicular == True:
                return ' -com Mobilidade Extraveicular'
orbitas = []
def get_orbita_terrestre(): return orbitas
def inserir_orbita_terrestre(orbita): orbitas.append(orbita)