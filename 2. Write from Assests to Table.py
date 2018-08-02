from azure.storage.blob import BlockBlobService
import pyodbc
import re
import datetime

account_name = "enter account name"
account_key = "enter account key"


blob_login = BlockBlobService(account_name=account_name, account_key=account_key)
generator = blob_login.list_blobs('images')



for kpis_data in data:
    kpis_date = kpis_data[0]

    for blob in generator:
        blob_name = blob.name
        image_url = blob_login.make_blob_url('images', blob_name)

        if "/TBS_EMAIL/" in image_url:
            em_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
            em_date_match = em_regex.search(image_url)
            em_date_match = em_date_match.group()
            date_match = em_date_match +' '+'00:00:00'

            if str(kpis_date) in str(date_match):
    
                print ("em_update", image_url, date_match)
            else:
                pass

        elif "/TBS_SOCIAL_FB/" in image_url:
            fb_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
            fb_date_match = fb_regex.search(image_url)
            fb_date_match = fb_date_match.group()
            date_match = fb_date_match +' '+'00:00:00'
            # print ("2")
            # print (kpis_date)
            # print (date_match)

            if str(kpis_date) in str(date_match):


                print ("fb_update", image_url, date_match)
            else:
                pass

        elif "/TBS_SOCIAL_TW/" in image_url:
            tw_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
            tw_date_match = tw_regex.search(image_url)
            tw_date_match = tw_date_match.group()
            date_match = tw_date_match +' '+'00:00:00'
            # print ("3")
            # print (kpis_date)
            # print (date_match)

            if str(kpis_date) in str(date_match):


                print ("tw_update", image_url, date_match)
            else:
                pass

        elif "/TBS/" in image_url:
            web_regex = re.compile(r'\d\d\d\d\w\w\w\d\d')
            web_date_match = web_regex.search(image_url)
            web_date_match = web_date_match.group()
            web_date_match = datetime.datetime.strptime(str(web_date_match), '%Y%b%d').strftime('%Y-%m-%d')
            date_match = web_date_match + ' ' + '00:00:00'
            # print ("4")
            # print (kpis_date)
            # print (date_match)



# Update view table

    social_fulfilled = 'Y'

    print ("updated Y", kpis_date)





