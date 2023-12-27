import csv

from googleapiclient.discovery import build
import TOKEN

API_KEY = TOKEN.api
VIDEO_ID = TOKEN.id_ut

youtube = build('youtube', 'v3', developerKey=API_KEY)

# Получаем информацию о видео
video_response = youtube.videos().list(
    part='snippet,statistics',
    id=VIDEO_ID
).execute()

# Получаем количество комментариев
comment_count = video_response['items'][0]['statistics']['commentCount']
print(f"Количество комментариев: {comment_count}")

# Получаем комментарии
comments_response = youtube.commentThreads().list(
    part='snippet',
    videoId=VIDEO_ID,
    textFormat='plainText',
    maxResults=comment_count  # Максимальное количество комментариев для получения (можно увеличить)
).execute()

# текст каждого комментария
# for comment in comments_response['items']:
#     comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
#     print(f"Комментарий: {comment_text}")


csv_file_path = 'comments.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Комментарий', 'Время', 'Лайки'])

    # Получаем комментарии по страницам
    next_page_token = None
    while True:
        comments_response = youtube.commentThreads().list(
            part='snippet',
            videoId=VIDEO_ID,
            textFormat='plainText',
            maxResults=100,
            order='time',
            pageToken=next_page_token
        ).execute()

        for comment in comments_response['items']:
            comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
            comment_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
            comment_likes = comment['snippet']['topLevelComment']['snippet']['likeCount']

            csv_writer.writerow([comment_text, comment_time, comment_likes])

        # Проверяем наличие следующей страницы
        next_page_token = comments_response.get('nextPageToken')
        if not next_page_token:
            break

# Выводим сообщение об успешном завершении
print(f"Комментарии сохранены в файл: {csv_file_path}")