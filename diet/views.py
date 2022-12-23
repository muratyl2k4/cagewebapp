from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import userInformations
from collections import Counter
from django.contrib import messages
from blog.models import Program



def home(request) :
    program = Program.objects.all()
    length = len(program)
    print(program)
    data = {
        "p" : program[length-3 : length]
    }
    return render(request , "index.html" , data)

def beslenme(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.error(request , "Bu Alana Devam Etmek için Giriş Yapmalısınız")
        return redirect("login")

    info = userInformations.objects.values().filter(userid = request.user)
    stats = [1]
## CREATE USER STATS
    if not info:
        newquery = userInformations(userid = request.user , userweight = 0 , userage = 0 ,
        userlength = 0 , userrepastlength = 0 , userchoice = "KG+" , userweightrange = 0 , usermoving= "az" )
        newquery.save()
        return redirect("/beslenme")

## MAIN FUNCS
    class Main:
        boy = [x.get("userlength") for x in info]
        yas = [x.get("userage") for x in info]
        kilo = [x.get("userweight") for x in info]
        cinsiyet = [x.get("usergender") for x in info]
        weightrange = [x.get("userweightrange") for x in info]
        movingchoice = [x.get("usermoving") for x in info]
        bmr = [x.get("bmr") for x in info]
        ## 1 kilogram =? kalori
        weighttargetquestion = [x.get("userchoice") for x in info]
        if weighttargetquestion[0] == "KG+":
            onekgcalori =7777

        elif weighttargetquestion[0] == "KG-":
            onekgcalori = 8000

        def bmrhesapla(self):
            if self.cinsiyet[0] == "Kadın":
                self.bmr = ((self.boy[0] * 4.7) / 2.54) + (self.kilo[0] * 4.35 * 100/45) - (self.yas[0] * 4.7) + 651
            elif self.cinsiyet[0] == "Erkek":
                self.bmr = ((self.boy[0] * 12.7) / 2.54) + (self.kilo[0] * 6.2 * 100/45) - (self.yas[0] * 6.76) + 66
            if self.movingchoice[0] == "az":
                self.bmr *= 1.2
            elif  self.movingchoice[0] == "orta" :
                self.bmr *= 1.375
            elif  self.movingchoice[0] == "cok":
                self.bmr *= 1.55
            elif self.movingchoice[0] == "asiri":
                self.bmr *= 1.725
            return self.bmr

        def gunlukbmrhesapla(self):
            self.bmrhesapla()
            eksikalori = self.weightrange[0] * self.onekgcalori
            gunlukeksikalori = eksikalori / 30
            if self.weighttargetquestion[0] == "KG+":
                self.bmr += gunlukeksikalori
            elif self.weighttargetquestion[0] == "KG-":
                self.bmr -= gunlukeksikalori
            return self.bmr
    ##UPDATE USER STATS
    if request.method == "POST":
        updateuser = Main()
        updateuser.kilo = [int(request.POST["kginput"])]
        updateuser.yas = [int(request.POST["ageinput"])]
        updateuser.boy = [int(request.POST["lengthinput"])]
        updateuser.weightrangequestion = [int(request.POST["weight+-"])]
        updateuser.weighttargetquestion = [request.POST["+-choice"]]
        updateuser.movingchoice = [request.POST["moving"]]
        updateuser.cinsiyet = [request.POST["gender"]]

        info.update(userweight = request.POST["kginput"])
        info.update(userage = request.POST["ageinput"])
        info.update(userlength = request.POST["lengthinput"])
        info.update(userrepastlength = request.POST["repastinput"])
        info.update(userweightrange = int(request.POST["weight+-"]))
        info.update(userchoice = request.POST["+-choice"])
        info.update(usermoving = request.POST["moving"])
        info.update(usergender = request.POST["gender"])
        info.update(bmr = int(updateuser.gunlukbmrhesapla()))

        print(int(updateuser.gunlukbmrhesapla()))
        print(int(Main().gunlukbmrhesapla()))

        return HttpResponseRedirect("../pre-workout-sec")
    stats[0] = {"bmr" : int(Main().gunlukbmrhesapla()) , "dbmr" : int(Main().bmrhesapla())}
    print(Main().bmrhesapla())
    print(Main().gunlukbmrhesapla())

    data = {
        "a" : info,
        "stats" : stats
    }

    return render(request , "beslenme.html" , data)

@login_required(login_url="/login")
def preworkout(request):
    info = userInformations.objects.filter(userid = request.user)
    if request.method == "POST":
        if request.POST.getlist("hurma"):
            info.update(HURMA = True)
        else:
            info.update(HURMA = False)
        if request.POST.getlist("muz"):
            info.update(MUZZ = True)
        else:
            info.update(MUZZ = False)
        if request.POST.getlist("bcaa"):
            info.update(BCAA = True)
        else:
            info.update(BCAA = False)
        if request.POST.getlist("kahve"):
            info.update(KAHVE = True)
        else:
            info.update(KAHVE = False)
        if request.POST.getlist("preworkout"):
            info.update(PRE_WORKOUT = True)
        else:
            info.update(PRE_WORKOUT = False)
        if request.POST.getlist("churcill"):
            info.update(CHURCILL = True)
        else:
            info.update(CHURCILL = False)
        return redirect("ogun-1-secim")

    data = {
        "a" : info
    }
    return render(request , "preworkout.html" , data)

@login_required(login_url="/login")
def ogun1secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 0 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun1protein = request.POST["protein"])
        info.update(ogun1karb = request.POST["karbonhidrat"])
        if repastlength[0] > 1:
            return redirect("ogun-2-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }
    return render(request , "ogun-1-secim.html" , data)

@login_required(login_url="/login")
def ogun2secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 1:
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun2protein = request.POST["protein"])
        info.update(ogun3karb = request.POST["karbonhidrat"])
        if repastlength[0] > 2:
            return redirect("ogun-3-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }

    return render(request , "ogun-2-secim.html" , data)
@login_required(login_url="/login")
def ogun3secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 2 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun3protein = request.POST["protein"])
        info.update(ogun3karb = request.POST["karbonhidrat"])
        if repastlength[0] > 3:
            return redirect("ogun-4-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }
    return render(request , "ogun-3-secim.html" , data)
@login_required(login_url="/login")
def ogun4secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 3 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun4protein = request.POST["protein"])
        info.update(ogun4karb = request.POST["karbonhidrat"])
        if repastlength[0] > 4:
            return redirect("ogun-5-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }
    return render(request , "ogun-4-secim.html" , data)

@login_required(login_url="/login")
def ogun5secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 4 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun5protein = request.POST["protein"])
        info.update(ogun5karb = request.POST["karbonhidrat"])
        if repastlength[0] > 5:
            return redirect("ogun-6-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }
    return render(request , "ogun-5-secim.html" , data)

@login_required(login_url="/login")
def ogun6secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 5 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun6protein = request.POST["protein"])
        info.update(ogun6karb = request.POST["karbonhidrat"])
        if repastlength[0] > 6:
            return redirect("ogun-7-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }
    return render(request , "ogun-6-secim.html" , data)

@login_required(login_url="/login")
def ogun7secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 6 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun7protein = request.POST["protein"])
        info.update(ogun7karb = request.POST["karbonhidrat"])
        if repastlength[0] > 7:
            return redirect("ogun-8-secim")
        else:
            return redirect("../beslenmeprogrami")
    data = {
        "a" : info
    }
    return render(request , "ogun-7-secim.html" , data)

