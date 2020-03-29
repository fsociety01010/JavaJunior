import java.util.UUID;

public class test {
    public static void main(String[] args) {
        final String uuid = UUID.randomUUID().toString().replace("-", "");
        System.out.println("uuid = " + uuid);

        System.out.format("%,d \n",Long.MAX_VALUE);
        System.out.format("%,d\n",Integer.MAX_VALUE);
        System.out.format("%,f\n",Double.MAX_VALUE);
        System.out.format("Long contains %,d integers\n", Long.MAX_VALUE / Integer.MAX_VALUE);
        System.out.format("Double contains %,f longs\n", Double.MAX_VALUE / Long.MAX_VALUE);

       
    }

}