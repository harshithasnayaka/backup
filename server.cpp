//here need to write a server only code
#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include<iostream>
#include <string.h>

#define SERVER_HOST 0
#define PORT_NO 15050
#define BUFFER_SIZE = 4096
#define SEPARATOR = "<SEPARATOR>"
char *filename = "file.txt";
int main()
{
	//socklen_t addrlen;
	
	struct sockaddr_in addr_con;
	int addrlen = sizeof(addr_con);
	addr_con.sin_family = AF_INET;
	addr_con.sin_port = htons(PORT_NO);
	addr_con.sin_addr.s_addr = INADDR_ANY;
	char buffer[1024] = { 0 };
	FILE* fp;
    struct sockaddr_in new_addr;
    socklen_t addr_size;
    int new_sock;
    //char* filename = "file.txt";



//create socket
int s = socket(AF_INET, SOCK_DGRAM, SERVER_HOST);
//int s = socket(AF_INET, SOCK_STREAM, 0);
//binding
int e = bind(s, (struct sockaddr*)&addr_con, sizeof(addr_con));
  if(e < 0) {
    perror("Error in bind");
    exit(1);
  }
  std::cout<<"Binding successfull.\n";
 
//s.bind(SERVER_HOST,PORT_NO);
//s.listen(5);
if(listen(s, 5) == 0)
{
    std::cout<<"Listening....\n";
 }
 else
 {
    perror("Error in listening");
    exit(1);
 }
   addr_size = sizeof(new_addr);
   new_sock = accept(s, (struct sockaddr*)&new_addr, &addr_size);
   int valread = read(new_sock, buffer, 1024);
    printf("%s\n", buffer);
    send(new_sock, filename,strlen(filename),0);
    //sendFile(fp, net_buf, NET_BUF_SIZE);
    
    
  // closing the connected socket
    close(new_sock);
  // closing the listening socket
    shutdown(s, SHUT_RDWR);
    return 0;




}