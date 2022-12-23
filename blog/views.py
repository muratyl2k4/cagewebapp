from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render
from .models import Program
# Create your views here.
def allPrograms(request):

    programs = reversed(Program.objects.all())

    print(programs)
    data = {
        "programs" : programs
    }
    return render(request , "programlar.html" , data)

def ProgramPage(request , id):
    print(1)
    try:
        program= Program.objects.get(id=id)
        print(program)
        print("1")
    except Program.DoesNotExist:
        program = None
    if program is not None:

        return render(request , "program.html" , {"program" : program})
    else:
        raise Http404("Aradığınız Sayfa Namevcud")

def iletisimPage(request):
    def sendMail(name , last_name , mail , phone , message):

        send_mail(
        'CAGE STRENGTH İLETİŞİM',
        f"""
        Kimden : {name} {last_name} \n
        Gönderen E-Mail :{mail} \n
        Gönderen Telefon   {phone}\n
        Mesaj : {message}  """,
        'cagestrengthsendmail@gmail.com',
        ['cagestrength06@gmail.com'],
        fail_silently=False,
    )
    if request.method == "POST":
        name = request.POST["name"]
        last_name = request.POST["last_name"]
        mail = request.POST["e-mail"]

        phone = str(request.POST["phone"])

        message = request.POST["message"]

        sendMail(name , last_name , mail , phone , message)





    return render(request , "iletisim.html")



def koclukalPage(request):



    return render(request , "koclukal.html")