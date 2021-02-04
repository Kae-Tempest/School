// demo: CAN-BUS Shield, send data
#include <mcp_can.h>
#include <SPI.h>

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 10;

MCP_CAN CAN(SPI_CS_PIN);     


void setup()
{
  Serial.begin(115200);
  // init can bus, baudrate: 500k
  if(CAN.begin(CAN_500KBPS) ==CAN_OK) Serial.print("can init ok!!\r\n");
  else Serial.print("Can init fail!!\r\n");
}

unsigned char Data_Id_0[8] = {0, 1, 2, 3, 4, 5, 6, 7};
unsigned char Data_Id_1[8] = {8, 9, 10, 11, 12, 13, 14, 15};

void loop()
{
  // send data:  id = 0x00, standrad flame, data len = 8, stmp: data buf
  CAN.sendMsgBuf(0x00, 0, 8, Data_Id_0);
  delay(500);                       // send data per 500ms
  
  // send data:  id = 0x01, standrad flame, data len = 8, stmp: data buf
  CAN.sendMsgBuf(0x01, 0, 8, Data_Id_1);  
  delay(500);                       // send data per 500ms
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
