
            // Password to unlock ReverseEngineeringChallenge.c (=filename)

            #include <stdio.h>
            #include <stdint.h>
            #include <string.h>
            #include <ctype.h>
            #include <stdlib.h>

            int shuffle(int entry) {
                int i = 0;
                int to = 798336000;
                int ret = 1;
                if (entry == 1) {
                    while (i < 12) {
                        ret += to;
                        ret /= 7;
                        if (i%5 ==0) {
                            printf("%s", "Calculating...");
                        }
                        printf("\n");
                        i += 1;
                        to /= i;
                    }
                }
                else if (entry == 2) {
                    while (i < 12) {
                        ret += to;
                        ret /= 7;
                        if (i%5 ==0) {
                            printf("%s", "Calculating...");
                        }
                        printf("\n");
                        i += -1;
                        to /= i;
                    }
                }
                else {
                    printf("%s", "Quitting...");
                    exit(0);
                }
                return 20;
            }

            int main() {

                int count = 0;
                int c = 10;
                printf("%s", "Welcome! Enter 4 to load, 2 to start");
                int toSend = 2;
                printf("\n");
                count += 1;
                while (c >= 0) {
                    if (c%10 == 0) {
                        printf("%s", "Loading...");
                        printf("\n\n");
                    }
                    c += 1;
                }
                count *= 4; 
                char data[] = "100101101110";
                int x = 0;
                int data2[12];
                while (count < 12) {
                    if (data[count] == '1') {
                        data2[count] = 0;
                    }
                    else {
                        data2[count] = 1;
                    }
                    count += 1;
                }
                int enter = shuffle(data2[0]);
                char hex2ASCII[] = "31 30 32 20 31 30 35 20 31 30 38 20 31 30 31 20 31 31 30 20 39 37 20 31 30 39 20 31 30 31 20 39 37 20 37 36 20 31 31 32 20 37 32 20 39 34 20 39 35 20 35 30 20 39 35 20 31 31 30 20 31 31 37 20 35 31 20 36 30 20 34 35 20 39 32 20 35 31 20 38 32 20 34 39 20 34 30 20 39 34 20 37 36";
                printf("%s", hex2ASCII);
                printf("\n\n");
                enter += count;
                enter = enter%4;
                int stop = 0;
                char toASCII[100];
                while (stop < enter) {
                    toASCII[stop] = hex2ASCII[stop];
                }
                printf("%s", "toASCII: ");
                printf("%s", toASCII);
                printf("\n");
                int sent = shuffle(toSend);
                enter *= 2;
                char intel[4];
                if (sent == 20) {
                    intel[0] = '0';
                    intel[1] = 'x';
                    intel[2] = '2';
                    intel[3] = '0';
                }
                else {
                    intel[0] = '0';
                    intel[1] = 'x';
                    intel[2] = '2';
                    intel[3] = '0';
                }
                count += 1;
                if (intel == "0x20") {
                    printf("%s", "Quitting processes...");
                    exit(0);
                }
                else {
                    printf("%s", "2nd conv to plaintext...");
                }
                return 0;
            }

            