
    #include "uart.h"
    #include "beaverssl.h"
    #include <stdlib.h>
    #include <string.h>

    #define KEY_LEN 0x10
    #define KEY "thistheembseckey"

    int main() {
        uart_init(UART2);


        // TODO ...


        // Reads the flag for you!
        char flag[256];
        for(int i = 0; i < 256; i++) {
            flag[i] = uart_read(UART2, BLOCKING, &ret);
            if (flag[i] == '\n')
                break;
        }

        return 0;
    }
    