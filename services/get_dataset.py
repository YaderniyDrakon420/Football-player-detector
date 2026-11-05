#автоматичне скачування необхідних малюнків
import os
from icrawler.builtin import BingImageCrawler


def download_data(search_queries):
    # 1. Твої запити для пошуку (можна писати українською або англійською)
    # Англійською мовою Google/Bing зазвичай знаходять більше якісних фото


    # Кількість фоток для кожного запиту (поки що поставимо по 15, щоб зібрати ~90 фото)
    # За бажанням можеш збільшити це число
    max_images_per_query = 15

    print("Запуск робота-збирача фотографій ведмедя...")

    # 2. Цикл, який проходить по кожному запиту
    for folder_name, query_text in search_queries.items():
        # Створюємо шлях до папки, наприклад: dataset/polar_owl
        output_directory = f"../dataset/{folder_name}"

        # Перевіряємо, якщо папки немає — створюємо її
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        print(f"\n Шукаю та завантажую для: '{query_text}' -> у папку {output_directory}")

        # 3. Налаштовуємо пошуковий робот (використовуємоBing, бо він менше блокує скрипти)
        crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': output_directory})

        # Стартуємо завантаження
        crawler.crawl(keyword=query_text, max_num=max_images_per_query)
        for i, filename in enumerate(os.listdir(output_directory), start=1):
            old_path = os.path.join(output_directory, filename)
            new_path = os.path.join(output_directory, f"{folder_name}_{i}.jpg")
            os.rename(old_path, new_path)

    print("\n Ура! Робот закінчив роботу. Перевіряй папку 'dataset' у своєму проекті!")


search_queries = {
        # "polar_owl": "полярная сова, арктическая сова",
        # "barn_owl": "barn owl сова сипуха",
        # "owl_in_forest": "сова на дереве",
        # "owl_close_up": "сова крупным планом",
        # "toy_owl": "игрушечная сова, сова из аниме",
        # "cartoon_owl": "сова из мультика, из мультфильма сова"
        # "cartoon" : "Tom and Jerry",
        "bears": "bear",
    }
if __name__ == "__main__":
    download_data(search_queries)