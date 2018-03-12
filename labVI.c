//
//  main.c
//  LabVI
//
//  Created by Siddhant Jain on 2018-03-10.
//  Copyright © 2018 Siddhant Jain. All rights reserved.
//

#include <stdio.h>

unsigned char prng(unsigned char x, unsigned char pattern) {
    unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
    unsigned char r = x >> 1;        /* shift right   */
    unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
    r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
    return r^pattern;
}

unsigned char FSR(unsigned char x) {
    unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
    unsigned char r = x >> 1;        /* shift right   */
    unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
    r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
    return r;
}

int cryp(char *data,unsigned int size,unsigned char password) {// change back to crypt later
    unsigned char prngVal = password;
    
    for (int i =0; i < size; i++) {
        prngVal = prng(prngVal,0xb8);
        data[i] = (data[i]) ^ prngVal;
    }
    return 0;
}

int main() {
    unsigned char a = '0';
    /*for (int i = 0; i<128; i++) {
        //printf("%c, %d, %d\n",a+i, a+i, FSR(a+i));
        printf("%c, %d, %d\n",a+i, a+i, prng(a+i, 0xb8));
    }*/
    char data[] = {"saachi"};
    cryp(data, 6, a);
    for (int i =0; i < 6; i++) {
        printf("%d ", data[i]);
    }
    
    
    
    return 0;
}
