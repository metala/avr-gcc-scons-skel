#include <avr/io.h>
#include <util/delay.h>

#include "mega16.h"

#define BAUDRATE 38400

static void sendchar(uint8_t data)
{
	while (!(UART_STATUS & (1<<UART_TXREADY)));
	UART_DATA = data;
}

static uint8_t recvchar(void)
{
	while (!(UART_STATUS & (1<<UART_RXREADY)));
	return UART_DATA;
}

void init_uart()
{
	// Set baud rate
	UART_BAUD_HIGH = (UART_CALC_BAUDRATE(BAUDRATE)>>8) & 0xFF;
	UART_BAUD_LOW = (UART_CALC_BAUDRATE(BAUDRATE) & 0xFF);

	UART_CTRL = UART_CTRL_DATA;
	UART_CTRL2 = UART_CTRL2_DATA;
	asm("NOP");asm("NOP");
	
}

#define TL_PORT PORTC
#define TL_DDR DDRC

void main() {
	uint8_t c;
	
	TL_DDR  = 0b11111111;
	TL_PORT = 0b00000000; 

	init_uart();
	
	while (1) { 
		c = recvchar();
		
		TL_PORT = c;
		
		asm("NOP");asm("NOP");
		sendchar(TL_PORT);
	}
}
