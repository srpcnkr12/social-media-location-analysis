import pandas as pd

def load_instagram_data(liked_comments_path, liked_posts_path):
    # Load Instagram liked comments
    liked_comments = pd.read_json(liked_comments_path)
    comments_list = []
    for entry in liked_comments["likes_comment_likes"]:
        for data in entry["string_list_data"]:
            comments_list.append({
                "platform": "Instagram",
                "interaction": "Liked Comment",
                "timestamp": pd.to_datetime(data["timestamp"], unit='s'),
                "url": data["href"]
            })
    liked_comments_df = pd.DataFrame(comments_list)

    # Load Instagram liked posts
    liked_posts = pd.read_json(liked_posts_path)
    posts_list = []
    for entry in liked_posts["likes_media_likes"]:
        for data in entry["string_list_data"]:
            posts_list.append({
                "platform": "Instagram",
                "interaction": "Liked Post",
                "timestamp": pd.to_datetime(data["timestamp"], unit='s'),
                "url": data["href"]
            })
    liked_posts_df = pd.DataFrame(posts_list)

    return liked_comments_df, liked_posts_df

def load_tiktok_data(tiktok_data_path):
    # Load TikTok data
    tiktok_data = pd.read_json(tiktok_data_path)

    # TikTok comments
    comments_list = []
    for entry in tiktok_data["Activity"]["Comments"]["CommentsList"]:
        comments_list.append({
            "platform": "TikTok",
            "interaction": "Comment",
            "timestamp": pd.to_datetime(entry["date"]),
            "content": entry["comment"]
        })
    comments_df = pd.DataFrame(comments_list)

    # TikTok favorite videos
    favorites_list = []
    for entry in tiktok_data["Activity"]["Favorite Videos"]["FavoriteVideoList"]:
        favorites_list.append({
            "platform": "TikTok",
            "interaction": "Favorite Video",
            "timestamp": pd.to_datetime(entry["Date"]),
            "url": entry["Link"]
        })
    favorites_df = pd.DataFrame(favorites_list)

    return comments_df, favorites_df

def load_weather_data(weather_path):
    # Load weather data
    weather_df = pd.read_csv(weather_path)
    weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
    weather_df['date'] = weather_df['datetime'].dt.date
    return weather_df

def merge_data(instagram_comments, instagram_posts, tiktok_comments, tiktok_favorites, weather_df):
    # Filter data for 2024
    instagram_comments = instagram_comments[instagram_comments['timestamp'].dt.year == 2024]
    instagram_posts = instagram_posts[instagram_posts['timestamp'].dt.year == 2024]
    tiktok_comments = tiktok_comments[tiktok_comments['timestamp'].dt.year == 2024]
    tiktok_favorites = tiktok_favorites[tiktok_favorites['timestamp'].dt.year == 2024]

    # Combine all social media data
    combined_df = pd.concat([
        instagram_comments[['platform', 'interaction', 'timestamp']],
        instagram_posts[['platform', 'interaction', 'timestamp']],
        tiktok_comments[['platform', 'interaction', 'timestamp']],
        tiktok_favorites[['platform', 'interaction', 'timestamp']]
    ])

    combined_df['date'] = combined_df['timestamp'].dt.date

    # Merge with weather data
    merged_df = combined_df.merge(weather_df, on='date', how='left')
    return merged_df