from dispositivo import Dispositivo

class Database():
    def __init__(self, template : dict):
        self.database = []
        lista = template.get('dispositivos')
        for dici in lista:
            self.database.append(Dispositivo(diccionario=dici))

    def delete_by_id(self, id):

        for i in range(0,len(self.database)-1):
            if self.database[i].id == id:
                self.database.pop(i)

    def add_dispositivo(self, dispositivo : Dispositivo = None, diccionario = None):
        if not dispositivo is None:
            self.database.append(dispositivo)
        if not diccionario is None:
            self.database.append(Dispositivo(diccionario=diccionario))


