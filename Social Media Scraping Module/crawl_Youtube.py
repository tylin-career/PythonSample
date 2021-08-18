import json
import urllib.request, urllib.parse, urllib.error # Read website
import ssl
from datetime import date
import csv

def write_to_csv(table):
    with open("US_youtube_trending_data.csv", "a+", encoding='utf-8-sig', newline='') as file:
        write = csv.writer(file) 
        write.writerows(table)
        
def get_apiKey(api_path):
    with open(api_path, 'r') as file:
        api_key = file.readline()

    return api_key


today = date.today()
today = today.strftime("%Y-%m-%d" + "T00:00:00Z")

#'just do them'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode=US&maxResults=50&key=AIzaSyCG4tOuQgQ1SFILDtkDG5RVUuaGahaV-wU"

table = list()
comments_disabled = False
ratings_disabled = False

html = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(html)
info = data['items']

for thing in info:
    # We can assume something is wrong with the video if it has no statistics, often this means it has been deleted
    # so we can just skip it
    if "statistics" not in thing:
        continue
    video_id = thing['id']
    title = thing['snippet']['title']
    publishedAT = thing['snippet']['publishedAt']
    channelID = thing['snippet']['channelId']
    channelTitle = thing['snippet']['channelTitle']
    categoryId = thing['snippet']['categoryId']
    trending_date = today
    
    if 'tags' in thing['snippet']:
        tag = thing['snippet']['tags']
    else:
        tag = ''
    
    view_Count = thing['statistics']['viewCount']
    # print('viewCount = ', thing['statistics']['viewCount'])
    if 'likeCount' in thing['statistics'] and 'dislikeCount' in thing['statistics']:
        likes = thing['statistics']['likeCount']
        dislikes = thing['statistics']['dislikeCount']
    else:
        ratings_disabled = True
        likes = 0
        dislikes = 0
    
    if 'commentCount' in thing['statistics']:
        comment_count = thing['statistics']['commentCount']
    else:
        comments_disabled = True
        comment_count = 0

    thumbnails = thing['snippet']['thumbnails']['default']['url']
    description = thing['snippet']['description'].replace('\n','')
    
    data_list = [video_id, title, publishedAT, channelID, channelTitle, categoryId, trending_date, tag, view_Count, 
            likes, dislikes, comment_count, thumbnails, comments_disabled, ratings_disabled, description]


    table.append(data_list)

if 'nextPageToken' in data:
    pageToken = data['nextPageToken']
else:
    print('haha')
# print(pageToken)


url = url+'&pageToken='+pageToken
print(url)

# write_to_csv(table)





