import requests
import json
import pandas as pd
import datetime as dt
# noinspection SpellCheckingInspection


class ReadDB:

    def __init__(self):
        """This object was created to extract data from API XM"""

        self.url = "http://servapibi.xm.com.co/hourly"
        self.connection = None
        self.request = ''
        self.inventario_metricas = \
            {'Gene': [(0, 'Generacion Real', 'Sistema', 'Horaria'),
                      (1, 'Generacion Real por Recurso', 'Recurso', 'Horaria')],
             'DemaCome': [(0, 'Demanda Comercial', 'Sistema', 'Horaria'),
                          (1, 'Demanda Comercial por Agente', 'Agente', 'Horaria')],
             'AporEner': [(0, 'Aportes Energia', 'Sistema', 'Diaria'),
                          (1, 'Aportes Energia por Rio', 'Rio', 'Diaria')],
             'PrecEscaAct': [(0, 'Precio de Escasez de Activacion', 'Sistema', 'Diaria')],
             'ConsCombustibleMBTU': [(0, 'Cons. Comb. Recursos DC', 'Recurso', 'Horaria')],
             'PrecOferDesp': [(0, 'Precio de Oferta del Despacho', 'Recurso', 'Horaria')],
             'PrecBolsNaci': [(0, 'Precio de Bolsa Nacional', 'Sistema', 'Horaria')],
             'MaxPrecOferNal': [(0, 'Máximo Precio de Oferta Nacional', 'Sistema', 'Horaria')],
             'RestAliv': [(0, 'Restricciones Aliviadas', 'Sistema', 'Horaria')],
             'GeneIdea': [(0, 'Generacion Ideal', 'Sistema', 'Horaria'),
                          (1, 'Generacion Ideal', 'Recurso', 'Horaria')],
             'VoluUtilDiarEner': [(0, 'Volumen Util Diario', 'Sistema', 'Diaria'),
                                  (1, 'Volumen Util Diario por Embalse', 'Embalse', 'Diaria')],
             'RemuRealIndiv': [(0, 'RRID', 'Sistema', 'Diaria')],
             'CapEfecNeta': [(0, 'Listado de recursos térmicos CEN por mes', 'Sistema', 'Anual'),
                             (1, 'Listado Recursos Generación', 'Recurso', 'Diaria')],
             'VentContEner': [(0, 'Ventas en Contratos Energía', 'Sistema', 'Horaria'),
                              (1, 'Ventas en Contratos Energía por Agente', 'Agente', 'Horaria')],
             'CompContEner': [(0, 'Compras en Contrato Energía', 'Sistema', 'Horaria'),
                              (1, 'Compras en Contrato Energía por Agente', 'Agente', 'Horaria')],
             'CompBolsNaciEner': [(0, 'Compras en Bolsa Nacional Energía', 'Sistema', 'Horaria'),
                                  (1, 'Compras en Bolsa Nacional Energía por Agente', 'Agente', 'Horaria')],
             'PrecPromContRegu': [(0, 'Precio Promedio Contratos Regulado', 'Sistema', 'Diaria')],
             'PrecPromContNoRegu': [(0, 'Precio Promedio Contratos No Regulado', 'Sistema', 'Diaria')],
             'ConsCombAprox': [(0, 'Consumo Comb Aprox.', 'RecursoComb', 'Horaria')],
             'EmisionesCO2': [(0, 'Emisiones CO2', 'RecursoComb', 'Horaria')],
             'EmisionesCH4': [(0, 'Emisiones CH4', 'RecursoComb', 'Horaria')],
             'EmisionesN2O': [(0, 'Emisiones N2O', 'RecursoComb', 'Horaria')],
             'EmisionesCO2Eq': [(0, 'Emisiones CO2e', 'Recurso', 'Horaria')],
             'factorEmisionCO2e': [(0, 'factor emision CO2e', 'Sistema', 'Horaria')],
             'ImpoEner': [(0, 'Importaciones Energía', 'Sistema', 'Horaria')],
             'DemaOR': [(0, 'Demanda por OR', 'Agente', 'Horaria')],
             'PerdidasEner': [(0, 'Perdidas en Energía', 'Sistema', 'Horaria')],
             'DemaSIN': [(0, 'Demanda del SIN', 'Sistema', 'Diaria')],
             'DemaNoAtenProg': [(0, 'Demanda No Atendida Programada por Área', 'Area', 'Diaria'),
                                (1, 'Demanda No Atendida Programada por Subárea', 'Subarea', 'Diaria')],
             'DemaNoAtenNoProg': [(0, 'Demanda No Atendida No Programada por Área', 'Area', 'Diaria'),
                                  (1, 'Demanda No Atendida No Programada por Subárea', 'Subarea', 'Diaria')],
             'CapaUtilDiarEner': [(0, 'Capacidad Util Diario', 'Sistema', 'Diaria'),
                                  (1, 'Capacidad Util Diario por Embalse', 'Embalse', 'Diaria')],
             'AporEnerMediHist': [(0, 'Media Historica Aportes', 'Sistema', 'Diaria'),
                                  (1, 'Media Historica Aportes por Rio', 'Rio', 'Diaria')],
             'GeneSeguridad': [(0, 'Generación Seguridad', 'Recurso', 'Horaria')],
             'GeneFueraMerito': [(0, 'Generación Fuera de Merito', 'Recurso', 'Horaria')],
             'ObligEnerFirme': [(0, 'Obligaciones de Energía Firme', 'Recurso', 'Diaria')],
             'FAZNI': [(0, 'Recaudo FAZNI', 'Sistema', 'Diaria')],
             'PRONE': [(0, 'Recaudo PRONE', 'Sistema', 'Diaria')],
             'FAER': [(0, 'Recaudo FAER', 'Sistema', 'Diaria')]
             }

    def get_collections(self, coleccion):
        return self.inventario_metricas[coleccion]

    def request_data(self, coleccion, metrica, start_date, end_date):
        """ request public server data from XM by the API
        Args:
            coleccion: one of the set of variables availables at self.get_collections()
            metrica:one of this variables "DemaCome", "Gene", "GeneIdea", "PrecBolsNaci", "RestAliv"
            start_date: start date consult data
            end_date: end date consult data
        Returns: DataFrame with the raw Data
        """
        if coleccion not in self.inventario_metricas.keys():
            print('No existe la colección {}'.format(coleccion))
            return pd.DataFrame()
        if metrica > len(self.inventario_metricas[coleccion]):
            print('No existe la metrica')
            return pd.DataFrame()

        if self.inventario_metricas[coleccion][metrica][3] == 'Horaria':

            end = end_date
            condition = True
            aux = True
            data = None
            while condition:
                if (start_date - end_date).days < 30:
                    end = start_date + dt.timedelta(29)
                if end > end_date:
                    end = end_date
                self.request = {"MetricId": coleccion,
                                "StartDate": "{}".format(str(start_date)),
                                "EndDate": "{}".format(str(end)),
                                'Entity': self.inventario_metricas[coleccion][metrica][2]}

                self.connection = requests.post(self.url, json=self.request)

                data_json = json.loads(self.connection.content)

                temporal_data = pd.json_normalize(data_json['Items'], 'HourlyEntities', 'Date', sep='_')

                if data is None:
                    data = temporal_data.copy()
                else:
                    data = data.append(temporal_data, ignore_index=True)
                start_date = start_date + dt.timedelta(30)

                if end == end_date:
                    aux = False
                condition = ((end - start_date).days > 30 | (end - end_date).days != 0) | aux
        elif self.inventario_metricas[coleccion][metrica][3] == 'Diaria' and coleccion == 'CapEfecNeta':
            end = end_date
            condition = True
            aux = True
            data = None
            while condition:
                if (start_date - end_date).days < 1:
                    end = start_date + dt.timedelta(0)
                if end > end_date:
                    end = end_date
                self.request = {"MetricId": coleccion,
                                "StartDate": "{}".format(str(start_date)),
                                "EndDate": "{}".format(str(end)),
                                'Entity': self.inventario_metricas[coleccion][metrica][2]}
                self.url = self.url.replace('hourly', 'daily')
                self.connection = requests.post(self.url, json=self.request)

                data_json = json.loads(self.connection.content)

                temporal_data = pd.json_normalize(data_json['Items'], 'DailyEntities', 'Date', sep='_')

                if data is None:
                    data = temporal_data.copy()
                else:
                    data = data.append(temporal_data, ignore_index=True)
                start_date = start_date + dt.timedelta(1)

                if end == end_date:
                    aux = False
                condition = ((end - start_date).days > 1 | (end - end_date).days != 0) | aux
        elif self.inventario_metricas[coleccion][metrica][3] == 'Diaria':
            end = end_date
            condition = True
            aux = True
            data = None
            while condition:
                if (start_date - end_date).days < 30:
                    end = start_date + dt.timedelta(29)
                if end > end_date:
                    end = end_date

                self.request = {"MetricId": coleccion,
                                "StartDate": "{}".format(str(start_date)),
                                "EndDate": "{}".format(str(end)),
                                'Entity': self.inventario_metricas[coleccion][metrica][2]}
                self.url = self.url.replace('hourly', 'daily')
                self.connection = requests.post(self.url, json=self.request)
                data_json = json.loads(self.connection.content)
                temporal_data = pd.json_normalize(data_json['Items'], 'DailyEntities', 'Date', sep='_')
                if data is None:
                    data = temporal_data.copy()
                else:
                    data = data.append(temporal_data, ignore_index=True)

                start_date = start_date + dt.timedelta(30)
                if end == end_date:
                    aux = False
                condition = ((end - start_date).days > 29 | (end - end_date).days != 0) | aux

        elif self.inventario_metricas[coleccion][metrica][3] == 'Anual':

            end = end_date
            condition = True
            aux = True
            data = None
            while condition:
                if (start_date - end_date).days < 366:
                    end = start_date + dt.timedelta(365)
                if end > end_date:
                    end = end_date

                self.request = {"MetricId": coleccion,
                                "StartDate": "{}".format(str(start_date)),
                                "EndDate": "{}".format(str(end)),
                                'Entity': self.inventario_metricas[coleccion][metrica][2]}
                self.url = self.url.replace('hourly', 'annual')
                self.connection = requests.post(self.url, json=self.request)
                data_json = json.loads(self.connection.content)
                temporal_data = pd.json_normalize(data_json['Items'], 'AnnualEntities', 'Code', sep='_')
                if data is None:
                    data = temporal_data.copy()
                else:
                    data = data.append(temporal_data, ignore_index=True)

                start_date = start_date + dt.timedelta(366)
                if end == end_date:
                    aux = False
                condition = ((end - start_date).days > 365 | (end - end_date).days != 0) | aux

        return data

