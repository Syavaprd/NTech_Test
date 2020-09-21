Здесь находится решение 2-ой задачи тестового задания. <br/>
4: Подготовка данных. Я использовал ImagdeDataGenerator для аугментации, и функцию efficient_net.preprocess_input для преобразования картинки. <br/>
Обучающую выборку поделил на 80% обучающей и 20% валидационной. Все фотографии приводил к (260, 260, 3) размеру. Архитектуру использовал EfficientNetB2 так, как <br/>
это SOTA архитектура, у нее высокая точность и мало параметров. EfficientNet в своей реализации использует MobileNet блоки. Имплементация MobileNet_v3 есть у меня  на github <br/>
![alt text](https://github.com/Syavaprd/NTech_Test/blob/master/Task%202/ntech_image.png) <br/>
https://arxiv.org/abs/1905.11946  <br/>
Функция train_classifier(img_dir, epochs, batch_size, num_classes = 2, fast_train=False) принимает директорию, где лежат фотографии разбитые по папкам (классам), <br/>
epochs - кол-во эпох, batch_size - кол-во сэмплов в батче, num_classes - кол-во классов. fasr_train, если True, то очень быстро обучится (для тестирования функции). <br/>
Результаты на валидации - 97% <br/>
Обученную модель можно скачать, по ссылке https://drive.google.com/file/d/1mbuQ_G2FKSwR9ON96Sxp8jX9yzZdW24N/view?usp=sharing <br/>
Для скрипта classify.py нужно передать в аргументах директорию файла с моделью и путь к папке. Функция сохранит json файл в той же директории, где и она сама.

Запуск тренировки просто подразумевает вызов функции train_classifier(img_dir, epochs, batch_size, num_classes = 2, fast_train=False)

