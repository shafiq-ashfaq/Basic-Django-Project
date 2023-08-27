# I have created this file :
# Django views are Python functions that takes http requests and returns http response, like HTML documents.
from django.http import HttpResponse
from django.shortcuts import render

# Basic code for learning django views concept:

# import os

# def index(request):
#     return HttpResponse("Welcome to my first website:") # in argument we can also pass html code

# def about(request):
#     return HttpResponse("About User")



# def home(request):
#     f = open("1.txt",'r')
#     content =f.read()
#     f.close()
#     return HttpResponse(content)

# def navigatorpage(request):
#     return HttpResponse('''<h1> Navigator Page <h1> <a href = "https://www.youtube.com/"> www.youtube.com </br>  
#                         <a href = "https://www.w3schools.com/ " > www.w3schools.com</a>''')

'''
Views:
Views are Python functions or classes that process incoming HTTP requests and return HTTP responses. Each view is responsible for a specific functionality of the application, such as rendering a webpage, processing form data, or serving JSON data for AJAX requests. Views are the bridge between the URL patterns defined in the URLs configuration and the actual logic of your application.
In a view function, you can perform various operations, such as querying the database, processing user input, and rendering templates. Once the view has processed the request and generated a response, it returns the response object, which is sent back to the client. '''






# Code for laying pipeline concept with backward button

# def index(request):
#     return HttpResponse(''' Home </br> <a href = "http://127.0.0.1:8000/removpunc" > Remove Punctuations , </br> 
#                         <a href = "http://127.0.0.1:8000/capitalizefirst" > Capitalize First , </br>
#                         <a href = "http://127.0.0.1:8000/spaceremove" > Space Remover , </br>
#                         <a href = "http://127.0.0.1:8000/charcount" > Charcount ,
#                         </br>
#                         <a href = '/'> back  </a>''')

# def removepunc(requeset):
#     return HttpResponse('''Remove Punctuations </br> <a href = "http://127.0.0.1:8000" > Home , </br> 
#                         <a href = "http://127.0.0.1:8000/capitalizefirst" > Capitalize First , </br>
#                         <a href = "http://127.0.0.1:8000/spaceremove" > Space Remover , </br>
#                         <a href = "http://127.0.0.1:8000/charcount" > Charcount ,  </br>
#                         <a href = '/'> back  </a>''')

# def capfirst(requeset):
#     return HttpResponse('''Capitalize first </br> <a href = "http://127.0.0.1:8000" > Home , </br> 
#                         <a href = "http://127.0.0.1:8000/removpunc" > Remove Punctuations, </br>
#                         <a href = "http://127.0.0.1:8000/spaceremove" > Space Remover , </br>
#                         <a href = "http://127.0.0.1:8000/charcount" > Charcount , 
#                           </br>
#                         <a href = '/'> back </a>''')

# def spaceremove(requeset):
#     return HttpResponse('''Space Remover </br> <a href = "http://127.0.0.1:8000" > Home , </br> 
#                         <a href = "http://127.0.0.1:8000/capitalizefirst" > Capitalize First , </br>
#                         <a href = "http://127.0.0.1:8000/removpunc" > Remove Punctutions , </br>
#                         <a href = "http://127.0.0.1:8000/charcount" > Charcount , 
#                         </br>
#                         <a href = '/'> back </a>''')

# def charcount(requeset):
#     return HttpResponse(''' charcount </br> <a href = "http://127.0.0.1:8000" > Home , </br> 
#                         <a href = "http://127.0.0.1:8000/capitalizefirst" > Capitalize First , </br>
#                         <a href = "http://127.0.0.1:8000/removpunc" > Remove Punctutions , </br>
#                         <a href = "http://127.0.0.1:8000/spaceremove" > Space Remover, 
#                           </br>
#                         <a href = '/'> back  </a>''')




# Code for learning template concept in django, first we should go setting.py of Template of DIR  and write templates. then import render in views.py

'''In Django, the render() function is a built-in shortcut that simplifies the process of rendering an HTML template with data and returning an HTTP response. It is commonly used in view functions to generate dynamic content for web pages.

The render() function takes the following parameters:

request: The HTTP request object representing the user's request to the view.
template_name: The name of the template file to be rendered. This can be a string containing the template's path relative to the TEMPLATES setting in your Django project's settings.py file.
context: A dictionary containing the data that will be passed to the template for rendering (optional).
'''

# def index(request):
#     return render(request, 'index.html')

