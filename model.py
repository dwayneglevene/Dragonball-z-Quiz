#from random import randint
import random

Vegeta = {"cname":"Vegeta","description":"Vegeta is the Prince of an extraterrestrial warrior race known as the Saiyans. He is extremely arrogant, proud and hardworking; constantly referring to his heritage and royal status throughout the series","source":'static/images/vegeta.gif'}

Goku = {"cname":"Goku","description":"Son Goku , is the main protagonist of the Dragon Ball metaseries. Goku is a Saiyan originally sent to destroy Earth as an infant. However, a head injury at an early age alters his memory, ridding him of his initial destructive nature and allowing him to grow up to become one of Earth's greatest defenders. He constantly strives and trains to be the greatest warrior possible, which has kept the Earth and the universe safe from destruction many times.","source":'static/images/nimbus.gif'}

Bulma = {"cname":"Bulma","description":"Bulma (ブルマ Buruma) is a brilliant scientist and the second daughter of Capsule Corporation's founder Dr. Brief and his wife Panchy,[10] the younger sister of Tights,[11] and is Goku's first friend.[1][2] She used to be the girlfriend of Yamcha,[12][13] but moved on (while remaining friends with him) and, eventually, became the wife of Vegeta, as well as the mother of Trunks and Bulla. While she is unable to physically fight most of the villains in the series, her gadgetry plays a key role in winning several battles as well as the search for the Dragon Balls.","source":'static/images/bulma.gif'}

#Piccolo = {"cname":"Piccolo","description":"Piccolo Jr. (ピッコロ・ジュニア , usually just called Piccolo and also known as Ma Junior (マジュニア Majunia), is a Namekian and also the final child and reincarnation of King Piccolo, later becoming the reunification of the Nameless Namekian after fusing with Kami. According to Grand Elder Guru, Piccolo, along with Kami and King Piccolo, are part of the Dragon Clan, who were the original creators of the Dragon Balls.","source":'static/images/piccolo.gif'}

Gohan = {"cname":"Gohan","description":"Son Gohan (孫そん悟ご飯はん Son Gohan) is a half-breed Saiyan and one of the most prominent characters in the Dragon Ball series. He is the elder son of the series' primary protagonist Goku and his wife Chi-Chi, the older brother of Goten, the husband of Videl and father to Pan. He is named after Goku's adoptive grandfather, Gohan.","source":'static/images/gohan.gif'}

Piccolo = {"cname":"Piccolo","description":"s a fictional character in the Dragon Ball manga series created by Akira Toriyama. He is first seen as the reincarnation of the evil Piccolo Daimaō in chapter #161 Son Goku Wins!! ... He also trains Goku's first child Gohan in martial arts, with the two forming a strong bond.","source":'static/images/piccolo.gif'}

#poll = request.form.get("hour")

clist= [Piccolo,Gohan]

def getProperties(formResults):
    #if poll == "hour":
    print(formResults)

    if formResults['hour'] == 'hour' and formResults['mode'] == 'cloud' and formResults['hv'] == 'good':
        return Goku
    if formResults['hour'] == 'study' and formResults['mode'] == 'car' and formResults['hv'] == 'good':
        return Bulma
    if formResults['hour'] == 'hour' and formResults['mode'] == 'car' and formResults['hv'] == 'kindof':
        return Vegeta
    else:
        r = random.randint(0,len(clist)-1)
        return clist[r]
    