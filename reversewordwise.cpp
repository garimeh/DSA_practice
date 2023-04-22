
#include<string.h>
void reverseStringWordWise(char str[]) {
    int len = strlen(str);
    char temp;
    //reversing array
    int end = len-1;
    int start = 0;
    while(end>start){
        temp = str[start];
        str[start] = str[end];
        str[end] = temp;
        end--;
        start++;
    }
    
	int i=0;
    start = 0, end = 0;
    
	while(str[i] != '\0'){
		start=i;
		while(str[i] != ' '){
			i++;
        }
		end=i-1;

		while(start<end){
			temp = str[start];
            str[start] = str[end];
            str[end] = temp;
			start++;
			end++ ;
		}
	}
    
    end=i-1;
	while(start<end){
		temp = str[start];
        str[start] = str[end];
        str[end] = temp;
		start++;
		end++ ;
}
}

