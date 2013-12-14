int threshold = 635;           // Below this, the chest is considered compressed
int breathTime = 250;          // How many milliseconds a typical breath lasts
int breathPin = 13;            // pin that the LED is connected to
int breaths = 0;               // How many breaths you've taken
double timer = 60000;             // How many milliseconds to sample for
int timerStep = 25;            // How long to wait between samples
boolean isBreathing = false;   // Whether or not the wearer is currently taking a breath 
double force;       // from A0 
 
void setup() {
  Serial.begin(9600);    // start communicating
  pinMode(13, OUTPUT);   // the LED to blink
  
  while (getForce() > threshold) { 
    delay(25);           // Wait for a breath to be taken
  }
}
 
double getForce() {
   int i;
   double average;
   int samples = 20;
   for (i = 0 ; i < samples ; i = i + 1) {
     average = average + analogRead(A0);
   }
    force = average / samples;
   return force;
}
 
void timerPause(int amount) {
   delay(amount);
   timer = timer - amount; 
}
 
void resetTimer() {
   timer = 60000; 
}
 
void loop() {
  timer = 60000;
  while (timer > 0) {
    //getForce();
    if (getForce() < threshold) {
       digitalWrite(breathPin, HIGH);
       if (isBreathing) {
         delay(20);
       }
       else {
         breaths = breaths + 1;
         isBreathing = true;
         Serial.println("You took a breath. ");
         // timerPause(breathTime);
       }
    }
    else {
      digitalWrite(breathPin, LOW);
      if (isBreathing) {
        Serial.print("Breath complete at ");
         Serial.print(timer/1000);
         Serial.println(" Seconds");
        delay(50);
        isBreathing = false;
      }
    }
    timerPause(timerStep);
  }
  Serial.print("Breaths Per Minute: ");
  Serial.println(breaths);
}
