# Barcode Reader

## Описание проекта (Description)

Программа для распознания штрихкодов

Barcode recognition software

## Реализованные требования (Implemented Requirements)

- Распознает изображения штрихкодов и выводит содержащуюся в них информацию;
- Если на картинке нет штрихкодов, выводит сообщение, что штрихкоды не найдены;
- Использован Docker для контейнеризации.

<!--Space-->

- Recognizes barcode images and outputs the information contained in them;
- If there are no barcodes in the picture, it displays a message that the barcodes have not been found;
- Used Docker for containerization.

## Подготовка проекта (Project preparation)
1. Перед началом работы установите Docker

2. Пропишите в консоль ```docker run``` и укажите папку из которой будете подтягивать изображения с штрихкодами, используя 

    ```bash
    docker run -it -v "Путь_к_вашей_папке":/app/input_images barcode-reader
    ```
    "Путь_к_вашей_папке" - замените на абсолютный путь к папке на вашем компьютере (например, D:\MyBarcodes)
    
    barcode-reader - имя Docker-образа приложения
    
    Пример:

    ```bash
    docker run -it -v "D:\MyBarcodes":/app/input_images barcode-reader
    ```


3. В открывшемся приложении вы можете вввести 

    ```bash
    /app/input_images/название_файла
    ```
    Далее высветится информация о вашем образе

4. Для выхода введите ```0```


<!--Space-->
##

1. Install Docker before you start

2. Write ```docker run``` to the console and specify the folder from which you will pull up images with barcodes using
    ```bash
    docker run -it -v "Path_to_your_Folder":/app/input_images barcode-reader
    ```
    
    "Path to your folder" - replace it with the absolute path to the folder on your computer (for example, D:\MyBarcodes )
    
    barcode-reader is the name of the Docker image of the application.
    
    Example:
    
   ```bash
    docker run -it -v "D:\MyBarcodes":/app/input_images barcode-reader
    ```

3. In the application that opens, you can enter 

    ```bash
    /app/input_images/file_name
    ```
    Next, information about the current image will be displayed.

4. To exit, enter ```0```

## Использованные технологии (Technology Stack)

- **Python 3.13**
- **Docker**
