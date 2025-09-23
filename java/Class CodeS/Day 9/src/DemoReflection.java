package day9;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.util.Arrays;

public class DemoReflection {

	public static void main(String[] args) throws IllegalArgumentException, IllegalAccessException, InvocationTargetException, InstantiationException {
		Student st = new Student();
		Class c= st.getClass();
		
		Field [] fields = c.getDeclaredFields();
		for(Field f : fields)
		{
			System.out.println(f.getType());
			System.out.println(f.getName());
			if(f.getName().equals("rollno"))
			{
				f.setAccessible(true); //access the private field
				f.setInt(st, 10);
			}
		}
		System.out.println(st);
		System.out.println("------------------");
		Method [] methods = c.getDeclaredMethods();
		for(Method m : methods)
		{
			System.out.println(m.getName());
			System.out.println(m.getParameterCount());
			Parameter [] params = m.getParameters();
			System.out.println(Arrays.toString(params));
			
			if(m.getName().equals("privateMethod"))
			{
				m.setAccessible(true);
				m.invoke(st);
			}
			
			if(m.getName().equals("staticMethod"))
			{
				m.setAccessible(true);
				m.invoke(null);
			}
			
			if(m.getName().equals("setValues"))
			{
				m.setAccessible(true);
				m.invoke(st, 20, "aaa");
				System.out.println(st);
			}
		}
		
		System.out.println("------------------");
		Constructor<Student>  [] cons = c.getDeclaredConstructors();
		for(Constructor<Student> con : cons)
		{
			System.out.println(con.getParameterCount());
			Parameter [] params= con.getParameters();
			System.out.println(Arrays.toString(params));
			if(con.getParameterCount()==2)
			{
				Student s = con.newInstance(23, "kk");
				System.out.println(s);
			}
		}
	}
}
