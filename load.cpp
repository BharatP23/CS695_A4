#include <bits/stdc++.h>
#include <unistd.h>
#include <sys/mman.h>

using namespace std;


int main() {
   
    void *mem = mmap(NULL, 10000*4096, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (mem == MAP_FAILED) {
        return 1;
    }

    memset(mem, 1, 10000*4096);

    while (1) {
    	for(int i=0;i<10000*4096;i++)
    		char x=*((char *)mem+i);
        sleep(1); 
    }

    return 0;
}
