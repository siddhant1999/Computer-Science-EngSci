/* chemistry.c
 mathaine@ecf
 
 This code illustrates a few things:
 1. Another example of defining structs
 2. Recursively defined structs (inter-related)
 3. Another dynamic data structures to suit a particular problem
 (specifically, how to represent molecular structure)
 4. How to do recursion where each recursion is "aware" of
 its recursion depth
 (note how I print spaces in order to structure the output
 in a pretty manner --- the spaces are a function of recursion
 depth).
 
 Note: bondList is a linked list, however, I only added a single
 function for ll management, bondList_add, since that's all the
 application required.
 
 None of this required any special intuition. We just designed
 this "ad hoc" based on the requirements of the application, using
 the "dynamicism" we learned from our linked list lesson.
 */

#include<stdio.h>
#include<stdlib.h>

struct bondNode;
struct atom;

struct bondNode {
    int strength;
    struct atom *pAtom;
    struct bondNode *pNext;
};

struct atom {
    int atomicNumber;
    struct bondNode *bondList;
};

typedef struct bondNode bondNode;
typedef struct atom atom;

int addBond(atom *pAtom, int strength, atom *pAtom2);
atom *createAtom(int atomicNumber);
int bondList_add(bondNode **ppList, int strength, atom *pAtom);
int printAtom(atom *pAtom,int n);
int printBonds(bondNode *pList,int n);

atom *createAtom(int atomicNumber) {
    atom *p=(atom *)malloc(sizeof(atom));
    p->atomicNumber = atomicNumber;
    p->bondList = NULL;
    return p;
}

int bondList_add(bondNode **ppList, int strength, atom *pAtom) {
    if (ppList == NULL) { return -1; }
    if (*ppList == NULL) {
        *ppList = (bondNode *)malloc(sizeof(bondNode));
        (*ppList)->strength=strength;
        (*ppList)->pAtom=pAtom;
        (*ppList)->pNext=NULL;
        return 0;
    } else {
        return bondList_add( &((*ppList)->pNext), strength, pAtom );
    }
}

int addBond(atom *pAtom, int strength, atom *pAtom2) {
    if (pAtom == NULL) { return -1; }
    
    return bondList_add( &(pAtom->bondList), strength, pAtom2);
}

int printAtom(atom *pAtom,int n) {
    int i;
    if (pAtom == NULL) {
        printf("black hole sun...\n");
    } else {
        for(i=0;i<n;i=i+1) {
            printf("   ");
        }
        printf("-> atomic number=%d: bonded to:\n",pAtom->atomicNumber);
        //printBonds(pAtom->bondList,n);
        for(i=0;i<n;i=i+1) {
            printf("   ");
        }
        printf("<- atomic number=%d\n",pAtom->atomicNumber);
        
    }
    return 0;
}

int printBonds(bondNode *pList,int n) {
    int i;
    for(i=0;i<n;i=i+1) {
        printf("   ");
    }
    if (pList == NULL) {
        printf("no bonds\n");
    } else {
        printf("strength=%d connected to:\n",pList->strength);
        printAtom(pList->pAtom,n+1);
        printBonds(pList->pNext,n);
    }
    return 0;
}
int counter = 1;

/*
Let's brainstrom
 so we need to first determine all of the atoms in the structure
 then we need the count of each atom
 given a starting node let's traverse the graph and append each new element that doesn't exist to the array
 to know if it does exist we will just do a linear search of the even indexes
 if it does exist just increment the following odd index
 
 
 */

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


int main(void) {
    int r=0;
    atom *S;
    atom *tmp1,*tmp2;
    
    S = createAtom(16);
    
    tmp1=createAtom(8);
    r=addBond(S,2,tmp1);
    
    tmp1=createAtom(8);
    r=addBond(S,2,tmp1);
    
    tmp1=createAtom(8);
    tmp2=createAtom(1);
    r=addBond(tmp1,1,tmp2);
    r=addBond(S,1,tmp1);
    
    tmp1=createAtom(8);
    tmp2=createAtom(1);
    r=addBond(tmp1,1,tmp2);
    r=addBond(S,1,tmp1);
    int *output= (int *) malloc(sizeof(int)*8);
    output[0] = 0;
    output[1] = 0;
    output[2] = 0;
    output[3] = 0;
    output[4] = 0;
    output[5] = 0;
    output[6] = 0;
    output[7] = 0;
    int *k = output;
    int **t = &k;
    int y = 8;
    //printf("%p\n", output);
    
    //printf("%d %d %d %d %d %d %d %d\n\n", output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7]);
    genFormula(S,&output, &y);
    printf("%d %d %d %d %d %d %d %d\n\n", output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7]);
    //printAtom(S,0);
    return 0;
}
