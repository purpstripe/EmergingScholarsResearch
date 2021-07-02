class Body {
  // using a distance from the parent body and an angle to describe the pos of each body
  float distance, angle; 
  float rad; // radius of the body
  Body[] bodies; // RECURSION!!! - children to this parent object
  float orbitSpeed;
  PVector distVect;
  
  PShape globe;

  Body(float r, float d, float o, PImage img) {
    distVect = new PVector(1,0,0);
    
    rad = r;
    distance = d;
    distVect.mult(distance);
    
    angle = random(TWO_PI);
    orbitSpeed = o;
    
    noStroke();
    noFill();
    sphereDetail(40);
    globe = createShape(SPHERE, rad);
    globe.setTexture(img);
  }
  
  void spawnChildren(int total, int level) { // INITIALIZING RECURSIVE OBJECTS
    bodies = new Body[total];  
    for (int i = 0; i < bodies.length; i++) {
      float r = rad/(level*1.8); // shrink object radii in size based off of their level
      float d = (rad + r)*2; 
      float o = -0.01; 
      bodies[i] = new Body(r, d, o, textures[level-1]);
      // determines how many levels of bodies will be made, keep in mind a lvl is made above^
      if (level < 2) { 
        int num = 1; // int(random(4)); // how many moons each object will have
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
    
    
    PVector v2 = new PVector(1,0,1); // arbitrary vector
    PVector p = distVect.cross(v2); // perpendicular vector for three dimensional rotation
    stroke(255);
    line(0,0,0,p.x,p.y,p.z);
    
    // now rotating around an axis!!!
    rotate(angle, p.x, p.y, p.z); // must rotate before translating otherwise the rotation is not 'used'
    
    // translates each body distance away from the last 
    translate(distVect.x, distVect.y, distVect.z);  // remember that translate is cumulative so we must push/pop
    shape(globe);
    //sphere(rad);
    // ellipseMode(RADIUS);
    // ellipse(0, 0, rad, rad);
    
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
