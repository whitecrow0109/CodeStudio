#include <bits/stdc++.h> 
bool countPlatesOnTable(int n, int R, int r){
    if (n == 1) {
        if (r <= R) return 1;
        return 0;
    }
    if (r < (R - r) * sin(M_PI / n) + 1e-6) return 1;
    return 0;
}