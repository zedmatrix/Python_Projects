"""
    Date Helper Function returns prints formatted date
"""

def dash(symbol='=', count=40):
    return f"{symbol * count}"

def Display(latest):
    try:
        title = latest["title"].strip()
        published = latest["published"]
        media = latest["media_content"]
        url = media[0]['url']
        print(dash())
        print(f'Title: {title}')
        print(f'Published: {published}')
        print(f'URL: {url}')
        print(f'Rating: {latest.rating}')
        print(f'Credit: {latest.credit}')
        print(dash(symbol='_', count=50))
    except Exception as e:
        print(f"Error in Display function: {e}")

def WritePodcast(FIND: str, REPLACE: str, save_dir, latest):
    try:
        print(FIND, REPLACE)
        title = latest["title"].strip()
        new_title = title.replace(FIND, REPLACE)
        media = latest["media_content"]
        url = media[0]['url']
        outdir = f"$HOME/Videos/Youtube/Podcasts/{save_dir}"
        outfile = f'yt-dlp {url} \\\n-P {outdir} \\\n-o "{new_title}.mp4"'
        with open('youtube.sh', "a") as myfile:
            myfile.write(f"[ ! -d {outdir} ] && mkdir -v {outdir}\n")
            myfile.write(f"{outfile}\n")

    except Exception as e:
        print(f"Error in WritePodcast function: {e}")
