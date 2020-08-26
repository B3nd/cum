float r1 = 150;
float r2 = 150;
float m1 = 40;
float m2 = 40;
float a1 = 0;
float a2 = PI / 2;
void setup(){
  size(600, 600);
}
void draw(){
   background(255);
   stroke(0);
   strokeWeight(2);
   translate(300, 50);
   float x1 = r1 * sin(a1);
   float y1 = r1 * cos(a1);
   line(0, 0, x1, y1);
   fill(0);
   ellipse(x1, y1, m1, m1);
   float x2 = r2 * sin(a2) + x1;
   float y2 = r2 * cos(a2) + y1;
   line(x1, y1, x2, y2);
   ellipse(x2, y2, m2, m2);
   a1 += 0.01;
   a2 -= 0.02;
}
