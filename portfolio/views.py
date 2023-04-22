from django.shortcuts import render

# Create your views here.
def index(request):
	if request.method=="POST":
		name=request.POST["Name"]
		email=request.POST["Email"]
		number=request.POST["Phone"]
		message=request.POST["Message"]
		print(name)
		print(email)
		print(number)
		print(message)
	return render(request,"index.html")


