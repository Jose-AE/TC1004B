#include <Arduino.h>
#include <U8g2lib.h>
#include <Wire.h>

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R0, 14, 12, U8X8_PIN_NONE);

void setup() {
   u8g2.begin();
   u8g2.setPowerSave(0);
}

void loop() {
   u8g2.clearBuffer();                // clear the internal memory
   u8g2.setFont(u8g2_font_10x20_tr);  // choose a suitable font
   u8g2.drawStr(0, 20,
                "Hello World");  // write something to the internal memory
   u8g2.sendBuffer();            // transfer internal memory to the display
   delay(1000);
}