inven_met = {'Recursos': {'freq': ['Horaria', 'Diaria'],
                          'Horaria': {'var': {'Generacion Ideal': ['GeneIdea', 1],
                                              'Generacion Real': ['Gene', 1],
                                              'Consumo Combustible Aprox. Factor de Emisión': ['ConsCombustibleMBTU', 0],
                                              'Precio de Oferta del Despacho': ['PrecOferDesp', 0],
                                              'Emisiones CO2e': ['EmisionesCO2Eq', 0],
                                              'Generación Seguridad': ['GeneSeguridad', 0],
                                              'Generación Fuera de Merito': ['GeneFueraMerito', 0]
                                              },
                                      'join_var': ['Id', 'Values_code', 'Date', 'Hour']
                                      },
                          'Diaria': {'var': {'Obligaciones de Energía Firme':['ObligEnerFirme', 0]},
                                     'join_var':['Id', 'Code', 'Date']
                                     }
                          },

             'Recursos_Combinados': {'freq': ['Horaria'],
                                     'Horaria': {'var': {'Consumo Comb Aprox.': ['ConsCombAprox', 0],
                                                         'Emisiones CO2': ['EmisionesCO2', 0],
                                                         'Emisiones CH4': ['EmisionesCH4', 0],
                                                         'Emisiones N2O': ['EmisionesN2O', 0]
                                                         },
                                                 'join_var': ['Id', 'Values_code', 'Values_Name', 'Date', 'Hour']
                                                 }
                                      },

              'Agentes': {'freq':['Horaria'],
                          'Horaria': {'var': {'Demanda Comercial': ['DemaCome', 1],
                                              'Ventas en Contratos Energía': ['VentContEner', 1],
                                              'Compras en Contratos Energía': ['CompContEner', 1],
                                              'Compras en Bolsa Nacional Energía': ['CompBolsNaciEner', 1],
                                              'Demanda por Operador de Red': ['DemaOR', 0]
                                              },
                                      'join_var': ['Id', 'Values_code', 'Date', 'Hour']
                                     }
                          },

              'Sistema': {'freq': ['Horaria', 'Diaria', 'Anual'],
                          'Horaria': {'var': {'Generacion Ideal': ['GeneIdea', 0],
                                              'Generacion Real': ['Gene', 0],
                                              'Demanda Comercial': ['DemaCome', 0],
                                              'Precio de Bolsa Nacional': ['PrecBolsNaci', 0],
                                              'Máximo Precio de Oferta Nacional': ['MaxPrecOferNal', 0],
                                              'Restricciones Aliviadas': ['RestAliv', 0],
                                              'Ventas en Contratos Energía': ['VentContEner', 0],
                                              'Compras en Contratos Energía': ['CompContEner', 0],
                                              'Compras en Bolsa Nacional Energía': ['CompBolsNaciEner', 0],
                                              'factor emision CO2e': ['factorEmisionCO2e', 0],
                                              'Importaciones Energía': ['ImpoEner', 0],
                                              'Perdidas en Energia': ['PerdidasEner', 0]
                                              },
                                      'join_var': ['Id', 'Values_code', 'Date', 'Hour']
                                     },
                          'Diaria': {'var': {'Aportes Energia': ['AporEner', 0],
                                             'Precio de Escasez de Activacion': ['PrecEscaAct', 0],
                                             'Remuneración Real Ind. Cargo Confiabilidad': ['RemuRealIndiv', 0],
                                             'Precio Promedio Contratos Regulado': ['PrecPromContRegu', 0],
                                             'Precio Promedio Contratos NO Regulado': ['PrecPromContNoRegu', 0],
                                             'Volumen Util Diario en Energia': ['VoluUtilDiarEner', 0],
                                             'Demanda del SIN': ['DemaSIN', 0],
                                             'Capacidad Util Diaria en Energia': ['CapaUtilDiarEner', 0],
                                             'Media Historica Aportes': ['AporEnerMediHist', 0],
                                             'FAZNI': ['FAZNI', 0],
                                             'PRONE': ['PRONE', 0],
                                             'FAER': ['FAER', 0]
                                             },
                                     'join_var': ['Id', 'Date']
                                    },
                          'Anual': {'var': {'Listado de recursos térmicos CEN por mes':['CapEfecNeta', 0]},
                                    'join_var': []
                                   }
                          },


              'Rios': {'freq': ['Diaria'],
                       'Diaria': {'var': {'Aportes Energia': ['AporEner', 1],
                                          'Media Historica Aportes': ['AporEnerMediHist', 1]
                                          },
                                  'join_var': ['Id', 'Name', 'Date']
                                 }
                      },

              'Embalses': {'freq': ['Diaria'],
                           'Diaria': {'var': {'Volumen Util Diario en Energia': ['VoluUtilDiarEner', 1],
                                              'Capacidad Util Diaria en Energia': ['CapaUtilDiarEner', 1]
                                             },
                                      'join_var': ['Id', 'Name', 'Date']
                                 }
                      },


              'Areas': {'freq': ['Diaria'],
                        'Diaria': {'var': {'Demanda No Atendida Programada por Área': ['DemaNoAtenProg', 0],
                                           'Demanda No Atendida No Programada por Área': ['DemaNoAtenNoProg', 0]
                                          },
                                   'join_var': ['Id', 'Name', 'Date']
                                  }
                        },

              'Subareas': {'freq': ['Diaria'],
                           'Diaria': {'var': {'Demanda No Atendida Programada por Subarea': ['DemaNoAtenProg', 1],
                                              'Demanda No Atendida No Programada por Subarea': ['DemaNoAtenNoProg', 1]
                                             },
                                      'join_var': ['Id', 'Name', 'Date']
                                      }
                          }

              }



