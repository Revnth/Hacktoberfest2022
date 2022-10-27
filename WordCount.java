import java.util.Arrays;

public class WordCount {
  private static int wordcount(String str) {
    int ct = 0;
    String[] arr = str.split(" ");
    for (String s : arr) {
      if (s.length() != 0) {
        ct++;
      }
    }
    return ct;
  }

  public static void main(String[] args) {
    String string = "    India Is My Country";
    System.out.println(wordcount(string) + " words.");
  }
}