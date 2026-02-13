#include<iostream>
#include<iomanip>
#include<cstring>
#include<fstream>
#include<ctime>
using namespace std;


void header(){
    cout << "============================================" << endl;
    cout << endl;
    cout << setw(6) << " **********Art Online Banking App************ ";
    cout << endl;
    cout << " " << endl;
    cout << "============================================" << endl;
}
string currentTime() {
	
    time_t now = time(0);
    char* dt = ctime(&now);
    string timeStr = dt;
    
    timeStr.pop_back();
    return timeStr;
    
}


void footer(){
    cout << "===========================================" << endl;
    cout << setw(6) << " ******Thanks for using Art Online Banking App******* ";
    cout << " " << endl;
    cout << "============================================" << endl;
}

void menu(){
    cout << "\n Enter your choice to proceed " << endl;
    cout << "\n 1. Withdraw Amount " << endl;
    cout << "\n 2. Account Balance " << endl;
    cout << "\n 3. Deposit Amount " << endl;
    cout << "\n 4. Change MPIN " << endl;
    cout << "\n 5. Cancel Transaction " << endl;
    cout<<  "\n 6. Mini statement "<<endl;
     cout<<  "\n 7. Transactions History (admin only)"<<endl;
     cout<<"\n";
     cout<<"-----------------------------------------------";
					cout<<"\n";
}

