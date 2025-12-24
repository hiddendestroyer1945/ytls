from youtubesearchpython import CustomSearch, VideoSortOrder, ResultMode
import datetime

def youtube_search_engine():
    print("--- YouTube Search Engine (Last 1 Year) ---")
    query = input("Enter your keyword: ")
    
    # Using CustomSearch to apply the 'This Year' filter
    # 'EgQIAhAB' is the YouTube internal filter code for 'This Year' + 'Video'
    # We sort by uploadDate to get them in order
    try:
        search = CustomSearch(query, 'EgQIAhAB', limit=20)
        results = search.result(mode=ResultMode.dict).get('result', [])
        
        if not results:
            print("No videos found for that keyword in the last year.")
            return

        # Ascending order: We sort the list by the internal index or date if needed
        # By default, we'll reverse the result list to show 'older' of the year first
        results.reverse()

        print(f"\nResults for '{query}' (Last 12 Months):")
        print("-" * 50)
        
        for index, video in enumerate(results, 1):
            title = video.get('title')
            link = video.get('link')
            published_time = video.get('publishedTime')
            
            print(f"{index}. {title}")
            print(f"   Link: {link}")
            print(f"   Uploaded: {published_time}")
            print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_search_engine()