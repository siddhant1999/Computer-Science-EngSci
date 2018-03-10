#include <stdio.h>

unsigned char FSR(unsigned char x) {
    unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
    unsigned char r = x >> 1;        /* shift right   */
    unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
    r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
    return r;
}

int main() {
    char a = 0;
    for (int i = 0; i<150; i++) {
        printf("%c, %d\n",a+i, FSR(a+i));
    }
    
    return 0;
}