instances = {'Recursos': {'Id': 'id', 'Values_Value1': 'tipo_despacho',
                                 'Values_Value2': 'tecnologia', 'Values_Value3': 'categoria',
                                 'Values_code':'submercado', 'datetime': 'fecha_hora',
                                 'Values_Name': 'Combustible', 'Values_code':'sub_mercado', 'Date': 'fecha'
                          },
            'Recursos_Combinados':{'Id': 'id', 'Values_Name':'sub_mercado', 'Values_code': 'Combustible'},
            'Agentes': {'Id': 'id', 'Values_code':'submercado', 'datetime': 'fecha_hora'},
            'Sistema': {'Id': 'id',  'datetime': 'fecha_hora', 'Date': 'fecha'},
            'Rios': {'Id': 'id', 'Name': 'nombre','Date': 'fecha'},
            'Embalses': {'Id': 'id', 'Name': 'nombre', 'Date': 'fecha'},
            'Areas': {'Id': 'id', 'Name': 'nombre', 'Date': 'fecha'},
            'Subareas': {'Id': 'id', 'Name': 'nombre', 'Date': 'fecha'}
            }

tiempos = {'Values_Hour01': '00:00:00', 'Values_Hour02': '00:01:00',
           'Values_Hour03': '00:02:00', 'Values_Hour04': '00:03:00',
           'Values_Hour05': '00:04:00', 'Values_Hour06': '00:05:00',
           'Values_Hour07': '00:06:00', 'Values_Hour08': '00:07:00',
           'Values_Hour09': '00:08:00', 'Values_Hour10': '00:09:00',
           'Values_Hour11': '00:10:00', 'Values_Hour12': '00:11:00',
           'Values_Hour13': '00:12:00', 'Values_Hour14': '00:13:00',
           'Values_Hour15': '00:14:00', 'Values_Hour16': '00:15:00',
           'Values_Hour17': '00:16:00', 'Values_Hour18': '00:17:00',
           'Values_Hour19': '00:18:00', 'Values_Hour20': '00:19:00',
           'Values_Hour21': '00:20:00', 'Values_Hour22': '00:21:00',
           'Values_Hour23': '00:22:00', 'Values_Hour24': '00:23:00'
           }




