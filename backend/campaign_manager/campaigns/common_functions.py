from .models import Campaign, MessageInfo
from bs4 import BeautifulSoup


domain = "http://127.0.0.1:8000"

def get_unsubscribe(campaign_id,message_id):
    unsub_link = f'{domain}/api/campaign/unsub_email/{campaign_id}/{message_id}/'
    return unsub_link

def check_unsubscribe(campaign_id,message_id):
    campaign_obj = Campaign.objects.get(id=campaign_id)
    message_obj = MessageInfo.objects.get(id=message_id)
    if message_obj.unsubscribe == "no":
        campaign_obj.unsubscribed += 1
    message_obj.unsubscribe = "yes"
    campaign_obj.save()
    message_obj.save()

def get_click_links(campaign_id,message_id,link):
    campaign_obj = Campaign.objects.get(id=campaign_id)
    try:
        with open(campaign_obj.redirect_urls,'r') as f:
            redirect_urls = f.read()
    except:
        redirect_urls = ''
    if redirect_urls != '':
        redirect_urls = redirect_urls.split("|")
        if link in redirect_urls:
            for i in range(len(redirect_urls)):
                if link == redirect_urls[i]:
                    number = i
        else:
            number = len(redirect_urls)
            redirect_urls.append(link)
    else:
        number = 0
        redirect_urls = []
        redirect_urls.append(link)
    with open(campaign_obj.redirect_urls,'w') as f:
        a = "|".join(redirect_urls)
        f.write(a)
    redirect_link = f'{domain}/api/campaign/click/{campaign_id}/{message_id}/{number}/'
    return redirect_link

def process_click_links(campaign_id,message_id,number):
    campaign_obj = Campaign.objects.get(id=campaign_id)
    message_obj = MessageInfo.objects.get(id=message_id)
    if message_obj.clicks == 0:
        campaign_obj.clicked += 1
    message_obj.clicks += 1
    campaign_obj.save()
    message_obj.save()
    with open(campaign_obj.redirect_urls,'r') as f:
        redirect_urls = f.read()
        redirect_urls = redirect_urls.split("|")
    return redirect_urls[number]

def get_open_id(campaign_id,message_id):
    link = f'{domain}/api/campaign/open/{campaign_id}/{message_id}/'
    return link

def process_open_id(campaign_id,message_id):
    campaign_obj = Campaign.objects.get(id=campaign_id)
    message_obj = MessageInfo.objects.get(id=message_id)
    if message_obj.opens == 0:
        campaign_obj.opened += 1
    message_obj.opens += 1
    campaign_obj.save()
    message_obj.save()


def change_message(campaign_id,message_id,message):
    message = "<html><body>" + message + "</body></html>"
    soup = BeautifulSoup(message,'html')
    a_tag = soup.find_all('a')

    for i in a_tag:
        link = get_click_links(campaign_id,message_id,i['href'])
        i['href'] = link

    link = get_open_id(campaign_id,message_id)
    soup.find('body').append(soup.new_tag('img', src=link, style="height:1px; width:1px;"))

    return str(soup)


def add_unsub_link(campaign_id,message_id,message):
    tag = ""
    soup = BeautifulSoup(tag,'html')

    link = get_unsubscribe(campaign_id,message_id)
    tag = soup.new_tag('a', href=link)
    tag.string = "Unsubscribe"
    tag = str(tag)

    message = message.replace("{ link }",tag)

    return message