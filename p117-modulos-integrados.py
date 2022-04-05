
import os
import datetime, calendar
# Algunas funciones del modulo os de pyhon
os.system('clear')
print(f'\nSistema operativo: \n{os.uname()}')
print(f'\nDirectorio actual: \n{os.getcwd()}')
print('\nListado de archivos en el directorio raiz:')
os.chdir('/')
print(os.listdir())
print('\nVariables de entorno: ')
print(os.environ)
print(f"\nRuta de ejecucion : \n{os.getenv('PATH')}")
# Algunas funciones del modulo datetime
ahora = datetime.datetime.now()
print('\nLa fecha y hora actuales:', ahora)
print('\nLa fecha actual :', ahora.strftime('%b / %d / %Y'))
print('\nLa hora actual :', ahora.strftime('%H:%M'))
# Algunas funciones del modulo calendar
print('\nCalendario 2022: \n')
calendar.prcal(2022)
print('\nMes abril 2022: \n')
calendar.prmonth(2022,4)