#include <SD.h>
#include <SPI.h>
#include <TMRpcm.h>

#define SD_ChipSelectPin 10
TMRpcm audio;
int file_number = 0;
bool recording_now = false;
const int button_pin = 2;
const int recording_led_pin = 3;
const int mic_pin = A0;
const int sample_rate = 16000;

void button_pushed() {
  char file_name[20] = "";
  itoa(file_number,file_name,10);
  strcat(file_name,".wav");

  if (!recording_now) {
    SD.open(file_name);
    recording_now = true;
    digitalWrite(recording_led_pin, HIGH);
    audio.startRecording(file_name, sample_rate, mic_pin); 
    Serial.println(file_name);
  }
  else {
    recording_now = false;
    digitalWrite(recording_led_pin, LOW);
    audio.stopRecording(file_name);
    file_number++;
  }
}

void setup() {
  Serial.begin(9600);
  Serial.println("loading...");

  pinMode(mic_pin, INPUT);
  pinMode(recording_led_pin, OUTPUT);
  pinMode(button_pin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(button_pin), button_pushed, FALLING);
  SD.begin(SD_ChipSelectPin);
  audio.CSPin = SD_ChipSelectPin;
}

void loop() {}