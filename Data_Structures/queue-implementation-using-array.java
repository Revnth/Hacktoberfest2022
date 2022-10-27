import java.util.Scanner;

public class QueueImplementationUsingArray {
    static int arr[];
    static int rear;
    static int capacity;

    public QueueImplementationUsingArray(int cap)
    {
        capacity=cap;
        arr = new int[capacity];
        rear=-1;
    }

    static void enqueue(int data) throws Exception
    {
           if(rear==capacity-1)
           {
               throw new Exception();
           }

           else
           {
               arr[++rear]=data;
           }
    }

    static int dequeue() throws Exception
    {
          if(rear==-1)
          {
              throw new Exception();
          }

          else{
              int res=arr[0];
              for(int i=0;i<rear;i++)
              {
                   arr[i]=arr[i+1];
              }
              rear--;
              return res;
          }
    }

    static void display()
    {
        for(int i=0;i<=rear;i++)
        {
             System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) throws Exception {
        int ch;
        Scanner in = new Scanner(System.in);
        int num;
        System.out.println("Enter No. Of Elements For Array ==> ");
        num=in.nextInt();
        QueueImplementationUsingArray obj =  new QueueImplementationUsingArray(num);
        
        do
        {
        System.out.println("1. Enqueue 2. Dequeue 3. Display 4. Exit");
        System.out.println("Enter Your Choice No.");

        ch = in.nextInt();

        switch(ch)
        {
            case 1: System.out.println("Enter Data Into Queue ==>");
                    int n = in.nextInt();
                    enqueue(n);
                    break;
            case 2: int del = dequeue();
                    System.out.println("Data Removed ==> "+del );
                    break;
            case 3: display();
            break;

            case 4: break;
            default: System.out.println("Invalid Choice!!");

        }
    } while(ch!=4);
        
    }


    
}
