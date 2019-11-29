package com.example.grpc.grpcClient;

import com.example.grpc.protocol.GreetRequest;
import com.example.grpc.protocol.GreetResponse;
import com.example.grpc.protocol.GreetServiceGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import java.util.concurrent.TimeUnit;


public class GrpcGreetClient {

    private final  ManagedChannel channel;

    private final GreetServiceGrpc.GreetServiceBlockingStub blockingStub;

    public GrpcGreetClient(String ip, int port) {
        channel = ManagedChannelBuilder
                .forAddress(ip, port)
                .usePlaintext()
                .build();
        blockingStub = GreetServiceGrpc.newBlockingStub(channel);
    }

    public GreetResponse greet(String name){
        GreetRequest request = GreetRequest.newBuilder()
                .setName(name)
                .build();
        return blockingStub.greet(request);
    }

    public void shutdown() throws InterruptedException {
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    public static void main(String[] args) throws InterruptedException {
        GrpcGreetClient grpcGreetClient = new GrpcGreetClient("localhost", 50055);
        System.out.println(grpcGreetClient.greet("Jack").getGreeting());
        grpcGreetClient.shutdown();
    }
}
