// https://www.youtube.com/watch?v=dncudkelNxwi
import peasy.*;

PeasyCam cam;

PImage starfield;

PImage sunText;
PImage[] textures = new PImage[2];

Body sun;

int bgColor;

void setup() {
  size(600, 600, P3D);
  
  starfield = loadImage("starfield.jpg");
  
  sunText = loadImage("sun.jpg");
  textures[0] = loadImage("earth.jpg");
  textures[1] = loadImage("moon.jpg");
  
  bgColor = 0;
  cam = new PeasyCam(this, 500);
  sun = new Body(50, 0, 0, sunText);
  sun.spawnChildren(1, 1);
}

void draw() {
  background(bgColor);

  lights();
  // spotLight(255,255,255,
  // pointLight(255,255,255,0,0,0);
  sun.display();
  sun.orbit();
}
