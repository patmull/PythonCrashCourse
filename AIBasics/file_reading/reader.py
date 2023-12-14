import csv
import os.path

FILE_PATH = 'all_posts_merged.csv'

with open(os.path.join(FILE_PATH)) as csv_file:
    file_content = csv.reader(csv_file)
    header = next(file_content)

    article_slugs = []
    for row in file_content:
        article_slugs.append(row[0])
