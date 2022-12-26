const int PIN_MFC1_VALUE = 13;
const int PIN_MFC2_VALUE = 11;
const int PIN_MFC3_VALUE = 10;
const int PIN_MFC1_OUTPUT = A0;
const int PIN_MFC2_OUTPUT = A1;
const int PIN_MFC3_OUTPUT = A2;

int voltage = 0.0;
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    delay(20);
    long val = Serial.parseInt();
    int input1 = val / 1000000;
    int input2 = (val % 1000000) / 1000;
    int input3 = (val % 1000);
    analogWrite(PIN_MFC1_VALUE, input1);
    analogWrite(PIN_MFC2_VALUE, input2);
    analogWrite(PIN_MFC3_VALUE, input3);
    while (Serial.available() > 0)
    {
      char t = Serial.read();
    }
  }
  int output1 = analogRead(PIN_MFC1_OUTPUT);
  int output2 = analogRead(PIN_MFC2_OUTPUT);
  int output3 = analogRead(PIN_MFC3_OUTPUT);
  Serial.print(output1 + 100);
  Serial.print(output2 + 100);
  Serial.println(output3 + 100);
  delay(100);
}