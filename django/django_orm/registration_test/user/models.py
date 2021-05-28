from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create(form):
    
    if form["password"] == form["pwdcon"]:
        User.objects.create(first_name=form["first_name"], last_name=form["last_name"], 
        email = form["email"], password = ["password"])

        return True

    else:
        return False

def login(email , passwordd):
    user= User.objects.filter(email =email)
    v = User.objects.get(id=5).password
    print(User.objects.get(id=5).password)
    if user:
        if passwordd == v :
            return True
        return None


    # print(user[0].password)

    # if user:
    #     print("AAAAAAAAAAAAAAAAAAA")
    #     if user1 == user[0].password: 
    #         print("xxxxxxxxxxxxxxx")

    #         return True





  

  
 

