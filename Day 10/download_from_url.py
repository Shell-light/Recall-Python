import os
import requests
import shutil
from download_util import download_file
THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOADS_DIR, '1.jpg')
url = "https://www.wta.org/site_images/hikes/boardman-lake-summer-hulk.jpg/@@images/37bc753a-631e-458c-b841-8512653aea4e.jpeg"

# a smallish iteam
r = requests.get(url, stream=True)
r.raise_for_status()
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)


# dl_filename = os.path.basename(url)
# new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)
# with requests.get(url, stream=True) as r:
#     with open(new_dl_path, 'wb') as file_obj:
#         shutil.copyfileobj(r.raw, file_obj)


download_file(url, DOWNLOADS_DIR)