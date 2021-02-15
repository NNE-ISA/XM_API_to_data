from matplotlib.pyplot import axis
import pandas as pd

url = 'https://github.com/NNE-ISA/XM_API_to_data/blob/main/info_xm.xlsx?raw=true'

def dictGeneradores(df):
    inf = {}
    for i in range(df.shape[0]):
        inf[df['submercado'][i]] = {'íd': 'Recurso ID',
                                    'nombre': df['Nombre Recurso'][i],
                                    'capacidad_efectiva': df['Capacidad Efectiva'][i],
                                    'factor_conversion': df['Factor Conversión'][i],
                                    'tipo_despacho': df['Tipo Despacho'][i],
                                    'tipo_generación': df['Combustible Por Defecto'][i],
                                    'inicio_operacion': df['Fecha Operación'][i],
                                    'estado': df['Estado'][i],
                                    'agente': df['Nombre Agente'][i],
                                    'combustible': df['Tipo Despacho'][i]}
    return inf

def dictAgentes(df):
    inf = {}
    for i in range(df.shape[0]):
        inf[df['Código'][i]] = {'nombre': df['Des Agente'][i],
                                'actividad': df['Actividad'][i],
                                'estado': df['Estado'][i],
                                'inicio_operacion': df['Fecha'][i]}
    return inf


def recursosDict():
    global url
    excel = pd.ExcelFile(url)
    generadores = dictGeneradores(excel.parse(sheet_name = 'generadores', header=0))
    return generadores


def recursosDict():
    global url
    excel = pd.ExcelFile(url)
    agentes = dictAgentes(excel.parse(sheet_name = 'agentes', header=0))
    return agentes


def recursosDF():
    global url
    excel = pd.ExcelFile(url)
    recursos = excel.parse(sheet_name = 'generadores', header=0)
    recursos.columns = ['Recurso ID', 'nombre', 'submercado', 'capacidad_efectiva',
                           'factor_conversion',	'es_menor', 'tipo_despacho',
                           'tipo_generacion', 'inicio_operacion', 'estado',	'nombre_agente',
                           'combustible', 'clasificacion']
    recursos = recursos.drop(['clasificacion'], axis=1)
    return recursos

def agentesDF():
    global url
    excel = pd.ExcelFile(url)
    agentes = excel.parse(sheet_name = 'agentes', header=0)
    agentes.columns = ['submercado', 'nombre',	'actividad', 'estado', 'inicio_operacion']
    return agentes

