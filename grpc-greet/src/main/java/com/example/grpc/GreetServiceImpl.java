package com.example.grpc;

import com.example.grpc.protocol.GreetRequest;
import com.example.grpc.protocol.GreetResponse;
import com.example.grpc.protocol.GreetServiceGrpc;
import io.grpc.stub.StreamObserver;

public class GreetServiceImpl extends GreetServiceGrpc.GreetServiceImplBase {

    @Override
    public void greet(GreetRequest request, StreamObserver<GreetResponse> responseObserver) {
        String name = request.getName();
        System.out.println("recv from: " + name);
        String greetResp = new StringBuilder()
                .append("Hello, ")
                .append(name)
                .toString();
        GreetResponse response = GreetResponse.newBuilder()
                .setGreeting(greetResp)
                .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
