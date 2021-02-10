from pydataxm import ReadDB
import pandas as pd


instances = {'Recursos': {'Freq':['Horaria', 'Diaria']},
            'Recursos_Combinados':{'Freq':['Horaria']},
            'Agentes': {'Freq':['Horaria']},
            'Sistema': {'Freq':['Horaria', 'Diaria']},
            'Rios': {'Freq':['Diaria']},
            'Embalses': {'Freq':['Diaria']},
            'Areas': {'Freq':['Diaria']},
            'Subareas': {'Freq':['Diaria']}
            }

data_dict = {'Hour':
                        {'Recursos': [['GeneIdea', 1], ['Gene', 1], ['ConsCombustibleMBTU', 0], ['PrecOferDesp', 0],
                                      ['EmisionesCO2Eq', 0], ['GeneSeguridad', 0], ['GeneFueraMerito', 0],
                                      ['Id', 'Values_code', 'Date', 'Hour']],

                        'Recursos_Combinados': [['ConsCombAprox', 0], ['EmisionesCO2', 0], ['EmisionesCH4', 0],
                                                ['EmisionesN2O', 0], ['Id', 'Values_code', 'Values_Name',
                                                                      'Date', 'Hour']],

                        'Agentes': [['DemaCome', 1], ['VentContEner', 1], ['CompContEner', 1], ['CompBolsNaciEner', 1],
                                    ['DemaOR', 0], ['Id', 'Values_code', 'Date', 'Hour']],

                        'Sistema': [['Gene', 0], ['GeneIdea', 0], ['DemaCome', 0], ['PrecBolsNaci', 0],
                                    ['MaxPrecOferNal', 0], ['RestAliv', 0], ['VentContEner', 0], ['VentContEner', 0],
                                    ['CompContEner', 0], ['CompBolsNaciEner', 0], ['factorEmisionCO2e', 0],
                                    ['ImpoEner', 0], ['PerdidasEner', 0], ['Id', 'Values_code', 'Date', 'Hour']]},

               'Day':
                        {'Recursos': [['ObligEnerFirme', 0], ['Id', 'Code', 'Date']],

                         'Rios': [['AporEner', 1], ['AporEnerMediHist', 1], ['Id', 'Name', 'Date']],

                         'Embalses': [['VoluUtilDiarEner', 1], ['CapaUtilDiarEner', 1], ['Id', 'Name', 'Date']],

                         'Areas': [['DemaNoAtenProg', 0], ['DemaNoAtenNoProg', 0], ['Id', 'Name', 'Date']],

                         'Subareas': [['DemaNoAtenProg', 1], ['DemaNoAtenNoProg', 1], ['Id', 'Name', 'Date']],

                         'Sistema': [['AporEner', 0], ['PrecEscaAct', 0], ['RemuRealIndiv', 0], ['PrecPromContRegu', 0],
                                     ['PrecPromContNoRegu', 0], ['VoluUtilDiarEner', 0], ['DemaSIN', 0],
                                     ['CapaUtilDiarEner', 0], ['AporEnerMediHist', 0], ['FAZNI', 0], ['PRONE', 0],
                                     ['FAER', 0], ['Id', 'Date']]}
                }


def queryToTable(var, index, sd, ed, freq):

    query = ReadDB() # Conect with the API
    d = query.request_data(var, index, sd, ed) # Do QUERY
    if len(d.columns) == 0: # Notify if a QUERY does not generate data
        print(f'No existen datos de {var} para estas fechas')
    else: # If QUERY generate data
        # Verify frequency
        if freq == 'Hour':
            value_vars = list(d.loc[:, 'Values_Hour01':'Values_Hour24'])
            id_vars =[x for x in d.columns if x not in value_vars]
            d = d.melt(id_vars=id_vars, value_vars=value_vars,
                       var_name="Hour", value_name=var)
            d[var] = pd.to_numeric(d[var])
        if freq == 'Day':
            d = query.request_data(var, index, sd, ed)
            d[var] = pd.to_numeric(d['Value'])
            d = d.drop(['Value'], axis=1)

    return d


def joinInfo(list_item, sd, ed, freq):

    d = pd.DataFrame()
    for var in list_item[:-1]:
        if len(d.columns) == 0:
            d = queryToTable(var[0], var[1], sd, ed, freq)
        else:
            df = queryToTable(var[0], var[1], sd, ed, freq)
            if len(df.columns) > 0:
                d = pd.merge(d, df, on=list_item[-1], how='outer')

    return d


def xmQueryAPI(item, sd, ed, freq):
    global data_dict
    d = joinInfo(data_dict[freq][item], sd, ed, freq)
    d['Date'] = pd.to_datetime(d['Date']).dt.date
    return d