from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup
from datetime import datetime, date
import matplotlib.pyplot as plt

# --------------------------

def Temperature(num): #เป็น pip module สำหรับทำดึงข้อมูลจาก Web site
    try:
        url = 'https://www.tmd.go.th/province.php?id=' + str(num)
        webopen = request(url)
        page_html = webopen.read()
        data = soup(page_html, 'html.parser')
        temp = data.findAll('td', {'class': 'strokeme'})
        province = data.findAll('span', {'class': 'title'})
        result = float(temp[0].text[0:4])
        result2 = (province[0].text)
        print(f'{num}.)จังหวัด:{result2}  อุณหภูมิ: {result}')
        webopen.close()
        return result
    except:
        print('ไม่มีข้อมูลจากกรมอุตุนิยมวิทยา')


def days():
    now = datetime.today()
    print(now)


def calcopim(word,c): #คำนวณค่าCOP COP ideal =ค่า copในอุดมคติของจังหวัดที่เลือกreturn copidealไปใช้ในเมน COP=
    float(c)
    temout = (c)
    COPideal = 1 / (((temout + 273) / (25 + 273)) - 1)
    if word == "COPideal":
        return COPideal
    if word == "COP":
        se = str(input("คุณมีค่า EER หรือ SEER เช็คได้ที่ฉลากแอร์เบอร์ 5 : "))
        se = str.upper(se)
        if (se == 'EER'):
            eer = float(input("ใส่ค่า EER ของท่าน : "))
            COP = eer / 3.142

        if (se == 'SEER'):
            seer = float(input("ใส่ค่า SEER : "))
            seer = seer * 0.947
            COP = seer / 3.142

        return COP


def country(b): #รับค่าชื่อจังหวัดมาเก็บเป็นตัวเลขที่ตัวแปร x
    str(b)
    if (b == 'เชียงราย'):
        x = 1
        return x
    if (b == 'เชียงใหม่'):
        x = 2
        return x
    if (b == 'แม่ฮ่องสอน'):
        x = 3
        return x
    if (b == 'ตาก'):
        x = 4
        return x
    if (b == 'น่าน'):
        x = 5
        return x
    if (b == 'อุตรดิตถ์'):
        x = 6
        return x
    if (b == 'พิษณุโลก'):
        x = 7
        return x
    if (b == 'กำแพงเพชร'):
        x = 8
        return x
    if (b == 'พิจิตร'):
        x = 9
        return x
    if (b == 'สุโขทัย'):
        x = 10
        return x
    if (b == 'พะเยา'):
        x = 11
        return x
    if (b == 'ลำพูน'):
        x = 12
        return x
    if (b == 'ลำปาง'):
        x = 13
        return x
    if (b == 'แพร่'):
        x = 14
        return x
    if (b == 'เพชรบูรณ์'):
        x = 15
        return x
    if (b == 'หนองคาย'):
        x = 16
        return x
    if (b == 'เลย'):
        x = 17
        return x
    if (b == 'ขอนแก่น'):
        x = 18
        return x
    if (b == 'อุบลราชธานี'):
        x = 19
        return x
    if (b == 'นครราชสีมา'):
        x = 20
        return x
    if (b == 'ร้อยเอ็ด'):
        x = 21
        return x
    if (b == 'มุกดาหาร'):
        x = 22
        return x
    if (b == 'อุดรธานี'):
        x = 23
        return x
    if (b == 'หนองบัวลำภู'):
        x = 24
        return x
    if (b == 'นครพนม'):
        x = 25
        return x
    if (b == 'สกลนคร'):
        x = 26
        return x
    if (b == 'มหาสารคาม'):
        x = 27
        return x
    if (b == 'กาฬสินธุ์'):
        x = 28
        return x
    if (b == 'ชัยภูมิ'):
        x = 29
        return x
    if (b == 'ศรีสะเกษ'):
        x = 30
        return x
    if (b == 'ยโสธร'):
        x = 31
        return x
    if (b == 'สุรินทร์'):
        x = 32
        return x
    if (b == 'บุรีรัมย์'):
        x = 33
        return x
    if (b == 'อำนาจเจริญ'):
        x = 34
        return x
    if (b == 'กาญจนบุรี'):
        x = 35
        return x
    if (b == 'นครสวรรค์'):
        x = 36
        return x
    if (b == 'กรุงเทพมหานคร'):
        x = 37
        return x
    if (b == 'สุพรรณบุรี'):
        x = 38
        return x
    if (b == 'ชัยนาท'):
        x = 39
        return x
    if (b == 'ลพบุรี'):
        x = 40
        return x
    if (b == 'พระนครศรีอยุธยา'):
        x = 41
        return x
    if (b == 'ราชบุรี'):
        x = 42
        return x
    if (b == 'ปทุมธานี'):
        x = 43
        return x
    if (b == 'สระบุรี'):
        x = 44
        return x
    if (b == 'สิงห์บุรี'):
        x = 45
        return x
    if (b == 'สมุทรสงคราม'):
        x = 46
        return x
    if (b == 'อ่างทอง'):
        x = 47
        return x
    if (b == 'อุทัยธานี'):
        x = 48
        return x
    if (b == 'นนทบุรี'):
        x = 49
        return x
    if (b == 'นครปฐม'):
        x = 50
        return x
    if (b == 'สมุทรปราการ'):
        x = 51
        return x
    if (b == 'สมุทรสาคร'):
        x = 52
        return x
    if (b == 'สระแก้ว'):
        x = 53
        return x
    if (b == 'ชลบุรี'):
        x = 54
        return x
    if (b == 'ระยอง'):
        x = 55
        return x
    if (b == 'ปราจีนบุรี'):
        x = 56
        return x
    if (b == 'ตราด'):
        x = 57
        return x
    if (b == 'จันทบุรี'):
        x = 58
        return x
    if (b == 'ฉะเชิงเทรา'):
        x = 59
        return x
    if (b == 'นครนายก'):
        x = 60
        return x
    if (b == 'พัทยา'):
        x = 61
        return x
    if (b == 'ประจวบคีริขันธ์'):
        x = 62
        return x
    if (b == 'ชุมพร'):
        x = 63
        return x
    if (b == 'นครศรีธรรมราช'):
        x = 64
        return x
    if (b == 'นราธิวาส'):
        x = 65
        return x
    if (b == 'สุราษฏร์ธานี'):
        x = 66
        return x
    if (b == 'ยะลา'):
        x = 67
        return x
    if (b == 'ปัตตานี'):
        x = 68
        return x
    if (b == 'สงขลา'):
        x = 69
        return x
    if (b == 'เพชรบุรี'):
        x = 70
        return x
    if (b == 'หัวหิน(ประจวบคีริขันธ์)'):
        x = 71
        return x
    if (b == 'เกาะสมุย(สุราษฏร์ธานี)'):
        x = 72
        return x
    if (b == 'พัทลุง'):
        x = 73
        return x
    if (b == 'ระนอง'):
        x = 74
        return x
    if (b == 'ภูเก็ต'):
        x = 75
        return x
    if (b == 'กระบี่'):
        x = 76
        return x
    if (b == 'ตรัง'):
        x = 77
        return x
    if (b == 'พังงา'):
        x = 78
        return x
    if (b == 'สตูล'):
        x = 79
        return x
    else :
        x = 0
        return x

