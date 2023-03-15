iclass Viagem:
    def __init__(self, mobilidade_extraveicular, id):
        self.mobilidade_extraveicular = mobilidade_extraveicular
        self.id = id

    def __str__(self):
        return self.id + self.mobilidade_str()

    def mobilidade_str(self):
        if self.mobilidade_extraveicular: return ' Tem mobilidade extraveicular'
        else: ''

class Orbita_Terrestre(Viagem):
    def __init__(self,mobilidade_extraveicular, id, numero_orbitas):
        super().__init__(mobilidade_extraveicular, id)
        self.numero_orbitas = numero_orbitas


