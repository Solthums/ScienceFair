void setup() {
  Serial.begin(115200);
  Serial.println("start");
}

void loop() {
  Serial.print("0:");
  Serial.println(analogRead(A0));
  Serial.print("1:");
  Serial.println(analogRead(A1));
}