def queryToTable(var, index, sd, ed, freq):

    query = ReadDB() # Conect with the API
    d = query.request_data(var, index, sd, ed) # Do QUERY
    if len(d.columns) == 0: # Notify if a QUERY does not generate data
        print(f'No existen datos de {var} para estas fechas')
    else: # If QUERY generate data
        # Verify frequency
        if freq == 'Horaria':
            value_vars = list(d.loc[:, 'Values_Hour01':'Values_Hour24'])
            id_vars =[x for x in d.columns if x not in value_vars]
            d = d.melt(id_vars=id_vars, value_vars=value_vars,
                       var_name='Hour', value_name=var)
            d[var] = pd.to_numeric(d[var])

        if freq == 'Diaria':
            d = query.request_data(var, index, sd, ed)
            d[var] = pd.to_numeric(d['Value'])
            d = d.drop(['Value'], axis=1)

    return d

def joinInfo(item_list, sd, ed, freq, join_var):

    d = pd.DataFrame()
    for var in item_list:
        if len(d.columns) == 0:
            d = queryToTable(var[0], var[1], sd, ed, freq)
        else:
            df = queryToTable(var[0], var[1], sd, ed, freq)
            if len(df.columns) > 0:
                d = pd.merge(d, df, on=join_var, how='outer')

    return d


