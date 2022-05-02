import xlsxwriter
from bs4 import BeautifulSoup

out_xlsx = 'ColdCase.xlsx'
# out_xlsx = 'Container02.xlsx'
# out_xlsx = 'Sport.xlsx'
# out_xlsx = 'Uma.xlsx'
# out_xlsx = 'Repair.xlsx'
# out_xlsx = 'Sortavala.xlsx'

with open("ColdCase.html", encoding='utf-8') as fp:
# with open("Container02.html", encoding='utf-8') as fp:
# with open("Sport.html", encoding='utf-8') as fp:
# with open("Uma.html", encoding='utf-8') as fp:
# with open("Repair.html", encoding='utf-8') as fp:
# with open("Sortavala.html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, "html.parser")
link = soup.find_all('div', class_='_3SLg2')
link1 = soup.find_all('div', class_='_1lBa-')


d = []

for i in link:

    a = 'Повысить мощность кулеров, проверить работу кулеров, заменить термопасту, заменить кулеры'
    b = 'Проверить, если риг есть но он неработает, то запустить, если рига нет удалить из базы'
    c = 'Проверить наличие карты, если есть проверить ' \
        'работу карты, проверить питание карты (карт), заменить рейзер. В крайнем случае отправить карту на диагностику'
    e = 'Перезагрузить, понизить разгон, если не помогло, убрать разгон. Проверить карту на месте.'
    damage1 = 'Не в сети'
    damage2 = 'Высокая температура'
    damage3 = 'Не майнит одна или несколько карт (красный квадратик)'
    damage4 = 'Низкий хешрейт, уснула одна или несколько карт'
    damage5 = 'В сети, но не майнит'
    done = 'Повысил скорость куллера'
    done1 = 'Перезагрузил'
    done2 = 'Перезагрузил. Понизил разгон. На контроле.'

    comp = i.find('span', class_='_2eLpa').text
    comp1 = i.find('span', class_='dXZrd').text
    gpu = i.find_all('span', class_='_13cP- _1g0Tq')
    text = i.find('a', class_='ESArK').text.strip()

    if gpu:
        print(f'{text} - {c}')
        item = {
            'Номер рига': text,
            'Неисправность': damage3,
            'Что требуется сделать': c,
            'Что сделано': '',
        }
        d.append(item)

    elif comp == "Низкий коэффициент":
        continue

    elif comp == "Высокая температура":
        print(f'{text} - {comp} - {a}')
        item = {
            'Номер рига': text,
            'Неисправность': damage2,
            'Что требуется сделать': a,
            'Что сделано': done,
        }
        d.append(item)

    elif comp1 == '-- --':
        print(f'{text} - {comp}')
        item = {
            'Номер рига': text,
            'Неисправность': damage5,
            'Что требуется сделать': '',
            'Что сделано': done1,
        }
        d.append(item)

    elif comp == "Не в сети":
        print(f'{text} - {comp} - {b}')
        item = {
            'Номер рига': text,
            'Неисправность': damage1,
            'Что требуется сделать': b,
            'Что сделано': '',
        }
        d.append(item)

    elif comp == "Низкий хешрейт":
        print(f'{text} - {comp} - {e}')
        item = {
            'Номер рига': text,
            'Неисправность': damage4,
            'Что требуется сделать': e,
            'Что сделано': done2,
        }
        d.append(item)

    elif comp == '':
        print(text)
        item = {
            'Номер рига': text,
            'Неисправность': '',
            'Что требуется сделать': '',
            'Что сделано': '',
        }
        d.append(item)


def main():
    with xlsxwriter.Workbook(out_xlsx) as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        header = ['НОМЕР РИГА', 'НЕИСПРАВНОСТЬ', 'ЧТО ТРЕБУЕТСЯ СДЕЛАТЬ', 'ЧТО СДЕЛАНО']
        for col, h in enumerate(header):
            ws.write_string(0, col, h, cell_format=bold)
        for row, items in enumerate(d, start=1):
            ws.write_string(row, 0, items['Номер рига'])
            ws.write_string(row, 1, items['Неисправность'])
            ws.write_string(row, 2, items['Что требуется сделать'])
            ws.write_string(row, 3, items['Что сделано'])


if '__main__' == __name__:
    main()
