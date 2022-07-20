
    #include "uart.h"
    #include "beaverssl.h"
    #include <stdlib.h>
    #include <string.h>

    #define KEY_LEN 0x10
    #define KEY "thistheembseckey"

    int main() {
        uart_init(UART2);

        // TODO ...

        return 0;
    }
    