def queryConstrain(item_list, sd, ed, freq, delta, join_var):
    ed = min(dt.date.today(), ed)

    if ed-sd <= delta:
        d = joinInfo(item_list, sd, ed, freq, join_var)
    else:
        print('break')
        dm = sd + delta
        d = joinInfo(item_list, sd, ed, freq, join_var)
        sd = dm
        dm = min(sd + delta, ed)
        while  dm <= ed:
            df = joinInfo(item_list, sd, ed, freq, join_var)
            d = pd.concat([d, df], axis=0)
            sd = dm
            dm = sd + delta
    return


def replace(dict, key):
    return dict[key]



def goodNames(d, item, freq):
    if freq == 'Horaria':
        d['Time'] = d['Hour'].apply(lambda x: replace(tiempos, x))
        d['datetime'] = d['Date'] + " " + d['Time']
        d['datetime'] = pd.to_datetime(d['datetime'])
        d = d.drop(['Hour'], axis=1)
        d = d.drop(['Time'], axis=1)
        d = d.drop(['Date'], axis=1)
        if item == 'Sistema':
            d = d.drop(['Values_code'], axis=1)
    if freq == 'Diaria':
        d['Date'] = pd.to_datetime(d['Date']).dt.date

    d = d.rename(columns=instances[item])
    return d