def btu(): #ให้เลือกใส่ระหว่าง BTU และ CC และ คำนวณค่า coolingcapacity
    bc = (input(str.upper(" คุณทราบค่า BTU หรือ Cooling capacity(CC) :")))
    bc = str.upper(bc)
    if (bc == 'BTU'):
        ccbtu = (float(input("ใส่ค่า BTU แอร์ของท่าน : ")))
        ccbtu = 0.2931 * ccbtu
        ucc = ccbtu/1000
        return ucc
    if (bc == 'CC'):
        cc = (float(input("ใส่ค่า Cooling Capacity แอร์ของท่าน : ")))
        ucc = cc/1000
        return ucc


def nexttempin(text,temper): #ทำหน้าที่คำนวณค่าไฟที่อุณหภูมิภายในเปลี่ยนไป
    Tempin=16
    COPI=[]
    Tempin2=[]
    while Tempin<31 :
        COP2=float(1 / (((temper + 273) / (Tempin + 273)) - 1))
        Tempin2.append(Tempin)
        COPI.append(COP2)
        Tempin+=1
    if (text == "Temperaturein") :
        return Tempin2
    if (text == "TCOPI") :
        return COPI
def power(k,t,e): #คำนวณค่าไฟไม่เกี่ยวเนื่องกับอุณหภูมิ
    for i in range (0,15) :
        power=float(((k-t[i])/100)+1)*ee
        Upower.append(round(power,3))
    return Upower
def nexttempout(text2,temper2) : #เหมือน def nexttempin แต่เปลี่ยนเป็นอุณหภูมิภายนอก
    temper2=temper2-7
    COPI2 = []
    Tempout2=[]
    for u in range(0,15) :
        COP3 = float(1 / (((temper2 + 273) / (25 + 273)) - 1))
        Tempout2.append(temper2)
        temper2 += 1
        COPI2.append(COP3)
    if (text2 == "Temperaturein2") :
        return Tempin2
    if (text2 == "TCOPI2") :
        return COPI2    
def powerout(k,t,e): #เหมือน def power แต่เป็นอุณหภูมิภายนอก
    Upower2=[]
    for i in range (0,15) :
        power=float(((k-t[i])/100)+1)*ee
        Upower2.append(round(power,3))
    return Upower2
def graph(y,x): #พลอตกราฟแสดงความสัมพันธ์ระหว่างอุณหภูมิและค่าไฟ
    plt.plot(y,x)
    plt.ylabel('Temperature  / Bath')
    plt.show()
####MAIN PROJECT
a = str(input("ใส่ชื่อจังหวัดที่ต้องการดูค่าอุณหภูมิ : "))
#country(a)
x = country(a)
while x==0 :
    a = str(input("ใส่ชื่อจังหวัดที่ต้องการดูค่าอุณหภูมิ : "))
    country(a)
    x = country(a)
result = Temperature(x)
COPideal = calcopim("COPideal", result)
COP = calcopim("COP", result)
ucc = btu()
eeunit = float(input("ค่าไฟ/หน่วย ของที่อยู่ท่าน : "))
ee = round(((ucc * eeunit * 0.80) / COP),3)
print("ค่าไฟของคุณต่อชั่วโมง(โดยทั่วไปไม่เกี่ยวกับอุณหภูมิ) คือ", ee)
Tempin2=nexttempin("Temperaturein",result)
COPI=nexttempin("TCOPI",result)
Upower=power(COPideal,COPI,ee)
print("อุณหภูมิภายในเปลี่ยน (ภายนอกคงที่) ค่าไฟ  บาท",Upower)
Tempout2=nexttempout("Temperaturein2",result)
COPI2=nexttempout("TCOPI2",result)
Upower2=powerout(COPideal,COPI2,ee)
print("อุณหภูมิภายนอกเปลี่ยน (ภายในคงที่25 องศา) ค่าไฟ  บาท",Upower)
graph(Tempout2,Upower2)
graph(Tempin2,Upower)
