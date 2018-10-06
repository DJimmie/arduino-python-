

int analogPin=3;
int data=0;




void setup() {
  Serial.begin(9600);    // setup serial


}

void loop() {
  data=analogRead(analogPin);
  Serial.println(data);

}
