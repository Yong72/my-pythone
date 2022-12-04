 #include <stdio.h> 
// ------------------------------------------------------------------------------------------------------ 
// set pin numbers : 
const int led1 =   9;
const int led2 =  10;
const int led3 =  11;
const int led4 =  12;
const int led5 =  13;
const int sw1 = 7;
const int sw2 = 8;

// Serial comunication :  
String inputString = "";         // a string to hold incoming data 
boolean stringComplete = false;  // whether the string is complete 

// Serial Communication Protocal 
String sC01 = "C01\r\n";  
String sC02 = "C02\r\n";  
String sC03 = "C03\r\n";  
String sC04 = "C04\r\n";

// variables will change:
int iButtonState = 0;         // variable for reading the pushbutton status

// My Funtions 
void funCheckComdand(String Cmd); 
void myfun01(void); 
void myfun02(void); 
void myfun03(void); 
void myfun04(void);
void myfun05(void);

void funCheckComdand(String Cmd) 
{
  if     ( Cmd == sC01 )   myfun01(); 
  else if( Cmd == sC02 )   myfun02(); 
  else if( Cmd == sC03 )   myfun04();
  else if( Cmd == sC04 )   myfun05();
  else                     myfun03();      
} 
// ------------------------------------------------------------------------------------------------------ 

void setup() { 
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(sw1,  INPUT);
  pinMode(sw2,  INPUT);
  Serial.begin(115200); 
  inputString.reserve(200); // reserve 200 bytes for the inputString 
}

// ------------------------------------------------------------------------------------------------------ 

void loop() { 
  if (Serial.available()) { 
    String sCommand = Serial.readString(); 
    funCheckComdand(sCommand); 
  } 
   // read the state of the pushbutton value:
  iButtonState = digitalRead(sw1);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (iButtonState == LOW) {
    // turn LED on:
    myfun02();
  } else {
    // turn LED off:
    myfun03();
  }

  // Serial.print("waiting for the command..."); 
  // delay(100); 
} //End of (main)loop 

// ------------------------------------------------------------------------------------------------------ 



// ------------------------------------------------------------------------------------------------------ 

void myfun01(void) 
{     
  for(int i=0; i<5; i++) 
  {   
    digitalWrite(led5, HIGH);  
    delay(1000);  
    digitalWrite(led5, LOW); 
    delay(1000);
  } 

  digitalWrite(led5, HIGH); 
  delay(10);  
  Serial.print("Processing the C01 function(v2).\n"); 
} 

void myfun02(void) 
{     
  for(int i=0; i<10; i++) 
  {   
    digitalWrite(led5, HIGH);  
    delay(100);  
    digitalWrite(led5, LOW); 
    delay(100); 
  }  
  digitalWrite(led5, HIGH); 
  delay(10);    
  Serial.print("Processing the C02 function(v2).\n");  
} 

void myfun03(void) 
{    
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW); 
  digitalWrite(led4, LOW);
  digitalWrite(led5, LOW);
  delay(10);
} 

void myfun04(void)
{
  for (int i=0;  i<3; i++)
  {
    flash(200); flash(200); flash(200);
  //S
  delay(300);
  
  flash(500); flash(500); flash(500);
  //O
  
  flash(200); flash(200); flash(200);
  //S
  delay(1000);
  }
  Serial.print("Processing the C03 function(v2).\n"); 
}

void myfun05(void)
{
  for (int i=0; i<5; i++)
  {
  digitalWrite(led1, HIGH); 
  delay(150);  
  digitalWrite(led2, HIGH); 
  delay(150);  
  digitalWrite(led3, HIGH); 
  delay(150);  
  digitalWrite(led4, HIGH); 
  delay(150);  
  digitalWrite(led5, HIGH); 
  delay(150);  
  digitalWrite(led1, LOW); 
  delay(150);  
  digitalWrite(led2, LOW); 
  delay(150);  
  digitalWrite(led3, LOW); 
  delay(150);  
  digitalWrite(led4, LOW); 
  delay(150);  
  digitalWrite(led5, LOW); 
  delay(150);  
  }
  Serial.print("Processing the C04 function(v2).\n"); 
}

void flash(int duration) {
  digitalWrite(led5, HIGH);  //LED 켜기
  delay(duration);              
  digitalWrite(led5, LOW);    //LED 끄기
  delay(duration);
}