# or

# def index(request):
#     intro = {'name':"Shafiq",'place': "Karachi"}
#     return render(request, 'index.html',intro)

# Code for Homepage using templates
# def index(request):
#     return render(request, 'index.html')

# def removepunc(request):
#     txt = request.GET.get('text', 'default')
#     print(txt)
#     return HttpResponse("Remove punctuations")


# Code for Basic Backend concept or create basic website

# def index(request):
#     return render(request, 'index.html')

# def analyze(request):
#     txt = request.GET.get('text', 'default') # get text from server
#     removpunc = request.GET.get('removepunc','off')
#     upper_case = request.GET.get('upper__case','off')
#     capitalize = request.GET.get('Capitalize','off')
#     newline = request.GET.get('Newline Remover','off')
#     spaceremover = request.GET.get('space remover','off')
#     # print(removpunc) # to check status of checkbox either it is on or off
#     # print(txt) # to print text   
   
#     # Code for remove punctuations from text
#     if removpunc == 'on':
#         punctuations = '''.,?!:;'"()[]{}-—.../\&@$%#+-=<>_?!~|'''
#         analyzed = ""
#         for char in txt:
#             if char not in punctuations:
#                 analyzed = analyzed + char            

#         parameters = {'purpose' : 'Remove Punctuations' , 'analyzed_text' : analyzed}        

#         return render(request , 'analyze.html' , parameters)
    
    
#     # code for conversion in upper case to text
#     elif(upper_case == 'on'):
#         uprcase = txt.upper()
#         parameters = {'purpose' : 'Convert in uppercase' , 'analyzed_text' : uprcase}        

#         return render(request , 'analyze.html' , parameters)
    
#     # code for capitalize the first letter of text
#     elif(capitalize == 'on'):
#         caps = txt.capitalize()
#         parameters = {'purpose' : 'Capitalize the text' , 'analyzed_text' : caps}        

#         return render(request , 'analyze.html' , parameters)
    
#     # code for removing newlinee from text
#     elif(newline == 'on'):
#         nlr = ""
#         for char in txt:
#             if char != '\n' and char != "\r":
#                 nlr = nlr + char
#         parameters = {'purpose' : "Remove Newlines" ,'analyzed_text' :  nlr }
#         return render(request, 'analyze.html', parameters)
    
#     # Code for removing extra space from text
#     elif(spaceremover == 'on'):
#         spc = ""
#         for index,char in enumerate(txt):
#             # if txt[index] == " " and txt[index +1] == " ":
#             #     pass
#             # else:
#             #     spc = spc + char
#     # OR
#             if not(txt[index] == " " and txt[index+1] == " "):
#                 spc = spc + char
#         parameters = {'purpose' : "Extra Space Remover" ,'analyzed_text' :  spc }
#         return render(request, 'analyze.html', parameters)   

                 
#     else:
#         return HttpResponse("Error! Please tick the checkbox for perform an action:")
#     # return HttpResponse("Remove punc")



# code for using POST request
"""POST Method:
The POST method is used to send data to a server to create or update a resource. It's often used when submitting forms on a website or sending data that should not be visible in the URL.

Characteristics of the POST method:

Data is included in the request body, which makes it suitable for sending larger amounts of data or sensitive information.
POST requests are not cached by default.
They are more secure for sending sensitive data as compared to GET requests."""

# def index(request):
#     return render(request, 'index.html')

# def analyze(request):
#     # txt = request.GET.get('text', 'default') # get text from server
#     # removpunc = request.GET.get('removepunc','off')
#     # upper_case = request.GET.get('upper__case','off')
#     # capitalize = request.GET.get('Capitalize','off')
#     # newline = request.GET.get('Newline Remover','off')
#     # spaceremover = request.GET.get('space remover','off')
#     txt = request.POST.get('text', 'default') 
#     removpunc = request.POST.get('removepunc','off')
#     upper_case = request.POST.get('upper__case','off')
#     capitalize = request.POST.get('Capitalize','off')
#     newline = request.POST.get('Newline Remover','off')
#     spaceremover = request.POST.get('space remover','off')
#     # print(removpunc) # to check status of checkbox either it is on or off
#     # print(txt) # to print text   
   
#     # Code for remove punctuations from text
#     if removpunc == 'on':
#         punctuations = '''.,?!:;'"()[]{}-—.../\&@$%#+-=<>_?!~|'''
#         analyzed = ""
#         for char in txt:
#             if char not in punctuations:
#                 analyzed = analyzed + char            

