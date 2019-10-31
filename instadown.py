from InstagramAPI import InstagramAPI
from requests import Session
from re import sub,findall
from sys import argv
from os import path,mkdir,system
api = InstagramAPI("USERNAME", "PASSWORD") # حط اليوزرنيم بتاع الأكونت والباسورد عادي 
try:
    assert api.login() # اسيرت دي هتشوف لو الدالة دي حصل فيها اي خطأ وترجع ايرور لو مفيش خطا البرنامج هيسجل الدخول عادي 
except:print("PASSWRD or USERNAME is incorrect\n");exit() # لو فيها خطأ هيقولك الخطأ ويطلع من البرنامج
username = argv[1] # انت عارف الكوماند دا مشلازم اقولك 
download=lambda name,url,path:open(path+name,"wb").write(Session().get(url).content) # دي فنكشن عملتها كدا بتحطلها لينك وباث و اسم وهتحمل الصورة من اللينك بس لازم يبق لينك الصورة المطلق الي بيبق اخره jpgدا 
getuserid=lambda username:sub("<|>", "", findall(">[0-9].*?<", Session().get("https://codeofaninja.com/tools/find-instagram-id-answer.php?instagram_username="+str(username)).text)[0])# دا بقى بيجيب ايدي اليوزر الي بتدور عليه علشان الأبي اي مش بيعملها 
save_json=lambda data:open("/home/abied/Documents/"+username+".json","w").write(str(data)) # دا بيحط الجسون داتا علشان لو عزتها بعدين ابق غير المسار على مزاجك بقى 
def get_full_pics(userid,lst=[]):
    # دي عامتا الدالة الي بتجيب لستة بكل لينكات الصور على الأكونت الي بتدور عليه او عايز تحمل صوره 
    media = api.getTotalUserFeed(userid) # دي دالة تبع الأبي اي بتجيب جسون داتا في تكست حاطة فيها كل الميتا داتا بتاعت اليوزر فيد 
    save_json(media) # دي الدالة الي قلتلك عليها فوق بتحط الجسون داتا علشان لو عزتها بعدين 
    total_media_lenth = len(media)
    for cmid in range(total_media_lenth):
        if "carousel_media" in media[cmid]:
            for i in range(media[cmid]["carousel_media_count"]):
                lst.append(media[cmid]["carousel_media"][i]["image_versions2"]["candidates"][0]["url"])
                if "video_versions" in media[cmid]["carousel_media"][i]:lst.append(media[cmid]["carousel_media"][i]["video_versions"][0]["url"])
        elif "video_versions" in media[cmid]:lst.append(media[cmid]["video_versions"][0]["url"])
        else:lst.append(media[cmid]["image_versions2"]["candidates"][0]["url"])
    return lst,total_media_lenth
def mkfile(folename):
    if not path.exists(folename):
        mkdir(folename)
    return folename+"/"  
lst,tl=get_full_pics(getuserid(username))
folder=mkfile(username)
print("Downloading %s Media" %(tl))
try:
    for url in lst:
        name=url.split("/")[-1].split("?")[0] if "?" in url else url.split("/")[-1]
        assert download(name,url,folder);print("Downloaded ->",name," -> ",folder)
except:
    print("\n\n\t\t Logging Out... \n")
    api.logout()
system("chmod -R 777 "+folder)
api.logout()