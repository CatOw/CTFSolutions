#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
		printf("res: [%d] (0x%08x) ip[%d]: %d (0x%08x)\n", res, res, i, ip[i], ip[i]);
        }
	printf("res: %d (0x%08x)\n", res, res);
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
	printf("Input is %s\n", argv[1]);
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes (%lu given)\n", strlen(argv[1]));
                return 0;
        }
        if(hashcode == check_password( argv[1] )){
                printf("working");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
