// gpa calculator

#include <iostream>
#include <string>
#include <iomanip>
using namespace std;


int main()
{
    string name;
    int numClasses;
    int numCredits;
    int numCreditsTotal = 0;
    int numGradePoints;
    int numGradePointsTotal = 0;
    double gpa;
    char grade;
    char repeat;

    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter the number of classes: ";
    cin >> numClasses;

    for (int i = 0; i < numClasses; i++)
    {
        cout << "Enter the number of credits for class " << i + 1 << ": ";
        cin >> numCredits;
        cout << "Enter the grade for class " << i + 1 << ": ";
        cin >> grade;

        switch (grade)
        {
        case 'A':
            numGradePoints = numCredits * 4;
            break;
        case 'B':
            numGradePoints = numCredits * 3;
            break;
        case 'C':
            numGradePoints = numCredits * 2;
            break;
        case 'D':
            numGradePoints = numCredits * 1;
            break;
        case 'F':
            numGradePoints = numCredits * 0;
            break;
        default:
            cout << "Invalid grade entered." << endl;
            break;
        }

        numCreditsTotal += numCredits;
        numGradePointsTotal += numGradePoints;
    }

    gpa = numGradePointsTotal / numCreditsTotal;
    cout << "Your GPA is: " << fixed << setprecision(2) << gpa << endl;

    cout << "Would you like to calculate another GPA? (Y/N): ";
    cin >> repeat;

    if (repeat == 'Y' || repeat == 'y')
    {
        main();
    }
    else
    {
        cout << "Goodbye!" << endl;
    }

    return 0;
}


