import requests
import datetime

# Фиксируем и выводим время старта работы кода
start = datetime.datetime.now()
print('Время старта: ' + str(start)[11:])

# URL и заголовки для запроса
API_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"
headers = {"Authorization": "Bearer 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"}


# Функция для отправки запроса
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


# Запрос изображения на основе текстового описания
image_bytes = query({
    "inputs": "Big city at night",
})


# Доступ к изображению
import io
from PIL import Image

image = Image.open(io.BytesIO(image_bytes))

# Сохраняем изображение на диск
image.save("output.png")

# Отображаем изображение
image.show()

# Фиксируем и выводим время окончания работы кода
finish = datetime.datetime.now()
print('Время окончания: ' + str(finish)[11:])

# Вычитаем время старта из времени окончания
print('Время работы: ' + str(finish - start))
