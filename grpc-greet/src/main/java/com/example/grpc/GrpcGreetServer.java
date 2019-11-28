package com.example.grpc;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class GrpcGreetServer {

    public static void main(String[] args) throws InterruptedException, IOException {
        int port = 50055;
        Server server = ServerBuilder
                .forPort(port)
                .addService(new GreetServiceImpl())
                .build();
        server.start();
        server.awaitTermination();
    }
}
