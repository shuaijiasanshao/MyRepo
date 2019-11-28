package com.example.grpc;

import com.example.grpc.protocol.GreetRequest;
import com.example.grpc.protocol.GreetResponse;
import com.example.grpc.protocol.GreetServiceGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class GrpcGreetClient {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder
                .forAddress("localhost", 50055)
                .usePlaintext()
                .build();
        GreetServiceGrpc.GreetServiceBlockingStub stub = GreetServiceGrpc.newBlockingStub(channel);
        GreetRequest request = GreetRequest.newBuilder()
                .setName("Jack")
                .build();
        GreetResponse response = stub.greet(request);
        System.out.println(response.getGreeting());
    }
}
