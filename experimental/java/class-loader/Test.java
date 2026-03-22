import java.net.URLClassLoader;
import java.net.URL;
import java.io.File;


class Test {
    public static void main(String... args) {
        if (args.length < 1 || (!args[0].equals("v1") && !args[0].equals("v2"))) {
            String version = args.length > 0 ? args[0] : "";
            System.out.println("Can't find a version: " + version);
            return;
        }

        String version = args[0];
        File classPathDir = new File("./module/colour/" + version);
        try {
            URL classPathUrl = classPathDir.toURI().toURL();
            ClassLoader loader = new URLClassLoader(new URL[] { classPathUrl }, Test.class.getClassLoader());
            Class<?> c = loader.loadClass("RedColourGenerator");
            System.out.println(c.getName());
            System.out.println(c.getProtectionDomain().getCodeSource().getLocation());
            ColourGenerator cg = (ColourGenerator) c.getDeclaredConstructor().newInstance();
            System.out.println(cg.getColour());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