#         parameters = {'purpose' : 'Remove Punctuations' , 'analyzed_text' : analyzed}        

#         return render(request , 'analyze.html' , parameters)
    
    
#     # code for conversion in upper case to text
#     elif(upper_case == 'on'):
#         uprcase = txt.upper()
#         parameters = {'purpose' : 'Convert in uppercase' , 'analyzed_text' : uprcase}        

#         return render(request , 'analyze.html' , parameters)
    
#     # code for capitalize the first letter of text
#     elif(capitalize == 'on'):
#         caps = txt.capitalize()
#         parameters = {'purpose' : 'Capitalize the text' , 'analyzed_text' : caps}        

#         return render(request , 'analyze.html' , parameters)
    
#     # code for removing newlinee from text
#     elif(newline == 'on'):
#         nlr = ""
#         for char in txt:
#             if char != '\n' and char != "\r":
#                 nlr = nlr + char
#         parameters = {'purpose' : "Remove Newlines" ,'analyzed_text' :  nlr }
#         return render(request, 'analyze.html', parameters)
    
#     # Code for removing extra space from text
#     elif(spaceremover == 'on'):
#         spc = ""
#         for index,char in enumerate(txt):
#             # if txt[index] == " " and txt[index +1] == " ":
#             #     pass
#             # else:
#             #     spc = spc + char
#     # OR
#             if not(txt[index] == " " and txt[index+1] == " "):
#                 spc = spc + char
#         parameters = {'purpose' : "Extra Space Remover" ,'analyzed_text' :  spc }
#         return render(request, 'analyze.html', parameters)   

                 
#     else:
#         return HttpResponse("Error! Please tick the checkbox for perform an action:")
#     # return HttpResponse("Remove punc")






# when Multiple checkbox is checked at a time

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # txt = request.GET.get('text', 'default') # get text from server
    # removpunc = request.GET.get('removepunc','off')
    # upper_case = request.GET.get('upper__case','off')
    # capitalize = request.GET.get('Capitalize','off')
    # newline = request.GET.get('Newline Remover','off')
    # spaceremover = request.GET.get('space remover','off')
    txt = request.POST.get('text', 'default') 
    removpunc = request.POST.get('removepunc','off')
    upper_case = request.POST.get('upper__case','off')
    capitalize = request.POST.get('Capitalize','off')
    newline = request.POST.get('Newline Remover','off')
    spaceremover = request.POST.get('space remover','off')
    print(removpunc) # to check status of checkbox either it is on or off
    print(txt) # to print text   
   
    # Code for remove punctuations from text
    if removpunc == 'on':
        punctuations = '''.,?!:;'"()[]{}-—.../\&@$%#+-=<>_?!~|'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char            

        parameters = {'purpose' : 'Remove Punctuations' , 'analyzed_text' : analyzed}        
        txt = analyzed

        
    
    
    # code for conversion in upper case to text
    if(upper_case == 'on'):
        uprcase = txt.upper()
        parameters = {'purpose' : 'Convert in uppercase' , 'analyzed_text' : uprcase}
        txt = uprcase


        
    
    # code for capitalize the first letter of text
    if(capitalize == 'on'):
        caps = txt.capitalize()
        parameters = {'purpose' : 'Capitalize the text' , 'analyzed_text' : caps}        
        txt = caps
    
    # code for removing newlinee from text
    if(newline == 'on'):
        nlr = ""
        for char in txt:
            if char != '\n' and char != "\r":
                nlr = nlr + char
        parameters = {'purpose' : "Remove Newlines" ,'analyzed_text' :  nlr }
        txt = nlr
    
    # Code for removing extra space from text
    if(spaceremover == 'on'):
        spc = ""
        for index,char in enumerate(txt):
            # if txt[index] == " " and txt[index +1] == " ":
            #     pass
            # else:
            #     spc = spc + char
    # OR
            if not(txt[index] == " " and txt[index+1] == " "):
                spc = spc + char
        parameters = {'purpose' : "Extra Space Remover" ,'analyzed_text' :  spc }
        txt = spc

    if (removpunc != 'on' and upper_case != "on" and capitalize != "on" and newline != "on" and spaceremover != "on"):
        return HttpResponse("PLease! Tick the checkbox otherwise no action will be perform")   
    
    
    return render(request , 'analyze.html' , parameters)     

                 
    