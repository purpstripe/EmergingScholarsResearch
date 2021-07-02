// https://www.youtube.com/watch?v=l8SiJ-RmeHU

// data
int bgColor;
Body sun;

void setup() {
  size(600, 600);
  bgColor = 0;
  sun = new Body(50, 0, 0);
  sun.spawnChildren(5, 1);
}

void draw() {
  background(bgColor);
  translate(width/2, height/2);
  sun.display();
  sun.orbit();
}
