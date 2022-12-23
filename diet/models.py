from django.contrib.auth.models import User
from django.db import models

class userInformations(models.Model):
    userid = models.OneToOneField(User ,  on_delete = models.CASCADE)
    sexChoices = [
        ("ERKEK" , "ERKEK"),
        ("KADIN" , "KADIN")
    ]
    usergender = models.CharField(max_length=100 , choices=sexChoices , default="Kadın" )
    userweight = models.IntegerField()
    userage = models.IntegerField()
    userlength = models.IntegerField()
    userrepastlength = models.IntegerField()
    KILO_ALMA = "KG+"
    KILO_VERME = "KG-"
    CHOICES = [( KILO_ALMA , "KİLO ALMA"),
                (KILO_VERME , "KİLO VERME" )]
    userchoice = models.CharField(max_length= 10 , 
    choices = CHOICES ,
    default = "KİLO VERME")
    userweightrange = models.IntegerField(default = 0)
    AZ = "az"
    COK = "cok"
    ORTA = "orta"
    ASIRI = "asiri"
    mChoices = [(AZ , "Az Hareketli"),
                (COK , "Cok Hareketli"),
                (ORTA , "Orta Hareketli"),
                (ASIRI , "Aşırı Hareketli")]
    usermoving = models.CharField(max_length = 100 , 
                                choices = mChoices,
                                default ="Az Hareketli")
    bmr = models.SmallIntegerField(default = 0)



    ##SPOR ÖNCESİ 
    MUZZ = models.BooleanField(default = True , null = True)
    HURMA = models.BooleanField(default = False , null = True)
    PRE_WORKOUT = models.BooleanField(default = False , null = True)
    CHURCILL = models.BooleanField(default = False , null = True)
    BCAA = models.BooleanField(default = False , null = True)
    KAHVE = models.BooleanField(default = False ,null = True)

    
    

    ##PROTEİN 
    TAVUK_G = "Tavuk Göğsü"
    C_BALIK = "Balık"
    HINDI = "Hindi"
    pChoices = [(TAVUK_G , TAVUK_G),
                (C_BALIK , C_BALIK),
                (HINDI , HINDI)]
    ##CARBS
    PIRINC = "Pirinç" 
    BULGUR = "Bulgur"
    YULAF = "Yulaf"
    MAKARNA = "Makarna"
    EKMEK = "Ekmek"
    
    cChoices = [(PIRINC , PIRINC),
                (BULGUR , BULGUR),
                (YULAF , YULAF),
                (MAKARNA , MAKARNA),
                (EKMEK , EKMEK)

    ]
    

    ##PROTEİN ÖĞÜNLERİ
    ogun1protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun2protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun3protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun4protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun5protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun6protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun7protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ogun8protein = models.CharField(max_length= 100 , 
    choices =  pChoices,
    default = "Tavuk Göğsü")
    ##KARBS
    ogun1karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun2karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun3karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun4karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun5karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun6karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun7karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
    ogun8karb = models.CharField(max_length= 100 , 
    choices =  cChoices,
    default = "Pirinç")
                  
    def __str__(self):
        return str(self.userid)
