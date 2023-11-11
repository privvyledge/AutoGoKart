#define Rudder 2
#define THRO 3
#define ELEV 4
#define STEER 5
#define sWA 6
#define sWD 7
#define sWB 8
#define sWC 9
#define sWE 10
#define sWF 11


int readChannel(int channelInput, int minLimit, int maxLimit, int defaultValue){
  int ch = pulseIn(channelInput, HIGH, 50000);
  if (ch < 100) return defaultValue;
  int mapped_input = map(ch, 1000, 2000, minLimit, maxLimit);
  return mapped_input;
  //return ch;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(THRO, INPUT);
  pinMode(STEER, INPUT);
  pinMode(Rudder, INPUT);
  pinMode(ELEV, INPUT);
  pinMode(sWA, INPUT);
  pinMode(sWB, INPUT);
  pinMode(sWC, INPUT);
  pinMode(sWD, INPUT);
  pinMode(sWE, INPUT);
  pinMode(sWF, INPUT);
}

// uint8_t throttle_cmd, steer_angle, Rudder_angle, Elev_height, sWA_value, sWB_value, sWC_value, sWD_value, sWE_value, sWF_value;
uint8_t cmd[10];

void loop() {
  // put your main code here, to run repeatedly:
  cmd[0] = readChannel(THRO, 0, 100, 0);
  cmd[1] = readChannel(STEER, 0, 100, 0);
  cmd[2] = readChannel(Rudder, 0, 100, 0);
  cmd[3] = readChannel(ELEV, 0, 100, 0);
  cmd[4] = readChannel(sWA, 0, 100, 0);
  cmd[5] = readChannel(sWB, 0, 100, 0);
  cmd[6] = readChannel(sWC, 0, 100, 0);
  cmd[7] = readChannel(sWD, 0, 100, 0);
  cmd[8] = readChannel(sWE, 0, 100, 0);
  cmd[9] = readChannel(sWE, 0, 100, 0);

  // uint8_t buf[10] = {throttle_cmd, steer_angle, Rudder_angle, Elev_height, sWA_value, sWB_value, sWC_value, sWD_value, sWE_value, sWF_value};

  Serial.write(cmd,sizeof(cmd));
  Serial.write("\n");
  
//  Serial.print("throttle cmd: ");
  //Serial.print(throttle_cmd);
  //Serial.print(",");
  //Serial.println(steer_angle);
  //Serial.print(",");
  //Serial.print(Rudder_angle);
  //Serial.print(",");
  //Serial.println(Elev_height);
  //Serial.print(",");
  //Serial.print(sWA_value);
  //Serial.print(",");
  //Serial.print(sWB_value);
  //Serial.print(",");
  //Serial.print(sWC_value);
  //Serial.print(",");
  //Serial.print(sWD_value);
  //Serial.print(",");
  //Serial.print(sWE_value);
  //Serial.print(",");
  //Serial.println(sWF_value);
}
