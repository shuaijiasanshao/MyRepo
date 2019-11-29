package com.example.jemeter.greetPlugin;

import com.example.grpc.grpcClient.GrpcGreetClient;
import com.example.grpc.protocol.GreetResponse;
import io.grpc.StatusRuntimeException;
import org.apache.jmeter.config.Arguments;
import org.apache.jmeter.protocol.java.sampler.AbstractJavaSamplerClient;
import org.apache.jmeter.protocol.java.sampler.JavaSamplerContext;
import org.apache.jmeter.samplers.SampleResult;


import java.util.logging.Logger;

public class GreetSampler extends AbstractJavaSamplerClient{

	private static final Logger logger = Logger.getLogger(GreetSampler.class.getName());

	private GrpcGreetClient client = null;

	@Override
	public void setupTest(JavaSamplerContext context){
		String ip = context.getParameter("ip");
		int port = context.getIntParameter("port");
		this.client = new GrpcGreetClient(ip, port);
		super.setupTest(context);
	}

	@Override
	public Arguments getDefaultParameters() {
	    Arguments defaultParameters = new Arguments();
		defaultParameters.addArgument("ip", "localhost");
		defaultParameters.addArgument("port", "50055");
		defaultParameters.addArgument("name", "Jack");
		return defaultParameters;
	}

	@Override
	public SampleResult runTest(JavaSamplerContext context) {
		String name = context.getParameter("name");
		if(null == name || name.isEmpty()){
			name = "test name";
		}
		logger.info("begin run test, name: " + name);

		SampleResult result = new SampleResult();
		result.sampleStart();
	    try {
	    	GreetResponse response = this.client.greet(name);
	    	result.sampleEnd();
	    	result.setSuccessful(true);
	    	result.setResponseData(response.getGreeting(), SampleResult.TEXT);
	    	result.setResponseMessage("Successfully performed");
            result.setResponseCodeOK();
	    }
	    catch (StatusRuntimeException e){
	    	result.sampleEnd();
            result.setSuccessful(false);
            result.setResponseMessage("Exception: " + e);
            java.io.StringWriter stringWriter = new java.io.StringWriter();
            e.printStackTrace(new java.io.PrintWriter(stringWriter));
            result.setResponseData(stringWriter.toString().getBytes());
            result.setDataType(org.apache.jmeter.samplers.SampleResult.TEXT);
            result.setResponseCode("500");
	    }
	    return result;
	}
	
	@Override
    public void teardownTest(JavaSamplerContext context){
		try {
			client.shutdown();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		super.teardownTest(context);
    }
}
