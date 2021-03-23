import pandas as pd
from celery import shared_task
from .models import contactList, Contact
import os

@shared_task(name="save_list_toDb")
def save_list_toDb(cfile,list_id,emailfield,first_name,last_name,ref,desc,add,bank,ph):
    df = pd.read_csv(f"D:/capstone/app/backend/campaign_manager/{cfile}")
    obj = contactList.objects.get(id=list_id)
    length = len(df[emailfield])
    for i in range(length):
        objs = Contact.objects.filter(email=df.iloc[i][emailfield])
        if len(objs) == 0:
            cobj = Contact.objects.create(user = obj.user,email = df.iloc[i][emailfield])
            try: 
                cobj.first_name = df.iloc[i][first_name]
            except:
                pass
            try: 
                cobj.last_name = df.iloc[i][last_name]
            except:
                pass
            try: 
                cobj.mobile = df.iloc[i][ph]
            except:
                pass
            try: 
                cobj.address = df.iloc[i][add]
            except:
                pass
            try: 
                cobj.bank = df.iloc[i][bank]
            except:
                pass
            try: 
                cobj.ref = df.iloc[i][ref]
            except:
                pass
            try: 
                cobj.desc = df.iloc[i][desc]
            except:
                pass
            cobj.save()
            obj.contact.add(cobj)
            obj.save()
        else:
            obj.contact.add(objs[0])
            obj.save()
    
    if os.path.isfile(cfile):
        os.remove(cfile)