def findData(item, item_list, sd, ed, freq, join_var):

    d = joinInfo(item_list, sd, ed, freq, join_var)
    d = goodNames(d, item, freq)

    if item == 'Recursos':
        names = pd.read_csv('https://raw.githubusercontent.com/NNE-ISA/XM_API_to_data/main/info_nombres/recursos.csv')
        vars_join = [i for i in list(names.columns) if i in list(d.columns)]
        d = pd.merge(d, names, on= vars_join, how='left')
    if item == 'Agentes':
        names = pd.read_csv('https://raw.githubusercontent.com/NNE-ISA/XM_API_to_data/main/info_nombres/agentes.csv')
        vars_join = [i for i in list(names.columns) if i in list(d.columns)]
        d = pd.merge(d, names, on= vars_join, how='left')

    return d


def xmQueryAPI(item, sd, ed, freq, var=[], save=False):
    global inven_met

    if not var:
        var = list(inven_met[item][freq]['var'].keys())

    join_var = inven_met[item][freq]['join_var']
    item_list = list([inven_met[item][freq]['var'][x] for x in var])

    if save:
        d = findData(item, item_list, sd, ed, freq, join_var)
        name = item + '_' + str(sd) + '__' + str(ed) + '.csv'
        d.to_csv(name, index = False)
        print('se ha guardado la información correctamente')
    else:
        d = findData(item, item_list, sd, ed, freq, join_var)

    return d

def selectDate():
    date_input = input("use solo núeros separados por coma (no utilice espacio despues de la comm); año,mes,día: ")
    date = date_input.split(',')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    date = dt.date(year, month, day)
    return date



def manualQuery(save = True):
    global inven_met

    is_sd = False
    is_ed = False

    while is_sd == False:
        print("Ingrese la fecha inicial de la consulta")
        sd = selectDate()
        print ('la fecha elegida es %s' %str(sd))
        if input('ingrese 1 para confirmar 2 para corregir: ') == '1':
            is_sd = True

    while is_ed == False:
        print("Ingrese la fecha final de la consulta")
        ed = selectDate()
        print ('la fecha elegida es %s' %str(ed))
        if input('ingrese 1 para confirmar 2 para corregir: ') == '1':
            is_ed = True


    items = list(inven_met.keys())
    tx = 'selecione la instancia ingresando el numero correspondiente =>      '
    tx1 = str([item+': '+str(items.index(item)) for item in items]) + ': '
    item = items[int(input(tx+tx1))]
    freqs = inven_met[item]['freq']
    tx2 = str([freq+': '+str(freqs.index(freq)) for freq in freqs])+ ': '
    freq = freqs[int(input(tx+tx2))]
    vbs = list(inven_met[item][freq]['var'].keys())
    tx3 = str([var+': '+str(vbs.index(var)) for var in vbs])+ ': '
    var = input(tx+tx3)

    ed = min(ed, dt.date.today())

    if var:
        var = [vbs[int(i)] for i in var.split(',')]
    else:
       var = []

    print('\nSe realizara la consulta de %s \nde las varaibles: %s, \ncon una frecuencia %s' %(item, var, freq))

    d = xmQueryAPI(item, sd, ed, freq, var=var, save=save)

    return d

def main():
    data = manualQuery()
    print('\nPROCESO TERMINADO\n')

if __name__ == '__main__':
    main()