int main() {
ofstream mini_clear("mini_statement.txt"); 
mini_clear.close();
ifstream in;
    int original_password = 1234;
    int user_password ,new_pin,confirm_pin,old_pin;
    int choice, w_amnt = 0, chck1, t_amnt = 50000;
    string name;

    bool isloggedin = false;  // FIXED: control login
	bool session = true;
	
    header();
    cout << " Enter User Name : ";
    getline(cin, name);
    cout<<endl;
    cout << "\n Welcome To ABL ATM " << endl;
    cout << " Dear " << name << endl;
    cout << "\n Enter Your Account Password " << endl;
    cout << " To Access Your Account : \n";
     cout<<"-----------------------------------------------";
					cout<<"\n";
    cin >> user_password;
   
    // ---------- LOGIN CHECK ----------
    if (user_password == original_password){
        isloggedin = true;
    }
    else {
        int k = 2;  // attempts left after first wrong
        for(int i = 0; i < 3; i++){
            if(i == 0) k = 2;
            cout << " WRONG PASSWORD! Try again !! "<<endl;
            cout << " You Have "<< k <<" attempts left"<<endl;
            k--;
            cin >> user_password;

            if(user_password == original_password){
                isloggedin = true;
                break;  // FIXED: break to menu
            }

            if(i == 2){
                system("cls");
                cout << " Dear ABL user your ATM card was blocked due to multiple wrong attempts \n";
                cout << " Thanks for using ABL ATM machine \n";
            }
        }
    }

    // ---------- IF LOGGED IN ----------
    while(session){
	
    if(isloggedin){
        system("cls");
        header();
        menu();
        cin >> choice;
//while(choice != 4){

        switch (choice){
            case 1:
            	
            	system("cls");
            	header();
                cout << " Enter Amount To Withdraw: ";
                cin >> w_amnt;
                if(w_amnt <t_amnt){
				
                cout << " So, You Want To Withdraw Amount of " << w_amnt << " Rupees " << endl;
                cout << "\n Do you want a receipt or not? " << endl;
                cout << " Enter 1 to continue or 0 to exit ";
                cin >> chck1;
                cout<<"\n";
                 cout<<"-----------------------------------------------";
					cout<<"\n";
                if(chck1 == 1){
                    system("cls");
                    header();
                    int temp = t_amnt;
                    cout << "\n ---------- Receipt ------------" << endl;
                    cout << "User Name : " << setw(4) << name << endl;
                    cout << " Account Balance : " << setw(4) << t_amnt << endl;
                    cout << "Amount Withdrawn : " << setw(4) << w_amnt << endl;
                    t_amnt = t_amnt - w_amnt;  // FIXED: update balance
                    cout<<"\n";
					cout << " Remaining Account Balance : " << setw(4) << t_amnt << endl;
                    footer();
                    ofstream wout("withdraw_transactions",ios::app);
                     ofstream out("transaction.txt",ios::app);
                     ofstream mini("mini_statement.txt",ios::app);
                    out<<"User Name :  "<<name<<" | Amount Withdraw : " <<w_amnt<<" | before withdraw Account Balance : "<<temp<<" | After withdraw Account Balance : "<<t_amnt<<" | Time: "<< currentTime()<<endl;
             		mini<<"User Name :  "<<name<<" | Amount Withdraw : " <<w_amnt<<" | before withdraw Account Balance : "<<temp<<" | After withdraw Account Balance : "<<t_amnt<<" | Time: "<< currentTime()<<endl;
					 wout<<"User Name :  "<<name<<" | Amount Withdraw : " <<w_amnt<<" | before withdraw Account Balance : "<<temp<<" | After withdraw Account Balance : "<<t_amnt<<" | Time: "<< currentTime()<<endl;
			    wout.close();
			    mini.close();
			    wout.close();
				}
			}
			else
			{
				header();
				cout<<"\n Insufficient Blance!! \n";
				footer();
			}
                break;

            case 2:
                system("cls");
                header();
                cout << "\n -------- Account Balance Details ----------" << endl;
                cout << "User Name : " << setw(4) << name << endl;
                cout << " Account Balance : " << setw(4) << t_amnt << endl;
                cout << "Amount Withdrawn : " << setw(4) << w_amnt << endl;
                cout << " Remaining Account Balance : " << setw(4) << t_amnt << endl;
               cout<<"\n";
			    footer();
                break;

            case 3:
                {
                	
                    int d_s;
                    system("cls");
                    header();
                    cout<<"\n 1. 500 Rs ";
                    cout<<"\n 2. 1000 Rs ";
                    cout<<"\n 3. 5000 Rs ";
                    cout<<"\n 4. 10000 Rs ";
                    cout<<"\n 5. Other Amount ";
                    cin>>d_s;

                    int deposit = 0;
                    if(d_s == 1)
					{
					 deposit = 500;
					 

				 }
                    else if(d_s == 2)
					{
                    	deposit = 1000;
                    	
					
					} 
                    else if(d_s == 3)
					{
                    	deposit = 5000;
                    	 

					} 
                    else if(d_s == 4)
					{
                    	deposit = 10000;
                    	 
				
					} 
					if( deposit > 0 && deposit <= 5000){
						int b_deposit;
						b_deposit = t_amnt;
						t_amnt += deposit;
						ofstream out("transaction.txt",ios::app);
						 ofstream mini("mini_statement.txt",ios::app);
						 ofstream dout("dposits_only",ios::out);
                        out<<"User: " << name << " | Deposit: " << deposit << " |Before Deposit Balance: " << b_deposit <<" |After Deposit Balance: "<<t_amnt <<" | Time: "<< currentTime()<< endl;
                        mini<<"User: " << name << " | Deposit: " << deposit << " |Before Deposit Balance: " << b_deposit <<" |After Deposit Balance: "<<t_amnt <<" | Time: "<< currentTime()<< endl;
                        dout<<"User: " << name << " | Deposit: " << deposit << " |Before Deposit Balance: " << b_deposit <<" |After Deposit Balance: "<<t_amnt <<" | Time: "<< currentTime()<< endl;
                        out.close();
                        mini.close();
                        dout.close();
                 }
                    else if(d_s == 5)
					{
                        cout << " Enter the amount you want to deposit (less than 50000): ";
                        cin >> deposit;
                       
                        if(deposit >= 50000){
                            cout << " You have exceeded the limit " << endl;
                            deposit = 0;
                        }
                        else if(deposit <=50000 && deposit> 1000)
                        {
                        	 int total;
                        total = t_amnt +deposit ;
                        ofstream dout("dposits_only",ios::out);
                        ofstream out("transaction.txt",ios::app);
                        ofstream mini("mini_statement.txt",ios::app);
                        out<<"User: " << name << " | Amount Deposit: " << deposit << " |Before Deposit Balance: " << t_amnt <<" |After Deposit Balance: "<<total<<" | Time: "<< currentTime()<< endl;
                          mini<<"User: " << name << " | Amount Deposit: " << deposit << " |Before Deposit Balance: " << t_amnt <<" |After Deposit Balance: "<<total<<" | Time: "<< currentTime()<< endl;
                        dout<<"User: " << name << " | Amount Deposit: " << deposit << " |Before Deposit Balance: " << t_amnt <<" |After Deposit Balance: "<<total<<" | Time: "<< currentTime()<< endl;
						out.close();
                        mini.close();
						 t_amnt = total;
						 dout.close();
						}
                    }

//

                    system("cls");
                    header();
                    cout << "\n -----Amount deposited successfully ------";
                    cout << "\n ---------- Current Account Details ------------" << endl;
                    cout << "User Name : " << setw(4) << name << endl;
                    cout << " Account Balance : " << setw(4) << t_amnt << endl;
                    cout << " Amount Deposited : " << setw(4) << deposit << endl;
                   
                    cout << " Current Account balance : " << setw(4) << t_amnt << endl;
                    footer();
                }
                break;
				case 4:
					{
						system("cls");
						header();
						cout <<"\n Enter Your old PIN : ";
						cin>>old_pin;
						if(old_pin == original_password){
							cout <<"\n Enter your new PIN : ";
							cin>>new_pin;
							cout<<"\n Confirm your new PIN (enter again) :";
							cin>>confirm_pin;
							if(confirm_pin==new_pin){
								cout<< "\n Your new pin was created successfully : ";
								original_password = confirm_pin;
							}
							else 
								{
									cout<<"\n wrong pin dear "<<name;
									cin>>confirm_pin;
							if(confirm_pin==new_pin){
								cout<< "\n Your new pin was created successfully : ";
								original_password = confirm_pin;
								}
						}
					}
					cout<<"\n";
					footer();
					break;
            case 5:{
            	system("cls");
            	header();
                cout << "\n Transaction Cancelled \n" << endl;
                footer();
                session = false;
                break;
                break;
					}
					
				case 6:
				{
					ifstream mini("mini_statement.txt");
					string line;
					header();
					cout<<"\n-------- Mini Statement-------\n\n";
					while(getline(mini,line)){
						cout<<line <<endl;
					}
					mini.close();
					cout<<"\n";
					footer();
					break;
				}
				case 7:
					{ 
					system("cls");
					header();
					string password = "admin123";
					string pass;
					cout <<" Enter Password \n";
						cout<<"-----------------------------------------------";
					cout<<"\n";
					cin>>pass;
					
					if(pass == password){
						int choose;
					system("cls");
					header();
					cout<<"\n welcome Dear Admin "<<name;
					cout<<"\n Which History do you want Dear "<<name;
					cout<<"\n 1. All Transactions \n";
					cout<<"\n 2. All Deposits Only \n";
					cout<<"\n 3. All Withdraws Only \n";
					cout<<"-----------------------------------------------";
					cout<<"\n";
					cin>>choose;
					footer();
				if(choose ==3){
					system("cls");
						header();
						cout<<"\n --------- ALL Transations History ---------- \n";
						ifstream out("transaction.txt");
					string st;
					while(getline(out,st)){
						
						cout<<st<<endl;
					}
					out.close();
					cout<<endl;
					footer();	
					cout<<"------------------------------------------------";
					cout<<"\n";					
					
				}
				else if(choose ==2){
					system("cls");
					header();
					cout<<"\n --------- ALL Deposits History ---------- \n";
					ifstream dout("dposits_only");
				string l;
				while(getline(dout,l)){
					cout<<l<<endl;
				}
				cout<<"-----------------------------------------------";
					cout<<"\n";
				footer();
				
				
				}
				else if(choose ==1){
					system("cls");
					header();
					cout<<"\n --------- ALL Withdraws History ---------- \n";
					string p;
					ifstream wout("withdraw_transactions");
					while(getline(wout,p)){
						cout<<p<<endl;
					}
					cout<<"-----------------------------------------------";
					cout<<"\n";
					footer();
				}
				
				
					
						
						}else
					{
						cout <<" wrong password !Access Denied "<<endl;
						break;
					}
					break;
					}
            default:
                cout << " Invalid choice " << endl;
        }
    }
    }
    
    cout << "\n Press enter to continue...";
    cin.ignore();
    cin.get();
}

    return 0;
}