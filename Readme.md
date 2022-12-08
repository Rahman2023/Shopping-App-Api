

1)On GitHub.com, navigate to the main page of the repository.

2)To clone your repository using the command line using HTTPS, under "Quick setup", click

. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click

. Empty repository clone URL button

. Alternatively, to clone your repository in Desktop, click

Set up in Desktop and follow the prompts to complete the clone. Empty repository clone desktop button

3)Open Git Bash.

4)hange the current working directory to the location where you want the cloned directory.

5)Type git clone, and then paste the URL you copied earlier.

$ git clone https://github.com/Rahman2023/Shopping-App-Api.git

6)Press Enter to create your local clone.

msg:
$ git clone https://github.com/Rahman2023/Shopping-App-Api.git
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.

7) After Showing this msg Cloning was completed.Now you can change the code and create newproject.

Finally we are going to run our project.

step 1 : first open any database management tool like datagrip,mysqlworkbench etc..
![Screenshot (32)](https://user-images.githubusercontent.com/109596307/202860985-f752047d-7dc1-439d-9ab2-608f3bbb748b.png)

step 2 : create database for project using sql query : CREATE DATABASE projectname
![Screenshot (25)](https://user-images.githubusercontent.com/109596307/202860904-1a1a765b-10c4-453d-a299-ff39f2bfb69f.png)

step 3 : Open our project in any editor.I prefered visual studio code and go to setting.py in project.
![Screenshot (41)](https://user-images.githubusercontent.com/109596307/202861097-1badd07e-1a66-41a0-94d9-91f7a214fcfb.png)
 Now first thing we need to do , changing the database password. Here change the password , Whatever we use to loging into mysql on our machine.
 
 step 4 : Now we need to install our project dependencies , so we open a terminal window . go to project path folder using 
          command : cd 
          for mac :
          Run : pipenv install
          for windows :
          Run : py -m venv .
          ![Screenshot (42)](https://user-images.githubusercontent.com/109596307/202861584-248e4cef-d875-47c4-9645-83c29ebe805e.png)
          
step 5 : Active our vitual environment.
         for mac :
         pipenv shell
         for windows :
         foldername/Scripts/activate.bat
         ![Screenshot (43)](https://user-images.githubusercontent.com/109596307/202862087-1b5c864d-6063-455a-9833-bacfaf6a6738.png)
        
step 6 : Select python interpreter in vscode.
         1)Press the python show in the figure.
         ![Screenshot (44)](https://user-images.githubusercontent.com/109596307/202862136-8923f982-abb9-4d77-96dd-22c20200ad66.png)
         2)Select the path of interpreter.
         ![Screenshot (45)](https://user-images.githubusercontent.com/109596307/202862199-d5910807-8bd5-4640-9ce6-b7059e6faf81.png)
         for windows select scripts/pythow.exe as show in the picture below.
         ![Screenshot (48)](https://user-images.githubusercontent.com/109596307/202862352-fc7baff1-dc70-411e-9213-e15e0dfd37c5.png)
         3)successfully selected as show in the below fig.
         ![Screenshot (49)](https://user-images.githubusercontent.com/109596307/202862464-32508c49-29dc-4b17-bf9c-e8e4b80a3a7a.png)
         4)for creating tables in database migrate :
         command : python manage.py migrate
         ![Screenshot (52)](https://user-images.githubusercontent.com/109596307/202862927-34378d4b-2aef-417b-8867-863dbebb8693.png)

step 7 : population data into our database.I gave seed file in this project.
         ![Screenshot (51)](https://user-images.githubusercontent.com/109596307/202862833-99847d08-4b3f-48d6-8b8e-2d8adbdc9610.png)
         
step 8 : crate an admin user for our api.
         Run : python manage.py createsuperuser
         ![Screenshot (55)](https://user-images.githubusercontent.com/109596307/202863035-b58dda12-cb42-4207-9932-926e6c62241d.png)
         
step 9 : Run server : python manage.py runserver
         ![Screenshot (56)](https://user-images.githubusercontent.com/109596307/202863116-047389d4-9573-4bef-84a0-4dade3196f9d.png)
       
Successfully run our api.
![Screenshot (57)](https://user-images.githubusercontent.com/109596307/202863130-1dffe39a-b4c0-449b-965d-d7fadb372f42.png)


         





         



         ![Screenshot (43)](https://user-images.githubusercontent.com/109596307/202861966-a8ea72c7-0726-4ec8-9ebe-cf1d8dbf56d2.png)


 
 
          
          




