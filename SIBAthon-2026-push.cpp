#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
using namespace std;
const int Committee_limit=1000;
const int CommitteeMember_limit=10;
int totalCommittees=0;
int committeeMenu(){
	cout<<"=================================="<<endl;
	cout<<setw(6)<<"**** Digital committee ****"<<endl;
	cout<<"1. Create Committee "<<endl;
	cout<<"2. Add a Member "<<endl;
	cout<<"3. View Committees "<<endl;
	cout<<"4. Exit "<<endl;
	int ch;
	cout<<"Enter your choice: ";
	cin>> ch;
	return ch;
	}
	int ChooseCommitteeType(){
		int choice;
		cout<<"You have been given 3 choices to choose between: "<<endl;
		cout<<"1. Committee of Rs: 2000"<<endl;
		cout<<"2. Committee of Rs: 5000"<<endl;
		cout<<"3. Committee of Rs: 10,000"<<endl;
		cin>>choice;
		return choice;
	}
	void Committee1(){
	  string name;
      cout << "Enter committee name: ";
      getline(cin, name);
      cout<<"Your committee contribution per person will be: Rs: 2000 "<<endl;
      //we have to save names (file handling will be done)
      cout<<"Committee"<<name<<" has been successfully created!"<<endl;
      }
      void Committee2(){
	  string name;
      cout << "Enter committee name: ";
      getline(cin, name);
      cout<<"Your committee contribution per person will be: Rs: 5000 "<<endl;
      //we have to save names (file handling will be done)
      cout<<"Committee"<<name<<" has been successfully created!"<<endl;
      }
      void Committee3(){
	  string name;
      cout << "Enter committee name: ";
      getline(cin, name);
      cout<<"Your committee contribution per person will be: Rs: 10,000 "<<endl;
      //we have to save names (file handling will be done)
      cout<<"Committee"<<name<<" has been successfully created!"<<endl;
      }
int main(){
	cout<<"********* Wellcome to Digital Committee ********* "<<endl;
	
	switch(committeeMenu()) {
            case 1: 
				if(ChooseCommitteeType() == 1)
				{
					Committee1();
				}
				else if(ChooseCommitteeType() == 2)
				{
					Committee2();
				}
				else if(ChooseCommitteeType() == 3)
				{
					Committee3();
				}
				else {
					cout<<"Invalid Choice!";
				}
					
				break;
            case 2: 
			//addMember(); 
			break;
            case 3: 
			//viewCommittees(); 
			break;
            case 4: 
			cout << "Exiting program." << endl; 
			break;
            default: 
			cout << "Invalid choice! Try again." << endl;
	        
	return 0;
}}
