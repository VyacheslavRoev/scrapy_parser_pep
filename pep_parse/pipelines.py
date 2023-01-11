import csv
from collections import defaultdict

from .settings import BASE_DIR
from .utils import now_formatted


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = defaultdict(int)

    def process_item(self, item, spider):
        self.counter[''.join(item['status'])] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / "results"
        try:
            results_dir.mkdir(exist_ok=True)
        except FileExistsError:
            print('Невозможно создать папку')
        file_name = f"status_summary_{now_formatted}.csv"
        file_path = results_dir / file_name
        result = [("Статус", "Количество")]
        try:
            result.extend(self.counter.items())
        except Exception:
            print('Не найдены статусы PEP')
        total = sum(self.counter.values())
        try:
            result.append(("Total", total))
        except Exception:
            print('Невозможно посчитать общее количество статусов')
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                writer = csv.writer(f, dialect='unix')
                writer.writerows(result)
        except FileNotFoundError:
            print('Файл не создан')
        self.counter.clear()