@login_required(login_url="/login")
def ogun8secim(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    if not repastlength[0] > 7 :
        return redirect("beslenme")
    if request.method == "POST":
        info.update(ogun8protein = request.POST["protein"])
        info.update(ogun8karb = request.POST["karbonhidrat"])
        return redirect("../beslenmeprogrami")

    data = {
        "a" : info
    }
    return render(request , "ogun-8-secim.html" , data)

@login_required(login_url="/login")
def diet(request):
    info = userInformations.objects.values().filter(userid = request.user)
    repastlength = [x.get("userrepastlength") for x in info]
    repast_foods = []
    yaglist = []
    class Main:
        ogunler = []
        besinlist = []
        yemekler = []
        kilo = [x.get("userweight") for x in info]
        bmr = [x.get("bmr") for x in info]
        def __init__(self):

            self.proteinlistesi = {
                'Tavuk Göğsü': {'kalori': 1.1, 'protein': 0.23, 'carb': 0.0, 'yag': 0.0125},
                'Balık': {'kalori': 1.09, 'protein': 0.195, 'carb': 0.0, 'yag': 0.0275},
                'Hindi': {'kalori': 1.07, 'protein': 0.25, 'carb': 0.0, 'yag': 0.01},
                }
            self.karblistesi = {
                'Pirinç': {'kalori': 3.41, 'protein': 0.0675, 'carb': 0.76, 'yag': 0.005},
                'Bulgur': {'kalori': 3.42, 'protein': 0.125, 'carb': 0.76, 'yag': 0.015},
                'Yulaf': {'kalori': 3.6, 'protein': 0.14, 'carb': 0.53, 'yag': 0.075},
                'Makarna': {'kalori': 3.58, 'protein': 0.115, 'carb': 0.72, 'yag': 0.02},
                'Ekmek': {'kalori': 2.66, 'protein': 0.075, 'carb': 0.5, 'yag': 0.035},
                }

            self.yaglistesi = {
                'Yağ': {'kalori': 9.0, 'protein': 0.0, 'carb': 0.0, 'yag': 1.0},

                 }
            self.ogunkalorisi = 0
            self.sistemprotein = 0
            self.sistemyag = 0
            self.sistemkarb = 0
            self.sistemogunyag = 0
            self.sistemogunkarb = 0
            self.sistemogunprotein = 0
            self.ogunprotein = 0
            self.ogunyag = 0
            self.ogunkarb = 0
            self.protein = 0
            self.karb = 0
            self.yag = 0
        def choosefood(self):
            for mealnum in range(1,repastlength[0]+1):
                ogun = []
                for x in info:
                    ogun.append(x.get(f"ogun{mealnum}protein"))
                    ogun.append(x.get(f"ogun{mealnum}karb"))
                    self.yemekler.append(x.get(f"ogun{mealnum}protein"))
                    self.yemekler.append(x.get(f"ogun{mealnum}karb"))
                    self.ogunler.append(ogun)
        def ogunkalori(self):
            self.choosefood()
            self.ogunkalorisi += self.bmr[0] / repastlength[0]
        def makrohesaplama(self):
            self.ogunkalori()
            self.protein += self.kilo[0] * 2
            self.yag += self.kilo[0]*0.65
            self.karb += (self.bmr[0] - (self.protein*4 + self.yag*9)) / 4
            self.ogunprotein = self.protein / repastlength[0]
            self.ogunkarb = self.karb /  repastlength[0]
            self.ogunyag = self.yag /  repastlength[0]
        def besinmiktari(self):
            self.makrohesaplama()
            ##TODO
            for xyz in self.ogunler:
                for a in xyz:
                    print(a)
                    if a in self.proteinlistesi.keys():
                        print("p")
                        while self.sistemogunprotein <= self.ogunprotein:
                            self.besinlist.append(a)
                            self.sistemyag += self.proteinlistesi.get(a).get("yag")
                            self.sistemprotein += self.proteinlistesi.get(a).get("protein")
                            self.sistemkarb += self.proteinlistesi.get(a).get("carb")
                            self.sistemogunyag += self.proteinlistesi.get(a).get("yag")
                            self.sistemogunprotein += self.proteinlistesi.get(a).get("protein")
                            self.sistemogunkarb += self.proteinlistesi.get(a).get("carb")
                    elif a in self.karblistesi.keys():
                        print("p")
                        while self.sistemogunkarb <= self.ogunkarb:
                            self.besinlist.append(a)
                            self.sistemyag += self.karblistesi.get(a).get("yag")
                            self.sistemprotein += self.karblistesi.get(a).get("protein")
                            self.sistemkarb += self.karblistesi.get(a).get("carb")
                            self.sistemogunyag += self.karblistesi.get(a).get("yag")
                            self.sistemogunprotein += self.karblistesi.get(a).get("protein")
                            self.sistemogunkarb += self.karblistesi.get(a).get("carb")
                self.sistemogunyag = 0
                self.sistemogunkarb = 0
                self.sistemogunprotein = 0
            while self.sistemyag <= self.yag:
                self.besinlist.append("Yağ")
                self.sistemyag += self.yaglistesi.get("Yağ").get("yag")
            sistemfazlalik = self.sistemprotein - self.protein
            sistemogunfazlalik = sistemfazlalik / repastlength[0]
            equaliser = 0
            print(self.sistemogunkarb , self.ogunkarb , self.bmr[0])
            if self.sistemprotein > self.protein :
                for i in range(repastlength[0]):
                    while equaliser < sistemogunfazlalik:
                        self.besinlist.remove(self.ogunler[i][0])
                        self.sistemyag -= self.proteinlistesi.get(self.ogunler[i][0]).get("yag")
                        self.sistemprotein -= self.proteinlistesi.get(self.ogunler[i][0]).get("protein")
                        self.sistemkarb -= self.proteinlistesi.get(self.ogunler[i][0]).get("carb")
                        equaliser += self.proteinlistesi.get(self.ogunler[i][0]).get("protein")
                    equaliser = 0
            yaglist.append(self.besinlist.count("Yağ"))
            print(type(Counter(self.besinlist)))
            print(Counter(self.besinlist))
            print(self.sistemkarb , self.sistemprotein , self.sistemyag)
        ##TODO
        def dataframe(self):
            self.besinmiktari()
            ###Öğünlerdeki besinler
            repastnum = 1
            for abc in self.ogunler:
                dictx = {"num" : None ,"p" : None , "k" : None}
                for k,v in Counter(self.besinlist).items():
                    print(abc)
                    if k == abc[0]:
                        dictx["p"] = f"{k}  {round(v / self.yemekler.count(k))} gram"
                    elif k == abc[1]:
                        dictx["k"] = f"{k}  {round(v / self.yemekler.count(k))} gram"
                dictx["num"] = repastnum
                repastnum += 1
                repast_foods.append(dictx)
                print(dictx)
    pwlist = []
    Main().dataframe()
    print(repast_foods)
    print(Main.yemekler)
    ###PREWORKOUT
    for abc in info:
        pwdict = {
        "muz" : abc.get("MUZZ"),
        "hurma" : abc.get("HURMA"),
        "kahve" : abc.get("KAHVE"),
        "preworkout" : abc.get("PRE_WORKOUT"),
        "churcill" : abc.get("CHURCILL"),
        "bcaa" : abc.get("BCAA"),            }
        for k , v in pwdict.items():
            if k == "kahve" :
                if v == True:
                    pwlist.append(f"Kahve (max {Main.kilo[0] * 4} mg)")
            elif v == True:
                pwlist.append(k.upper())
        print(pwlist)
    data ={
        "a" : info ,
        "b" : repast_foods ,
        "y" : yaglist[0] ,
        "p" : pwlist

    }
    return render(request , "diyetson.html" , data)
def urunlerPage(request):
    return render(request , "urunler.html")