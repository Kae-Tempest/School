// demo: CAN-BUS Shield, receive data
#include <mcp_can.h>
#include <SPI.h>

unsigned char Flag_Recv = 0;
unsigned char len = 0;
unsigned char buf[8];
char str[20];
int CAN_Id;

// the cs pin of the version after v1.1 is default to D9
// v0.9b and v1.0 is default D10
const int SPI_CS_PIN = 10;

MCP_CAN CAN(SPI_CS_PIN);     

void setup()
{
  CAN.begin(CAN_500KBPS);                       // init can bus : baudrate = 500k
  attachInterrupt(0, MCP2515_ISR, FALLING);     // start interrupt
  Serial.begin(115200);
  
  // Test XM ////////////////////////////////////////////////////////////////////////
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void MCP2515_ISR()
{
    Flag_Recv = 1;
}

void loop()
{
    if(Flag_Recv)                           // check if get data
    {
      Flag_Recv = 0;                        // clear flag
      
      Serial.println("CAN_BUS GET DATA!");
      
      // Test XM ////////////////////////////////////////////////////////////////////////
      CAN_Id = CAN.getCanId();
      CAN.readMsgBuf(&len, buf);            // read data,  len: data length, buf: data buf
      Serial.print("data len = ");
      Serial.println(len);
      
      for(int i = 0; i<len; i++)            // print the data
      {
        Serial.print(buf[i]);Serial.print("\t");
      }
      Serial.println();
      Serial.println();
      
      if (CAN_Id == 0)
      {
        Serial.println("CAN_Id = 0");
        digitalWrite(3,0);
        digitalWrite(4,1);
      }
        
      if (CAN_Id == 1)
      {
        Serial.println("CAN_Id = 1");
        digitalWrite(3,1);
        digitalWrite(4,0);
      }  
    }    
}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
