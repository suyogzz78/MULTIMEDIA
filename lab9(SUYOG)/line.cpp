#include <graphics.h>
#include <iostream>

int main() {
    int gd = DETECT, gm;

    // Initialize graphics mode
    initgraph(&gd, &gm, (char*)"");

    // Draw a horizontal line
    line(100, 200, 400, 200);  // (x1, y1) to (x2, y2)

    // Draw a vertical line
    line(250, 100, 250, 300);  // (x1, y1) to (x2, y2)

    // Keep the window open until a key is pressed
    std::cin.get();

    // Close graphics mode
    closegraph();
    return 0;
}
