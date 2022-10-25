import java.util.Scanner;

public class Alphabet {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a character: ");
        char ch = input.next().trim().charAt(0);
        input.close();
        if (ch >= 'a' && ch <= 'z') {
            System.out.println("Lower case");
        } else if (ch >= 'A' && ch <= 'Z') {
            System.out.println("Upper case");
        }
    }
}
