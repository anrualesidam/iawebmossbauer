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

# Create your views here.


class minitoringLogin:        

    def login(self,request):            
            if request.method == 'POST':

                username = request.POST.get('username')
                print(username)
                password = request.POST.get('password')
                print(password)
                user = authenticate(request, username=username, password=password)

                context = {'contenido': username}
                if user is not None:
                    login(request, user)
                    return render(request, 'home.html', context)
                else:
                    #messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                    messages.warning(request, 'You must load a file with a .txt extension Ex: GE21-RO-M2-0008_20210916_11-02.txt ')
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
        if request.method == 'GET':
            search_query = request.GET.get('q')
            if search_query:
                # Initialize Firebase with your credentials
                #cred = credentials.Certificate("./static/config/firebase_credencials.json")
                cred = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', "./static/config/firebase_credencials.json")
                firebase_admin.initialize_app(cred, {'databaseURL': 'https://radiacion-c50d8.firebaseio.com/'})
                print("print aaa",cred)
                # Perform the search query in Firebase Realtime Database
                ref = db.reference('/your-data-node')  # Replace with your data node
                results = ref.order_by_child('name').equal_to(search_query).get()

                # Process the results and return them to the template
                return render(request, 'search_results.html', {'results': results})

        return render(request, 'search_espectral.html')


class iaMossbauer:
    def modelIa(self,request):
        return render(request, 'iamossbauer.html')