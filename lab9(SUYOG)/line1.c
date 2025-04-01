#include <stdio.h>
#include <graphics.h>
#include <conio.h>
#include <math.h>
#include <stdlib.h>

void main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);

    float x1, y1, x2, y2, steps, xi, yi, dx, dy;
    int k = 0;

    printf("Enter the endpoints of the line (x1, y1, x2, y2): ");
    scanf("%f%f%f%f", &x1, &y1, &x2, &y2);

    dx = x2 - x1;
    dy = y2 - y1;

    if (fabs(dx) > fabs(dy)) {
        steps = fabs(dx);
    } else {
        steps = fabs(dy);
    }

    xi = dx / steps;
    yi = dy / steps;

    int x = round(x1);
    int y = round(y1);
    
    putpixel(x, y, WHITE);  // Start pixel

    while (k < steps) {
        x1 += xi;
        y1 += yi;
        putpixel(round(x1), round(y1), WHITE);  // Convert to int for putpixel()
        k++;
    }

    getch();  // Wait for user input
    closegraph();  // Close graphics mode
}
