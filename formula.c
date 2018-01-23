int genFormula(atom *pAtom,int **output,int *size){
    int at = pAtom->atomicNumber;
    int i, j,swapped = 1, li = -1, exists=0, temp, tt;
    
    if (pAtom == NULL) return -1;
    if (output == NULL) return -1;
    if (*size%2 || size == NULL ) return -1;
    
    
    for (i = 0; i < *size; i+=2) {
        if ((*output)[i] == at) {
            (*output)[i+1]++;
            exists =1;
            break;
        }
        if ((*output)[i+1] != 0) {
            li = i+1;
        }
    }
    li++;
    
    if (!exists) {
        (*output)[li]=at;
        (*output)[li+1]=1;
    }
    
    while (swapped) {
        swapped = 0;
        for (j = 0; j < *size-2; j+=2) {
            if ((*output)[j] > (*output)[j+2] && (*output)[j+2] != 0) {
                temp = (*output)[j];
                tt = (*output)[j+1];
                (*output)[j] = (*output)[j+2];
                (*output)[j+1] = (*output)[j+3];
                (*output)[j+2] = temp;
                (*output)[j+3] = tt;
                
                swapped = 1;
            }
        }
    }
    if (pAtom->bondList == NULL) return 0;
    
    
    bondNode *jamesbond = pAtom->bondList->pNext;
    
    while (jamesbond != NULL) {
        genFormula((jamesbond->pAtom), output, size);
        jamesbond = jamesbond->pNext;
    }
    if (pAtom->bondList->pAtom != NULL) {
        genFormula((pAtom->bondList->pAtom), output, size);
    }
    
    return 0;
}