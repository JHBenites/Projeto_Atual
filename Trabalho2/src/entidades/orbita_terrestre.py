class OrbitaTerrestre:
    def __init__(self, vagas, numero_de_orbitas):
        self.numero_de_orbitas = numero_de_orbitas if 1 <= numero_de_orbitas <= 9 else -1
        self.vagas = vagas

    def __str__(self):
        return 'Número de vagas contratadas: ' + self.vagas + \
            ' - Número de Órbitas: ' + str(self.numero_de_orbitas)

orbitas = []

def get_orbita_terrestre(): return orbitas
