import pandas as pd
import datetime as dt
import xm_query as xq

def main():
    data = xq.manualQuery()
    print('\nPROCESO TERMINADO\n')

if __name__ == '__main__':
    main()