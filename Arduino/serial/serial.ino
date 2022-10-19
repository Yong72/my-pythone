  #include <stdio.h> 
// ------------------------------------------------------------------------------------------------------ 
// set pin numbers : 
const int ledPin =  13;      // the number of the LED pin 

// Serial comunication :  
String inputString = "";         // a string to hold incoming data 
boolean stringComplete = false;  // whether the string is complete 

// Serial Communication Protocal 
String sC01 = "C01\r\n";  
String sC02 = "C02\r\n";  

// My Funtions 
void funCheckComdand(String Cmd); 
void myfun01(void); 
void myfun02(void); 
void myfun03(void); 

// ------------------------------------------------------------------------------------------------------ 

void setup() { 
  pinMode(ledPin, OUTPUT);  // Control Pin for the LED // HIGH: On, LOW: Off 
  Serial.begin(115200); 
  inputString.reserve(200); // reserve 200 bytes for the inputString 
}

// ------------------------------------------------------------------------------------------------------ 

void loop() { 
  if (Serial.available()) { 
    String sCommand = Serial.readString(); 
    funCheckComdand(sCommand); 
  } 

  // Serial.print("waiting for the command..."); 
  // delay(100); 
} //End of (main)loop 

// ------------------------------------------------------------------------------------------------------ 

void funCheckComdand(String Cmd) 
{
  if     ( Cmd == sC01 )   myfun01(); 
  else if( Cmd == sC02 )   myfun02(); 
  else                     myfun03();      
} 

// ------------------------------------------------------------------------------------------------------ 

void myfun01(void) 
{     
  for(int i=0; i<5; i++) 
  {   
    digitalWrite(ledPin, HIGH);  
    delay(1000);  
    digitalWrite(ledPin, LOW); 
    delay(1000);
  } 

  digitalWrite(ledPin, HIGH); 
  delay(10);  
  Serial.print("Processing the C01 function(v2).\n"); 
} 

void myfun02(void) 
{     
  for(int i=0; i<10; i++) 
  {   
    digitalWrite(ledPin, HIGH);  
    delay(100);  
    digitalWrite(ledPin, LOW); 
    delay(100); 
  }  
  digitalWrite(ledPin, HIGH); 
  delay(10);    
  Serial.print("Processing the C02 function(v2).\n");  
} 

void myfun03(void) 
{    
  digitalWrite(ledPin, LOW); 
  delay(10); 
  Serial.print("It is not the commands.\n");  
} 
