from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from django.utils.html import strip_tags
from urllib.parse import unquote

import firebase_admin
from firebase_admin import credentials, db


from django.shortcuts import render
import os

#emails
import string
import json

from django.contrib.auth import get_user_model
from monitoreoia.models import CustomUser 

# Create your views here.


url = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static/config/firebasekey.json")
cred = credentials.Certificate(url)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://radiacion-c50d8.firebaseio.com"
})

class minitoringLogin:
    def login(self,request):            
            if request.method == 'POST':

                self.username = request.POST.get('username')
           
                self.password = request.POST.get('password')
            
                user = authenticate(request, username=self.username.lower(), password=self.password)

                context = {'contenido': self.username.lower()}
                if user is not None:
                    login(request, user)
                    request.session['minitoring_username'] = self.username.lower()
                    return render(request, 'home.html', context)
                else:
                    #messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                    messages.warning(request, 'Incorrect password or user name, please check! ')
                    return render(request, 'alert_nofile.html')
            
            return render(request, 'login.html')

          
    



    def contac(self,request):
            if request.method == 'POST':
                    #form = ContactForm(request.POST)

                    name = request.POST['name']
                    email = request.POST['email'] 
                    subject = request.POST['subject']
                    message = request.POST['message']
                    

                    # Crear un objeto MIMEText con el mensaje y el tipo de contenido
                    # Send the email
                    subject = 'GEM platform support - ' + subject
                    from_email = 'alruba40@gmail.com'
                    to_email = [email,'arualesb.1@cern.ch']
                    
                    message_with_sender = f"Hello {string.capwords(name)}: \n\n \
                        Thank you very much for contacting us!!. \n\n \
                        We will be contacting you shortly by email {email}  to resolve the concern \n\n \
                        \"{message}\" \n\n Best regards \n Alexis Ruales!!"

                    
                    # Send the email
                    send_mail(subject,message_with_sender, from_email,to_email)
        
                    messages.success(request, f'We will process the request with the email {email.upper()}, \n\n \
                                    ¿Is that correct?')
                    return render(request, "confirmation_send_email.html")
            
            else:
                return render(request, "contact.html")


class Home:
     def home(self,request):
          return render(request,"home.html")   
     
     def contactin(self,request):
           if request.method == 'POST':
                    #form = ContactForm(request.POST)

                    name = request.POST['name']
                    email = request.POST['email'] 
                    subject = request.POST['subject']
                    message = request.POST['message']
                    

                    # Crear un objeto MIMEText con el mensaje y el tipo de contenido
                    # Send the email
                    subject = 'GEM platform support - ' + subject
                    from_email = 'alruba40@gmail.com'
                    to_email = [email,'arualesb.1@cern.ch']
                    
                    message_with_sender = f"Hello {string.capwords(name)}: \n\n \
                        Thank you very much for contacting us!!. \n\n \
                        We will be contacting you shortly by email {email}  to resolve the concern \n\n \
                        \"{message}\" \n\n Best regards \n Alexis Ruales!!"

                    
                    # Send the email
                    send_mail(subject,message_with_sender, from_email,to_email)
        
                    messages.success(request, f'We will process the request with the email {email.upper()}, \n\n \
                                    ¿Is that correct?')
                    return render(request, "confirmation_send_emailin.html")
           else:
                return render(request, "contactin.html")

class database:
    def search_view(self,request):
        # Datbase

        ref = db.reference('database')


        #name user
        minitoring_username = request.session.get('minitoring_username')
       

        if minitoring_username:
            User = get_user_model()
            options=list(["None"])
            try:
                user = CustomUser.objects.get(username=minitoring_username)
                user_id_to_delete = user.id
                


                data=ref.child(str(user_id_to_delete)).get()
                try:
                     options =list(data.keys())
                except:
                     options=list(["None"])
                     

                data_points = []
                selected_option = ""
                data_vale=[]
                if request.method == 'POST':
                    
                    try:
                        selected_option = request.POST.get('selected_option')
                        datal=data[selected_option]
                        primer_elemento = next(iter(datal.items()))
                        clave, valor = primer_elemento
                        

                        data_vale=[int(number) for number in valor.split(",")]
                        for i in range(len(data_vale)):
                            data_points.append({"x":i+1,"y":data_vale[i]})
                    except:
                         data_points = [{"x":0,"y":0}]
                         pass
                    
                
                else:
                    
                    try:
                        selected_option = options[0]
                        datal=data[selected_option]
                        primer_elemento = next(iter(datal.items()))
                        clave, valor = primer_elemento
                        

                        data_vale=[int(number) for number in valor.split(",")]
                        for i in range(len(data_vale)):
                            data_points.append({"x":i+1,"y":data_vale[i]})
                    except:
                         data_points = [{"x":0,"y":0}]
                         pass 
                
            except User.DoesNotExist:
                print("User with the specified email does not exist.")
           
            return render(request, 'search_espectral.html',{'options': options, 
                                                            'selected_option': selected_option,
                                                            'data': data_points,
                                                            'dataspectral':data_vale,
                                                            'selectoption':[selected_option]})
        else:
             messages.success(request, f'Please enter the username and password again!')
             return render(request, "uploadloging.html")
             
             


class iaMossbauer:
    def modelIa(self,request):
        return render(request, 'iamossbauer.html')