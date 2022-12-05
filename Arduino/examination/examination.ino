//기본 시리얼 통신 템플릿
//컴파일러에 의존해서 만들었고 실 기기 테스트는 안해봄
//이거 그대로 써먹지 말고 함수 이름이랑 내용 바꿔가면서 사용하시길 바랍니다.
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
String sC01 = "C01\r\n";
String sC02 = "C02\r\n";

int iButtonState = 0;

//이 부분은 없어도 동작 될거같은데 혹시 모르니 넣어둠.
void funCheckComdand(String Cmd);
void test(void);
void sos(void);
void error(void);

//커맨드와 일치하면 함수 호출
void funCheckComdand (String Cmd) {
  if      ( Cmd == sC01)  test();
  else if ( Cmd == sC02)  sos();
  else                    error();
}

//핀 샛업
//setup 은 반드시 있어야함.
void setup(){
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(sw1, INPUT);
  pinMode(sw2, INPUT);
  Serial.begin(115200); 
  inputString.reserve(200); //inputString용으로 200바이트 예약
}

//loop 는 내용이 없어도 반드시 있어야함.
void loop() { 
  if (Serial.available()) { 
    String sCommand = Serial.readString(); 
    funCheckComdand(sCommand); 
  }
   // 푸시 버튼 값의 상태를 읽습니다.
  iButtonState = digitalRead(sw1);
  if (iButtonState == LOW) {
    buttonON();
  } else {
    buttonOFF();
  }
}

//테스트용 함수
void test() {
  digitalWrite(led5, HIGH);
  delay(250);
  digitalWrite(led5, LOW);
  delay(10);
  Serial.print("TEST DONE NO ERROR.\n");
}

//테스트용으로 만든 LED를 이용해 sos를 모스부호로 출력하는 함수
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

//버튼이 ON일때 작동
void buttonON(){
  flash(250);
  delay(250);
}

//버튼이 OFF일때 작동
void buttonOFF(){
  flash(120);
  delay(120);
}

//알맞지 않은 커맨드가 입력 되었을때 호출
void error(){
  Serial.print("Invalid command.\n");
}

//지연시간을 입력하면 그 시간동안 13번 LED를 켰다 꺼주는 기능
//사용 예 flash(200); = 200ms 동안 13번 LED를 켰다 꺼준다
void flash(int duration) {
  digitalWrite(led5, HIGH);  //LED 켜기
  delay(duration);              
  digitalWrite(led5, LOW);    //LED 끄기
  delay(duration);
}
