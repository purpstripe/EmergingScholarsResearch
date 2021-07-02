//This value specifies where in the ellipse orbit
//your object is, from 0 to 2*PI
float val;

//The speed your object moves at along the orbit
float speed = 0.05;

void setup(){
  size(500, 500);
}

void draw(){
  background(0);
  
  //Calculate x and y as values between -1 and 1
  //Search wikipedia for sinus and cosinus if this is unclear :)
  float x = sin(val);
  float y = cos(val);
  
  //Multiply x and y by the ellipses width (100) and height (500)
  x *= 100;
  y *= 50;
  
  //Move the centrepoint of the ellipse orbit where you want it
  x+= mouseX;
  y+= mouseY;
  
  //Draw your object!
  fill(255);
  ellipse(x, y, 20, 20);
  
  //Update the value
  val += speed;
}
