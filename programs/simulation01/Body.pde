class Body {
  // using a distance from the parent body and an angle to describe the pos of each body
  float distance, angle; 
  float rad; // radius of the body
  Body[] bodies; // RECURSION!!! - children to this parent object
  float orbitSpeed;

  Body(float r, float d, float o) {
    rad = r;
    distance = d;
    angle = random(TWO_PI);
    orbitSpeed = o;
  }
  
  void spawnChildren(int total, int level) { // INITIALIZING RECURSIVE OBJECTS
    bodies = new Body[total];  
    for (int i = 0; i < bodies.length; i++) {
      float r = rad/(level*1.4); // shrink object radii in size based off of their level
      float d = random(100, 250); // random distance away from parent body b/w 100, 200
      float o = random(-0.06, 0.06); // some orbit speed value between neg and pos .06
      bodies[i] = new Body(r, d/level, o); // shrink distance away from parent body by lvl
      // determines how many levels of bodies will be made, keep in mind a lvl is made above^
      if (level < 2) { 
        int num = int(random(4)); // how many moons each object will have
        bodies[i].spawnChildren(num, level+1); // recursive call for making children
      }
    }
  }
  
  void orbit() { // controlling orbit of each body, and its children
    angle += orbitSpeed;
    if (bodies != null) {
      for (int i = 0; i < bodies.length; i++) {
        bodies[i].orbit();
      }
    }
  }


  void display() {
    pushMatrix(); // pushes current orientation (for one planet) onto the matrix stack
    rotate(angle); // must rotate before translating otherwise the rotation is not 'used'
    // translates each body distance away from the last 
    translate(distance, 0);  // remember that translate is cumulative so we must push/pop
    stroke(0);
    strokeWeight(0);
    fill(255, 208, 0, 100);
    ellipseMode(RADIUS);
    ellipse(0, 0, rad, rad);
    
    // VERY IMPORTANT: this stops recursive loop before no more children planets are available (null)
    if (bodies != null) {
      // RECURSION, for each body, display its bodies
      for (int i = 0; i < bodies.length; i++) {
        bodies[i].display();
      }
    }
    popMatrix(); // pops the current transformation matrix of the stack
  }
}
