# YoutubeVideoSearch
A Small Search engine which searches Youtube.com for videos and saves it to Database

## Prerequisites
Python 3.6+
UNIX operating System
    
### How To Run?
1. Create a Virtual env as `python3 -m venv <VIRTUAL_ENV_NAME>`
    - Change directory to the env `cd <VIRTUAL_ENV_NAME>`
2. Clone the Repository inside Virtual environment :-  `git clone git@github.com:programmeranand/YoutubeVideoSearch.git`
    - Activate virtual environment `source bin/activate`
    - Change Directory to cloned repo `cd YoutubeVideoSearch`
     
3. Install Requirements file  :- `pip install -r requirements.txt`
4. Run Migrations `python3 manage.py migrate`
5. Create Super User in DB :- `python3 manage.py createsuperuser`
    - Enter username and Password
6. Adding Credentials :-
    - Run the server :- `python3 manage.py runserver`, server will run at :-  http://127.0.0.1:8000/
    - Open `http://127.0.0.1:8000/admin/videosearch/setting/` and add following credentials
        * FETCH_VIDEO_KEYWORDS :- Enter Keyword to search for e.g `Programming`
        * FETCH_VIDEO_MAX_RESULTS :- Max Results to Fetch from Youtube Data API V3 e.g `30`
        * FETCH_VIDEO_PUBLISHED_AFTER :- Timestamp in ISO Format, e.g `2019-01-01T00:00:00`
        
    - Add Youtube Data API credentials :- 
        * Open `http://127.0.0.1:8000/admin/integrations/youtubecredentials/`
        * Add API_Key, and set is_active to True by clicking on it
     
    Exit the Server by Pressing Ctrl+C
           
7. Adding the CRON JOB Scheduling :- `python3 manage.py crontab add`
8. Running the Server :- `python3 manage.py runserver`
        
### How to Check Videos?
1. Check Objects in DB :- `http://127.0.0.1:8000/admin/videosearch/youtubevideo/`
2. Using GET API request :- `http://127.0.0.1:8000/videos/`
    
### NOTE 
1. Kindly Enter only valid API Credentials ans set `is_active` to True
2. For issues Throw and Email to `ankit.anand.95@gmail.com`