import requests
import json

def fetch_reddit_trending():
   
    url = "https://www.reddit.com/r/popular/hot.json?limit=10"
    
    headers = {
        'User-Agent': 'MyInternshipBot/1.0 by YourName'
    }
    
    print("Fetching trending topics from Reddit (r/popular)...")
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            posts = data.get('data', {}).get('children', [])
            
            if not posts:
                print("No posts found in the response.")
                return

            print("\n--- 🔥 Top 10 Trending Posts & Topics 🔥 ---\n")
            trending_topics = set()
            
            for i, post in enumerate(posts):
                post_data = post.get('data', {})
                
                title = post_data.get('title')
                subreddit = post_data.get('subreddit')
                score = post_data.get('score')
                
                print(f"{i + 1}. Title: {title}")
                print(f"   Topic (Subreddit): r/{subreddit}")
                print(f"   Score: {score}\n")
                
                trending_topics.add(subreddit)
            
            print("-------------------------------------------------")
            print("Summary of Trending 'Hashtags' (Subreddits):")
            print(trending_topics)
            print("-------------------------------------------------")

        else:
            print(f"Error: Failed to fetch data. HTTP Status Code: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    fetch_reddit_trending()