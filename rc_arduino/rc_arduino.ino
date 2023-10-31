#define THRO 2
#define STEER 3
#define sWA 5
#define sWD 6
#define sWB 7
#define sWC 8
#define sWE 9
#define sWF 10

int readChannel(int channelInput, int minLimit, int maxLimit, int defaultValue){
  int ch = pulseIn(channelInput, HIGH, 50000);
  //if (ch < 100) return defaultValue;
  //return map(ch, 1000, 2000, minLimit, maxLimit);
  return ch;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(THRO, INPUT);
  pinMode(STEER, INPUT);
  pinMode(sWA, INPUT);
  pinMode(sWB, INPUT);
  pinMode(sWC, INPUT);
  pinMode(sWD, INPUT);
  pinMode(sWE, INPUT);
  pinMode(sWF, INPUT);
}

int throttle_cmd, steer_angle, sWA_value, sWB_value, sWC_value, sWD_value, sWE_value, sWF_value;

void loop() {
  // put your main code here, to run repeatedly:
  throttle_cmd = readChannel(THRO, -100, 100, 0);
  steer_angle = readChannel(STEER, -100, 100, 0);
  sWA_value = readChannel(sWA, -100, 100, 0);
  sWB_value = readChannel(sWB, -100, 100, 0);
  sWC_value = readChannel(sWC, -100, 100, 0);
  sWD_value = readChannel(sWD, -100, 100, 0);
  sWE_value = readChannel(sWE, -100, 100, 0);
  sWF_value = readChannel(sWE, -100, 100, 0);
  
//  Serial.print("throttle cmd: ");
  Serial.print(throttle_cmd);
  Serial.print(",");
  Serial.println(steer_angle);
  Serial.print(",");
  Serial.print(sWA_value);
  Serial.print(",");
  Serial.print(sWB_value);
  Serial.print(",");
  Serial.print(sWC_value);
  Serial.print(",");
  Serial.print(sWD_value);
  Serial.print(",");
  Serial.print(sWE_value);
  Serial.print(",");
  Serial.println(sWF_value);
  delay(500);
}
