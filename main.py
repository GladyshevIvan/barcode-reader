import os
import cv2
import zxingcpp


def barcode_decoder(file_path):
    '''Считыватель информации из штрихкода

    Принимает путь к изображению, распознает его. Если штрихкод найден, выводит результат
    Если нет, выводит сообщение, что штрихкод не найден

    Args:
         file_path (str): путь к файлу
    '''

    try:
        #Проверка существует ли файл по указанному пути
        if os.path.exists(file_path):
            #Распознание изображение
            img = cv2.imread(file_path)
            barcodes = zxingcpp.read_barcodes(img)

            #Проверка был ли распознан хотя бы один штрихкод
            if len(barcodes) == 0:
                print('Штрихкоды не найдены')
            else:
                #Штрихкодов может быть несколько, поэтому перебирается коллекция barcodes
                #И выводится информация про каждый распознанный штриход
                for barcode in barcodes:
                    print('Найден штрихкод:',
                          f'    Содержимое: "{barcode.text}"',
                          f'    Тип: {barcode.format}',
                          sep='\n')
        else:
            print('Файл не найден, пожалуйста, введите путь заново')

    except Exception as err:
        print('Что-то пошло не так...')
        print(f'Подробнее: {err}')


def request_handler():
    '''Обрабатывает запросы пользователя

    Бесконечный цикл, в котором на каждой интерации пользователь отпавляет путь к изображению штрихкода
    или вводит 0, чтобы выйти из программы
    '''

    while True:
        print('Введите путь к изображению со штрихкодом;', '0 - чтобы выйти', sep='\n')
        request = input('>')
        if request == '0':
            print('Выход из приложения')
            break
        else:
            barcode_decoder(request) #Распознание изображения


if __name__ == '__main__':
    '''Запуск программы'''
    request_handler()