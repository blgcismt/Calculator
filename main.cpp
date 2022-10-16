#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

void login();
void registration();
void forgot_password();

int main()
{
    int action;

    cout<<"\t\t\t*********************************************\n\n\n";
    cout<<"\t\t\t           Welcome to the login page         \n\n\n";
    cout<<"\t\t\t******************* Menu ********************\n\n";
    cout<<"                 Welcome to the login page         \n\n";
    cout<<"\t | Press 1 to login...     |"<<endl;
    cout<<"\t | Press 2 to register...     |"<<endl;
    cout<<"\t | Press 3 if your forgot your password...     |"<<endl;
    cout<<"\t | Press 4 to exit...     |"<<endl;
    cout<<"\n\t\t\t Please enter your action :";
    cin>>action;
    cout<<endl;

    switch(action)
    {
        case 1:
            login();
            break;
        
        case 2:
            registration();
            break;
        
        case 3:
            forgot_password();
        
        case 4:
            cout<<"\t\t\t Good bye! See you later...\n\n";
            break;
        
        default:
            system("cls");
            cout<<"\t\t\t Invalid action! Please select a valid action...\n"<<endl;
            main();

    }
}

void login()

{
    int validator;
    string username, password, id, pass;
    system("cls");
    cout<<"\t\t\t Please enter the username and password : "<<endl;
    cout<<"\t\t\t Username : ";
    cin>>username;
    cout<<"\t\t\t Password : ";
    cin>>password;

    ifstream input("database.txt");

    while (input>>id>>pass)
    {
        if (id == username && pass == password)
        {
            validator = 1;
            system("cls");
        }
    }
    input.close();

    if (validator == 1)
    {
        cout<<username<<"\n Login successful! \n Thank you.. \n";
        main();
    }

    else{
        cout<<"\n Login unsuccessful! Please check your inputs...\n";
        main();
    }

}

void registration()
{
    string newusername, newpassword, newid, newpass;
    system("cls");

    cout<<"\t\t\t Enter username : ";
    cin>>newusername;
    cout<<"\t\t\t Enter password : ";
    cin>>newpassword;

    ofstream f1("database.txt", ios::app);
    f1<<newusername<<""<<newpassword<<endl;
    system("cls");
    cout<<"\n\t\t\t Registration completed...\n";
    main();
}

void forgot_password()

{
    int action;
    system("cls");
    cout<<"\t\t\t Have you forgot your password?\n";
    cout<<"Press 1 to search your id by username"<<endl;
    cout<<"Press 2 to go back to main menu"<<endl;
    cout<<"\t\t\t Enter your action :";
    cin>>action;
    switch(action)
    {
        case 1 :
        {
            int validation = 0;
            string fusername, fuserid, fpass;
            cout<<"\n\t\t\t Enter your username : ";
            cin>>fusername;

            ifstream f2("database.txt");
            while (f2>>fuserid>>fpass);
            {
                if (fuserid == fusername)
                {
                    validation = 1;
                }
            }
            f2.close();
            if (validation == 1)
            {
                cout<<"\n\nThis account exists...\n";
                cout<<"\n\n Here is your password :\n"<<fpass;
                main();
            }
            else{
                cout<<"\n\t This account does not exist! Check your inputs...\n";
            }
            break;
        }
        case 2:
        {
                main();
                }
            default :
                cout<<"\t\t\t Invalid action! Enter a valid action..."<<endl;
                forgot_password();
        
    }
}