from pydataxm import ReadDB
import pandas as pd
import datetime as dt

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


def xmQueryAPI(item, sd, ed, freq, var=[], phat='./', save=False):
    global inven_met

    print('Se inicia la consulta')

    if not var:
        var = list(inven_met[item][freq]['var'].keys())

    join_var = inven_met[item][freq]['join_var']
    item_list = list([inven_met[item][freq]['var'][x] for x in var])

    if save:
        d = findData(item, item_list, sd, ed, freq, join_var)
        name = phat + '\\' + item + '_' + str(sd) + '__' + str(ed) + '.csv'

        try:
            d.to_csv(name, index = False)
        except:
            name = name.replace('\\','/')
            d.to_csv(name, index = False)

        print('se ha guardado la información correctamente')
    else:
        d = findData(item, item_list, sd, ed, freq, join_var)
        print('Se ha consultado al informaciónc on exito')
    return d