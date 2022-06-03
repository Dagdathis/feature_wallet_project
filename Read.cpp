#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
struct transaction {             //Структура транзакции
	string code;
    string date;
    string category;
    string sum;  
};

int choice1 =0;
int i=0, j;

void mainMenu(){
    do {                            //Меню
    cout << "Wellcome\n";
    cout << "1 - Graph\n";          //График
    cout << "2 - Circle diagram\n"; //Круговая
    cout << "3 - Exit\n";
    cout << "Please choose: ";
    cin >> choice1;    
    switch(choice1) {

        case 1:
            cout << "Diagram\n";
            break;

        case 2:
            cout << "Circle diagram\n";
            break;
        case 3:
            break;

        }

    }while(choice1 != 3);
}

void diagram(void){

}

int main(){
    transaction TR[10];
    ifstream transactions("data.csv");  //открыть файл
    if(!transactions.is_open()) cout << "File open"; //Проверка занятости 
    while(!transactions.eof())
    {
        getline(transactions, TR[i].code, ',');
        getline(transactions, TR[i].date, ',');
        getline(transactions, TR[i].category, ',');
        getline(transactions, TR[i].sum, ';');
        
        i++;
    }
    i--;
    
    transactions.close();
    
    for (j = 0; j < 10; j++)
    {
        cout << '\n' << "code: " << TR[j].code << "  data:  " << TR[j].date << "  typ:  " << TR[j].category << "  sum:  " << TR[j].sum;
    }
    cout << '\n';
    
    mainMenu();
    }