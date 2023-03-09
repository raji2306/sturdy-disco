package hello;

import org.joda.time.LocalTime;
import static com.rollbar.notifier.config.ConfigBuilder.withAccessToken;
import com.rollbar.notifier.Rollbar;

public class HelloWorld {
    public static void main(String[] args) {
     try {
      LocalTime currentTime = new LocalTime();
		  System.out.println("The current local time is: " + currentTime);

        Greeter greeter = new Greeter();
        System.out.println(greeter.sayHello());
	    
    Rollbar rollbar = Rollbar.init(withAccessToken("f14a1ad6e0e644009d456897cfab76ac").build());
    rollbar.log("Hello, Rollbar");
    rollbar.close(true);
     }    
    catch (Exception e) {
	System.out.println("error");
    }    
    }
}
