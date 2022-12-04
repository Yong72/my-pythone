//기본 시리얼 통신 템플릿
#include <stdio.h>


//SET Pin numbers
//9번 ~ 13번까지 LED 포트, 7~8은 스위치 포트
const int led1 =   9;
const int led2 =  10;
const int led3 =  11;
const int led4 =  12;
const int led5 =  13;
const int sw1 = 7;
const int sw2 = 8;

//시리얼 커뮤니케이션
String inputString = "";         //수신데이터를 저장하는 문자열
boolean stringComplete = false;  //문자열이 완전한지 확인한다

//시리얼 커뮤니케이션 프로토콜
//이 템플릿에서 기본적으로 재공하는건 2가지 프로토콜을 재공함.
String sc01 = "c01\r\n";
String sc02 = "c02\r\n";

int iButtonState = 0;

void funCheck (String Cmd) {
  if      ( Cmd == sc01)  test();
  else if ( Cmd == sc02)  sos();
  else                    error();
}

void setup(){
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(sw1, INPUT);
  pinMode(sw2, INPUT);
  Serial.begin(115200); 
  inputString.reserve(200);
}

void loop() { 
  if (Serial.available()) { 
    String sCommand = Serial.readString(); 
    funCheck(sCommand); 
  } 
   // read the state of the pushbutton value:
  iButtonState = digitalRead(sw1);
  if (iButtonState == LOW) {
    buttonON();
  } else {
    buttonOFF();
  }
}

void test() {
  digitalWrite(led5, HIGH);
  delay(250);
  digitalWrite(led5, LOW);
  delay(10);
  Serial.print("TEST DONE NO ERROR.\n");
}

void sos() {
  for (int i=0;  i<3; i++)
  {
    flash(200); flash(200); flash(200);
  //S
    delay(300);
    flash(500); flash(500); flash(500);
  //O
    flash(200); flash(200); flash(200);
  //S
    delay(320);
  }
  Serial.print("Sending SOS signal for 3time.\n"); 
}

void buttonON(){
  delay(10);
  digitalWrite(led5, HIGH);
  delay(250);
  digitalWrite(led5, LOW);
  delay(250);
}

void buttonOFF(){
    delay(10);
  digitalWrite(led5, HIGH);
  delay(120);
  digitalWrite(led5, LOW);
  delay(120);
}

void error(){
  Serial.print("Invalid command.\n");
}

void flash(int duration) {
  digitalWrite(led5, HIGH);  //LED 켜기
  delay(duration);              
  digitalWrite(led5, LOW);    //LED 끄기
  delay(duration);
}
