.PHONY: build run

DatabaseApp.class: DatabaseApp.java
	javac DatabaseApp.java

build: DatabaseApp.class

run: build
	java -cp .:sqlite-jdbc-3.39.3.0.jar DatabaseApp