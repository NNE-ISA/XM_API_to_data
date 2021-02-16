import xm_query as xq
import datetime as dt
import os


def selectDate():
    date_input = input("use solo núeros separados por coma (no utilice espacio despues de la comm); año,mes,día: ")
    date = date_input.split(',')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    date = dt.date(year, month, day)
    return date

def selectPhat():
    exist_phat = False
    while exist_phat == False:
        phat = input(input('ingrese la dirección de la carpeta donde quiere guardar la información'))
        try:
            os.chdir(phat)
        except:
            phat = os.getcwd()
            print('La dirección ingresada no es valida se utilizará el disco %s por defecto' % phat)
            os.chdir(phat)
        print('La información se guardará en %s' % os.getcwd())
        if input('ingrese 1 para confirmar y 2 para volver a ingresar la dirección: ') == '1':
            exist_phat = True
    return phat

def manualQuery():
    inven_met = xq.inven_met

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

    phat = selectPhat()

    d = xq.xmQueryAPI(item, sd, ed, freq, var=var, phat=phat, save=True)

    return d






def main():
    manualQuery()
    print('\nPROCESO TERMINADO\n')

if __name__ == '__main__':
    main()