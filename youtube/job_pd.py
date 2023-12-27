import pandas as pd

df = pd.read_csv('comments.csv')
df['Комментарий'] = df['Комментарий'].str.lower()
df_sorted = df.sort_values(by='Лайки', ascending=False)
filtered_comments = df_sorted[df_sorted['Комментарий'].str.contains('ивлеев|ивлев|вечери|мутаб|голой|голая|трэш|треш', case=False, na=False)]

top_100_filtered_comments = filtered_comments
for index, row in top_100_filtered_comments.iterrows():
    comment_text = row['Комментарий']
    comment_time = row['Время']
    comment_likes = row['Лайки']
    print(f"Комментарий: {comment_text}\nВремя: {comment_time}\nЛайки: {comment_likes}\n")