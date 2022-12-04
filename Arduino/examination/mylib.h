//필요한거 있으면 바로 꺼내서 쓸려고 만든 거지발싸개급 라이브러리 테스트
#include <Arduino.h>
#ifndef mylib_h
#define mylib_h
#include <mylib.h>
class mylib
{
//LED를 켯다 껏다하는 함수
  void flash(char lednum; int duration)
  {
    digitalwrite(lednum, HIGH);
    delay(duration);
    digitalwrite(lednum, LOW;
    delay(duration);
  }
}