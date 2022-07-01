from datetime import datetime
import pytz

def get_hora(zona_horaria, fecha = ['d', 'm', 'Y'] , hora = ['H', 'M', 'S']):
    zona = pytz.timezone(zona_horaria)
    now_zone = datetime.now(zona)
    zona_print = ''
    i = 0
    for imp in fecha:
        zona_print += now_zone.strftime(f'%{imp}') + '/'
    zona_print = zona_print[:-1] + ' '
    
    for imp in hora:
        zona_print += now_zone.strftime(f'%{imp}') + ':'
    zona_print = zona_print[:-1] + ' '
    return zona_print

def main():
    bogota = get_hora('America/Bogota')
    mexico = get_hora('America/Mexico_City', fecha = [])
    korea = get_hora('Asia/Seoul', fecha = ['Y', 'm', 'd'])
    madrid = get_hora('Europe/Madrid', fecha = ['m', 'd', 'Y'], hora = ['H', 'M'])

    print(f'Bogota: {bogota}')
    print(f'Mexico: {mexico}')
    print(f'Korea: {korea}')
    print(f'Madrid: {madrid}')
    
if __name__ == '__main__':
    main()