#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    float t[100001], fi[100001], dfidt[100001];
    const float g = 9.81, c = 0.1, m = 0.2, l = 1, omega = 1000, A = 100, fi0 = 0.05, tau = 0.01;
    float omega02, k, delta;

    omega02 = g / l;
    k = omega02 / 3;
    delta = c / (m * l);

    ofstream f1("t.csv", ios::out);
    ofstream f2("fi.csv", ios::out);
    ofstream f3("dfidt.csv", ios::out);

    t[0] = 0;
    t[1] = tau;
    fi[0] = 0.2;
    fi[1] = fi[0] * (1 - (sqrt(omega02) * tau * sqrt(omega02) * tau)/2);
    dfidt[0] = 0;
    dfidt[1] = (fi[1] - fi[0]) / tau;
    f1 << t[0] << endl;
    f2 << fi[0] << endl;
    f3 << dfidt[0] << endl;
    f1 << t[1] << endl;
    f2 << fi[1] << endl;
    f3 << dfidt[1] << endl;

    cout << "Integration has started!" << endl;

    for (int i = 2; i < 100001; i++)
    {
        t[i] = t[i-1] + tau;
        if (abs(fi[i-1]) <= fi0)
            fi[i] = ((2 + delta * tau - omega02 * pow(tau, 2)) * fi[i-1] - fi[i-2] + A * cos(omega * t[i]) * pow(tau, 2) + k * pow(tau, 2) * pow(fi[i-1], 3)) / (1 + delta * tau);
        else
            fi[i] = ((2 + delta * tau - omega02 * pow(tau, 2)) * fi[i-1] - fi[i-2] + k * pow(tau, 2) * pow(fi[i-1], 3)) / (1 + delta * tau);
        dfidt[i] = (fi[i] - fi[i-1]) / tau;
        f1 << t[i] << endl;
        f2 << fi[i] << endl;
        f3 << dfidt[i] << endl;
    }

    cout << "Integration has finished!" << endl;

    return 0;
}
