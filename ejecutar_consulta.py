import pandas as pd
import datetime as dt
import xm_query as xq

def main():
    data = xq.manualQuery()
    print('\nRESULTADO: \n')
    return data

if __name__ == '__main__':
    main()