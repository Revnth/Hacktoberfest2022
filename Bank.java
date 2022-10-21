import java.util.Scanner;
interface Bank 
{
Scanner sc = new Scanner (System.in);
void getDetails ();
void calculateInterest ();
void getMAmount ();
}
class SBI implements Bank
{
String name;
double principal;
double period;
double interest;
double roi = 8.5;
public void getDetails ()
{
System.out.println ("Enter Name");
name = sc.nextLine();
System.out.println ("Enter Principal");
principal = sc.nextDouble();
System.out.println ("Enter Period");
period = sc.nextDouble();
}
public void calculateInterest ()
{
interest = (principal * period * roi)/100;
}
public void getMAmount ()
{
double mAmount = principal + interest;
System.out.println (name+" your Maturity Amount in SBI is Rs. "+mAmount+"\n");
}
}
class CanaraBank implements Bank 
{
String name;
double principal;
double period;
double interest;
double roi = 8.5;
public void getDetails ()
{
System.out.println ("Enter Name");
name = sc.next();
System.out.println ("Enter Principal");
principal = sc.nextDouble();
System.out.println ("Enter Period");
period = sc.nextDouble();
}
public void calculateInterest ()
{
interest = (principal * period * roi)/100;
}
public void getMAmount ()
{
double mAmount = principal + interest;
System.out.println (name+" your Maturity Amount in Canara Bank is Rs. "+mAmount+"\n");
}
}
class BRun 
{
public static void main (String args[])
{
Bank b;
SBI sb = new SBI ();
CanaraBank cb = new CanaraBank ();
b = sb;
b.getDetails ();
b.calculateInterest ();
b.getMAmount ();
b = cb;
b.getDetails ();
b.calculateInterest ();
b.getMAmount ();
}
}