from pickle import load
from sklearn import svm


def cargar_modelo(nombre):
    input = open(nombre, 'rb')
    modelo = load(input)
    input.close()
    return modelo


def clasifica(datos):
    listado = datos.split(sep=';')
    listado2 = [listado]
    ruta = './cancerapp/modelos/'
    nombre = 'svm_cancer.pkl'
    modelo = cargar_modelo(ruta + nombre)
    print(listado)
    tipo = modelo.predict(listado2)
    return tipo
