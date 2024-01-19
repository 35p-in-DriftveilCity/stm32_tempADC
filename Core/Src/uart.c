/*
 * uart.c
 *
 *  Created on: Jan 10, 2024
 *      Author: USER
 */

#include "uart.h"

UART_HandleTypeDef *huart; // variable declare

void initUart(UART_HandleTypeDef *inHuart){
	huart = inHuart;// huart's address is inHuart's address
}

int _write(int file, char *p, int len){
	HAL_UART_Transmit(huart, (uint8_t *)p, len, len);
	return len;
}
