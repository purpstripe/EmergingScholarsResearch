// https://www.youtube.com/watch?v=dncudkelNxwi
import peasy.*;

Body sun;

PeasyCam cam;

int bgColor;

void setup() {
  size(600, 600, P3D);
  bgColor = 0;
  cam = new PeasyCam(this, 500);
  sun = new Body(50, 0, 0);
  sun.spawnChildren(1, 1);
}

void draw() {
  background(bgColor);
  lights();
  sun.display();
  sun.orbit();
}
