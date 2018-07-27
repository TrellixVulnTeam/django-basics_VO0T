from django.http import HttpResponse
from django.shortcuts import render

'''def Homepage(request):
     """return HttpResponse("Hello world !!")"""
     my_html="""
     <!DOCTYPE html>
        <html lang="en">
        <head>
          <!-- Theme Made By www.w3schools.com - No Copyright -->
          <title>Bootstrap Theme Simply Me</title>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
          <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
          <style>
          body {
              font: 20px Montserrat, sans-serif;
              line-height: 1.8;
              color: #f5f6f7;
          }
          p {font-size: 16px;}
          .margin {margin-bottom: 45px;}
          .bg-1 { 
              background-color: #1abc9c; /* Green */
              color: #ffffff;
          }
          .bg-2 { 
              background-color: #474e5d; /* Dark Blue */
              color: #ffffff;
          }
          .bg-3 { 
              background-color: #ffffff; /* White */
              color: #555555;
          }
          .bg-4 { 
              background-color: #2f2f2f; /* Black Gray */
              color: #fff;
          }
          .container-fluid {
              padding-top: 70px;
              padding-bottom: 70px;
          }
          .navbar {
              padding-top: 15px;
              padding-bottom: 15px;
              border: 0;
              border-radius: 0;
              margin-bottom: 0;
              font-size: 12px;
              letter-spacing: 5px;
          }
          .navbar-nav  li a:hover {
              color: #1abc9c !important;
          }
          </style>
        </head>
        <body>
        
        <!-- Navbar -->
        <nav class="navbar navbar-default">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>                        
              </button>
              <a class="navbar-brand" href="#">Me</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
              <ul class="nav navbar-nav navbar-right">
                <li><a href="#">WHO</a></li>
                <li><a href="#">WHAT</a></li>
                <li><a href="#">WHERE</a></li>
              </ul>
            </div>
          </div>
        </nav>
        
        <!-- First Container -->
        <div class="container-fluid bg-1 text-center">
          <h3 class="margin">Who Am I?</h3>
          <img src="https://www.siasat.com/wp-content/uploads/2018/03/Sunita_Williams.jpg" class="img-responsive img-circle margin" style="display:inline" alt="Human" width="350" height="350">
          <h3>I'm an astronaut</h3>
        </div>
        
        <!-- Second Container -->
        <div class="container-fluid bg-2 text-center">
          <h3 class="margin">What Am I?</h3>
          <p>Indian-origin astronaut Sunita Williams is now helping privately-held companies like Space X and Boeing to develop their new spacecraft systems, which will eventually provide round-trip crew transportation services to the International Space Station (ISS) </p>
          <a href="#" class="btn btn-default btn-lg">
            <span class="glyphicon glyphicon-search"></span> Search
          </a>
        </div>
        
        <!-- Footer -->
        <footer class="container-fluid bg-4 text-center">
          <p> Theme Made By Gayatri </p> 
        </footer>
        
        </body>
        </html>
     """
     return HttpResponse(my_html)'''

def Homepage(request):
    context={
        "title":"Hello!",
        "name" :"Gayatri"
    }
    return render(request, "homeview.html",context)

def Gayatripage(request):
    return render(request,"homeview.html",[])
