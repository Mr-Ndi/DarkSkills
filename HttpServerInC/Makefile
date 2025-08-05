all: http_server

http_server: main.o server.o utils.o
	gcc main.o server.o utils.o -o http_server

main.o: main.c
	gcc -c main.c

server.o: server.c
	gcc -c server.c

utils.o: utils.c
	gcc -c utils.c

clean:
	rm -f *.o http_server
