#define CH1 2
#define CH2 3
#define CH3 4

int readChannel(int channelInput, int minLimit, int maxLimit, int defaultValue){
  int ch = pulseIn(channelInput, HIGH, 50000);
  //if (ch < 100) return defaultValue;
  //return map(ch, 1000, 2000, minLimit, maxLimit);
  return ch;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(CH1, INPUT);
  pinMode(CH2, INPUT);
  pinMode(CH3, INPUT);
}

int ch1Value, ch2Value, ch3Value;

void loop() {
  // put your main code here, to run repeatedly:
  ch1Value = readChannel(CH1, -100, 100, 0);
  ch2Value = readChannel(CH2, -100, 100, 0);
  ch3Value = readChannel(CH3, -100, 100, -100);  
//  Serial.print("Ch1: ");
  Serial.print(ch1Value);
  Serial.print(",");
  Serial.println(ch2Value);
//  Serial.print(" Ch3: ");
//  Serial.println(ch3Value);  
  delay(500);
}
